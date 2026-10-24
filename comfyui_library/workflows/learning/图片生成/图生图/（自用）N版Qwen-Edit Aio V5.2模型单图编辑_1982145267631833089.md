---
key: 图片生成/图生图/（自用）N版Qwen-Edit Aio V5.2模型单图编辑_1982145267631833089.json
name: （自用）N版Qwen-Edit Aio V5.2模型单图编辑_1982145267631833089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（自用）N版Qwen-Edit Aio V5.2模型单图编辑_1982145267631833089.json
hash: e9a31b371d85d55d
coverage: 0.9375
learned_at: 2026-10-23 13:38:09
nodes: [EmptyLatentImage, TextEncodeQwenImageEditPlus, GetImageSizeAndCount, KSampler, TextEncodeQwenImageEditPlus, LoadImage, Text Multiline, TT_img_enc, SaveImage, SaveImage, CR Prompt Text, TT_img_enc_v2, VAEDecode, ImageScaleToTotalPixels, CheckpointLoaderSimple, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v5.2.safetensors", "denoise": 1, "height": 768, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 442822051703987, "steps": 8, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/（自用）N版Qwen-Edit Aio V5.2模型单图编辑_1982145267631833089.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（自用）N版Qwen-Edit Aio V5.2模型单图编辑_1982145267631833089.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImageEditPlus`
- `GetImageSizeAndCount`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `Text Multiline`
- `TT_img_enc`
- `SaveImage`
- `SaveImage`
- `CR Prompt Text`
- `TT_img_enc_v2`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `CheckpointLoaderSimple` ★核心
- `Note`

## 关键参数

- `width` = `768`
- `height` = `768`
- `batch_size` = `1`
- `seed` = `442822051703987`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v5.2.safetensors`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`EmptyLatentImage`、`TextEncodeQwenImageEditPlus`、`GetImageSizeAndCount`、`KSampler`、`LoadImage`、`Text Multiline`、`TT_img_enc`、`SaveImage`、`CR Prompt Text`、`TT_img_enc_v2`、`VAEDecode`、`ImageScaleToTotalPixels`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、EmptyLatentImage、LoadImage、TextEncodeQwenImageEditPlus、CR Prompt Text、GetImageSizeAndCount

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
