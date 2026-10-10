---
key: qwen-Image -nunchaku+lora_1963114884189884418.json
name: qwen-Image -nunchaku+lora_1963114884189884418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-Image -nunchaku+lora_1963114884189884418.json
hash: 1d831bae0e748581
coverage: 1
learned_at: 2026-10-10 20:59:24
nodes: [CLIPTextEncode, CLIPLoader, VAELoader, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, VAEDecode, SaveImage, EmptySD3LatentImage, CLIPTextEncode, KSampler, NunchakuQwenImageLoraLoader1]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1008056321523755, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# qwen-Image -nunchaku+lora_1963114884189884418.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-Image -nunchaku+lora_1963114884189884418.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `NunchakuQwenImageLoraLoader1` ★核心

## 关键参数

- `seed` = `1008056321523755`
- `steps` = `8`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`NunchakuQwenImageDiTLoader`、`VAEDecode`、`SaveImage`、`EmptySD3LatentImage`、`KSampler`、`NunchakuQwenImageLoraLoader1`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、NunchakuQwenImageLoraLoader1、SaveImage、EmptySD3LatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
