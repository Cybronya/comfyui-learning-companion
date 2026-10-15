---
key: 图片生成/文生图/nunchaku F.1 D+水墨_1968880877902155777.json
name: nunchaku F.1 D+水墨_1968880877902155777
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/nunchaku F.1 D+水墨_1968880877902155777.json
hash: eb6b13fed5e44b1d
coverage: 1
learned_at: 2026-10-10 20:59:23
nodes: [ConditioningZeroOut, VAEDecode, SaveImage, EmptyLatentImage, LoadImage, VAEEncode, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, VAELoader, NunchakuFluxLoraLoader, DualCLIPLoader, UNETLoader, LoraLoader, LoraLoader, KSampler, CLIPTextEncode]
patterns: [text_to_image, image_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 3, "denoise": 1, "height": 1024, "lora_name": "FLUX_国风水墨场景_V1_FLUX_国风水墨场景_V1.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 162353702622056, "steps": 35, "strength_clip": 1, "strength_model": 0.8, "width": 1024}
---

# 图片生成/文生图/nunchaku F.1 D+水墨_1968880877902155777.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/nunchaku F.1 D+水墨_1968880877902155777.json`

## 结构

**节点**（16 个）：
- `ConditioningZeroOut`
- `VAEDecode`
- `SaveImage`
- `EmptyLatentImage`
- `LoadImage`
- `VAEEncode`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `VAELoader`
- `NunchakuFluxLoraLoader`
- `DualCLIPLoader`
- `UNETLoader`
- `LoraLoader`
- `LoraLoader`
- `KSampler`
- `CLIPTextEncode`

**识别到的模式**：text_to_image、image_to_image、lora

## 关键参数

- `batch_size` = `1`
- `cfg` = `3`
- `denoise` = `1`
- `height` = `1024`
- `lora_name` = `FLUX_国风水墨场景_V1_FLUX_国风水墨场景_V1.safetensors`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `162353702622056`
- `steps` = `35`
- `strength_clip` = `1`
- `strength_model` = `0.8`
- `width` = `1024`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`LoadImage`、`VAEEncode`、`NunchakuFluxDiTLoader`、`NunchakuFluxLoraLoader`、`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`LoraLoader`、`KSampler`、`CLIPTextEncode`
