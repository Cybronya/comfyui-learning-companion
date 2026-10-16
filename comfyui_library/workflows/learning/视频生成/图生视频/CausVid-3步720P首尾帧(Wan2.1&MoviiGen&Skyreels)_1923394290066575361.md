---
key: 视频生成/图生视频/CausVid-3步720P首尾帧(Wan2.1&MoviiGen&Skyreels)_1923394290066575361.json
name: CausVid-3步720P首尾帧(Wan2.1&MoviiGen&Skyreels)_1923394290066575361.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1923394290066575361.json
hash: 27e3d4da6b3893d0
coverage: 1
learned_at: 2026-10-15 22:29:48
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, GetImageSizeAndCount, WanVideoVACEModelSelect, WanVideoTorchCompileSettings, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoExperimentalArgs, WanVideoSLG, VHS_VideoCombine, WanVideoLoraSelect, WanVideoModelLoader, ImageResizeKJ, WanVideoDecode, WanVideoBlockSwap, WanVideoSampler, LoadImage, String Literal, WanVideoVACEEncode, ImageResizeKJ, INTConstant, INTConstant, INTConstant, LoadImage, WanVideoVACEStartToEndFrame, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, GetImageSizeAndCount, WanVideoVACEModelSelect, WanVideoTorchCompileSettings, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoExperimentalArgs, WanVideoSLG, VHS_VideoCombine, WanVideoLoraSelect, ImageResizeKJ, WanVideoDecode, WanVideoBlockSwap, WanVideoSampler, LoadImage, String Literal, WanVideoVACEEncode, ImageResizeKJ, INTConstant, INTConstant, INTConstant, LoadImage, WanVideoVACEStartToEndFrame, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, GetImageSizeAndCount, WanVideoVACEModelSelect, WanVideoTorchCompileSettings, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoExperimentalArgs, WanVideoSLG, VHS_VideoCombine, WanVideoLoraSelect, ImageResizeKJ, WanVideoDecode, WanVideoBlockSwap, WanVideoSampler, LoadImage, String Literal, WanVideoVACEEncode, ImageResizeKJ, INTConstant, INTConstant, INTConstant, LoadImage, WanVideoVACEStartToEndFrame, WanVideoModelLoader, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/CausVid-3步720P首尾帧(Wan2.1&MoviiGen&Skyreels)_1923394290066575361.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1923394290066575361.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（78 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `GetImageSizeAndCount`
- `WanVideoVACEModelSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `ImageResizeKJ`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `LoadImage`
- `String Literal`
- `WanVideoVACEEncode`
- `ImageResizeKJ`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `WanVideoVACEStartToEndFrame`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `GetImageSizeAndCount`
- `WanVideoVACEModelSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `ImageResizeKJ`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `LoadImage`
- `String Literal`
- `WanVideoVACEEncode`
- `ImageResizeKJ`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `WanVideoVACEStartToEndFrame`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `GetImageSizeAndCount`
- `WanVideoVACEModelSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `ImageResizeKJ`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `LoadImage`
- `String Literal`
- `WanVideoVACEEncode`
- `ImageResizeKJ`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `WanVideoVACEStartToEndFrame`
- `WanVideoModelLoader`
- `WanVideoModelLoader`

## 知识

覆盖率 **100%**（78/78）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`GetImageSizeAndCount`、`WanVideoVACEModelSelect`、`WanVideoTorchCompileSettings`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`ImageResizeKJ`、`WanVideoDecode`、`WanVideoBlockSwap`、`WanVideoSampler`、`LoadImage`、`String Literal`、`WanVideoVACEEncode`、`INTConstant`、`WanVideoVACEStartToEndFrame`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
