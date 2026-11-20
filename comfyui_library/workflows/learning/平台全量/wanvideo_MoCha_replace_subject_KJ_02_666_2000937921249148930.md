---
key: 平台全量/wanvideo_MoCha_replace_subject_KJ_02_666_2000937921249148930.json
name: wanvideo_MoCha_replace_subject_KJ_02_666_2000937921249148930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wanvideo_MoCha_replace_subject_KJ_02_666_2000937921249148930.json
hash: e904e2ea147217b6
coverage: 0.581395
learned_at: 2026-11-14 01:20:10
nodes: [PreviewImage, ImageResizeKJv2, SetNode, PreviewImage, MarkdownNote, MochaEmbeds, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, ImageResizeKJv2, MarkdownNote, MarkdownNote, GetNode, GetNode, SetNode, Sam2Segmentation, SetNode, MaskPreview, GrowMaskWithBlur, DownloadAndLoadSAM2Model, WanVideoModelLoader, WanVideoVAELoader, Note, WanVideoLoraSelectMulti, SetNode, SetNode, VHS_VideoCombine, WanVideoDecode, GetNode, VHS_VideoCombine, ImageConcanate, GetNode, PreviewImage, GetImageRangeFromBatch, WanVideoSampler, WanVideoTextEncodeCached, WanVideoBlockSwap, ImageResizeKJv2, GetNode, GetNode, VHS_LoadVideo, LoadImage, LoadImage, PointsEditor]
patterns: []
missing: []
---

# 平台全量/wanvideo_MoCha_replace_subject_KJ_02_666_2000937921249148930.json

> 来源文件 `comfyui_library/workflows/平台全量/wanvideo_MoCha_replace_subject_KJ_02_666_2000937921249148930.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（43 个）：
- `PreviewImage`
- `ImageResizeKJv2`
- `SetNode`
- `PreviewImage`
- `MarkdownNote`
- `MochaEmbeds`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `ImageResizeKJv2`
- `MarkdownNote`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `SetNode`
- `Sam2Segmentation`
- `SetNode`
- `MaskPreview`
- `GrowMaskWithBlur`
- `DownloadAndLoadSAM2Model`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `Note`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `GetNode`
- `VHS_VideoCombine`
- `ImageConcanate`
- `GetNode`
- `PreviewImage`
- `GetImageRangeFromBatch`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `LoadImage`
- `LoadImage`
- `PointsEditor`

## 知识

覆盖率 **58%**（25/43）

**有卡**：`ImageResizeKJv2`、`MochaEmbeds`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`Sam2Segmentation`、`MaskPreview`、`GrowMaskWithBlur`、`DownloadAndLoadSAM2Model`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`WanVideoDecode`、`ImageConcanate`、`GetImageRangeFromBatch`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`LoadImage`、`PointsEditor`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、ImageResizeKJv2、MaskPreview
