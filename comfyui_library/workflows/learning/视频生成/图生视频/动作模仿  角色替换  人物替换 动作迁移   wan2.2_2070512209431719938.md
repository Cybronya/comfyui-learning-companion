---
key: 视频生成/图生视频/动作模仿  角色替换  人物替换 动作迁移   wan2.2_2070512209431719938.json
name: 动作模仿  角色替换  人物替换 动作迁移   wan2.2_2070512209431719938.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2070512209431719938.json
hash: a6e4b4632b40e354
coverage: 0.974359
learned_at: 2026-10-15 22:40:40
nodes: [DrawViTPose, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoDecode, GetImageSizeAndCount, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, easy showAnything, VHS_LoadVideo, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoInfoLoaded, SeCModelLoader, easy int, LayerUtility: ImageMaskScaleAsV2, ImageFromBatch, SeCVideoSegmentation, CLIPVisionLoader, ClothesSegment, WanVideoVAELoader, PoseAndFaceDetection, OnnxDetectionModelLoader, GrowMask, BlockifyMask, DrawMaskOnImage, Evaluate Integers, WanVideoClipVisionEncode, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoTorchCompileSettings, WanVideoContextOptions, ImageConcatMulti, ImageBlend, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoTextEncodeCached, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  角色替换  人物替换 动作迁移   wan2.2_2070512209431719938.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070512209431719938.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `DrawViTPose`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy showAnything`
- `VHS_LoadVideo`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoInfoLoaded`
- `SeCModelLoader`
- `easy int`
- `LayerUtility: ImageMaskScaleAsV2`
- `ImageFromBatch`
- `SeCVideoSegmentation`
- `CLIPVisionLoader`
- `ClothesSegment`
- `WanVideoVAELoader`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoContextOptions`
- `ImageConcatMulti`
- `ImageBlend`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **97%**（38/39）

**有卡**：`DrawViTPose`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageConcatMulti`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfoLoaded`、`SeCModelLoader`、`easy int`、`LayerUtility: ImageMaskScaleAsV2`、`ImageFromBatch`、`SeCVideoSegmentation`、`CLIPVisionLoader`、`ClothesSegment`、`WanVideoVAELoader`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoContextOptions`、`ImageBlend`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
