from unsloth import FastModel
from transformers import TextStreamer
from datasets import load_dataset
from unsloth.chat_templates import get_chat_template
from trl import SFTTrainer, SFTConfig
from unsloth import is_bfloat16_supported

model, tokenizer = FastModel.from_pretrained(
    model_name="unsloth/gemma-3-270m-it",
    max_seq_length=2048,
    load_in_4bit=True,
    load_in_8bit=False,
    full_finetuning=False,
)

model = FastModel.get_peft_model(
    model,
    finetune_vision_layers=False,
    finetune_language_layers=True,
    finetune_attention_modules=True,
    finetune_mlp_modules=True,
    r=8,
    lora_alpha=8,
    lora_dropout=0,
    bias="none",
    random_state=3407,
    use_gradient_checkpointing="unsloth",
)

dataset = load_dataset("bebechien/MobileGameNPC", "martian", split="train")

tokenizer = get_chat_template(tokenizer, chat_template="gemma-3")

formatted_texts = []

for i in range(len(dataset)):
    conversation = [
        {"role": "user", "content": dataset[i]["player"]},
        {"role": "assistant", "content": dataset[i]["alien"]},
    ]
    text = tokenizer.apply_chat_template(
        conversation,
        tokenize=False,
        add_generation_prompt=False,
    )
    formatted_texts.append(text)

dataset = dataset.add_column("text", formatted_texts)

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    args=SFTConfig(
        dataset_text_field="text",
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        warmup_steps=5,
        num_train_epochs=30,
        learning_rate=2e-4,
        fp16=not is_bfloat16_supported(),
        bf16=is_bfloat16_supported(),
        logging_steps=5,
        optim="adamw_8bit",
        weight_decay=0.01,
        lr_scheduler_type="linear",
        seed=3407,
        output_dir="outputs",
        report_to="none",
    ),
)

trainer.train()

model = FastModel.for_inference(model)

def do_inference(messages, max_new_tokens=128):
    _ = model.generate(
        **tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
        ).to("cuda"),
        max_new_tokens=max_new_tokens,
        temperature=1.0,
        top_p=0.95,
        top_k=64,
        streamer=TextStreamer(tokenizer, skip_prompt=True),
    )

do_inference([{"role": "user", "content": "Hello there."}])