---
key: 视频生成/图生视频/wan2.1fun超强控制视频人物动作迁移丝滑不崩脸_1934538219805417473.json
name: wan2.1fun超强控制视频人物动作迁移丝滑不崩脸_1934538219805417473.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1fun超强控制视频人物动作迁移丝滑不崩脸_1934538219805417473.json
hash: e9349bce48a6f3fb
coverage: 0.722222
learned_at: 2026-10-15 22:30:17
nodes: [GetNode, Primitive integer [Crystools], Primitive integer [Crystools], AddLabel, GetNode, AddLabel, Primitive integer [Crystools], ImageResizeKJ, Note, GetNode, GetNode, EmptyImage, easy cleanGpuUsed, Text Concatenate, GetNode, GetNode, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoTorchCompileSettings, SetNode, WanVideoModelLoader, WanVideoVACEModelSelect, SetNode, SetNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, GetNode, WanVideoDecode, Reroute, ImageConcatMulti, WanVideoTextEncode, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, GetImageSizeAndCount, WanVideoVACEEncode, SetNode, ImageResizeKJ, Reroute, GetImageSizeAndCount, ImageConcatMulti, WanVideoSampler, ColorMatch, Text Multiline, RH_Captioner, VHS_VideoCombine, Primitive integer [Crystools], VHS_VideoCombine, SetNode, VHS_LoadVideo, VHS_LoadVideo, LoadImage, AIO_Preprocessor, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1fun超强控制视频人物动作迁移丝滑不崩脸_1934538219805417473.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1934538219805417473.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（54 个）：
- `GetNode`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `AddLabel`
- `GetNode`
- `AddLabel`
- `Primitive integer [Crystools]`
- `ImageResizeKJ`
- `Note`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `easy cleanGpuUsed`
- `Text Concatenate`
- `GetNode`
- `GetNode`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `WanVideoDecode`
- `Reroute`
- `ImageConcatMulti`
- `WanVideoTextEncode`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `GetImageSizeAndCount`
- `WanVideoVACEEncode`
- `SetNode`
- `ImageResizeKJ`
- `Reroute`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `WanVideoSampler` ★核心
- `ColorMatch`
- `Text Multiline`
- `RH_Captioner`
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`
- `VHS_VideoCombine`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `LoadImage`
- `AIO_Preprocessor`
- `VHS_VideoCombine`

## 知识

覆盖率 **72%**（39/54）

**有卡**：`Primitive integer [Crystools]`、`AddLabel`、`ImageResizeKJ`、`EmptyImage`、`easy cleanGpuUsed`、`Text Concatenate`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoTextEncode`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`GetImageSizeAndCount`、`WanVideoVACEEncode`、`WanVideoSampler`、`ColorMatch`、`Text Multiline`、`RH_Captioner`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`、`AIO_Preprocessor`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
