---
key: 平台全量/CausVid-3步720P控制+参考(Wan2.1&MoviiGen&Skyreels)_1923413100647600129.json
name: CausVid-3步720P控制+参考(Wan2.1&MoviiGen&Skyreels)_1923413100647600129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/CausVid-3步720P控制+参考(Wan2.1&MoviiGen&Skyreels)_1923413100647600129.json
hash: 8d4ce21c270d60be
coverage: 0.962963
learned_at: 2026-11-14 00:22:07
nodes: [VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoVAELoader, GetImageSizeAndCount, VHS_VideoCombine, WanVideoEnhanceAVideo, WanVideoSLG, AIO_Preprocessor, WanVideoExperimentalArgs, WanVideoBlockSwap, WanVideoTextEncode, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoVACEModelSelect, WanVideoTeaCache, INTConstant, WanVideoDecode, WanVideoLoraSelect, INTConstant, VHS_LoadVideo, ImageResizeKJ, PreviewImage, WanVideoVACEEncode, WanVideoSampler, ImageResizeKJ, RH_Captioner, LoadImage, RH_Captioner, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoVAELoader, GetImageSizeAndCount, VHS_VideoCombine, WanVideoEnhanceAVideo, WanVideoSLG, AIO_Preprocessor, WanVideoExperimentalArgs, WanVideoBlockSwap, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEModelSelect, WanVideoTeaCache, INTConstant, WanVideoDecode, WanVideoLoraSelect, INTConstant, VHS_LoadVideo, ImageResizeKJ, PreviewImage, WanVideoVACEEncode, WanVideoSampler, ImageResizeKJ, LoadImage, RH_Captioner, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoVAELoader, GetImageSizeAndCount, VHS_VideoCombine, WanVideoEnhanceAVideo, WanVideoSLG, AIO_Preprocessor, WanVideoExperimentalArgs, WanVideoBlockSwap, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEModelSelect, WanVideoTeaCache, INTConstant, WanVideoDecode, WanVideoLoraSelect, INTConstant, VHS_LoadVideo, ImageResizeKJ, PreviewImage, WanVideoVACEEncode, WanVideoSampler, ImageResizeKJ, LoadImage, WanVideoModelLoader, WanVideoModelLoader, RH_Captioner, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoVAELoader, GetImageSizeAndCount, VHS_VideoCombine, WanVideoEnhanceAVideo, WanVideoSLG, AIO_Preprocessor, WanVideoExperimentalArgs, WanVideoBlockSwap, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEModelSelect, WanVideoTeaCache, INTConstant, WanVideoDecode, WanVideoLoraSelect, INTConstant, VHS_LoadVideo, ImageResizeKJ, PreviewImage, WanVideoVACEEncode, WanVideoSampler, ImageResizeKJ, WanVideoModelLoader, LoadImage]
patterns: []
missing: []
---

# 平台全量/CausVid-3步720P控制+参考(Wan2.1&MoviiGen&Skyreels)_1923413100647600129.json

> 来源文件 `comfyui_library/workflows/平台全量/CausVid-3步720P控制+参考(Wan2.1&MoviiGen&Skyreels)_1923413100647600129.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（108 个）：
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `AIO_Preprocessor`
- `WanVideoExperimentalArgs`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEModelSelect`
- `WanVideoTeaCache`
- `INTConstant`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `INTConstant`
- `VHS_LoadVideo`
- `ImageResizeKJ`
- `PreviewImage`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `ImageResizeKJ`
- `RH_Captioner`
- `LoadImage`
- `RH_Captioner`
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `AIO_Preprocessor`
- `WanVideoExperimentalArgs`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEModelSelect`
- `WanVideoTeaCache`
- `INTConstant`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `INTConstant`
- `VHS_LoadVideo`
- `ImageResizeKJ`
- `PreviewImage`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `ImageResizeKJ`
- `LoadImage`
- `RH_Captioner`
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `AIO_Preprocessor`
- `WanVideoExperimentalArgs`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEModelSelect`
- `WanVideoTeaCache`
- `INTConstant`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `INTConstant`
- `VHS_LoadVideo`
- `ImageResizeKJ`
- `PreviewImage`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `ImageResizeKJ`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `RH_Captioner`
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `AIO_Preprocessor`
- `WanVideoExperimentalArgs`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEModelSelect`
- `WanVideoTeaCache`
- `INTConstant`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `INTConstant`
- `VHS_LoadVideo`
- `ImageResizeKJ`
- `PreviewImage`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `ImageResizeKJ`
- `WanVideoModelLoader`
- `LoadImage`

## 知识

覆盖率 **96%**（104/108）

**有卡**：`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`AIO_Preprocessor`、`WanVideoExperimentalArgs`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoVACEModelSelect`、`WanVideoTeaCache`、`INTConstant`、`WanVideoDecode`、`WanVideoLoraSelect`、`VHS_LoadVideo`、`ImageResizeKJ`、`WanVideoVACEEncode`、`WanVideoSampler`、`RH_Captioner`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect
