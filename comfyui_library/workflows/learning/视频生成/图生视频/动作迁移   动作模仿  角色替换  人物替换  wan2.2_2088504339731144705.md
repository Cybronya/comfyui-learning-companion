---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088504339731144705.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088504339731144705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088504339731144705.json
hash: b812d269e3fde40f
coverage: 1
learned_at: 2026-10-16 21:43:48
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoDecode, WanVideoContextOptions, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, DrawViTPose, ClothesSegment, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, ImageBlend, WanVideoSampler, WanVideoTextEncodeCached, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoLoraSelectMulti, ImageFromBatch, LayerUtility: ImageMaskScaleAsV2, easy int, VHS_VideoInfoLoaded, SeCModelLoader, SeCVideoSegmentation, OnnxDetectionModelLoader, CLIPVisionLoader, WanVideoVAELoader, GrowMask, BlockifyMask, DrawMaskOnImage, PoseAndFaceDetection, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088504339731144705.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088504339731144705.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `DrawViTPose`
- `ClothesSegment`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageBlend`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `ImageFromBatch`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `VHS_VideoInfoLoaded`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `OnnxDetectionModelLoader`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `PoseAndFaceDetection`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoContextOptions`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`DrawViTPose`、`ClothesSegment`、`ImageConcatMulti`、`ImageBlend`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`ImageFromBatch`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`VHS_VideoInfoLoaded`、`SeCModelLoader`、`SeCVideoSegmentation`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`WanVideoVAELoader`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`PoseAndFaceDetection`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
