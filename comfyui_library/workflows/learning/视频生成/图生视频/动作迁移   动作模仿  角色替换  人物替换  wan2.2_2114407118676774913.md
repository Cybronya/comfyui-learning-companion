---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2114407118676774913.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2114407118676774913
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2114407118676774913.json
hash: 27bff9926158dde2
coverage: 0.952381
learned_at: 2026-10-26 22:15:30
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoTextEncodeCached, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, SetNode, VHS_VideoCombine, GetImageSizeAndCount, GetNode, LayerUtility: ImageMaskScaleAsV2, easy int, ImageFromBatch, SeCModelLoader, VHS_VideoInfoLoaded, ClothesSegment, SeCVideoSegmentation, GrowMask, BlockifyMask, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawMaskOnImage, WanVideoVAELoader, CLIPVisionLoader, LoadImage, ImageConcatMulti, Evaluate Integers, DrawViTPose, WanVideoContextOptions, ImageBlend, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2114407118676774913.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2114407118676774913.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（42 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `SetNode`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `GetNode`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `ImageFromBatch`
- `SeCModelLoader`
- `VHS_VideoInfoLoaded`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `LoadImage`
- `ImageConcatMulti`
- `Evaluate Integers`
- `DrawViTPose`
- `WanVideoContextOptions`
- `ImageBlend`
- `VHS_LoadVideo`

## 知识

覆盖率 **95%**（40/42）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageConcatMulti`、`GetImageSizeAndCount`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`ImageFromBatch`、`SeCModelLoader`、`VHS_VideoInfoLoaded`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`WanVideoVAELoader`、`CLIPVisionLoader`、`LoadImage`、`Evaluate Integers`、`DrawViTPose`、`WanVideoContextOptions`、`ImageBlend`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
