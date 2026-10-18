---
key: 视频生成/图生视频/陆老师_Wan2.2 多合一极速模型 Rapid-AIO-Mega 【图生视频】_1971574546153336834.json
name: 陆老师_Wan2.2 多合一极速模型 Rapid-AIO-Mega 【图生视频】_1971574546153336834.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/陆老师_Wan2.2 多合一极速模型 Rapid-AIO-Mega 【图生视频】_1971574546153336834.json
hash: b3a7e9a6dde5aeb0
coverage: 0.896552
learned_at: 2026-10-15 22:31:57
nodes: [ImageResizeKJ, Primitive integer [Crystools], Primitive integer [Crystools], LoadImage, ImageResizeKJ, ImageResizeKJ, DWPreprocessor, Zoe-DepthMapPreprocessor, ImageBlend, CLIPTextEncode, CheckpointLoaderSimple, VAEDecode, Note, SimpleMath+, ModelSamplingSD3, SaveImage, VHS_VideoCombine, LoadImage, RH_Nano_Banana_Image2Image, CLIPTextEncode, WanVaceToVideo, WanVideoVACEStartToEndFrame, KSampler, LoadImage, VHS_LoadVideo, Reroute, Fast Groups Bypasser (rgthree), INTConstant, TextBox]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 7567358653673, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/陆老师_Wan2.2 多合一极速模型 Rapid-AIO-Mega 【图生视频】_1971574546153336834.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1971574546153336834.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `ImageResizeKJ`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `LoadImage`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `DWPreprocessor`
- `Zoe-DepthMapPreprocessor`
- `ImageBlend`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `Note`
- `SimpleMath+`
- `ModelSamplingSD3`
- `SaveImage`
- `VHS_VideoCombine`
- `LoadImage`
- `RH_Nano_Banana_Image2Image`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `KSampler` ★核心
- `LoadImage`
- `VHS_LoadVideo`
- `Reroute`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `TextBox`

## 关键参数

- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`
- `seed` = `7567358653673`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`ImageResizeKJ`、`Primitive integer [Crystools]`、`LoadImage`、`DWPreprocessor`、`Zoe-DepthMapPreprocessor`、`ImageBlend`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`VAEDecode`、`SimpleMath+`、`ModelSamplingSD3`、`SaveImage`、`VHS_VideoCombine`、`RH_Nano_Banana_Image2Image`、`WanVaceToVideo`、`WanVideoVACEStartToEndFrame`、`KSampler`、`VHS_LoadVideo`、`INTConstant`、`TextBox`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、Zoe-DepthMapPreprocessor、ImageResizeKJ、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
