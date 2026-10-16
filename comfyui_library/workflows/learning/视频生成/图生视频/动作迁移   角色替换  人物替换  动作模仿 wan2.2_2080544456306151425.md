---
key: 视频生成/图生视频/动作迁移   角色替换  人物替换  动作模仿 wan2.2_2080544456306151425.json
name: 动作迁移   角色替换  人物替换  动作模仿 wan2.2_2080544456306151425.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2080544456306151425.json
hash: e1b49cdb7afe1d65
coverage: 1
learned_at: 2026-10-15 22:42:14
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, ImageConcatMulti, WanVideoDecode, WanVideoContextOptions, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, VHS_VideoCombine, ImageBlend, DrawViTPose, ImageConcatMulti, VHS_VideoCombine, VHS_LoadVideo, LoadImage, LayerUtility: ImageMaskScaleAsV2, SeCModelLoader, VHS_VideoInfoLoaded, ImageFromBatch, ClothesSegment, SeCVideoSegmentation, GrowMask, BlockifyMask, DrawMaskOnImage, OnnxDetectionModelLoader, WanVideoVAELoader, CLIPVisionLoader, PoseAndFaceDetection]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   角色替换  人物替换  动作模仿 wan2.2_2080544456306151425.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2080544456306151425.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `ImageConcatMulti`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `ImageBlend`
- `DrawViTPose`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `SeCModelLoader`
- `VHS_VideoInfoLoaded`
- `ImageFromBatch`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `OnnxDetectionModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoContextOptions`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageBlend`、`DrawViTPose`、`VHS_LoadVideo`、`LoadImage`、`LayerUtility: ImageMaskScaleAsV2`、`SeCModelLoader`、`VHS_VideoInfoLoaded`、`ImageFromBatch`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`PoseAndFaceDetection`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
