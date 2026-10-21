---
key: 图片生成/文生图/图像编辑FireRed-Image-Edit-1.1_2053727183633432578.json
name: 图像编辑FireRed-Image-Edit-1.1_2053727183633432578
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/图像编辑FireRed-Image-Edit-1.1_2053727183633432578.json
hash: 6b60e821b7ad7401
coverage: 0.869565
learned_at: 2026-10-21 02:59:34
nodes: [TextEncodeQwenImageEditPlus, LoraLoaderModelOnly, VAELoader, KSampler, EmptyLatentImage, CLIPTextEncode, PrimitiveNode, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveBoolean, SaveImage, LoadImage, SeedVR2, VAEDecode, ComfySwitchNode, JjkText, CustomAddLabel, SaveImage, CLIPLoader, LoadImage, LoadImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 202217693743598, "steps": 8, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/图像编辑FireRed-Image-Edit-1.1_2053727183633432578.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/图像编辑FireRed-Image-Edit-1.1_2053727183633432578.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveBoolean`
- `SaveImage`
- `LoadImage`
- `SeedVR2`
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `JjkText`
- `CustomAddLabel`
- `SaveImage`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `202217693743598`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`TextEncodeQwenImageEditPlus`、`LoraLoaderModelOnly`、`VAELoader`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`PrimitiveBoolean`、`SaveImage`、`LoadImage`、`SeedVR2`、`VAEDecode`、`CustomAddLabel`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
