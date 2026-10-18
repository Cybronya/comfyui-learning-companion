---
key: 视频生成/图生视频/Wan2.2 多合一极速模型 Rapid-AIO-Mega 【图生视频】_1968241987252047874.json
name: Wan2.2 多合一极速模型 Rapid-AIO-Mega 【图生视频】_1968241987252047874.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 多合一极速模型 Rapid-AIO-Mega 【图生视频】_1968241987252047874.json
hash: e81f4a1989a31d12
coverage: 0.913043
learned_at: 2026-10-15 22:31:44
nodes: [ModelSamplingSD3, ImageResizeKJ, VAEDecode, CLIPTextEncode, LoadImage, ImageResizeKJ, LoadImage, KSampler, WanVaceToVideo, VHS_LoadVideo, DWPreprocessor, Zoe-DepthMapPreprocessor, ImageBlend, CheckpointLoaderSimple, CLIPTextEncode, Fast Groups Bypasser (rgthree), Primitive integer [Crystools], INTConstant, Primitive integer [Crystools], ImageResizeKJ, WanVideoVACEStartToEndFrame, VHS_VideoCombine, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 7567358653673, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 多合一极速模型 Rapid-AIO-Mega 【图生视频】_1968241987252047874.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1968241987252047874.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（23 个）：
- `ModelSamplingSD3`
- `ImageResizeKJ`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ImageResizeKJ`
- `LoadImage`
- `KSampler` ★核心
- `WanVaceToVideo`
- `VHS_LoadVideo`
- `DWPreprocessor`
- `Zoe-DepthMapPreprocessor`
- `ImageBlend`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Primitive integer [Crystools]`
- `INTConstant`
- `Primitive integer [Crystools]`
- `ImageResizeKJ`
- `WanVideoVACEStartToEndFrame`
- `VHS_VideoCombine`
- `Note`

## 关键参数

- `seed` = `7567358653673`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`ModelSamplingSD3`、`ImageResizeKJ`、`VAEDecode`、`CLIPTextEncode`、`LoadImage`、`KSampler`、`WanVaceToVideo`、`VHS_LoadVideo`、`DWPreprocessor`、`Zoe-DepthMapPreprocessor`、`ImageBlend`、`CheckpointLoaderSimple`、`Primitive integer [Crystools]`、`INTConstant`、`WanVideoVACEStartToEndFrame`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、Zoe-DepthMapPreprocessor、ImageResizeKJ、ImageBlend

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
