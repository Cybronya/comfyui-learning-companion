---
key: 视频生成/图生视频/kitten practicing kung fu_2091771507398762498.json
name: kitten practicing kung fu_2091771507398762498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/kitten practicing kung fu_2091771507398762498.json
hash: 0f25ede745e2c342
coverage: 0.605405
learned_at: 2026-10-16 22:30:50
nodes: [GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, GetNode, easy cleanGpuUsed, WanVideoSetBlockSwap, easy cleanGpuUsed, INTConstant, INTConstant, SetNode, SetNode, SetNode, PoseAndFaceDetection, SeedVR2LoadDiTModel, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoSetLoRAs, GetImageSizeAndCount, SetNode, ImageResizeKJv2, BlockifyMask, SetNode, CLIPVisionLoader, DrawViTPose, OnnxDetectionModelLoader, WanVideoSampler, GrowMask, WanVideoVAELoader, GetImageSizeAndCount, GetNode, INTConstant, DrawMaskOnImage, easy cleanGpuUsed, SetNode, VHS_VideoCombine, VHS_VideoInfo, MaskToImage, InvertMask, ImageFromBatch+, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcanate, SetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, GetNode, JWInteger, easy cleanGpuUsed, WanVideoSetBlockSwap, easy cleanGpuUsed, INTConstant, INTConstant, SetNode, SetNode, WanVideoModelLoader, GetNode, GetNode, SetNode, PoseAndFaceDetection, SeedVR2LoadDiTModel, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoSetLoRAs, GetImageSizeAndCount, INTConstant, SeedVR2LoadVAEModel, SetNode, Note, Note, ImageResizeKJv2, BlockifyMask, SetNode, CLIPVisionLoader, WanVideoClipVisionEncode, DrawViTPose, OnnxDetectionModelLoader, WanVideoSampler, GrowMask, LayerUtility: ImageBlend, WanVideoDecode, WanVideoVAELoader, WanVideoBlockSwap, WanVideoTextEncodeCached, CR Text, GetImageSizeAndCount, ImageScaleToTotalPixels, ImageFromBatch, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, INTConstant, VHS_VideoCombine, DrawMaskOnImage, easy cleanGpuUsed, SetNode, WanVideoLoraSelectMulti, VHS_VideoCombine, VHS_VideoInfo, MaskToImage, InvertMask, GetNode, SeCModelLoader, ImageFromBatch+, PreviewImage, SetNode, SeCVideoSegmentation, PointsEditor, VHS_VideoCombine, LoadImage, PreviewImage, VHS_VideoCombine, MemoryCleaner, SeedVR2VideoUpscaler, SetNode, VHS_VideoCombine, GetNode, Text Multiline, VHS_LoadVideo, SetNode, IndexTTSNode, GetNode, WanVideoTextEncodeCached, GetNode, GetNode, WanVideoLoraSelectMulti, WanVideoDecode, SeCVideoSegmentation, SetNode, JWInteger, WanVideoBlockSwap, LayerUtility: ImageBlend, PreviewImage, GetNode, GetNode, GetNode, SetNode, ImageConcanate, WanVideoClipVisionEncode, INTConstant, ImageScaleToTotalPixels, ImageFromBatch, GetNode, WanVideoAnimateEmbeds, GetNode, GetNode, VHS_VideoCombine, WanVideoModelLoader, SeCModelLoader, MemoryCleaner, CR Text, VHS_VideoCombine, PointsEditor, GetNode, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/kitten practicing kung fu_2091771507398762498.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/kitten practicing kung fu_2091771507398762498.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（185 个）：
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `easy cleanGpuUsed`
- `WanVideoSetBlockSwap`
- `easy cleanGpuUsed`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SetNode`
- `PoseAndFaceDetection`
- `SeedVR2LoadDiTModel`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `SetNode`
- `ImageResizeKJv2`
- `BlockifyMask`
- `SetNode`
- `CLIPVisionLoader`
- `DrawViTPose`
- `OnnxDetectionModelLoader`
- `WanVideoSampler` ★核心
- `GrowMask`
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `DrawMaskOnImage`
- `easy cleanGpuUsed`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `MaskToImage`
- `InvertMask`
- `ImageFromBatch+`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `JWInteger`
- `easy cleanGpuUsed`
- `WanVideoSetBlockSwap`
- `easy cleanGpuUsed`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `PoseAndFaceDetection`
- `SeedVR2LoadDiTModel`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `INTConstant`
- `SeedVR2LoadVAEModel`
- `SetNode`
- `Note`
- `Note`
- `ImageResizeKJv2`
- `BlockifyMask`
- `SetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `DrawViTPose`
- `OnnxDetectionModelLoader`
- `WanVideoSampler` ★核心
- `GrowMask`
- `LayerUtility: ImageBlend`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `CR Text`
- `GetImageSizeAndCount`
- `ImageScaleToTotalPixels`
- `ImageFromBatch`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `easy cleanGpuUsed`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `MaskToImage`
- `InvertMask`
- `GetNode`
- `SeCModelLoader`
- `ImageFromBatch+`
- `PreviewImage`
- `SetNode`
- `SeCVideoSegmentation`
- `PointsEditor`
- `VHS_VideoCombine`
- `LoadImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `MemoryCleaner`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `Text Multiline`
- `VHS_LoadVideo`
- `SetNode`
- `IndexTTSNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `GetNode`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoDecode`
- `SeCVideoSegmentation`
- `SetNode`
- `JWInteger`
- `WanVideoBlockSwap`
- `LayerUtility: ImageBlend`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageConcanate`
- `WanVideoClipVisionEncode`
- `INTConstant`
- `ImageScaleToTotalPixels`
- `ImageFromBatch`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `SeCModelLoader`
- `MemoryCleaner`
- `CR Text`
- `VHS_VideoCombine`
- `PointsEditor`
- `GetNode`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **61%**（112/185）

**有卡**：`easy cleanGpuUsed`、`WanVideoSetBlockSwap`、`INTConstant`、`PoseAndFaceDetection`、`SeedVR2LoadDiTModel`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`BlockifyMask`、`CLIPVisionLoader`、`DrawViTPose`、`OnnxDetectionModelLoader`、`WanVideoSampler`、`GrowMask`、`WanVideoVAELoader`、`DrawMaskOnImage`、`VHS_VideoCombine`、`VHS_VideoInfo`、`MaskToImage`、`InvertMask`、`ImageFromBatch+`、`ImageConcanate`、`JWInteger`、`WanVideoModelLoader`、`SeedVR2LoadVAEModel`、`WanVideoClipVisionEncode`、`LayerUtility: ImageBlend`、`WanVideoDecode`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`CR Text`、`ImageScaleToTotalPixels`、`ImageFromBatch`、`WanVideoAnimateEmbeds`、`WanVideoLoraSelectMulti`、`SeCModelLoader`、`SeCVideoSegmentation`、`PointsEditor`、`LoadImage`、`MemoryCleaner`、`SeedVR2VideoUpscaler`、`Text Multiline`、`VHS_LoadVideo`、`IndexTTSNode`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode
