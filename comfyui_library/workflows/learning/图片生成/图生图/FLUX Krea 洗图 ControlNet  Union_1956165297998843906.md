---
key: 图片生成/图生图/FLUX Krea 洗图 ControlNet  Union_1956165297998843906.json
name: FLUX Krea 洗图 ControlNet  Union_1956165297998843906
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX Krea 洗图 ControlNet  Union_1956165297998843906.json
hash: e4eba1b2ab2eadde
coverage: 0.869565
learned_at: 2026-10-23 10:53:29
nodes: [VAELoader, CLIPTextEncode, easy imageSize, FluxGuidance, DualCLIPLoader, Joy_caption_two_load, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, ShowText|pysssss, EmptyLatentImage, SDVN Translate, LayerUtility: PurgeVRAM, Image Comparer (rgthree), LoadImage, Joy_caption_two, ShowText|pysssss, SaveImage, VAEDecode, KSampler, ControlNetApplyAdvanced, ControlNetLoader, SetUnionControlNetType]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 4, "cfg": 1, "controlnet_strength": 0.6000000000000001, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 899651250548331, "steps": 25, "width": 512}
---

# 图片生成/图生图/FLUX Krea 洗图 ControlNet  Union_1956165297998843906.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX Krea 洗图 ControlNet  Union_1956165297998843906.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `easy imageSize`
- `FluxGuidance`
- `DualCLIPLoader`
- `Joy_caption_two_load`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `EmptyLatentImage` ★核心
- `SDVN Translate`
- `LayerUtility: PurgeVRAM`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Joy_caption_two`
- `ShowText|pysssss`
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `SetUnionControlNetType`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `4`
- `seed` = `899651250548331`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.6000000000000001`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`VAELoader`、`CLIPTextEncode`、`easy imageSize`、`FluxGuidance`、`DualCLIPLoader`、`Joy_caption_two_load`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLatentImage`、`SDVN Translate`、`LayerUtility: PurgeVRAM`、`LoadImage`、`Joy_caption_two`、`SaveImage`、`VAEDecode`、`KSampler`、`ControlNetApplyAdvanced`、`ControlNetLoader`、`SetUnionControlNetType`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced
