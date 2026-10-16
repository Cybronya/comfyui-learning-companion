---
key: 视频生成/图生视频/（单参版）Wan2.1 Mocha V2V人物视频替换V2（优化加速版）_1980912658343968770.json
name: （单参版）Wan2.1 Mocha V2V人物视频替换V2（优化加速版）_1980912658343968770.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1980912658343968770.json
hash: b3101413f2b7dc6f
coverage: 0.702128
learned_at: 2026-10-15 22:32:35
nodes: [GetNode, GetNode, GetImageRangeFromBatch, MaskPreview, DownloadAndLoadSAM2Model, Sam2Segmentation, SetNode, GrowMask, GetNode, PreviewImage, WanVideoSampler, MochaEmbeds, MarkdownNote, LoadImage, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelectMulti, SetNode, PointsEditor, JWInteger, SetNode, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, ImageConcanate, ImageConcanate, PDIMAGE_LongerSize, MarkdownNote, RMBG, CR Prompt Text, LoadImage, Crop Face, SaveImage, PreviewImage, Load RetinaFace, ImageResizeKJv2, SetNode, PreviewImage, GetNode, SaveImage, VHS_VideoCombine, VHS_VideoCombine, WanVideoDecode, VHS_LoadVideo, VHS_VideoInfo]
patterns: []
missing: []
---

# 视频生成/图生视频/（单参版）Wan2.1 Mocha V2V人物视频替换V2（优化加速版）_1980912658343968770.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980912658343968770.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（47 个）：
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `MaskPreview`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `SetNode`
- `GrowMask`
- `GetNode`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `MochaEmbeds`
- `MarkdownNote`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `PointsEditor`
- `JWInteger`
- `SetNode`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `ImageConcanate`
- `ImageConcanate`
- `PDIMAGE_LongerSize`
- `MarkdownNote`
- `RMBG`
- `CR Prompt Text`
- `LoadImage`
- `Crop Face`
- `SaveImage`
- `PreviewImage`
- `Load RetinaFace`
- `ImageResizeKJv2`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `SaveImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `VHS_LoadVideo`
- `VHS_VideoInfo`

## 知识

覆盖率 **70%**（33/47）

**有卡**：`GetImageRangeFromBatch`、`MaskPreview`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMask`、`WanVideoSampler`、`MochaEmbeds`、`LoadImage`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`PointsEditor`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`ImageConcanate`、`PDIMAGE_LongerSize`、`RMBG`、`CR Prompt Text`、`Crop Face`、`SaveImage`、`Load RetinaFace`、`VHS_VideoCombine`、`WanVideoDecode`、`VHS_LoadVideo`、`VHS_VideoInfo`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoLoraSelectMulti、CR Prompt Text
