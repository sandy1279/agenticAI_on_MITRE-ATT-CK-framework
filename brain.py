from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load Falcon model
model_name = "tiiuae/falcon-7b-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", torch_dtype=torch.bfloat16)

def generate_ai_recommendation(ttp_name, ttp_desc, mitigation):
    prompt = f"""
    Cybersecurity Alert: A potential attack has been detected.

    🚨 **Attack Technique:** {ttp_name}
    📌 **Description:** {ttp_desc}
    ✅ **Suggested Mitigation:** {mitigation}

    Provide a concise incident response recommendation for SOC analysts.
    """

    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    output = model.generate(**inputs, max_length=200)
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    return response

# Example: Get Falcon's recommendation
for ttp in matched_ttps:
    ai_response = generate_ai_recommendation(ttp["name"], "MITRE technique description", "Apply EDR rules")
    print(f"\n🔹 Technique: {ttp['name']}")
    print(f"🤖 AI-Generated Response: {ai_response}")
