---
key: 视频生成/图生视频/【跳舞视频 】最新wan2.1上传图片生成跳舞视频_1912765246451216385.json
name: 【跳舞视频 】最新wan2.1上传图片生成跳舞视频_1912765246451216385.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【跳舞视频 】最新wan2.1上传图片生成跳舞视频_1912765246451216385.json
hash: 69ce2ee226422146
coverage: 0.942857
learned_at: 2026-10-15 22:29:32
nodes: [WanVideoTorchCompileSettings, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, WanVideoSampler, WanVideoControlEmbeds, WanVideoExperimentalArgs, WanVideoDecode, VHS_VideoCombine, WanVideoBlockSwap, ImageBlend, WanVideoTextEncode, WanVideoClipVisionEncode, LoadImage, WanVideoImageToVideoEncode, ImageResizeKJ, ImageResizeKJ, VHS_LoadVideo, VHS_VideoCombine, JanusModelLoader, JanusImageUnderstanding, AIO_Preprocessor, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, AIO_Preprocessor, WanVideoEncode, Int, Note, easy cleanGpuUsed, easy cleanGpuUsed, ImageUpscaleWithModel, UpscaleModelLoader, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/【跳舞视频 】最新wan2.1上传图片生成跳舞视频_1912765246451216385.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1912765246451216385.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `WanVideoControlEmbeds`
- `WanVideoExperimentalArgs`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `ImageBlend`
- `WanVideoTextEncode`
- `WanVideoClipVisionEncode`
- `LoadImage`
- `WanVideoImageToVideoEncode`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `JanusModelLoader`
- `JanusImageUnderstanding`
- `AIO_Preprocessor`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `AIO_Preprocessor`
- `WanVideoEncode`
- `Int`
- `Note`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoSampler`、`WanVideoControlEmbeds`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`ImageBlend`、`WanVideoTextEncode`、`WanVideoClipVisionEncode`、`LoadImage`、`WanVideoImageToVideoEncode`、`ImageResizeKJ`、`VHS_LoadVideo`、`JanusModelLoader`、`JanusImageUnderstanding`、`AIO_Preprocessor`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoEncode`、`Int`、`easy cleanGpuUsed`、`ImageUpscaleWithModel`、`UpscaleModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
