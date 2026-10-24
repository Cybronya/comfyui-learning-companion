---
key: 图片生成/图生图/【阡陌】Qwen-Image六合一In Context Controlnet lora精准控制工作流_1960248554344361985.json
name: 【阡陌】Qwen-Image六合一In Context Controlnet lora精准控制工作流_1960248554344361985
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【阡陌】Qwen-Image六合一In Context Controlnet lora精准控制工作流_1960248554344361985.json
hash: 3f177f6c850e3826
coverage: 0.947368
learned_at: 2026-10-23 11:52:47
nodes: [CLIPLoader, LoadImage, ModelSamplingAuraFlow, LoraLoaderModelOnly, LoraLoaderModelOnly, ReferenceLatent, ReferenceLatent, VAELoader, VAEEncode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, AIO_Preprocessor, PreviewImage, KSampler, SaveImage, VAEDecode, CLIPTextEncode, UNETLoader, CLIPTextEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1122969699846388, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/【阡陌】Qwen-Image六合一In Context Controlnet lora精准控制工作流_1960248554344361985.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【阡陌】Qwen-Image六合一In Context Controlnet lora精准控制工作流_1960248554344361985.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `VAELoader`
- `VAEEncode` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AIO_Preprocessor`
- `PreviewImage`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1122969699846388`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`CLIPLoader`、`LoadImage`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`ReferenceLatent`、`VAELoader`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`AIO_Preprocessor`、`KSampler`、`SaveImage`、`VAEDecode`、`CLIPTextEncode`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
