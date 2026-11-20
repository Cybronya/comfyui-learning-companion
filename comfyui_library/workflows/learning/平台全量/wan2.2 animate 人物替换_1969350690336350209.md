---
key: 平台全量/wan2.2 animate 人物替换_1969350690336350209.json
name: wan2.2 animate 人物替换_1969350690336350209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2 animate 人物替换_1969350690336350209.json
hash: 26fecb88cad1fdd2
coverage: 0.911765
learned_at: 2026-11-14 01:19:19
nodes: [WanVideoBlockSwap, Reroute, WanVideoDecode, WanVideoClipVisionEncode, WanVideoSetBlockSwap, PixelPerfectResolution, WanVideoSetLoRAs, CLIPVisionLoader, DWPreprocessor, WanVideoModelLoader, WanVideoLoraSelectMulti, VHS_VideoCombine, FaceMaskFromPoseKeypoints, WanVideoTextEncodeCached, WanVideoVAELoader, CR Text, VHS_VideoCombine, Sam2Segmentation, DownloadAndLoadSAM2Model, PreviewImage, ImageResizeKJv2, LoadImage, WanVideoAnimateEmbeds, ImageCropByMaskAndResize, GrowMask, WanVideoSampler, BlockifyMask, VHS_VideoCombine, DrawMaskOnImage, JWInteger, JWInteger, VHS_LoadVideo, Reroute, PointsEditor]
patterns: []
missing: []
---

# 平台全量/wan2.2 animate 人物替换_1969350690336350209.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2 animate 人物替换_1969350690336350209.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（34 个）：
- `WanVideoBlockSwap`
- `Reroute`
- `WanVideoDecode`
- `WanVideoClipVisionEncode`
- `WanVideoSetBlockSwap`
- `PixelPerfectResolution`
- `WanVideoSetLoRAs`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `FaceMaskFromPoseKeypoints`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `CR Text`
- `VHS_VideoCombine`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `PreviewImage`
- `ImageResizeKJv2`
- `LoadImage`
- `WanVideoAnimateEmbeds`
- `ImageCropByMaskAndResize`
- `GrowMask`
- `WanVideoSampler` ★核心
- `BlockifyMask`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `JWInteger`
- `JWInteger`
- `VHS_LoadVideo`
- `Reroute`
- `PointsEditor`

## 知识

覆盖率 **91%**（31/34）

**有卡**：`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`PixelPerfectResolution`、`WanVideoSetLoRAs`、`CLIPVisionLoader`、`DWPreprocessor`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`FaceMaskFromPoseKeypoints`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`CR Text`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`ImageResizeKJv2`、`LoadImage`、`WanVideoAnimateEmbeds`、`ImageCropByMaskAndResize`、`GrowMask`、`WanVideoSampler`、`BlockifyMask`、`DrawMaskOnImage`、`JWInteger`、`VHS_LoadVideo`、`PointsEditor`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
