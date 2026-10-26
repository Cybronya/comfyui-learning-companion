---
key: 数字人/数字人/SP503-动作迁移+动态运镜（wan2.2 Animate）_1970122062549426177.json
name: SP503-动作迁移+动态运镜（wan2.2 Animate）_1970122062549426177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/SP503-动作迁移+动态运镜（wan2.2 Animate）_1970122062549426177.json
hash: f8b561604251ca9d
coverage: 0.95
learned_at: 2026-10-26 01:57:13
nodes: [DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, Reroute, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, ImageResizeKJv2, easy convertAnything, Reroute, GetImageSizeAndCount, ImageFromBatch, MathExpression|pysssss, PlaySound|pysssss, ImageResizeKJv2, WanVideoEncode, WanVideoBlockSwap, Int, LoadImage, WanVideoUni3C_ControlnetLoader, WanVideoVAELoader, GetImageSizeAndCount, WanVideoSampler, WanVideoAnimateEmbeds, WanVideoModelLoader, easy positive, JWInteger, JWInteger, easy convertAnything, PixelPerfectResolution, Note Plus (mtb), VHS_LoadVideo, VHS_VideoCombine, VHS_LoadVideo, VHS_VideoCombine, WanVideoUni3C_embeds, WanVideoTextEncodeCached, WanVideoClipVisionEncode]
patterns: []
missing: []
---

# 数字人/数字人/SP503-动作迁移+动态运镜（wan2.2 Animate）_1970122062549426177.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/SP503-动作迁移+动态运镜（wan2.2 Animate）_1970122062549426177.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `Reroute`
- `CLIPVisionLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `ImageResizeKJv2`
- `easy convertAnything`
- `Reroute`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `MathExpression|pysssss`
- `PlaySound|pysssss`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `WanVideoBlockSwap`
- `Int`
- `LoadImage`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `WanVideoModelLoader`
- `easy positive`
- `JWInteger`
- `JWInteger`
- `easy convertAnything`
- `PixelPerfectResolution`
- `Note Plus (mtb)`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoUni3C_embeds`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`ImageResizeKJv2`、`easy convertAnything`、`GetImageSizeAndCount`、`ImageFromBatch`、`MathExpression|pysssss`、`PlaySound|pysssss`、`WanVideoEncode`、`WanVideoBlockSwap`、`Int`、`LoadImage`、`WanVideoUni3C_ControlnetLoader`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`WanVideoModelLoader`、`easy positive`、`JWInteger`、`PixelPerfectResolution`、`Note Plus (mtb)`、`VHS_LoadVideo`、`VHS_VideoCombine`、`WanVideoUni3C_embeds`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
