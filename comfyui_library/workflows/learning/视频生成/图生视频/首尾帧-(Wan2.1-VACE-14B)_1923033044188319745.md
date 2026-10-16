---
key: 视频生成/图生视频/首尾帧-(Wan2.1-VACE-14B)_1923033044188319745.json
name: 首尾帧-(Wan2.1-VACE-14B)_1923033044188319745.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1923033044188319745.json
hash: f58f55c10965df38
coverage: 1
learned_at: 2026-10-15 22:29:47
nodes: [WanVideoVACEEncode, WanVideoDecode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, GetImageSizeAndCount, WanVideoVACEModelSelect, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoExperimentalArgs, WanVideoSLG, WanVideoSampler, ImageResizeKJ, LoadImage, WanVideoVACEStartToEndFrame, ImageResizeKJ, LoadImage, INTConstant, INTConstant, INTConstant, String Literal, WanVideoBlockSwap, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧-(Wan2.1-VACE-14B)_1923033044188319745.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1923033044188319745.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `WanVideoVACEEncode`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `GetImageSizeAndCount`
- `WanVideoVACEModelSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `ImageResizeKJ`
- `LoadImage`
- `WanVideoVACEStartToEndFrame`
- `ImageResizeKJ`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `String Literal`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`WanVideoVACEEncode`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`GetImageSizeAndCount`、`WanVideoVACEModelSelect`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoSampler`、`ImageResizeKJ`、`LoadImage`、`WanVideoVACEStartToEndFrame`、`INTConstant`、`String Literal`、`WanVideoBlockSwap`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、GetImageSizeAndCount
