---
key: 图片生成/文生图/Description to Image _ Z-IMAGE_1993955579181940738.json
name: Description to Image _ Z-IMAGE_1993955579181940738
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Description to Image _ Z-IMAGE_1993955579181940738.json
hash: df230d297a70ff3d
coverage: 0.857143
learned_at: 2026-10-19 21:32:27
nodes: [CLIPLoader, UNETLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, MarkdownNote, easy showAnything, RH_Captioner, LoadImage, KSampler, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 288395240733439, "steps": 10, "width": 512}
---

# 图片生成/文生图/Description to Image _ Z-IMAGE_1993955579181940738.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Description to Image _ Z-IMAGE_1993955579181940738.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `MarkdownNote`
- `easy showAnything`
- `RH_Captioner`
- `LoadImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `288395240733439`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyLatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`RH_Captioner`、`LoadImage`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage
