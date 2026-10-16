---
key: 视频生成/图生视频/动作迁移 动作模仿 角色替换 人物替换 wan2.2_2062167725232967682.json
name: 动作迁移 动作模仿 角色替换 人物替换 wan2.2_2062167725232967682.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2062167725232967682.json
hash: 3a774a1160c015ed
coverage: 0.913043
learned_at: 2026-10-15 22:39:01
nodes: [WanVideoAnimateEmbeds, WanVideoContextOptions, Evaluate Integers, ImageConcatMulti, WanVideoDecode, WanVideoVAELoader, VHS_LoadVideo, LoadImage, easy int, Evaluate Integers, easy int, easy int, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoInfoLoaded, ClothesSegment, ImageFromBatch, SeCModelLoader, easy int, SeCVideoSegmentation, PreviewImage, GrowMask, BlockifyMask, DrawMaskOnImage, LayerUtility: ImageMaskScaleAsV2, PreviewImage, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, VHS_VideoCombine, PrimitiveStringMultiline, WanVideoTextEncodeCached, ImageBlend, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSampler, GetImageSizeAndCount, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移 动作模仿 角色替换 人物替换 wan2.2_2062167725232967682.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062167725232967682.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `Evaluate Integers`
- `ImageConcatMulti`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `VHS_LoadVideo`
- `LoadImage`
- `easy int`
- `Evaluate Integers`
- `easy int`
- `easy int`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoInfoLoaded`
- `ClothesSegment`
- `ImageFromBatch`
- `SeCModelLoader`
- `easy int`
- `SeCVideoSegmentation`
- `PreviewImage`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `PreviewImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `WanVideoTextEncodeCached`
- `ImageBlend`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`Evaluate Integers`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoVAELoader`、`VHS_LoadVideo`、`LoadImage`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfoLoaded`、`ClothesSegment`、`ImageFromBatch`、`SeCModelLoader`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`LayerUtility: ImageMaskScaleAsV2`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`ImageBlend`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`GetImageSizeAndCount`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
