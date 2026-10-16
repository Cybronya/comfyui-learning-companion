---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2092656695536340993.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2092656695536340993
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2092656695536340993.json
hash: 5a03bf98823f27f4
coverage: 1
learned_at: 2026-10-16 22:59:47
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, DrawViTPose, VHS_VideoCombine, VHS_LoadVideo, LayerUtility: ImageMaskScaleAsV2, easy int, ClothesSegment, SeCVideoSegmentation, GrowMask, BlockifyMask, DrawMaskOnImage, OnnxDetectionModelLoader, WanVideoVAELoader, SeCModelLoader, ImageFromBatch, PoseAndFaceDetection, CLIPVisionLoader, LoadImage, ImageBlend, WanVideoContextOptions, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2092656695536340993.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2092656695536340993.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
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
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `OnnxDetectionModelLoader`
- `WanVideoVAELoader`
- `SeCModelLoader`
- `ImageFromBatch`
- `PoseAndFaceDetection`
- `CLIPVisionLoader`
- `LoadImage`
- `ImageBlend`
- `WanVideoContextOptions`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`DrawViTPose`、`VHS_LoadVideo`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`SeCModelLoader`、`ImageFromBatch`、`PoseAndFaceDetection`、`CLIPVisionLoader`、`LoadImage`、`ImageBlend`、`WanVideoContextOptions`、`ImageConcatMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
