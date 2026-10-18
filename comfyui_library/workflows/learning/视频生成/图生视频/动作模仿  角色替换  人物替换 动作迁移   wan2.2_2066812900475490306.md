---
key: 视频生成/图生视频/动作模仿  角色替换  人物替换 动作迁移   wan2.2_2066812900475490306.json
name: 动作模仿  角色替换  人物替换 动作迁移   wan2.2_2066812900475490306.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作模仿  角色替换  人物替换 动作迁移   wan2.2_2066812900475490306.json
hash: 2df6c0cc7c0d05a4
coverage: 0.974359
learned_at: 2026-10-15 22:39:53
nodes: [VHS_VideoCombine, WanVideoModelLoader, GetImageSizeAndCount, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetBlockSwap, ImageConcatMulti, VHS_VideoCombine, WanVideoDecode, WanVideoContextOptions, VHS_VideoCombine, VHS_VideoInfoLoaded, easy int, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, LayerUtility: ImageMaskScaleAsV2, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, WanVideoTextEncodeCached, VHS_LoadVideo, LoadImage, easy showAnything, SeCModelLoader, ImageFromBatch, ClothesSegment, SeCVideoSegmentation, GrowMask, OnnxDetectionModelLoader, BlockifyMask, DrawMaskOnImage, PoseAndFaceDetection, WanVideoVAELoader, CLIPVisionLoader, ImageBlend, ImageConcatMulti, DrawViTPose]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  角色替换  人物替换 动作迁移   wan2.2_2066812900475490306.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2066812900475490306.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `GetImageSizeAndCount`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageMaskScaleAsV2`
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `VHS_LoadVideo`
- `LoadImage`
- `easy showAnything`
- `SeCModelLoader`
- `ImageFromBatch`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `GrowMask`
- `OnnxDetectionModelLoader`
- `BlockifyMask`
- `DrawMaskOnImage`
- `PoseAndFaceDetection`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `ImageBlend`
- `ImageConcatMulti`
- `DrawViTPose`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`VHS_VideoCombine`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoContextOptions`、`VHS_VideoInfoLoaded`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`、`LoadImage`、`SeCModelLoader`、`ImageFromBatch`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`OnnxDetectionModelLoader`、`BlockifyMask`、`DrawMaskOnImage`、`PoseAndFaceDetection`、`WanVideoVAELoader`、`CLIPVisionLoader`、`ImageBlend`、`DrawViTPose`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
