---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2085631135127793665.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2085631135127793665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2085631135127793665.json
hash: 03e31c078e6c3eea
coverage: 1
learned_at: 2026-10-16 20:50:51
nodes: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, ClothesSegment, VHS_LoadVideo, easy int, SeCModelLoader, ImageFromBatch, OnnxDetectionModelLoader, CLIPVisionLoader, SeCVideoSegmentation, GrowMask, WanVideoVAELoader, PoseAndFaceDetection, BlockifyMask, DrawMaskOnImage, WanVideoClipVisionEncode, DrawViTPose, Evaluate Integers, VHS_VideoCombine, ImageBlend, WanVideoAnimateEmbeds, WanVideoContextOptions, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, ImageConcatMulti, WanVideoBlockSwap, WanVideoTextEncodeCached, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, ImageConcatMulti, VHS_VideoCombine, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2085631135127793665.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2085631135127793665.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageMaskScaleAsV2`
- `ClothesSegment`
- `VHS_LoadVideo`
- `easy int`
- `SeCModelLoader`
- `ImageFromBatch`
- `OnnxDetectionModelLoader`
- `CLIPVisionLoader`
- `SeCVideoSegmentation`
- `GrowMask`
- `WanVideoVAELoader`
- `PoseAndFaceDetection`
- `BlockifyMask`
- `DrawMaskOnImage`
- `WanVideoClipVisionEncode`
- `DrawViTPose`
- `Evaluate Integers`
- `VHS_VideoCombine`
- `ImageBlend`
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `ImageConcatMulti`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`ClothesSegment`、`VHS_LoadVideo`、`easy int`、`SeCModelLoader`、`ImageFromBatch`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`SeCVideoSegmentation`、`GrowMask`、`WanVideoVAELoader`、`PoseAndFaceDetection`、`BlockifyMask`、`DrawMaskOnImage`、`WanVideoClipVisionEncode`、`DrawViTPose`、`Evaluate Integers`、`VHS_VideoCombine`、`ImageBlend`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`ImageConcatMulti`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`GetImageSizeAndCount`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
