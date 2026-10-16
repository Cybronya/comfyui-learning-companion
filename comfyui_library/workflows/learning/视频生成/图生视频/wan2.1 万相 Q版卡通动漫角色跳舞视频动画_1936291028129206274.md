---
key: 视频生成/图生视频/wan2.1 万相 Q版卡通动漫角色跳舞视频动画_1936291028129206274.json
name: wan2.1 万相 Q版卡通动漫角色跳舞视频动画_1936291028129206274.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1936291028129206274.json
hash: 26ba3be7f4223ac9
coverage: 0.603448
learned_at: 2026-10-15 22:30:25
nodes: [SetNode, ImageResizeKJv2, GetImageSizeAndCount, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoVACEModelSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, SetNode, SetNode, GetNode, GetNode, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTeaCache, ImageConcatMulti, EmptyImage, SetNode, GetNode, GetNode, GetNode, AddLabel, GetNode, AddLabel, GetNode, SetNode, SetNode, SetNode, WanVideoDecode, WanVideoSampler, ImageResizeKJv2, ImageResizeKJv2, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, WanVideoVACEStartToEndFrame, VHS_LoadVideo, GetImageSizeAndCount, ImageConcatMulti, ImageResize+, VHS_VideoInfo, WanVideoUniAnimateDWPoseDetector, ImageResize+, VHS_VideoCombine, Fast Groups Bypasser (rgthree), LoadImage, VHS_LoadVideo, LoadImage, WanVideoLoraSelect, GetNode, GetNode, VHS_VideoCombine, WanVideoVACEEncode, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1 万相 Q版卡通动漫角色跳舞视频动画_1936291028129206274.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1936291028129206274.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（58 个）：
- `SetNode`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `ImageConcatMulti`
- `EmptyImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `AddLabel`
- `GetNode`
- `AddLabel`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoVACEStartToEndFrame`
- `VHS_LoadVideo`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageResize+`
- `VHS_VideoInfo`
- `WanVideoUniAnimateDWPoseDetector`
- `ImageResize+`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoLoraSelect`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoVACEEncode`
- `WanVideoTextEncode`

## 知识

覆盖率 **60%**（35/58）

**有卡**：`ImageResizeKJv2`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoVACEModelSelect`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`ImageConcatMulti`、`EmptyImage`、`AddLabel`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoVACEStartToEndFrame`、`VHS_LoadVideo`、`ImageResize+`、`VHS_VideoInfo`、`WanVideoUniAnimateDWPoseDetector`、`VHS_VideoCombine`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoVACEEncode`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
