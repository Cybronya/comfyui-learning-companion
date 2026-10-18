---
key: 视频生成/图生视频/SP503-表情迁移（wan2.2 Animate）加速版视频表情迁移_1969386195249733634.json
name: SP503-表情迁移（wan2.2 Animate）加速版视频表情迁移_1969386195249733634.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/SP503-表情迁移（wan2.2 Animate）加速版视频表情迁移_1969386195249733634.json
hash: 4cf5329eb3520104
coverage: 1
learned_at: 2026-10-15 22:31:49
nodes: [JWInteger, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, WanVideoVAELoader, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoClipVisionEncode, WanVideoTextEncodeCached, WanVideoDecode, PixelPerfectResolution, easy convertAnything, GetImageSizeAndCount, ImageFromBatch, PlaySound|pysssss, WanVideoSampler, LoadImage, JWInteger, WanVideoBlockSwap, VHS_VideoCombine, Int, easy convertAnything, ImageResizeKJv2, WanVideoAnimateEmbeds, MathExpression|pysssss, DWPreprocessor, VHS_LoadVideo, WanVideoModelLoader, CLIPVisionLoader, easy positive, VHS_VideoCombine, Note Plus (mtb)]
patterns: []
missing: []
---

# 视频生成/图生视频/SP503-表情迁移（wan2.2 Animate）加速版视频表情迁移_1969386195249733634.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969386195249733634.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（32 个）：
- `JWInteger`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncodeCached`
- `WanVideoDecode`
- `PixelPerfectResolution`
- `easy convertAnything`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `PlaySound|pysssss`
- `WanVideoSampler` ★核心
- `LoadImage`
- `JWInteger`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `Int`
- `easy convertAnything`
- `ImageResizeKJv2`
- `WanVideoAnimateEmbeds`
- `MathExpression|pysssss`
- `DWPreprocessor`
- `VHS_LoadVideo`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `easy positive`
- `VHS_VideoCombine`
- `Note Plus (mtb)`

## 知识

覆盖率 **100%**（32/32）

**有卡**：`JWInteger`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`PixelPerfectResolution`、`easy convertAnything`、`GetImageSizeAndCount`、`ImageFromBatch`、`PlaySound|pysssss`、`WanVideoSampler`、`LoadImage`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`Int`、`ImageResizeKJv2`、`WanVideoAnimateEmbeds`、`MathExpression|pysssss`、`DWPreprocessor`、`VHS_LoadVideo`、`WanVideoModelLoader`、`CLIPVisionLoader`、`easy positive`、`Note Plus (mtb)`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
