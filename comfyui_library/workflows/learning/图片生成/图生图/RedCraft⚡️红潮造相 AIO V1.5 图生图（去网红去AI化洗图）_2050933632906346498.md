---
key: 图片生成/图生图/RedCraft⚡️红潮造相 AIO V1.5 图生图（去网红去AI化洗图）_2050933632906346498.json
name: RedCraft⚡️红潮造相 AIO V1.5 图生图（去网红去AI化洗图）_2050933632906346498
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/RedCraft⚡️红潮造相 AIO V1.5 图生图（去网红去AI化洗图）_2050933632906346498.json
hash: 36f138121636227f
coverage: 0.789474
learned_at: 2026-10-23 11:23:21
nodes: [VAEDecode, SaveImage, PreviewImage, easy showAnything, ShowText|pysssss, LayerUtility: PurgeVRAM, PreviewImage, Qwen3_VQA, JoinStrings, Text Multiline, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, CR Simple Image Compare, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, KSampler, LayerUtility: PurgeVRAM, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "checkpoint": "redcraftRedzimageUpdatedDEC03_redzimage15AIO.safetensors", "denoise": 0.7000000000000002, "sampler_name": "euler_cfg_pp", "scheduler": "beta", "seed": 553196243504620, "steps": 10}
---

# 图片生成/图生图/RedCraft⚡️红潮造相 AIO V1.5 图生图（去网红去AI化洗图）_2050933632906346498.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/RedCraft⚡️红潮造相 AIO V1.5 图生图（去网红去AI化洗图）_2050933632906346498.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `easy showAnything`
- `ShowText|pysssss`
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `Qwen3_VQA`
- `JoinStrings`
- `Text Multiline`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Simple Image Compare`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `redcraftRedzimageUpdatedDEC03_redzimage15AIO.safetensors`
- `seed` = `553196243504620`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler_cfg_pp`
- `scheduler` = `beta`
- `denoise` = `0.7000000000000002`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`VAEDecode`、`SaveImage`、`LayerUtility: PurgeVRAM`、`Qwen3_VQA`、`JoinStrings`、`Text Multiline`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Simple Image Compare`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`KSampler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、VAEEncode、SaveImage、JoinStrings
