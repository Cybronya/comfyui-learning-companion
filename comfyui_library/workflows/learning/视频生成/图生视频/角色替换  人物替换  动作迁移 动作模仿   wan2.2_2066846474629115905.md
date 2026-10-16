---
key: 视频生成/图生视频/角色替换  人物替换  动作迁移 动作模仿   wan2.2_2066846474629115905.json
name: 角色替换  人物替换  动作迁移 动作模仿   wan2.2_2066846474629115905.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2066846474629115905.json
hash: 997accc3e8444f57
coverage: 0.974359
learned_at: 2026-10-15 22:39:53
nodes: [LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, ImageFromBatch, SeCModelLoader, LayerUtility: ImageMaskScaleAsV2, ClothesSegment, SeCVideoSegmentation, easy int, VHS_VideoInfoLoaded, GrowMask, WanVideoVAELoader, BlockifyMask, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawMaskOnImage, CLIPVisionLoader, VHS_VideoCombine, DrawViTPose, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, Evaluate Integers, ImageBlend, WanVideoContextOptions, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/角色替换  人物替换  动作迁移 动作模仿   wan2.2_2066846474629115905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2066846474629115905.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `ImageFromBatch`
- `SeCModelLoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `easy int`
- `VHS_VideoInfoLoaded`
- `GrowMask`
- `WanVideoVAELoader`
- `BlockifyMask`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `DrawViTPose`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `Evaluate Integers`
- `ImageBlend`
- `WanVideoContextOptions`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`ImageFromBatch`、`SeCModelLoader`、`LayerUtility: ImageMaskScaleAsV2`、`ClothesSegment`、`SeCVideoSegmentation`、`easy int`、`VHS_VideoInfoLoaded`、`GrowMask`、`WanVideoVAELoader`、`BlockifyMask`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`CLIPVisionLoader`、`VHS_VideoCombine`、`DrawViTPose`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`Evaluate Integers`、`ImageBlend`、`WanVideoContextOptions`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageConcatMulti`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
