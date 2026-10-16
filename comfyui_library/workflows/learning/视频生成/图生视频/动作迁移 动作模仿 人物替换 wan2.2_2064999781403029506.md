---
key: 视频生成/图生视频/动作迁移 动作模仿 人物替换 wan2.2_2064999781403029506.json
name: 动作迁移 动作模仿 人物替换 wan2.2_2064999781403029506.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2064999781403029506.json
hash: 6cb6115e7f81fdb0
coverage: 0.913043
learned_at: 2026-10-15 22:39:33
nodes: [WanVideoLoraSelectMulti, ImageFromBatch, easy int, OnnxDetectionModelLoader, VHS_VideoInfoLoaded, ImageConcatMulti, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoSetLoRAs, GrowMask, BlockifyMask, DrawMaskOnImage, SeCModelLoader, SeCVideoSegmentation, PoseAndFaceDetection, DrawViTPose, VHS_VideoCombine, ImageBlend, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoContextOptions, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, ImageConcatMulti, PrimitiveStringMultiline, easy int, easy int, easy int, PreviewImage, PreviewImage, easy showAnything, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, Evaluate Integers, ClothesSegment, WanVideoTorchCompileSettings, VHS_VideoCombine, VHS_VideoCombine, WanVideoTextEncodeCached, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移 动作模仿 人物替换 wan2.2_2064999781403029506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064999781403029506.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `WanVideoLoraSelectMulti`
- `ImageFromBatch`
- `easy int`
- `OnnxDetectionModelLoader`
- `VHS_VideoInfoLoaded`
- `ImageConcatMulti`
- `WanVideoVAELoader`
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
- `ImageConcatMulti`
- `PrimitiveStringMultiline`
- `easy int`
- `easy int`
- `easy int`
- `PreviewImage`
- `PreviewImage`
- `easy showAnything`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Evaluate Integers`
- `ClothesSegment`
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`WanVideoLoraSelectMulti`、`ImageFromBatch`、`easy int`、`OnnxDetectionModelLoader`、`VHS_VideoInfoLoaded`、`ImageConcatMulti`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`SeCModelLoader`、`SeCVideoSegmentation`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_VideoCombine`、`ImageBlend`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ClothesSegment`、`WanVideoTorchCompileSettings`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
