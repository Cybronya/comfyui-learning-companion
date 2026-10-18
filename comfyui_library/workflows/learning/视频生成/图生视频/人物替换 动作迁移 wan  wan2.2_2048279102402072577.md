---
key: 视频生成/图生视频/人物替换 动作迁移 wan  wan2.2_2048279102402072577.json
name: 人物替换 动作迁移 wan  wan2.2_2048279102402072577.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/人物替换 动作迁移 wan  wan2.2_2048279102402072577.json
hash: 5b8451de2a559782
coverage: 0.913043
learned_at: 2026-10-15 22:37:08
nodes: [DrawViTPose, easy int, Evaluate Integers, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoModelLoader, VHS_LoadVideo, easy int, WanVideoTorchCompileSettings, CLIPVisionLoader, WanVideoSetBlockSwap, WanVideoBlockSwap, VHS_VideoInfoLoaded, easy showAnything, WanVideoVAELoader, OnnxDetectionModelLoader, VHS_VideoCombine, easy int, DrawMaskOnImage, PreviewImage, PreviewImage, ImageFromBatch, SeCModelLoader, SeCVideoSegmentation, GrowMask, BlockifyMask, WanVideoDecode, VHS_VideoCombine, GetImageSizeAndCount, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, WanVideoSampler, WanVideoTextEncodeCached, Evaluate Integers, WanVideoContextOptions, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, PrimitiveStringMultiline, ImageBlend, PoseAndFaceDetection, ClothesSegment, LayerUtility: ImageMaskScaleAsV2, easy int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/人物替换 动作迁移 wan  wan2.2_2048279102402072577.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2048279102402072577.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `DrawViTPose`
- `easy int`
- `Evaluate Integers`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `VHS_LoadVideo`
- `easy int`
- `WanVideoTorchCompileSettings`
- `CLIPVisionLoader`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `VHS_VideoCombine`
- `easy int`
- `DrawMaskOnImage`
- `PreviewImage`
- `PreviewImage`
- `ImageFromBatch`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `Evaluate Integers`
- `WanVideoContextOptions`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `PrimitiveStringMultiline`
- `ImageBlend`
- `PoseAndFaceDetection`
- `ClothesSegment`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`DrawViTPose`、`easy int`、`Evaluate Integers`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`VHS_LoadVideo`、`WanVideoTorchCompileSettings`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`VHS_VideoInfoLoaded`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`VHS_VideoCombine`、`DrawMaskOnImage`、`ImageFromBatch`、`SeCModelLoader`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageConcatMulti`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`ImageBlend`、`PoseAndFaceDetection`、`ClothesSegment`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
