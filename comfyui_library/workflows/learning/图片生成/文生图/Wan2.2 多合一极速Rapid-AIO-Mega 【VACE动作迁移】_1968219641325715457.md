---
key: 图片生成/文生图/Wan2.2 多合一极速Rapid-AIO-Mega 【VACE动作迁移】_1968219641325715457.json
name: Wan2.2 多合一极速Rapid-AIO-Mega 【VACE动作迁移】_1968219641325715457
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 多合一极速Rapid-AIO-Mega 【VACE动作迁移】_1968219641325715457.json
hash: 99bc65a02887ca23
coverage: 0.92
learned_at: 2026-10-15 22:27:35
nodes: [ModelSamplingSD3, Note, ImageResizeKJ, VAEDecode, CLIPTextEncode, LoadImage, ImageResizeKJ, LoadImage, VHS_VideoCombine, KSampler, WanVaceToVideo, VHS_LoadVideo, DWPreprocessor, Zoe-DepthMapPreprocessor, ImageBlend, VHS_VideoCombine, VHS_VideoCombine, CheckpointLoaderSimple, CLIPTextEncode, Fast Groups Bypasser (rgthree), Primitive integer [Crystools], INTConstant, Primitive integer [Crystools], ImageResizeKJ, WanVideoVACEStartToEndFrame]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 7567358653673, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Wan2.2 多合一极速Rapid-AIO-Mega 【VACE动作迁移】_1968219641325715457.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2 多合一极速Rapid-AIO-Mega 【VACE动作迁移】_1968219641325715457.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `ModelSamplingSD3`
- `Note`
- `ImageResizeKJ`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ImageResizeKJ`
- `LoadImage`
- `VHS_VideoCombine`
- `KSampler` ★核心
- `WanVaceToVideo`
- `VHS_LoadVideo`
- `DWPreprocessor`
- `Zoe-DepthMapPreprocessor`
- `ImageBlend`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Primitive integer [Crystools]`
- `INTConstant`
- `Primitive integer [Crystools]`
- `ImageResizeKJ`
- `WanVideoVACEStartToEndFrame`

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

**有卡**：`ModelSamplingSD3`、`ImageResizeKJ`、`VAEDecode`、`CLIPTextEncode`、`LoadImage`、`VHS_VideoCombine`、`KSampler`、`WanVaceToVideo`、`VHS_LoadVideo`、`DWPreprocessor`、`Zoe-DepthMapPreprocessor`、`ImageBlend`、`CheckpointLoaderSimple`、`Primitive integer [Crystools]`、`INTConstant`、`WanVideoVACEStartToEndFrame`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、Zoe-DepthMapPreprocessor、ImageResizeKJ、ImageBlend

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
