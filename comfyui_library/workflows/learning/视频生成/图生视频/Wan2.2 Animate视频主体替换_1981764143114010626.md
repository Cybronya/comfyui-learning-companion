---
key: 视频生成/图生视频/Wan2.2 Animate视频主体替换_1981764143114010626.json
name: Wan2.2 Animate视频主体替换_1981764143114010626.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate视频主体替换_1981764143114010626.json
hash: 8bcc5b721cdbb9cf
coverage: 0.918919
learned_at: 2026-10-15 22:32:38
nodes: [WanVideoAnimateEmbeds, DrawMaskOnImage, Sam2Segmentation, DownloadAndLoadSAM2Model, PoseAndFaceDetection, WanVideoLoraSelect, OnnxDetectionModelLoader, ImageFromBatch+, BlockifyMask, WanVideoLoraSelect, WanVideoDecode, LayerUtility: PurgeVRAM V2, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoVAELoader, GetImageSizeAndCount, WanVideoLoraSelect, WanVideoTextEncodeCached, WanVideoLoraSelect, WanVideoLoraSelect, DrawViTPose, WanVideoSampler, VHS_VideoInfo, CR Text, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, PrimitiveInt, SimpleMath+, WanVideoModelLoader, WanVideoBlockSwap, ImageResizeKJv2, GrowMaskWithBlur, ImageFromBatch+, LayerUtility: PurgeVRAM V2, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate视频主体替换_1981764143114010626.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981764143114010626.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoAnimateEmbeds`
- `DrawMaskOnImage`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `PoseAndFaceDetection`
- `WanVideoLoraSelect`
- `OnnxDetectionModelLoader`
- `ImageFromBatch+`
- `BlockifyMask`
- `WanVideoLoraSelect`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `WanVideoLoraSelect`
- `WanVideoTextEncodeCached`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `DrawViTPose`
- `WanVideoSampler` ★核心
- `VHS_VideoInfo`
- `CR Text`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `SimpleMath+`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `GrowMaskWithBlur`
- `ImageFromBatch+`
- `LayerUtility: PurgeVRAM V2`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **92%**（34/37）

**有卡**：`WanVideoAnimateEmbeds`、`DrawMaskOnImage`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`PoseAndFaceDetection`、`WanVideoLoraSelect`、`OnnxDetectionModelLoader`、`ImageFromBatch+`、`BlockifyMask`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`WanVideoTextEncodeCached`、`DrawViTPose`、`WanVideoSampler`、`VHS_VideoInfo`、`CR Text`、`VHS_VideoCombine`、`SimpleMath+`、`WanVideoModelLoader`、`ImageResizeKJv2`、`GrowMaskWithBlur`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoLoraSelect、GetImageSizeAndCount、ImageResizeKJv2
