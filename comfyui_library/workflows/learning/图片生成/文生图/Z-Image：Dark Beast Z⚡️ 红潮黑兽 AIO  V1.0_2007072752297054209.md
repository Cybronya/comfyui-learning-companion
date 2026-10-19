---
key: 图片生成/文生图/Z-Image：Dark Beast Z⚡️ 红潮黑兽 AIO  V1.0_2007072752297054209.json
name: Z-Image：Dark Beast Z⚡️ 红潮黑兽 AIO  V1.0_2007072752297054209
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image：Dark Beast Z⚡️ 红潮黑兽 AIO  V1.0_2007072752297054209.json
hash: 2b30055fc78c6965
coverage: 1
learned_at: 2026-10-19 22:01:03
nodes: [CLIPTextEncode, KSampler, CheckpointLoaderSimple, VAEDecode, SaveImage, CLIPTextEncode, EmptyLatentImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 4, "cfg": 1, "checkpoint": "darkBeastZDBZUpdatedDEC21_dbzAIOV10.safetensors", "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 154562796795437, "steps": 10, "width": 1920}
---

# 图片生成/文生图/Z-Image：Dark Beast Z⚡️ 红潮黑兽 AIO  V1.0_2007072752297054209.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image：Dark Beast Z⚡️ 红潮黑兽 AIO  V1.0_2007072752297054209.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（7 个）：
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `154562796795437`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `darkBeastZDBZUpdatedDEC21_dbzAIOV10.safetensors`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `4`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`CLIPTextEncode`、`KSampler`、`CheckpointLoaderSimple`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、SaveImage、sd15-t2i-basic、sd15-t2i-lora
