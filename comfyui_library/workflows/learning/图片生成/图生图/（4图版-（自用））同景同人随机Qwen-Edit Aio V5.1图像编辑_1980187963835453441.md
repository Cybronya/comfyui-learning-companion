---
key: 图片生成/图生图/（4图版-（自用））同景同人随机Qwen-Edit Aio V5.1图像编辑_1980187963835453441.json
name: （4图版-（自用））同景同人随机Qwen-Edit Aio V5.1图像编辑_1980187963835453441
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（4图版-（自用））同景同人随机Qwen-Edit Aio V5.1图像编辑_1980187963835453441.json
hash: 1fefa25cbe6077b6
coverage: 1
learned_at: 2026-10-23 13:36:13
nodes: [GetImageSizeAndCount, TextEncodeQwenImageEditPlus, SaveImage, CR Prompt Text, Text Concatenate, Text Multiline, TT_img_enc, SaveImage, ImageScaleToTotalPixels, VAEDecode, RH_LLMAPI_NODE, CR Prompt Text, TT_img_enc_v2, SaveImage, SaveImage, ImageConcanate, LoadImage, TextEncodeQwenImageEditPlus, EmptyLatentImage, CheckpointLoaderSimple, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 4, "cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v5.1.safetensors", "denoise": 1, "height": 768, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 500542912056598, "steps": 8, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/（4图版-（自用））同景同人随机Qwen-Edit Aio V5.1图像编辑_1980187963835453441.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（4图版-（自用））同景同人随机Qwen-Edit Aio V5.1图像编辑_1980187963835453441.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `GetImageSizeAndCount`
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `CR Prompt Text`
- `Text Concatenate`
- `Text Multiline`
- `TT_img_enc`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `RH_LLMAPI_NODE`
- `CR Prompt Text`
- `TT_img_enc_v2`
- `SaveImage`
- `SaveImage`
- `ImageConcanate`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `EmptyLatentImage` ★核心
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心

## 关键参数

- `width` = `768`
- `height` = `768`
- `batch_size` = `4`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v5.1.safetensors`
- `seed` = `500542912056598`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`GetImageSizeAndCount`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`CR Prompt Text`、`Text Concatenate`、`Text Multiline`、`TT_img_enc`、`ImageScaleToTotalPixels`、`VAEDecode`、`RH_LLMAPI_NODE`、`TT_img_enc_v2`、`ImageConcanate`、`LoadImage`、`EmptyLatentImage`、`CheckpointLoaderSimple`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、EmptyLatentImage、LoadImage、TextEncodeQwenImageEditPlus、CR Prompt Text、GetImageSizeAndCount

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
