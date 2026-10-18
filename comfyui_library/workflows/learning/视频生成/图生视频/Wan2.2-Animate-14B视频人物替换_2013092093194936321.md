---
key: 视频生成/图生视频/Wan2.2-Animate-14B视频人物替换_2013092093194936321.json
name: Wan2.2-Animate-14B视频人物替换_2013092093194936321.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Animate-14B视频人物替换_2013092093194936321.json
hash: 62c2474ae5afab87
coverage: 0.895833
learned_at: 2026-10-15 22:34:29
nodes: [WanVideoTorchCompileSettings, PoseAndFaceDetection, DrawViTPose, VHS_VideoCombine, WanVideoDecode, LayerUtility: ImageMaskScaleAsV2, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, PreviewImage, WanVideoVAELoader, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoTextEncodeCached, PrimitiveStringMultiline, Evaluate Integers, easy int, VHS_VideoCombine, WanVideoContextOptions, GetImageSizeAndCount, WanVideoBlockSwap, easy int, LayerUtility: ImageScaleByAspectRatio V2, DrawMaskOnImage, BlockifyMask, GrowMask, Note, VHS_VideoInfoLoaded, ImageFromBatch, easy int, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, PreviewImage, ClothesSegment, Evaluate Integers, easy int, OnnxDetectionModelLoader, SeCVideoSegmentation, ImageBlend, easy showAnything, VHS_VideoCombine, SeCModelLoader, WanVideoLoraSelectMulti, WanVideoSampler, WanVideoModelLoader, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-Animate-14B视频人物替换_2013092093194936321.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2013092093194936321.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（48 个）：
- `WanVideoTorchCompileSettings`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `LayerUtility: ImageMaskScaleAsV2`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `PreviewImage`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `PrimitiveStringMultiline`
- `Evaluate Integers`
- `easy int`
- `VHS_VideoCombine`
- `WanVideoContextOptions`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DrawMaskOnImage`
- `BlockifyMask`
- `GrowMask`
- `Note`
- `VHS_VideoInfoLoaded`
- `ImageFromBatch`
- `easy int`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `PreviewImage`
- `ClothesSegment`
- `Evaluate Integers`
- `easy int`
- `OnnxDetectionModelLoader`
- `SeCVideoSegmentation`
- `ImageBlend`
- `easy showAnything`
- `VHS_VideoCombine`
- `SeCModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **90%**（43/48）

**有卡**：`WanVideoTorchCompileSettings`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_VideoCombine`、`WanVideoDecode`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`Evaluate Integers`、`easy int`、`WanVideoContextOptions`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`DrawMaskOnImage`、`BlockifyMask`、`GrowMask`、`VHS_VideoInfoLoaded`、`ImageFromBatch`、`ImageConcatMulti`、`ClothesSegment`、`OnnxDetectionModelLoader`、`SeCVideoSegmentation`、`ImageBlend`、`SeCModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`WanVideoModelLoader`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
