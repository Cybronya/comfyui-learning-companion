---
key: 数字人/数字人/视频局部重绘  参考重绘 Wan2.2 KJ加速_2060936779016003585.json
name: 视频局部重绘  参考重绘 Wan2.2 KJ加速_2060936779016003585
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/视频局部重绘  参考重绘 Wan2.2 KJ加速_2060936779016003585.json
hash: fdd8f202f81e0657
coverage: 0.678161
learned_at: 2026-10-26 02:05:11
nodes: [VHS_VideoCombine, Reroute, DownloadAndLoadWav2VecModel, GetNode, AudioSeparation, WanVideoAnimateEmbeds, VHS_VideoCombine, VHS_VideoCombine, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, PixelPerfectResolution, Note, WanVideoTextEncodeCached, WanVideoModelLoader, VHS_VideoCombine, SetNode, SetNode, ImageFromBatch, DownloadAndLoadSAM2Model, ClothesSegment, Sam2Segmentation, SetNode, easy showAnything, WanVideoBlockSwap, GetNode, GrowMask, MaskToImage, DrawMaskOnImage, SetNode, SetNode, SetNode, SetNode, SetNode, SimpleMath+, easy showAnything, GetNode, GetNode, GetNode, GetNode, GetNode, MultiTalkWav2VecEmbeds, easy cleanGpuUsed, easy cleanGpuUsed, GetNode, WanVideoLoraSelectMulti, INTConstant, SetNode, SaveAudio, BlockifyMask, easy cleanGpuUsed, VHS_LoadVideo, GetImageSizeAndCount, WanVideoUni3C_ControlnetLoader, WanVideoEncode, WanVideoUni3C_embeds, GetNode, GetNode, MultiTalkModelLoader, WanVideoClipVisionEncode, CLIPVisionLoader, ImageResizeKJv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, easy promptConcat, Anything Everywhere, RH_Captioner, GetNode, ImageResizeKJv2, SimpleMath+, GetNode, WanVideoDecode, Reroute, SeCVideoSegmentation, DWPreprocessor, easy cleanGpuUsed, SeCModelLoader, ImageFromBatch, LoadImage, INTConstant, INTConstant, PointsEditor, Text, WanVideoSampler, VHS_VideoCombine, Note, VHS_LoadVideo]
patterns: []
missing: []
---

# 数字人/数字人/视频局部重绘  参考重绘 Wan2.2 KJ加速_2060936779016003585.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/视频局部重绘  参考重绘 Wan2.2 KJ加速_2060936779016003585.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（87 个）：
- `VHS_VideoCombine`
- `Reroute`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `AudioSeparation`
- `WanVideoAnimateEmbeds`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `PixelPerfectResolution`
- `Note`
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `ImageFromBatch`
- `DownloadAndLoadSAM2Model`
- `ClothesSegment`
- `Sam2Segmentation`
- `SetNode`
- `easy showAnything`
- `WanVideoBlockSwap`
- `GetNode`
- `GrowMask`
- `MaskToImage`
- `DrawMaskOnImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MultiTalkWav2VecEmbeds`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `INTConstant`
- `SetNode`
- `SaveAudio`
- `BlockifyMask`
- `easy cleanGpuUsed`
- `VHS_LoadVideo`
- `GetImageSizeAndCount`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoEncode`
- `WanVideoUni3C_embeds`
- `GetNode`
- `GetNode`
- `MultiTalkModelLoader`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `easy promptConcat`
- `Anything Everywhere`
- `RH_Captioner`
- `GetNode`
- `ImageResizeKJv2`
- `SimpleMath+`
- `GetNode`
- `WanVideoDecode`
- `Reroute`
- `SeCVideoSegmentation`
- `DWPreprocessor`
- `easy cleanGpuUsed`
- `SeCModelLoader`
- `ImageFromBatch`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `PointsEditor`
- `Text`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `Note`
- `VHS_LoadVideo`

## 知识

覆盖率 **68%**（59/87）

**有卡**：`VHS_VideoCombine`、`DownloadAndLoadWav2VecModel`、`AudioSeparation`、`WanVideoAnimateEmbeds`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`PixelPerfectResolution`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`ImageFromBatch`、`DownloadAndLoadSAM2Model`、`ClothesSegment`、`Sam2Segmentation`、`WanVideoBlockSwap`、`GrowMask`、`MaskToImage`、`DrawMaskOnImage`、`SimpleMath+`、`MultiTalkWav2VecEmbeds`、`easy cleanGpuUsed`、`WanVideoLoraSelectMulti`、`INTConstant`、`SaveAudio`、`BlockifyMask`、`VHS_LoadVideo`、`GetImageSizeAndCount`、`WanVideoUni3C_ControlnetLoader`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`MultiTalkModelLoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`ImageResizeKJv2`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`easy promptConcat`、`RH_Captioner`、`WanVideoDecode`、`SeCVideoSegmentation`、`DWPreprocessor`、`SeCModelLoader`、`LoadImage`、`PointsEditor`、`Text`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
