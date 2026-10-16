---
key: 视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2083114916705296386.json
name: 动作模仿  动作迁移   角色替换  人物替换  wan2.2_2083114916705296386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2083114916705296386.json
hash: 16220ddbab1a5a86
coverage: 0.904762
learned_at: 2026-10-16 19:17:33
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, WanVideoContextOptions, CLIPVisionLoader, PoseAndFaceDetection, VHS_VideoCombine, OnnxDetectionModelLoader, GrowMask, BlockifyMask, SeCVideoSegmentation, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoVAELoader, LayerUtility: ImageMaskScaleAsV2, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, DrawMaskOnImage, WanVideoBlockSwap, WanVideoTextEncodeCached, ImageBlend, DrawViTPose, ImageConcatMulti, ClothesSegment, ImageFromBatch, SeCModelLoader, LoadImage, VHS_VideoCombine, GetImageSizeAndCount, SetNode, VHS_LoadVideo, SetNode, GetNode, ImageConcatMulti, GetNode, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2083114916705296386.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2083114916705296386.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（42 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `GrowMask`
- `BlockifyMask`
- `SeCVideoSegmentation`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `DrawMaskOnImage`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageBlend`
- `DrawViTPose`
- `ImageConcatMulti`
- `ClothesSegment`
- `ImageFromBatch`
- `SeCModelLoader`
- `LoadImage`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **90%**（38/42）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoContextOptions`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`GrowMask`、`BlockifyMask`、`SeCVideoSegmentation`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVAELoader`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`DrawMaskOnImage`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageBlend`、`DrawViTPose`、`ImageConcatMulti`、`ClothesSegment`、`ImageFromBatch`、`SeCModelLoader`、`LoadImage`、`GetImageSizeAndCount`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
