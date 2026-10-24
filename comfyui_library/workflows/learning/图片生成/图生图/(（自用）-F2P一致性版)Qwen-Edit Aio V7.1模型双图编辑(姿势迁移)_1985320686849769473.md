---
key: 图片生成/图生图/(（自用）-F2P一致性版)Qwen-Edit Aio V7.1模型双图编辑(姿势迁移)_1985320686849769473.json
name: (（自用）-F2P一致性版)Qwen-Edit Aio V7.1模型双图编辑(姿势迁移)_1985320686849769473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/(（自用）-F2P一致性版)Qwen-Edit Aio V7.1模型双图编辑(姿势迁移)_1985320686849769473.json
hash: fd5b631c7fc989c7
coverage: 1
learned_at: 2026-10-23 10:46:55
nodes: [EmptyLatentImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, GetImageSizeAndCount, DWPreprocessor, KSampler, ImageScaleToTotalPixels, ImageScaleToTotalPixels, LoadImage, LoadImage, SaveImage, VAEDecode, TT_img_enc_v2, CR Prompt Text, SaveImage, Text Multiline, CheckpointLoaderSimple, LoraLoaderModelOnly, Float, TT_img_enc]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v5.2.safetensors", "denoise": 1, "height": 768, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 183875428619791, "steps": 8, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/(（自用）-F2P一致性版)Qwen-Edit Aio V7.1模型双图编辑(姿势迁移)_1985320686849769473.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/(（自用）-F2P一致性版)Qwen-Edit Aio V7.1模型双图编辑(姿势迁移)_1985320686849769473.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `GetImageSizeAndCount`
- `DWPreprocessor`
- `KSampler` ★核心
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `VAEDecode` ★核心
- `TT_img_enc_v2`
- `CR Prompt Text`
- `SaveImage`
- `Text Multiline`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `Float`
- `TT_img_enc`

## 关键参数

- `width` = `768`
- `height` = `768`
- `batch_size` = `1`
- `seed` = `183875428619791`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v5.2.safetensors`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`EmptyLatentImage`、`TextEncodeQwenImageEditPlus`、`GetImageSizeAndCount`、`DWPreprocessor`、`KSampler`、`ImageScaleToTotalPixels`、`LoadImage`、`SaveImage`、`VAEDecode`、`TT_img_enc_v2`、`CR Prompt Text`、`Text Multiline`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`Float`、`TT_img_enc`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、EmptyLatentImage、LoadImage、TextEncodeQwenImageEditPlus、CR Prompt Text

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
