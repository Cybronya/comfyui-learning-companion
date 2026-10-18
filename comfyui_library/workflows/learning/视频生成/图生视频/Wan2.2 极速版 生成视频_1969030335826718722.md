---
key: 视频生成/图生视频/Wan2.2 极速版 生成视频_1969030335826718722.json
name: Wan2.2 极速版 生成视频_1969030335826718722.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 极速版 生成视频_1969030335826718722.json
hash: 0e0d1fde906840f6
coverage: 0.92
learned_at: 2026-10-15 22:31:47
nodes: [ModelSamplingSD3, ImageResizeKJ, VAEDecode, CLIPTextEncode, ImageResizeKJ, KSampler, WanVaceToVideo, VHS_LoadVideo, DWPreprocessor, Zoe-DepthMapPreprocessor, ImageBlend, CheckpointLoaderSimple, CLIPTextEncode, Primitive integer [Crystools], INTConstant, Primitive integer [Crystools], ImageResizeKJ, WanVideoVACEStartToEndFrame, VHS_VideoCombine, Note, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 7567358653673, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 极速版 生成视频_1969030335826718722.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969030335826718722.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `ModelSamplingSD3`
- `ImageResizeKJ`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `KSampler` ★核心
- `WanVaceToVideo`
- `VHS_LoadVideo`
- `DWPreprocessor`
- `Zoe-DepthMapPreprocessor`
- `ImageBlend`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `Primitive integer [Crystools]`
- `INTConstant`
- `Primitive integer [Crystools]`
- `ImageResizeKJ`
- `WanVideoVACEStartToEndFrame`
- `VHS_VideoCombine`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `7567358653673`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`ModelSamplingSD3`、`ImageResizeKJ`、`VAEDecode`、`CLIPTextEncode`、`KSampler`、`WanVaceToVideo`、`VHS_LoadVideo`、`DWPreprocessor`、`Zoe-DepthMapPreprocessor`、`ImageBlend`、`CheckpointLoaderSimple`、`Primitive integer [Crystools]`、`INTConstant`、`WanVideoVACEStartToEndFrame`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、Zoe-DepthMapPreprocessor、ImageResizeKJ、ImageBlend

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
