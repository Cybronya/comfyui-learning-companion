---
key: 平台全量/人物替换 角色替换 动作迁移 wan22  wan2.2_2054902184705306626.json
name: 人物替换 角色替换 动作迁移 wan22  wan2.2_2054902184705306626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/人物替换 角色替换 动作迁移 wan22  wan2.2_2054902184705306626.json
hash: 3a332b76896d6d1d
coverage: 0.913043
learned_at: 2026-11-14 01:37:38
nodes: [DrawViTPose, easy int, Evaluate Integers, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoModelLoader, easy int, WanVideoTorchCompileSettings, CLIPVisionLoader, WanVideoSetBlockSwap, WanVideoBlockSwap, VHS_VideoInfoLoaded, easy showAnything, WanVideoVAELoader, OnnxDetectionModelLoader, VHS_VideoCombine, easy int, DrawMaskOnImage, PreviewImage, PreviewImage, ImageFromBatch, SeCModelLoader, SeCVideoSegmentation, GrowMask, BlockifyMask, WanVideoDecode, VHS_VideoCombine, GetImageSizeAndCount, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, WanVideoSampler, WanVideoTextEncodeCached, Evaluate Integers, WanVideoContextOptions, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, PrimitiveStringMultiline, ImageBlend, PoseAndFaceDetection, ClothesSegment, LayerUtility: ImageMaskScaleAsV2, easy int, LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 平台全量/人物替换 角色替换 动作迁移 wan22  wan2.2_2054902184705306626.json

> 来源文件 `comfyui_library/workflows/平台全量/人物替换 角色替换 动作迁移 wan22  wan2.2_2054902184705306626.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `DrawViTPose`
- `easy int`
- `Evaluate Integers`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
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
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`DrawViTPose`、`easy int`、`Evaluate Integers`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`VHS_VideoInfoLoaded`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`VHS_VideoCombine`、`DrawMaskOnImage`、`ImageFromBatch`、`SeCModelLoader`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageConcatMulti`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`ImageBlend`、`PoseAndFaceDetection`、`ClothesSegment`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
