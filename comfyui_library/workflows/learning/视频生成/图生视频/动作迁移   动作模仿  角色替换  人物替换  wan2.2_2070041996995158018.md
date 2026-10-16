---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2070041996995158018.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2070041996995158018.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2070041996995158018.json
hash: c89585fb38531224
coverage: 0.974359
learned_at: 2026-10-15 22:40:34
nodes: [ImageConcatMulti, WanVideoVAELoader, VHS_VideoCombine, VHS_VideoCombine, ClothesSegment, ImageFromBatch, SeCModelLoader, easy showAnything, VHS_LoadVideo, LoadImage, VHS_VideoInfoLoaded, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, easy int, SeCVideoSegmentation, GrowMask, BlockifyMask, OnnxDetectionModelLoader, CLIPVisionLoader, PoseAndFaceDetection, DrawMaskOnImage, WanVideoClipVisionEncode, VHS_VideoCombine, WanVideoAnimateEmbeds, DrawViTPose, Evaluate Integers, ImageBlend, WanVideoContextOptions, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, WanVideoSetLoRAs, WanVideoBlockSwap, ImageConcatMulti, WanVideoSetBlockSwap, WanVideoTextEncodeCached]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2070041996995158018.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070041996995158018.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `ImageConcatMulti`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ClothesSegment`
- `ImageFromBatch`
- `SeCModelLoader`
- `easy showAnything`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoInfoLoaded`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `OnnxDetectionModelLoader`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `DrawViTPose`
- `Evaluate Integers`
- `ImageBlend`
- `WanVideoContextOptions`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `ImageConcatMulti`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`ImageConcatMulti`、`WanVideoVAELoader`、`VHS_VideoCombine`、`ClothesSegment`、`ImageFromBatch`、`SeCModelLoader`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoInfoLoaded`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`DrawViTPose`、`Evaluate Integers`、`ImageBlend`、`WanVideoContextOptions`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
