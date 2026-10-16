---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2095208440544186369.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2095208440544186369
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2095208440544186369.json
hash: a442c029f2db590b
coverage: 1
learned_at: 2026-10-17 00:03:01
nodes: [LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, LayerUtility: ImageMaskScaleAsV2, easy int, SeCModelLoader, ClothesSegment, ImageFromBatch, GrowMask, WanVideoVAELoader, BlockifyMask, DrawMaskOnImage, CLIPVisionLoader, WanVideoClipVisionEncode, Evaluate Integers, DrawViTPose, WanVideoContextOptions, WanVideoAnimateEmbeds, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoSampler, VHS_LoadVideo, LoadImage, ImageConcatMulti, WanVideoLoraSelectMulti, ImageBlend, WanVideoTextEncodeCached, ImageConcatMulti, VHS_VideoCombine, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, GetImageSizeAndCount, WanVideoDecode, SeCVideoSegmentation, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_VideoCombine, VHS_VideoInfoLoaded]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2095208440544186369.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2095208440544186369.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `SeCModelLoader`
- `ClothesSegment`
- `ImageFromBatch`
- `GrowMask`
- `WanVideoVAELoader`
- `BlockifyMask`
- `DrawMaskOnImage`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `Evaluate Integers`
- `DrawViTPose`
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `LoadImage`
- `ImageConcatMulti`
- `WanVideoLoraSelectMulti`
- `ImageBlend`
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `SeCVideoSegmentation`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`SeCModelLoader`、`ClothesSegment`、`ImageFromBatch`、`GrowMask`、`WanVideoVAELoader`、`BlockifyMask`、`DrawMaskOnImage`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`Evaluate Integers`、`DrawViTPose`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoSampler`、`VHS_LoadVideo`、`LoadImage`、`ImageConcatMulti`、`WanVideoLoraSelectMulti`、`ImageBlend`、`WanVideoTextEncodeCached`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`GetImageSizeAndCount`、`WanVideoDecode`、`SeCVideoSegmentation`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`VHS_VideoInfoLoaded`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
