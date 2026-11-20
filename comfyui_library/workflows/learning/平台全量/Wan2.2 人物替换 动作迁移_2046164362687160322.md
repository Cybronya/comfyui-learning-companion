---
key: 平台全量/Wan2.2 人物替换 动作迁移_2046164362687160322.json
name: Wan2.2 人物替换 动作迁移_2046164362687160322
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 人物替换 动作迁移_2046164362687160322.json
hash: d41014922851325e
coverage: 0.913043
learned_at: 2026-11-14 01:05:39
nodes: [WanVideoLoraSelectMulti, VHS_VideoInfoLoaded, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoSampler, PreviewImage, easy showAnything, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, Evaluate Integers, ImageConcatMulti, ImageConcatMulti, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoSetLoRAs, VHS_VideoCombine, WanVideoTextEncodeCached, ClothesSegment, PreviewImage, GetImageSizeAndCount, WanVideoDecode, WanVideoContextOptions, VHS_VideoCombine, SeCVideoSegmentation, DrawViTPose, PoseAndFaceDetection, OnnxDetectionModelLoader, ImageBlend, VHS_VideoCombine, easy int, easy int, PrimitiveStringMultiline, easy int, SeCModelLoader, DrawMaskOnImage, BlockifyMask, GrowMask, easy int, ImageFromBatch, WanVideoVAELoader, WanVideoModelLoader, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 平台全量/Wan2.2 人物替换 动作迁移_2046164362687160322.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 人物替换 动作迁移_2046164362687160322.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `WanVideoLoraSelectMulti`
- `VHS_VideoInfoLoaded`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoSampler` ★核心
- `PreviewImage`
- `easy showAnything`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Evaluate Integers`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `ClothesSegment`
- `PreviewImage`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `SeCVideoSegmentation`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `ImageBlend`
- `VHS_VideoCombine`
- `easy int`
- `easy int`
- `PrimitiveStringMultiline`
- `easy int`
- `SeCModelLoader`
- `DrawMaskOnImage`
- `BlockifyMask`
- `GrowMask`
- `easy int`
- `ImageFromBatch`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`WanVideoLoraSelectMulti`、`VHS_VideoInfoLoaded`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoSampler`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcatMulti`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`ClothesSegment`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoContextOptions`、`SeCVideoSegmentation`、`DrawViTPose`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`ImageBlend`、`easy int`、`SeCModelLoader`、`DrawMaskOnImage`、`BlockifyMask`、`GrowMask`、`ImageFromBatch`、`WanVideoVAELoader`、`WanVideoModelLoader`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
