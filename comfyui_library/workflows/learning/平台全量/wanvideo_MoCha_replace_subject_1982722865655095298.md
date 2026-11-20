---
key: 平台全量/wanvideo_MoCha_replace_subject_1982722865655095298.json
name: wanvideo_MoCha_replace_subject_1982722865655095298
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wanvideo_MoCha_replace_subject_1982722865655095298.json
hash: 84dc6993100b3e86
coverage: 0.490566
learned_at: 2026-11-14 01:20:10
nodes: [WanVideoModelLoader, SetNode, SetNode, SetNode, SetNode, DownloadAndLoadSAM2Model, Sam2Segmentation, GetNode, GrowMaskWithBlur, SetNode, MaskPreview, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoVAELoader, ImageResizeKJv2, RMBG, PreviewImage, GetNode, GetNode, PreviewImage, MarkdownNote, MarkdownNote, WanVideoSampler, GetNode, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, WanVideoDecode, GetNode, ImageConcanate, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, ImageResizeKJv2, GetImageRangeFromBatch, PointsEditor, LoadImage, SetNode, GetNode, GetNode, ImageResizeKJv2, RMBG, PreviewImage, SetNode, LoadImage, WanVideoSetBlockSwap, SetNode, SetNode, MarkdownNote, GetNode, GetNode, MochaEmbeds]
patterns: []
missing: []
---

# 平台全量/wanvideo_MoCha_replace_subject_1982722865655095298.json

> 来源文件 `comfyui_library/workflows/平台全量/wanvideo_MoCha_replace_subject_1982722865655095298.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（53 个）：
- `WanVideoModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `GetNode`
- `GrowMaskWithBlur`
- `SetNode`
- `MaskPreview`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `RMBG`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `MarkdownNote`
- `MarkdownNote`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoDecode`
- `GetNode`
- `ImageConcanate`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `GetImageRangeFromBatch`
- `PointsEditor`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `RMBG`
- `PreviewImage`
- `SetNode`
- `LoadImage`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `MochaEmbeds`

## 知识

覆盖率 **49%**（26/53）

**有卡**：`WanVideoModelLoader`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMaskWithBlur`、`MaskPreview`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`ImageResizeKJv2`、`RMBG`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`ImageConcanate`、`VHS_VideoCombine`、`VHS_LoadVideo`、`GetImageRangeFromBatch`、`PointsEditor`、`LoadImage`、`WanVideoSetBlockSwap`、`MochaEmbeds`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、ImageResizeKJv2、MaskPreview
