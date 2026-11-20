---
key: 平台全量/控制+参考(Wan2.1-VACE-14B)_1923042463525892097.json
name: 控制+参考(Wan2.1-VACE-14B)_1923042463525892097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/控制+参考(Wan2.1-VACE-14B)_1923042463525892097.json
hash: f58ecd4d2de24c70
coverage: 0.923077
learned_at: 2026-11-14 02:09:34
nodes: [GetNode, WanVideoDecode, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoVACEEncode, GetImageSizeAndCount, VHS_VideoCombine, PreviewImage, WanVideoEnhanceAVideo, WanVideoSLG, ImageResizeKJ, AIO_Preprocessor, WanVideoSampler, WanVideoExperimentalArgs, WanVideoBlockSwap, WanVideoTextEncode, ImageResizeKJ, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoVACEModelSelect, WanVideoTeaCache, INTConstant, INTConstant, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/控制+参考(Wan2.1-VACE-14B)_1923042463525892097.json

> 来源文件 `comfyui_library/workflows/平台全量/控制+参考(Wan2.1-VACE-14B)_1923042463525892097.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（26 个）：
- `GetNode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoVACEEncode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `PreviewImage`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `ImageResizeKJ`
- `AIO_Preprocessor`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `ImageResizeKJ`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEModelSelect`
- `WanVideoTeaCache`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`WanVideoDecode`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoVACEEncode`、`GetImageSizeAndCount`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`ImageResizeKJ`、`AIO_Preprocessor`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoVACEModelSelect`、`WanVideoTeaCache`、`INTConstant`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、GetImageSizeAndCount
