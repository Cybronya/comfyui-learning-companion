---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2074824242725736450.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2074824242725736450.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2074824242725736450.json
hash: ac3f5404921a7ee7
coverage: 0.974359
learned_at: 2026-10-15 22:41:19
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, ImageConcatMulti, WanVideoDecode, WanVideoContextOptions, CLIPVisionLoader, PoseAndFaceDetection, VHS_VideoCombine, OnnxDetectionModelLoader, VHS_VideoInfoLoaded, easy int, SeCVideoSegmentation, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoVAELoader, LayerUtility: ImageMaskScaleAsV2, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, VHS_VideoCombine, DrawViTPose, ImageConcatMulti, VHS_VideoCombine, ClothesSegment, LoadImage, ImageFromBatch, SeCModelLoader, easy showAnything, VHS_LoadVideo, GrowMask, BlockifyMask, DrawMaskOnImage, ImageBlend]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2074824242725736450.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2074824242725736450.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `ImageConcatMulti`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `VHS_VideoInfoLoaded`
- `easy int`
- `SeCVideoSegmentation`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `DrawViTPose`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ClothesSegment`
- `LoadImage`
- `ImageFromBatch`
- `SeCModelLoader`
- `easy showAnything`
- `VHS_LoadVideo`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `ImageBlend`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoContextOptions`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`VHS_VideoInfoLoaded`、`easy int`、`SeCVideoSegmentation`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVAELoader`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`DrawViTPose`、`ClothesSegment`、`LoadImage`、`ImageFromBatch`、`SeCModelLoader`、`VHS_LoadVideo`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`ImageBlend`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
