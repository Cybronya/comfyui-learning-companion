---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2089745324331061249.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2089745324331061249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2089745324331061249.json
hash: 2591c2ea7a51cd97
coverage: 1
learned_at: 2026-10-16 22:02:27
nodes: [LoadImage, VHS_LoadVideo, ImageFromBatch, easy int, ClothesSegment, SeCModelLoader, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, GrowMask, BlockifyMask, DrawMaskOnImage, SeCVideoSegmentation, WanVideoVAELoader, OnnxDetectionModelLoader, PoseAndFaceDetection, CLIPVisionLoader, WanVideoClipVisionEncode, VHS_VideoCombine, DrawViTPose, Evaluate Integers, WanVideoAnimateEmbeds, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoContextOptions, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoSampler, ImageBlend, ImageConcatMulti, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2089745324331061249.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2089745324331061249.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `LoadImage`
- `VHS_LoadVideo`
- `ImageFromBatch`
- `easy int`
- `ClothesSegment`
- `SeCModelLoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SeCVideoSegmentation`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `DrawViTPose`
- `Evaluate Integers`
- `WanVideoAnimateEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoContextOptions`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `ImageBlend`
- `ImageConcatMulti`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（39/39）

**有卡**：`LoadImage`、`VHS_LoadVideo`、`ImageFromBatch`、`easy int`、`ClothesSegment`、`SeCModelLoader`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`SeCVideoSegmentation`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`DrawViTPose`、`Evaluate Integers`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoContextOptions`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`ImageBlend`、`ImageConcatMulti`、`WanVideoDecode`、`GetImageSizeAndCount`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
