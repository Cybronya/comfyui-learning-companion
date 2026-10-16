---
key: 视频生成/图生视频/WAN2.2-AllInOne 图生视频_1962495712468549634.json
name: WAN2.2-AllInOne 图生视频_1962495712468549634.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1962495712468549634.json
hash: 3ed1aadbe5449ec6
coverage: 0.823529
learned_at: 2026-10-15 22:31:31
nodes: [ModelSamplingSD3, WanImageToVideo, KSampler, VAEDecode, VHS_VideoCombine, LoadImage, GetImageSize, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, LayerUtility: ImageScaleByAspectRatio, Primitive integer [Crystools], Primitive integer [Crystools], Note, Note, Note, Primitive integer [Crystools]]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-nsfw-v9.2.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 192054346835137, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/WAN2.2-AllInOne 图生视频_1962495712468549634.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962495712468549634.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（17 个）：
- `ModelSamplingSD3`
- `WanImageToVideo`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LayerUtility: ImageScaleByAspectRatio`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Note`
- `Note`
- `Note`
- `Primitive integer [Crystools]`

## 关键参数

- `seed` = `192054346835137`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-nsfw-v9.2.safetensors`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`ModelSamplingSD3`、`WanImageToVideo`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`、`GetImageSize`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LayerUtility: ImageScaleByAspectRatio`、`Primitive integer [Crystools]`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、GetImageSize、GetImageSize、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
