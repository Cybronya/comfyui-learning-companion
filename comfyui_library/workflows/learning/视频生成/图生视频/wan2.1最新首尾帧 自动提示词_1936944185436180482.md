---
key: 视频生成/图生视频/wan2.1最新首尾帧 自动提示词_1936944185436180482.json
name: wan2.1最新首尾帧 自动提示词_1936944185436180482.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1最新首尾帧 自动提示词_1936944185436180482.json
hash: 2c8266de86513479
coverage: 0.571429
learned_at: 2026-10-15 22:30:27
nodes: [GetNode, WanVideoDecode, SetNode, GetNode, WanVideoVAELoader, SetNode, GetImageSizeAndCount, WanVideoVACEStartToEndFrame, WanVideoVACEEncode, GetNode, GetNode, ImageResizeKJ, SetNode, GetNode, GetNode, SetNode, ShowText|pysssss, SetNode, GetNode, GetNode, GetNode, LoadWanVideoT5TextEncoder, WanVideoTextEncodeSingle, WanVideoApplyNAG, GetNode, WanVideoMagCache, WanVideoSLG, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoSampler, ImageResizeKJ, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoTextEncodeSingle, easy imageConcat, WD14Tagger|pysssss, SetNode, LoadImage, SetNode, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1最新首尾帧 自动提示词_1936944185436180482.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1936944185436180482.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（42 个）：
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `GetNode`
- `WanVideoVAELoader`
- `SetNode`
- `GetImageSizeAndCount`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVACEEncode`
- `GetNode`
- `GetNode`
- `ImageResizeKJ`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ShowText|pysssss`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncodeSingle`
- `WanVideoApplyNAG`
- `GetNode`
- `WanVideoMagCache`
- `WanVideoSLG`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `ImageResizeKJ`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoTextEncodeSingle`
- `easy imageConcat`
- `WD14Tagger|pysssss`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **57%**（24/42）

**有卡**：`WanVideoDecode`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`WanVideoVACEStartToEndFrame`、`WanVideoVACEEncode`、`ImageResizeKJ`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`WanVideoMagCache`、`WanVideoSLG`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoSampler`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoModelLoader`、`easy imageConcat`、`WD14Tagger|pysssss`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoVACEEncode、GetImageSizeAndCount
