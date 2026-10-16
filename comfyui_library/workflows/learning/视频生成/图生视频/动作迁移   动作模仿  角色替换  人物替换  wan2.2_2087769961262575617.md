---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2087769961262575617.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2087769961262575617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2087769961262575617.json
hash: 098f7b62accefac9
coverage: 1
learned_at: 2026-10-16 21:28:03
nodes: [WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, DrawViTPose, VHS_LoadVideo, LoadImage, WanVideoTorchCompileSettings, easy int, SeCModelLoader, LayerUtility: ImageMaskScaleAsV2, ImageFromBatch, ClothesSegment, SeCVideoSegmentation, GrowMask, WanVideoVAELoader, OnnxDetectionModelLoader, PoseAndFaceDetection, BlockifyMask, DrawMaskOnImage, CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, Evaluate Integers, ImageBlend, WanVideoContextOptions, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, WanVideoSampler, WanVideoTextEncodeCached]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2087769961262575617.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2087769961262575617.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `DrawViTPose`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `easy int`
- `SeCModelLoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `ImageFromBatch`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `GrowMask`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `BlockifyMask`
- `DrawMaskOnImage`
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Evaluate Integers`
- `ImageBlend`
- `WanVideoContextOptions`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`DrawViTPose`、`VHS_LoadVideo`、`LoadImage`、`WanVideoTorchCompileSettings`、`easy int`、`SeCModelLoader`、`LayerUtility: ImageMaskScaleAsV2`、`ImageFromBatch`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`BlockifyMask`、`DrawMaskOnImage`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`Evaluate Integers`、`ImageBlend`、`WanVideoContextOptions`、`ImageConcatMulti`、`WanVideoSampler`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
