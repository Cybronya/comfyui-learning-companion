---
key: 视频生成/图生视频/wan  wan2.2 人物替换 动作迁移_2039971069947285506.json
name: wan  wan2.2 人物替换 动作迁移_2039971069947285506.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan  wan2.2 人物替换 动作迁移_2039971069947285506.json
hash: 8f37c217e604abd8
coverage: 0.913043
learned_at: 2026-10-15 22:36:13
nodes: [WanVideoLoraSelectMulti, VHS_VideoInfoLoaded, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoSampler, PreviewImage, easy showAnything, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, Evaluate Integers, ImageConcatMulti, ImageConcatMulti, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoSetLoRAs, VHS_VideoCombine, WanVideoTextEncodeCached, ClothesSegment, PreviewImage, GetImageSizeAndCount, WanVideoDecode, WanVideoContextOptions, LoadImage, VHS_LoadVideo, VHS_VideoCombine, SeCVideoSegmentation, DrawViTPose, PoseAndFaceDetection, OnnxDetectionModelLoader, ImageBlend, VHS_VideoCombine, easy int, easy int, PrimitiveStringMultiline, easy int, SeCModelLoader, DrawMaskOnImage, BlockifyMask, GrowMask, easy int, ImageFromBatch, WanVideoVAELoader, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/wan  wan2.2 人物替换 动作迁移_2039971069947285506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2039971069947285506.json`

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
- `LoadImage`
- `VHS_LoadVideo`
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

## 知识

覆盖率 **91%**（42/46）

**有卡**：`WanVideoLoraSelectMulti`、`VHS_VideoInfoLoaded`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoSampler`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcatMulti`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`ClothesSegment`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoContextOptions`、`LoadImage`、`VHS_LoadVideo`、`SeCVideoSegmentation`、`DrawViTPose`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`ImageBlend`、`easy int`、`SeCModelLoader`、`DrawMaskOnImage`、`BlockifyMask`、`GrowMask`、`ImageFromBatch`、`WanVideoVAELoader`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
