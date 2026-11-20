---
key: 平台全量/【阡陌】Qwen-Image-Lightning 4步lora闪电加速_1957359205059588098.json
name: 【阡陌】Qwen-Image-Lightning 4步lora闪电加速_1957359205059588098
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/【阡陌】Qwen-Image-Lightning 4步lora闪电加速_1957359205059588098.json
hash: 5aa7777c03f37acc
coverage: 1
learned_at: 2026-11-14 01:26:16
nodes: [CLIPLoader, CLIPTextEncode, SaveImage, VAEDecode, VAELoader, LoadImage, ModelSamplingAuraFlow, LoraLoaderModelOnly, CLIPTextEncode, KSampler, EmptyLatentImage, UNETLoader]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 843159626402938, "steps": 4, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/【阡陌】Qwen-Image-Lightning 4步lora闪电加速_1957359205059588098.json

> 来源文件 `comfyui_library/workflows/平台全量/【阡陌】Qwen-Image-Lightning 4步lora闪电加速_1957359205059588098.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `VAELoader`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `843159626402938`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`SaveImage`、`VAEDecode`、`VAELoader`、`LoadImage`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
