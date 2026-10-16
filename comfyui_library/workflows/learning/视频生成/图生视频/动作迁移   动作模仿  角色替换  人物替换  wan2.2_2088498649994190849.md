---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088498649994190849.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088498649994190849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088498649994190849.json
hash: 12b70137d16c9541
coverage: 1
learned_at: 2026-10-16 21:43:48
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, WanVideoContextOptions, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, DrawViTPose, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, ImageBlend, SeCModelLoader, ClothesSegment, LayerUtility: ImageMaskScaleAsV2, easy int, ImageFromBatch, GrowMask, BlockifyMask, DrawMaskOnImage, OnnxDetectionModelLoader, WanVideoVAELoader, CLIPVisionLoader, PoseAndFaceDetection, SeCVideoSegmentation, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088498649994190849.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2088498649994190849.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
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
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageBlend`
- `SeCModelLoader`
- `ClothesSegment`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `ImageFromBatch`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `OnnxDetectionModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `SeCVideoSegmentation`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoContextOptions`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`DrawViTPose`、`ImageConcatMulti`、`ImageBlend`、`SeCModelLoader`、`ClothesSegment`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`ImageFromBatch`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`SeCVideoSegmentation`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
