---
key: 视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2083955049767718914.json
name: 动作模仿  动作迁移   角色替换  人物替换  wan2.2_2083955049767718914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2083955049767718914.json
hash: 85cdaee5e05bec18
coverage: 1
learned_at: 2026-10-16 19:17:33
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, ImageConcatMulti, WanVideoDecode, WanVideoContextOptions, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, DrawViTPose, ImageConcatMulti, VHS_VideoCombine, VHS_LoadVideo, SeCModelLoader, LayerUtility: ImageMaskScaleAsV2, ImageFromBatch, easy int, ClothesSegment, SeCVideoSegmentation, GrowMask, OnnxDetectionModelLoader, WanVideoVAELoader, CLIPVisionLoader, BlockifyMask, PoseAndFaceDetection, DrawMaskOnImage, ImageBlend, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2083955049767718914.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作模仿  动作迁移   角色替换  人物替换  wan2.2_2083955049767718914.json`

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
- `DrawViTPose`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `SeCModelLoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `ImageFromBatch`
- `easy int`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `GrowMask`
- `OnnxDetectionModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `BlockifyMask`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `ImageBlend`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoContextOptions`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`DrawViTPose`、`VHS_LoadVideo`、`SeCModelLoader`、`LayerUtility: ImageMaskScaleAsV2`、`ImageFromBatch`、`easy int`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`BlockifyMask`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`ImageBlend`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
