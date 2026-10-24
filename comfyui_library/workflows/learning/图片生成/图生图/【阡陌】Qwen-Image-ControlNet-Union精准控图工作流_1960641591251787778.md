---
key: 图片生成/图生图/【阡陌】Qwen-Image-ControlNet-Union精准控图工作流_1960641591251787778.json
name: 【阡陌】Qwen-Image-ControlNet-Union精准控图工作流_1960641591251787778
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【阡陌】Qwen-Image-ControlNet-Union精准控图工作流_1960641591251787778.json
hash: 23a0d903d4829d63
coverage: 0.944444
learned_at: 2026-10-23 11:52:45
nodes: [CLIPLoader, CLIPTextEncode, VAELoader, LoadImage, KSampler, UNETLoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, LoadImage, EmptyLatentImage, CLIPTextEncode, VAEDecode, SaveImage, ControlNetApplyAdvanced, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, ControlNetLoader, AIO_Preprocessor]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 888728789910461, "steps": 4, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/【阡陌】Qwen-Image-ControlNet-Union精准控图工作流_1960641591251787778.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【阡陌】Qwen-Image-ControlNet-Union精准控图工作流_1960641591251787778.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoadImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ControlNetLoader`
- `AIO_Preprocessor`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `888728789910461`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `controlnet_strength` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`LoadImage`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`ControlNetApplyAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`ControlNetLoader`、`AIO_Preprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
