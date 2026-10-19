---
key: 图片生成/文生图/Z-Image：RedCraft⚡️红潮造相 AIO V1.5 文生图_1998731229589557249.json
name: Z-Image：RedCraft⚡️红潮造相 AIO V1.5 文生图_1998731229589557249
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image：RedCraft⚡️红潮造相 AIO V1.5 文生图_1998731229589557249.json
hash: 3cf610c41a0ac388
coverage: 0.823529
learned_at: 2026-10-19 21:47:04
nodes: [SaveImage, CheckpointLoaderSimple, CLIPTextEncode, ConditioningSetTimestepRange, PreviewImage, LayerUtility: PurgeVRAM, KSampler, VAEDecode, CLIPTextEncode, EmptyLatentImage, Text Multiline, easy showAnything, ShowText|pysssss, JoinStrings, Text Multiline, LoadImage, Qwen3_VQA]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "redcraftRedzimageUpdatedDEC03_redzimage15AIO.safetensors", "denoise": 1, "height": 1920, "sampler_name": "euler_cfg_pp", "scheduler": "beta", "seed": 217810764033401, "steps": 10, "width": 1080}
---

# 图片生成/文生图/Z-Image：RedCraft⚡️红潮造相 AIO V1.5 文生图_1998731229589557249.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image：RedCraft⚡️红潮造相 AIO V1.5 文生图_1998731229589557249.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningSetTimestepRange`
- `PreviewImage`
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `Text Multiline`
- `easy showAnything`
- `ShowText|pysssss`
- `JoinStrings`
- `Text Multiline`
- `LoadImage`
- `Qwen3_VQA`

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `redcraftRedzimageUpdatedDEC03_redzimage15AIO.safetensors`
- `seed` = `217810764033401`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler_cfg_pp`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`SaveImage`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`ConditioningSetTimestepRange`、`LayerUtility: PurgeVRAM`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`Text Multiline`、`JoinStrings`、`LoadImage`、`Qwen3_VQA`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ConditioningSetTimestepRange、SaveImage
