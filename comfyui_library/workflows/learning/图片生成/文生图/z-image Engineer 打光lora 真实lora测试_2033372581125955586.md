---
key: 图片生成/文生图/z-image Engineer 打光lora 真实lora测试_2033372581125955586.json
name: z-image Engineer 打光lora 真实lora测试_2033372581125955586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/z-image Engineer 打光lora 真实lora测试_2033372581125955586.json
hash: bf90ac31e99b0e59
coverage: 0.914286
learned_at: 2026-10-21 02:57:44
nodes: [KSampler, CLIPTextEncode, CLIPTextEncode, VAEDecode, SaveImage, ModelSamplingAuraFlow, EmptySD3LatentImage, PrimitiveStringMultiline, VAEDecode, CLIPTextEncode, KSampler, CLIPTextEncode, ModelSamplingAuraFlow, VAEDecode, SaveImage, CLIPTextEncode, KSampler, CLIPTextEncode, ModelSamplingAuraFlow, VAEDecode, SaveImage, CLIPTextEncode, KSampler, CLIPTextEncode, ModelSamplingAuraFlow, PrimitiveStringMultiline, PrimitiveStringMultiline, CLIPLoader, VAELoader, CLIPLoaderGGUF, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage, UNETLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 2025, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/z-image Engineer 打光lora 真实lora测试_2033372581125955586.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/z-image Engineer 打光lora 真实lora测试_2033372581125955586.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ModelSamplingAuraFlow`
- `EmptySD3LatentImage`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `VAELoader`
- `CLIPLoaderGGUF`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `2025`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（32/35）

**有卡**：`KSampler`、`CLIPTextEncode`、`VAEDecode`、`SaveImage`、`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`CLIPLoader`、`VAELoader`、`CLIPLoaderGGUF`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、CLIPLoaderGGUF

## 参数体检

发现 4 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
