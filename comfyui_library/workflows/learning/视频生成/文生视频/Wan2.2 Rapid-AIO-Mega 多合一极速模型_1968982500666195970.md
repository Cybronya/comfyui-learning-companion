---
key: 视频生成/文生视频/Wan2.2 Rapid-AIO-Mega 多合一极速模型_1968982500666195970.json
name: Wan2.2 Rapid-AIO-Mega 多合一极速模型_1968982500666195970.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Rapid-AIO-Mega 多合一极速模型_1968982500666195970.json
hash: fefee856af5a121b
coverage: 0.913043
learned_at: 2026-10-15 22:43:46
nodes: [ModelSamplingSD3, ImageResizeKJ, VAEDecode, ImageResizeKJ, KSampler, DWPreprocessor, Zoe-DepthMapPreprocessor, ImageBlend, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), INTConstant, Primitive integer [Crystools], ImageResizeKJ, WanVideoVACEStartToEndFrame, Note, VHS_VideoCombine, CLIPTextEncode, Primitive integer [Crystools], CLIPTextEncode, LoadImage, LoadImage, WanVaceToVideo, VHS_LoadVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 7567358653673, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2 Rapid-AIO-Mega 多合一极速模型_1968982500666195970.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1968982500666195970.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（23 个）：
- `ModelSamplingSD3`
- `ImageResizeKJ`
- `VAEDecode` ★核心
- `ImageResizeKJ`
- `KSampler` ★核心
- `DWPreprocessor`
- `Zoe-DepthMapPreprocessor`
- `ImageBlend`
- `CheckpointLoaderSimple` ★核心
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `Primitive integer [Crystools]`
- `ImageResizeKJ`
- `WanVideoVACEStartToEndFrame`
- `Note`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `Primitive integer [Crystools]`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `WanVaceToVideo`
- `VHS_LoadVideo`

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

**有卡**：`ModelSamplingSD3`、`ImageResizeKJ`、`VAEDecode`、`KSampler`、`DWPreprocessor`、`Zoe-DepthMapPreprocessor`、`ImageBlend`、`CheckpointLoaderSimple`、`INTConstant`、`Primitive integer [Crystools]`、`WanVideoVACEStartToEndFrame`、`VHS_VideoCombine`、`CLIPTextEncode`、`LoadImage`、`WanVaceToVideo`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、Zoe-DepthMapPreprocessor、ImageResizeKJ、ImageBlend

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
