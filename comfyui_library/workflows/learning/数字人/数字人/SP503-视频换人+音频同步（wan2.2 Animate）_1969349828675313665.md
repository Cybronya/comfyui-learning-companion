---
key: 数字人/数字人/SP503-视频换人+音频同步（wan2.2 Animate）_1969349828675313665.json
name: SP503-视频换人+音频同步（wan2.2 Animate）_1969349828675313665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/SP503-视频换人+音频同步（wan2.2 Animate）_1969349828675313665.json
hash: 58a1d59a2a225631
coverage: 1
learned_at: 2026-10-26 01:57:13
nodes: [JWInteger, DownloadAndLoadSAM2Model, Sam2Segmentation, GrowMask, BlockifyMask, DrawMaskOnImage, VHS_VideoCombine, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, WanVideoDecode, PixelPerfectResolution, easy convertAnything, Int, GetImageSizeAndCount, ImageFromBatch, MathExpression|pysssss, PlaySound|pysssss, WanVideoSampler, LoadImage, JWInteger, WanVideoBlockSwap, Int, easy convertAnything, ImageResizeKJv2, WanVideoVAELoader, WanVideoModelLoader, VHS_LoadVideo, WanVideoClipVisionEncode, Note Plus (mtb), easy positive, VHS_VideoCombine, VHS_VideoCombine, PointsEditor]
patterns: []
missing: []
---

# 数字人/数字人/SP503-视频换人+音频同步（wan2.2 Animate）_1969349828675313665.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/SP503-视频换人+音频同步（wan2.2 Animate）_1969349828675313665.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `JWInteger`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `CLIPVisionLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `PixelPerfectResolution`
- `easy convertAnything`
- `Int`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `MathExpression|pysssss`
- `PlaySound|pysssss`
- `WanVideoSampler` ★核心
- `LoadImage`
- `JWInteger`
- `WanVideoBlockSwap`
- `Int`
- `easy convertAnything`
- `ImageResizeKJv2`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `VHS_LoadVideo`
- `WanVideoClipVisionEncode`
- `Note Plus (mtb)`
- `easy positive`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PointsEditor`

## 知识

覆盖率 **100%**（40/40）

**有卡**：`JWInteger`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`VHS_VideoCombine`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`PixelPerfectResolution`、`easy convertAnything`、`Int`、`GetImageSizeAndCount`、`ImageFromBatch`、`MathExpression|pysssss`、`PlaySound|pysssss`、`WanVideoSampler`、`LoadImage`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`WanVideoVAELoader`、`WanVideoModelLoader`、`VHS_LoadVideo`、`WanVideoClipVisionEncode`、`Note Plus (mtb)`、`easy positive`、`PointsEditor`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
