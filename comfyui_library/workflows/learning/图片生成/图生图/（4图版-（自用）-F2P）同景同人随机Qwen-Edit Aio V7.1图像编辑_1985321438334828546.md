---
key: 图片生成/图生图/（4图版-（自用）-F2P）同景同人随机Qwen-Edit Aio V7.1图像编辑_1985321438334828546.json
name: （4图版-（自用）-F2P）同景同人随机Qwen-Edit Aio V7.1图像编辑_1985321438334828546
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（4图版-（自用）-F2P）同景同人随机Qwen-Edit Aio V7.1图像编辑_1985321438334828546.json
hash: 3e523192756a9098
coverage: 1
learned_at: 2026-10-23 13:36:13
nodes: [TextEncodeQwenImageEditPlus, SaveImage, TT_img_enc, SaveImage, ImageScaleToTotalPixels, VAEDecode, RH_LLMAPI_NODE, CR Prompt Text, TT_img_enc_v2, SaveImage, SaveImage, ImageConcanate, LoadImage, KSampler, CR Prompt Text, CheckpointLoaderSimple, LoraLoaderModelOnly, Text Multiline, Text Concatenate, GetImageSizeAndCount, TextEncodeQwenImageEditPlus, EmptyLatentImage, Float]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 4, "cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v7.1.safetensors", "denoise": 1, "height": 768, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 919708741343667, "steps": 8, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/（4图版-（自用）-F2P）同景同人随机Qwen-Edit Aio V7.1图像编辑_1985321438334828546.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（4图版-（自用）-F2P）同景同人随机Qwen-Edit Aio V7.1图像编辑_1985321438334828546.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
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
- `KSampler` ★核心
- `CR Prompt Text`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text Multiline`
- `Text Concatenate`
- `GetImageSizeAndCount`
- `TextEncodeQwenImageEditPlus`
- `EmptyLatentImage` ★核心
- `Float`

## 关键参数

- `seed` = `919708741343667`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v7.1.safetensors`
- `width` = `768`
- `height` = `768`
- `batch_size` = `4`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`TextEncodeQwenImageEditPlus`、`SaveImage`、`TT_img_enc`、`ImageScaleToTotalPixels`、`VAEDecode`、`RH_LLMAPI_NODE`、`CR Prompt Text`、`TT_img_enc_v2`、`ImageConcanate`、`LoadImage`、`KSampler`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`Text Multiline`、`Text Concatenate`、`GetImageSizeAndCount`、`EmptyLatentImage`、`Float`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、EmptyLatentImage、LoadImage、TextEncodeQwenImageEditPlus、CR Prompt Text

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
