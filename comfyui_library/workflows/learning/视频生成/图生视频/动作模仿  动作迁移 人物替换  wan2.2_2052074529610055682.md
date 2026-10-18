---
key: 视频生成/图生视频/动作模仿  动作迁移 人物替换  wan2.2_2052074529610055682.json
name: 动作模仿  动作迁移 人物替换  wan2.2_2052074529610055682.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作模仿  动作迁移 人物替换  wan2.2_2052074529610055682.json
hash: 710f29a308349e12
coverage: 0.913043
learned_at: 2026-10-15 22:37:26
nodes: [WanVideoLoraSelectMulti, ImageFromBatch, easy int, OnnxDetectionModelLoader, VHS_VideoInfoLoaded, VHS_LoadVideo, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoSetLoRAs, GrowMask, BlockifyMask, DrawMaskOnImage, SeCModelLoader, SeCVideoSegmentation, PoseAndFaceDetection, DrawViTPose, VHS_VideoCombine, ImageBlend, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoContextOptions, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, PrimitiveStringMultiline, easy int, easy int, easy int, PreviewImage, PreviewImage, WanVideoTextEncodeCached, easy showAnything, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, Evaluate Integers, ClothesSegment, LoadImage, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  动作迁移 人物替换  wan2.2_2052074529610055682.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052074529610055682.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `WanVideoLoraSelectMulti`
- `ImageFromBatch`
- `easy int`
- `OnnxDetectionModelLoader`
- `VHS_VideoInfoLoaded`
- `VHS_LoadVideo`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `VHS_VideoCombine`
- `ImageBlend`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `PrimitiveStringMultiline`
- `easy int`
- `easy int`
- `easy int`
- `PreviewImage`
- `PreviewImage`
- `WanVideoTextEncodeCached`
- `easy showAnything`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Evaluate Integers`
- `ClothesSegment`
- `LoadImage`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`WanVideoLoraSelectMulti`、`ImageFromBatch`、`easy int`、`OnnxDetectionModelLoader`、`VHS_VideoInfoLoaded`、`VHS_LoadVideo`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`SeCModelLoader`、`SeCVideoSegmentation`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_VideoCombine`、`ImageBlend`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoTextEncodeCached`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ClothesSegment`、`LoadImage`、`ImageConcatMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
