---
key: 视频生成/图生视频/动作迁移 动作模仿 人物替换 wan2.2_2053529540592447490.json
name: 动作迁移 动作模仿 人物替换 wan2.2_2053529540592447490.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移 动作模仿 人物替换 wan2.2_2053529540592447490.json
hash: e960262e661157aa
coverage: 0.913043
learned_at: 2026-10-15 22:37:40
nodes: [WanVideoLoraSelectMulti, ImageFromBatch, easy int, OnnxDetectionModelLoader, VHS_VideoInfoLoaded, WanVideoVAELoader, GrowMask, BlockifyMask, DrawMaskOnImage, SeCModelLoader, SeCVideoSegmentation, PoseAndFaceDetection, DrawViTPose, VHS_VideoCombine, ImageBlend, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoSampler, easy int, PreviewImage, easy showAnything, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, Evaluate Integers, ImageConcatMulti, ImageConcatMulti, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoSetLoRAs, easy int, easy int, PrimitiveStringMultiline, VHS_VideoCombine, WanVideoTextEncodeCached, ClothesSegment, PreviewImage, GetImageSizeAndCount, WanVideoDecode, WanVideoContextOptions, VHS_VideoCombine, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移 动作模仿 人物替换 wan2.2_2053529540592447490.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053529540592447490.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `WanVideoLoraSelectMulti`
- `ImageFromBatch`
- `easy int`
- `OnnxDetectionModelLoader`
- `VHS_VideoInfoLoaded`
- `WanVideoVAELoader`
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
- `WanVideoSampler` ★核心
- `easy int`
- `PreviewImage`
- `easy showAnything`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Evaluate Integers`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `easy int`
- `easy int`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `ClothesSegment`
- `PreviewImage`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`WanVideoLoraSelectMulti`、`ImageFromBatch`、`easy int`、`OnnxDetectionModelLoader`、`VHS_VideoInfoLoaded`、`WanVideoVAELoader`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`SeCModelLoader`、`SeCVideoSegmentation`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_VideoCombine`、`ImageBlend`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoSampler`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcatMulti`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoTextEncodeCached`、`ClothesSegment`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoContextOptions`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
