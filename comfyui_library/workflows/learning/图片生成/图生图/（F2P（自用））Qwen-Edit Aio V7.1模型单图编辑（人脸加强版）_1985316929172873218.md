---
key: 图片生成/图生图/（F2P（自用））Qwen-Edit Aio V7.1模型单图编辑（人脸加强版）_1985316929172873218.json
name: （F2P（自用））Qwen-Edit Aio V7.1模型单图编辑（人脸加强版）_1985316929172873218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（F2P（自用））Qwen-Edit Aio V7.1模型单图编辑（人脸加强版）_1985316929172873218.json
hash: c1665a98dbf06ee4
coverage: 0.9
learned_at: 2026-10-23 13:37:11
nodes: [GetImageSizeAndCount, KSampler, TextEncodeQwenImageEditPlus, LoadImage, SaveImage, SaveImage, TT_img_enc_v2, VAEDecode, TT_img_enc, EmptyLatentImage, Note, Float, CR Prompt Text, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, CheckpointLoaderSimple, Note, ImageScaleToTotalPixels, CR Prompt Text, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v7.1.safetensors", "denoise": 1, "height": 768, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 715595503636240, "steps": 8, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/（F2P（自用））Qwen-Edit Aio V7.1模型单图编辑（人脸加强版）_1985316929172873218.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（F2P（自用））Qwen-Edit Aio V7.1模型单图编辑（人脸加强版）_1985316929172873218.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `GetImageSizeAndCount`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `TT_img_enc_v2`
- `VAEDecode` ★核心
- `TT_img_enc`
- `EmptyLatentImage` ★核心
- `Note`
- `Float`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `ImageScaleToTotalPixels`
- `CR Prompt Text`
- `SaveImage`

## 关键参数

- `seed` = `715595503636240`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `768`
- `height` = `768`
- `batch_size` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v7.1.safetensors`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`GetImageSizeAndCount`、`KSampler`、`TextEncodeQwenImageEditPlus`、`LoadImage`、`SaveImage`、`TT_img_enc_v2`、`VAEDecode`、`TT_img_enc`、`EmptyLatentImage`、`Float`、`CR Prompt Text`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`ImageScaleToTotalPixels`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、EmptyLatentImage、LoadImage、TextEncodeQwenImageEditPlus、CR Prompt Text

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
