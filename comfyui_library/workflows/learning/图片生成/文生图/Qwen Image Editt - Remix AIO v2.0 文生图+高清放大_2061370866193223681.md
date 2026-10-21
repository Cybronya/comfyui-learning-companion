---
key: 图片生成/文生图/Qwen Image Editt - Remix AIO v2.0 文生图+高清放大_2061370866193223681.json
name: Qwen Image Editt - Remix AIO v2.0 文生图+高清放大_2061370866193223681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image Editt - Remix AIO v2.0 文生图+高清放大_2061370866193223681.json
hash: 86e05f73c3c5ec5b
coverage: 0.8
learned_at: 2026-10-19 23:02:39
nodes: [SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, Image Comparer (rgthree), SaveImage, CheckpointLoaderSimple, Anything Everywhere3, SaveImage, VAEDecode, KSampler, easy setNode, ReferenceLatent, ConditioningZeroOut, Seed (rgthree), EmptyLatentImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, CR Text, Fast Groups Bypasser (rgthree), easy getNode, Any Switch (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Image-Edit-Remix-AIO-v2.0.safetensors", "denoise": 1, "height": 1920, "sampler_name": "lcm", "scheduler": "normal", "seed": 882818245383612, "steps": 10, "width": 1080}
---

# 图片生成/文生图/Qwen Image Editt - Remix AIO v2.0 文生图+高清放大_2061370866193223681.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image Editt - Remix AIO v2.0 文生图+高清放大_2061370866193223681.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `Image Comparer (rgthree)`
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `Anything Everywhere3`
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `easy setNode`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `Seed (rgthree)`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `easy getNode`
- `Any Switch (rgthree)`

## 关键参数

- `checkpoint` = `Qwen-Image-Edit-Remix-AIO-v2.0.safetensors`
- `seed` = `882818245383612`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SaveImage`、`CheckpointLoaderSimple`、`VAEDecode`、`KSampler`、`easy setNode`、`ReferenceLatent`、`ConditioningZeroOut`、`Seed (rgthree)`、`EmptyLatentImage`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`CR Text`、`easy getNode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、ConditioningZeroOut、EmptyLatentImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler
