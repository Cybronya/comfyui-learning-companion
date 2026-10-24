---
key: 图片生成/图生图/FLUX Krea 重绘洗图 ControlNet  Union_1951500495967997953.json
name: FLUX Krea 重绘洗图 ControlNet  Union_1951500495967997953
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX Krea 重绘洗图 ControlNet  Union_1951500495967997953.json
hash: bc633520c1a3da78
coverage: 0.869565
learned_at: 2026-10-23 10:53:29
nodes: [SetUnionControlNetType, VAELoader, CLIPTextEncode, easy imageSize, FluxGuidance, ControlNetApplyAdvanced, KSampler, DualCLIPLoader, ControlNetLoader, Joy_caption_two_load, VAEDecode, SaveImage, Image Comparer (rgthree), UNETLoader, SDVN Translate, Joy_caption_two, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, CLIPTextEncode, LoadImage, ShowText|pysssss, ShowText|pysssss, EmptyLatentImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 4, "cfg": 1, "controlnet_strength": 0.3, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 896033358695379, "steps": 25, "width": 512}
---

# 图片生成/图生图/FLUX Krea 重绘洗图 ControlNet  Union_1951500495967997953.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX Krea 重绘洗图 ControlNet  Union_1951500495967997953.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `SetUnionControlNetType`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `easy imageSize`
- `FluxGuidance`
- `ControlNetApplyAdvanced` ★核心
- `KSampler` ★核心
- `DualCLIPLoader`
- `ControlNetLoader`
- `Joy_caption_two_load`
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `SDVN Translate`
- `Joy_caption_two`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `controlnet_strength` = `0.3`
- `seed` = `896033358695379`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `4`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`SetUnionControlNetType`、`VAELoader`、`CLIPTextEncode`、`easy imageSize`、`FluxGuidance`、`ControlNetApplyAdvanced`、`KSampler`、`DualCLIPLoader`、`ControlNetLoader`、`Joy_caption_two_load`、`VAEDecode`、`SaveImage`、`UNETLoader`、`SDVN Translate`、`Joy_caption_two`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`、`LoadImage`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced
