---
key: 图片生成/图生图/qwen_image_edit_plus_MultipleAngles-运镜+动作-图片多角度编辑_1988568009021284353.json
name: qwen_image_edit_plus_MultipleAngles-运镜+动作-图片多角度编辑_1988568009021284353
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_edit_plus_MultipleAngles-运镜+动作-图片多角度编辑_1988568009021284353.json
hash: 6c317efcd72afcdf
coverage: 0.875
learned_at: 2026-10-23 11:44:06
nodes: [CLIPTextEncode, EmptyLatentImage, CLIPLoader, GetImageSize, TextEncodeQwenImageEditPlus, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, KSampler, LoadImage, VAEDecode, SaveImage, PreviewImage, JjkText]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 90425842843959, "steps": 8, "width": 1440}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen_image_edit_plus_MultipleAngles-运镜+动作-图片多角度编辑_1988568009021284353.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_edit_plus_MultipleAngles-运镜+动作-图片多角度编辑_1988568009021284353.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `GetImageSize`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `KSampler` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `JjkText`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1440`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `90425842843959`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`CLIPTextEncode`、`EmptyLatentImage`、`CLIPLoader`、`GetImageSize`、`TextEncodeQwenImageEditPlus`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`VAELoader`、`KSampler`、`LoadImage`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
