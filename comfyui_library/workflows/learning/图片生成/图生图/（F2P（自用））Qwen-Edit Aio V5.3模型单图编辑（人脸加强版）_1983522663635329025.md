---
key: 图片生成/图生图/（F2P（自用））Qwen-Edit Aio V5.3模型单图编辑（人脸加强版）_1983522663635329025.json
name: （F2P（自用））Qwen-Edit Aio V5.3模型单图编辑（人脸加强版）_1983522663635329025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（F2P（自用））Qwen-Edit Aio V5.3模型单图编辑（人脸加强版）_1983522663635329025.json
hash: 68a7f7fa9049337b
coverage: 0.9
learned_at: 2026-10-23 13:37:11
nodes: [EmptyLatentImage, TextEncodeQwenImageEditPlus, GetImageSizeAndCount, KSampler, TextEncodeQwenImageEditPlus, LoadImage, TT_img_enc, SaveImage, SaveImage, CR Prompt Text, TT_img_enc_v2, Note, ImageScaleToTotalPixels, VAEDecode, CheckpointLoaderSimple, Text Multiline, SaveImage, LoraLoaderModelOnly, Float, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v5.3.safetensors", "denoise": 1, "height": 768, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 544464807599820, "steps": 8, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/（F2P（自用））Qwen-Edit Aio V5.3模型单图编辑（人脸加强版）_1983522663635329025.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（F2P（自用））Qwen-Edit Aio V5.3模型单图编辑（人脸加强版）_1983522663635329025.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImageEditPlus`
- `GetImageSizeAndCount`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `TT_img_enc`
- `SaveImage`
- `SaveImage`
- `CR Prompt Text`
- `TT_img_enc_v2`
- `Note`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `Text Multiline`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `Float`
- `Note`

## 关键参数

- `width` = `768`
- `height` = `768`
- `batch_size` = `1`
- `seed` = `544464807599820`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v5.3.safetensors`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`EmptyLatentImage`、`TextEncodeQwenImageEditPlus`、`GetImageSizeAndCount`、`KSampler`、`LoadImage`、`TT_img_enc`、`SaveImage`、`CR Prompt Text`、`TT_img_enc_v2`、`ImageScaleToTotalPixels`、`VAEDecode`、`CheckpointLoaderSimple`、`Text Multiline`、`LoraLoaderModelOnly`、`Float`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、EmptyLatentImage、LoadImage、TextEncodeQwenImageEditPlus、CR Prompt Text

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
