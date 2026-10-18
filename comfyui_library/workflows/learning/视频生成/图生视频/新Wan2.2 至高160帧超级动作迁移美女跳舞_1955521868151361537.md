---
key: 视频生成/图生视频/新Wan2.2 至高160帧超级动作迁移美女跳舞_1955521868151361537.json
name: 新Wan2.2 至高160帧超级动作迁移美女跳舞_1955521868151361537.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/新Wan2.2 至高160帧超级动作迁移美女跳舞_1955521868151361537.json
hash: b24057a91fe9d74e
coverage: 0.708333
learned_at: 2026-10-15 22:31:09
nodes: [GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, WanVideoExperimentalArgs, SetNode, SetNode, ImageResizeKJ, AddLabel, GetNode, AddLabel, ImageConcatMulti, WanVideoDecode, WanVideoSLG, WanVideoVACEModelSelect, WanVideoVACEEncode, EmptyImage, ImageConcatMulti, Note, WanVideoTextEncode, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, UpscaleModelLoader, ImageUpscaleWithModel, WanVideoSampler, AIO_Preprocessor, WanVideoTeaCache, Note, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, LoadImage, VHS_LoadVideo, ImageResizeKJ, RHHiddenNodes, MarkdownNote, WanVideoVAELoader, WanVideoLoraSelect, RHHiddenNodes, MarkdownNote, Note, easy int, ColorMatch, GetImageSizeAndCount, GetImageSizeAndCount, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/新Wan2.2 至高160帧超级动作迁移美女跳舞_1955521868151361537.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955521868151361537.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（48 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoExperimentalArgs`
- `SetNode`
- `SetNode`
- `ImageResizeKJ`
- `AddLabel`
- `GetNode`
- `AddLabel`
- `ImageConcatMulti`
- `WanVideoDecode`
- `WanVideoSLG`
- `WanVideoVACEModelSelect`
- `WanVideoVACEEncode`
- `EmptyImage`
- `ImageConcatMulti`
- `Note`
- `WanVideoTextEncode`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `WanVideoSampler` ★核心
- `AIO_Preprocessor`
- `WanVideoTeaCache`
- `Note`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `LoadImage`
- `VHS_LoadVideo`
- `ImageResizeKJ`
- `RHHiddenNodes`
- `MarkdownNote`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `RHHiddenNodes`
- `MarkdownNote`
- `Note`
- `easy int`
- `ColorMatch`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **71%**（34/48）

**有卡**：`WanVideoExperimentalArgs`、`ImageResizeKJ`、`AddLabel`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoSLG`、`WanVideoVACEModelSelect`、`WanVideoVACEEncode`、`EmptyImage`、`WanVideoTextEncode`、`LayerUtility: PurgeVRAM V2`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`WanVideoSampler`、`AIO_Preprocessor`、`WanVideoTeaCache`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`LoadImage`、`VHS_LoadVideo`、`RHHiddenNodes`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`easy int`、`ColorMatch`、`GetImageSizeAndCount`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
