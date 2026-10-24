---
key: 图片生成/图生图/【阡陌】Qwen-Image Canny ControlNet提示词反推精准控图工作流_1959553457558597634.json
name: 【阡陌】Qwen-Image Canny ControlNet提示词反推精准控图工作流_1959553457558597634
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【阡陌】Qwen-Image Canny ControlNet提示词反推精准控图工作流_1959553457558597634.json
hash: b9d889f1ddd9e70d
coverage: 0.894737
learned_at: 2026-10-23 11:52:44
nodes: [LoadImage, ShowText|pysssss, LoadJanusModel, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, KSampler, EmptyLatentImage, VAEDecode, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, ModelSamplingAuraFlow, UNETLoader, LoraLoaderModelOnly, JanusImage2Text, SaveImage, workflow>controlnet]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 318925437347752, "steps": 4, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/【阡陌】Qwen-Image Canny ControlNet提示词反推精准控图工作流_1959553457558597634.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【阡陌】Qwen-Image Canny ControlNet提示词反推精准控图工作流_1959553457558597634.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `LoadImage`
- `ShowText|pysssss`
- `LoadJanusModel`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `JanusImage2Text`
- `SaveImage`
- `workflow>controlnet`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `318925437347752`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`LoadImage`、`LoadJanusModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`UNETLoader`、`LoraLoaderModelOnly`、`JanusImage2Text`、`SaveImage`、`workflow>controlnet`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
