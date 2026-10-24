---
key: 图片生成/图生图/Wan2.2 Animate视频主体替换（带货专用）_1985317372301033473.json
name: Wan2.2 Animate视频主体替换（带货专用）_1985317372301033473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2 Animate视频主体替换（带货专用）_1985317372301033473.json
hash: 65842ea4e93ee3e6
coverage: 0.918919
learned_at: 2026-10-23 11:27:58
nodes: [WanVideoAnimateEmbeds, DrawMaskOnImage, Sam2Segmentation, DownloadAndLoadSAM2Model, PoseAndFaceDetection, WanVideoLoraSelect, OnnxDetectionModelLoader, ImageFromBatch+, BlockifyMask, WanVideoLoraSelect, WanVideoDecode, LayerUtility: PurgeVRAM V2, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoVAELoader, GetImageSizeAndCount, WanVideoLoraSelect, WanVideoTextEncodeCached, WanVideoLoraSelect, WanVideoLoraSelect, DrawViTPose, WanVideoSampler, VHS_VideoInfo, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, SimpleMath+, WanVideoModelLoader, WanVideoBlockSwap, ImageResizeKJv2, GrowMaskWithBlur, ImageFromBatch+, LayerUtility: PurgeVRAM V2, PrimitiveInt, CR Text, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/Wan2.2 Animate视频主体替换（带货专用）_1985317372301033473.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2 Animate视频主体替换（带货专用）_1985317372301033473.json`

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
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `SimpleMath+`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `GrowMaskWithBlur`
- `ImageFromBatch+`
- `LayerUtility: PurgeVRAM V2`
- `PrimitiveInt`
- `CR Text`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **92%**（34/37）

**有卡**：`WanVideoAnimateEmbeds`、`DrawMaskOnImage`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`PoseAndFaceDetection`、`WanVideoLoraSelect`、`OnnxDetectionModelLoader`、`ImageFromBatch+`、`BlockifyMask`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`WanVideoTextEncodeCached`、`DrawViTPose`、`WanVideoSampler`、`VHS_VideoInfo`、`VHS_VideoCombine`、`SimpleMath+`、`WanVideoModelLoader`、`ImageResizeKJv2`、`GrowMaskWithBlur`、`CR Text`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoLoraSelect、GetImageSizeAndCount、ImageResizeKJv2
