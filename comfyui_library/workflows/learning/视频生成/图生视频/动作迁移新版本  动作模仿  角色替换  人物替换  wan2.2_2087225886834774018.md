---
key: 视频生成/图生视频/动作迁移新版本  动作模仿  角色替换  人物替换  wan2.2_2087225886834774018.json
name: 动作迁移新版本  动作模仿  角色替换  人物替换  wan2.2_2087225886834774018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移新版本  动作模仿  角色替换  人物替换  wan2.2_2087225886834774018.json
hash: b9d85198d93682a5
coverage: 0.974359
learned_at: 2026-10-16 21:28:05
nodes: [ImageConcatMulti, PoseAndFaceDetection, VHS_VideoCombine, VHS_VideoInfoLoaded, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, LayerUtility: ImageMaskScaleAsV2, GetImageSizeAndCount, WanVideoBlockSwap, VHS_VideoCombine, DrawViTPose, ImageConcatMulti, easy showAnything, SeCModelLoader, VHS_VideoCombine, LoadImage, ImageFromBatch, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, WanVideoContextOptions, ImageBlend, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoTextEncodeCached, ClothesSegment, SeCVideoSegmentation, BlockifyMask, GrowMask, OnnxDetectionModelLoader, WanVideoVAELoader, CLIPVisionLoader, WanVideoModelLoader, WanVideoDecode, DrawMaskOnImage, Evaluate Integers, WanVideoTorchCompileSettings, easy int, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移新版本  动作模仿  角色替换  人物替换  wan2.2_2087225886834774018.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移新版本  动作模仿  角色替换  人物替换  wan2.2_2087225886834774018.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `ImageConcatMulti`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageMaskScaleAsV2`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `DrawViTPose`
- `ImageConcatMulti`
- `easy showAnything`
- `SeCModelLoader`
- `VHS_VideoCombine`
- `LoadImage`
- `ImageFromBatch`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `ImageBlend`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `BlockifyMask`
- `GrowMask`
- `OnnxDetectionModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `DrawMaskOnImage`
- `Evaluate Integers`
- `WanVideoTorchCompileSettings`
- `easy int`
- `VHS_LoadVideo`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`ImageConcatMulti`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`VHS_VideoInfoLoaded`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`LayerUtility: ImageMaskScaleAsV2`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`DrawViTPose`、`SeCModelLoader`、`LoadImage`、`ImageFromBatch`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`ImageBlend`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`ClothesSegment`、`SeCVideoSegmentation`、`BlockifyMask`、`GrowMask`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoModelLoader`、`WanVideoDecode`、`DrawMaskOnImage`、`Evaluate Integers`、`WanVideoTorchCompileSettings`、`easy int`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
