---
key: 视频生成/图生视频/SP504-视频换装换脸（wan2.2 Animate）_1970147620683476994.json
name: SP504-视频换装换脸（wan2.2 Animate）_1970147620683476994.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1970147620683476994.json
hash: 8bd7c9f90e210faf
coverage: 1
learned_at: 2026-10-15 22:31:52
nodes: [JWInteger, GrowMask, BlockifyMask, DrawMaskOnImage, VHS_VideoCombine, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, WanVideoVAELoader, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoAnimateEmbeds, WanVideoDecode, PixelPerfectResolution, easy convertAnything, GetImageSizeAndCount, ImageFromBatch, MathExpression|pysssss, PlaySound|pysssss, WanVideoSampler, JWInteger, WanVideoBlockSwap, WanVideoTorchCompileSettings, Int, easy convertAnything, WanVideoClipVisionEncode, LoadImage, LayerMask: SegformerUltraV2, ImageResizeKJv2, WanVideoModelLoader, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, easy positive, Int, LayerMask: SegformerClothesPipelineLoader, WanVideoSetLoRAs, Note Plus (mtb), WanVideoTextEncodeCached]
patterns: []
missing: []
---

# 视频生成/图生视频/SP504-视频换装换脸（wan2.2 Animate）_1970147620683476994.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1970147620683476994.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `JWInteger`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `PixelPerfectResolution`
- `easy convertAnything`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `MathExpression|pysssss`
- `PlaySound|pysssss`
- `WanVideoSampler` ★核心
- `JWInteger`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `Int`
- `easy convertAnything`
- `WanVideoClipVisionEncode`
- `LoadImage`
- `LayerMask: SegformerUltraV2`
- `ImageResizeKJv2`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `easy positive`
- `Int`
- `LayerMask: SegformerClothesPipelineLoader`
- `WanVideoSetLoRAs`
- `Note Plus (mtb)`
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **100%**（40/40）

**有卡**：`JWInteger`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`VHS_VideoCombine`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`PixelPerfectResolution`、`easy convertAnything`、`GetImageSizeAndCount`、`ImageFromBatch`、`MathExpression|pysssss`、`PlaySound|pysssss`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`Int`、`WanVideoClipVisionEncode`、`LoadImage`、`LayerMask: SegformerUltraV2`、`ImageResizeKJv2`、`WanVideoModelLoader`、`VHS_LoadVideo`、`easy positive`、`LayerMask: SegformerClothesPipelineLoader`、`WanVideoSetLoRAs`、`Note Plus (mtb)`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
