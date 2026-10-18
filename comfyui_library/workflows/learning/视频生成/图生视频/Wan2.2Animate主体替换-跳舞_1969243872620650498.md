---
key: 视频生成/图生视频/Wan2.2Animate主体替换-跳舞_1969243872620650498.json
name: Wan2.2Animate主体替换-跳舞_1969243872620650498.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2Animate主体替换-跳舞_1969243872620650498.json
hash: dc1b8dbf2ecbba8e
coverage: 0.878049
learned_at: 2026-10-15 22:31:48
nodes: [WanVideoSetBlockSwap, ImageResizeKJv2, GetImageSizeAndCount, ImageFromBatch+, VHS_VideoCombine, WanVideoTextEncodeCached, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSampler, WanVideoDecode, VHS_VideoInfo, CR Text, WanVideoBlockSwap, LayerUtility: PurgeVRAM V2, LoadImage, VHS_LoadVideo, LayerUtility: PurgeVRAM V2, WanVideoAnimateEmbeds, ImageFromBatch+, DrawMaskOnImage, BlockifyMask, Sam2Segmentation, DownloadAndLoadSAM2Model, GrowMaskWithBlur, PoseAndFaceDetection, OnnxDetectionModelLoader, DrawViTPose, PrimitiveInt, LoadImage, MarkdownNote, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, WanVideoModelLoader, WanVideoVAELoader, WanVideoBlockSwap, SimpleMath+, PrimitiveInt]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2Animate主体替换-跳舞_1969243872620650498.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969243872620650498.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（41 个）：
- `WanVideoSetBlockSwap`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoInfo`
- `CR Text`
- `WanVideoBlockSwap`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `VHS_LoadVideo`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoAnimateEmbeds`
- `ImageFromBatch+`
- `DrawMaskOnImage`
- `BlockifyMask`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `GrowMaskWithBlur`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `DrawViTPose`
- `PrimitiveInt`
- `LoadImage`
- `MarkdownNote`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `SimpleMath+`
- `PrimitiveInt`

## 知识

覆盖率 **88%**（36/41）

**有卡**：`WanVideoSetBlockSwap`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`ImageFromBatch+`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`WanVideoLoraSelect`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoInfo`、`CR Text`、`WanVideoBlockSwap`、`LayerUtility: PurgeVRAM V2`、`LoadImage`、`VHS_LoadVideo`、`WanVideoAnimateEmbeds`、`DrawMaskOnImage`、`BlockifyMask`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`GrowMaskWithBlur`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`DrawViTPose`、`WanVideoModelLoader`、`WanVideoVAELoader`、`SimpleMath+`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoLoraSelect、GetImageSizeAndCount、ImageResizeKJv2
