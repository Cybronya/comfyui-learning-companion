---
key: 视频生成/文生视频/【多功能】Wan2.2 文生图 视频参考 动作迁移Rapid-AIO-Mega_1968469960844562434.json
name: 【多功能】Wan2.2 文生图 视频参考 动作迁移Rapid-AIO-Mega_1968469960844562434.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1968469960844562434.json
hash: 0cb196dd041a829f
coverage: 0.92
learned_at: 2026-10-15 22:43:45
nodes: [ModelSamplingSD3, ImageResizeKJ, VAEDecode, CLIPTextEncode, KSampler, WanVaceToVideo, CheckpointLoaderSimple, Primitive integer [Crystools], INTConstant, Primitive integer [Crystools], VHS_LoadVideo, ImageResizeKJ, DWPreprocessor, ImageBlend, Zoe-DepthMapPreprocessor, CLIPTextEncode, LoadImage, LoadImage, Note, ImageResizeKJ, WanVideoVACEStartToEndFrame, VHS_VideoCombine, Fast Groups Bypasser (rgthree), VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 7567358653673, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/【多功能】Wan2.2 文生图 视频参考 动作迁移Rapid-AIO-Mega_1968469960844562434.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1968469960844562434.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `ModelSamplingSD3`
- `ImageResizeKJ`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `WanVaceToVideo`
- `CheckpointLoaderSimple` ★核心
- `Primitive integer [Crystools]`
- `INTConstant`
- `Primitive integer [Crystools]`
- `VHS_LoadVideo`
- `ImageResizeKJ`
- `DWPreprocessor`
- `ImageBlend`
- `Zoe-DepthMapPreprocessor`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `Note`
- `ImageResizeKJ`
- `WanVideoVACEStartToEndFrame`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

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

**有卡**：`ModelSamplingSD3`、`ImageResizeKJ`、`VAEDecode`、`CLIPTextEncode`、`KSampler`、`WanVaceToVideo`、`CheckpointLoaderSimple`、`Primitive integer [Crystools]`、`INTConstant`、`VHS_LoadVideo`、`DWPreprocessor`、`ImageBlend`、`Zoe-DepthMapPreprocessor`、`LoadImage`、`WanVideoVACEStartToEndFrame`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、Zoe-DepthMapPreprocessor、ImageResizeKJ、ImageBlend

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
