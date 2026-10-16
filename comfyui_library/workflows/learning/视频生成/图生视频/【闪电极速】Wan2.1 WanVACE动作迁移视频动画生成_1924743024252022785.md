---
key: 视频生成/图生视频/【闪电极速】Wan2.1 WanVACE动作迁移视频动画生成_1924743024252022785.json
name: 【闪电极速】Wan2.1 WanVACE动作迁移视频动画生成_1924743024252022785.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1924743024252022785.json
hash: 4dac467f28bcf18c
coverage: 0.663636
learned_at: 2026-10-15 22:29:50
nodes: [MarkdownNote, Note, SetNode, GetNode, SetNode, GetNode, WanVideoVACEStartToEndFrame, GetImageSizeAndCount, MaskPreview+, WanVideoSLG, WanVideoExperimentalArgs, GetNode, GetNode, GetNode, GetNode, EmptyImage, AddLabel, AddLabel, ImageConcatMulti, GetImageSizeAndCount, ImageConcatMulti, SetNode, ImageResizeKJ, SetNode, VHS_VideoCombine, GetNode, WanVideoDecode, WanVideoTextEncode, LoadImage, LoadImage, PreviewImage, GetNode, GetNode, WanVideoSLG, WanVideoExperimentalArgs, GetNode, GetNode, EmptyImage, ImageConcatMulti, ImageConcatMulti, GetNode, GetNode, AddLabel, GetNode, AddLabel, SetNode, WanVideoVACEEncode, WanVideoVACEEncode, SetNode, WanVideoTeaCache, WanVideoTeaCache, GetNode, GetNode, GetNode, GetNode, EmptyImage, ImageConcatMulti, GetImageSizeAndCount, GetNode, WanVideoDecode, WanVideoTextEncode, WanVideoTeaCache, VHS_LoadVideo, ImageResizeKJ, SetNode, GetNode, WanVideoExperimentalArgs, WanVideoSLG, GetImageSizeAndCount, PreviewImage, GetImageRangeFromBatch, MaskPreview+, GetImageRangeFromBatch, WanVideoVACEEncode, ImagePadKJ, VHS_VideoCombine, AddLabel, WanVideoSampler, WanVideoSampler, WanVideoSampler, MarkdownNote, Note, Note, Note, WanVideoTextEncode, WanVideoDecode, GetImageSizeAndCount, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, ImagePadKJ, ImageResizeKJ, ImageResizeKJ, ImageResize+, SetNode, GetImageSizeAndCount, WanVideoVACEModelSelect, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTorchCompileSettings, DownloadAndLoadDepthAnythingV2Model, DepthAnything_V2, MimicMotionGetPoses, VHS_VideoCombine, ImageResizeKJ, VHS_VideoCombine, VHS_LoadVideo, LoadImage, Fast Groups Bypasser (rgthree), VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/【闪电极速】Wan2.1 WanVACE动作迁移视频动画生成_1924743024252022785.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1924743024252022785.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（110 个）：
- `MarkdownNote`
- `Note`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoVACEStartToEndFrame`
- `GetImageSizeAndCount`
- `MaskPreview+`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `SetNode`
- `ImageResizeKJ`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `AddLabel`
- `GetNode`
- `AddLabel`
- `SetNode`
- `WanVideoVACEEncode`
- `WanVideoVACEEncode`
- `SetNode`
- `WanVideoTeaCache`
- `WanVideoTeaCache`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `WanVideoTeaCache`
- `VHS_LoadVideo`
- `ImageResizeKJ`
- `SetNode`
- `GetNode`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `GetImageSizeAndCount`
- `PreviewImage`
- `GetImageRangeFromBatch`
- `MaskPreview+`
- `GetImageRangeFromBatch`
- `WanVideoVACEEncode`
- `ImagePadKJ`
- `VHS_VideoCombine`
- `AddLabel`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `MarkdownNote`
- `Note`
- `Note`
- `Note`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `ImagePadKJ`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `ImageResize+`
- `SetNode`
- `GetImageSizeAndCount`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `DownloadAndLoadDepthAnythingV2Model`
- `DepthAnything_V2`
- `MimicMotionGetPoses`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`

## 知识

覆盖率 **66%**（73/110）

**有卡**：`WanVideoVACEStartToEndFrame`、`GetImageSizeAndCount`、`MaskPreview+`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`EmptyImage`、`AddLabel`、`ImageConcatMulti`、`ImageResizeKJ`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoTextEncode`、`LoadImage`、`WanVideoVACEEncode`、`WanVideoTeaCache`、`VHS_LoadVideo`、`GetImageRangeFromBatch`、`ImagePadKJ`、`WanVideoSampler`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`ImageResize+`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`DownloadAndLoadDepthAnythingV2Model`、`DepthAnything_V2`、`MimicMotionGetPoses`

**用到的条目**：LoadImage、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
