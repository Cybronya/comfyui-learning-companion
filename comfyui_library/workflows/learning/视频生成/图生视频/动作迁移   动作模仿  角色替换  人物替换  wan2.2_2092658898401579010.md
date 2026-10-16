---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2092658898401579010.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2092658898401579010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2092658898401579010.json
hash: fe94e338dad18588
coverage: 1
learned_at: 2026-10-16 22:59:47
nodes: [WanVideoSetBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSetLoRAs, WanVideoBlockSwap, VHS_VideoInfoLoaded, easy int, SeCModelLoader, ClothesSegment, ImageFromBatch, GrowMask, BlockifyMask, DrawMaskOnImage, WanVideoClipVisionEncode, Evaluate Integers, DrawViTPose, WanVideoContextOptions, WanVideoAnimateEmbeds, WanVideoTorchCompileSettings, WanVideoModelLoader, ImageBlend, WanVideoDecode, VHS_LoadVideo, LoadImage, GetImageSizeAndCount, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, WanVideoLoraSelectMulti, WanVideoTextEncodeCached, ImageConcatMulti, WanVideoSampler, OnnxDetectionModelLoader, SeCVideoSegmentation, WanVideoVAELoader, VHS_VideoCombine, PoseAndFaceDetection, CLIPVisionLoader, LayerUtility: ImageMaskScaleAsV2]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2092658898401579010.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2092658898401579010.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoSetBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `VHS_VideoInfoLoaded`
- `easy int`
- `SeCModelLoader`
- `ClothesSegment`
- `ImageFromBatch`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `WanVideoClipVisionEncode`
- `Evaluate Integers`
- `DrawViTPose`
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `ImageBlend`
- `WanVideoDecode`
- `VHS_LoadVideo`
- `LoadImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `WanVideoSampler` ★核心
- `OnnxDetectionModelLoader`
- `SeCVideoSegmentation`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `CLIPVisionLoader`
- `LayerUtility: ImageMaskScaleAsV2`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`WanVideoSetBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`VHS_VideoInfoLoaded`、`easy int`、`SeCModelLoader`、`ClothesSegment`、`ImageFromBatch`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`WanVideoClipVisionEncode`、`Evaluate Integers`、`DrawViTPose`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`ImageBlend`、`WanVideoDecode`、`VHS_LoadVideo`、`LoadImage`、`GetImageSizeAndCount`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`OnnxDetectionModelLoader`、`SeCVideoSegmentation`、`WanVideoVAELoader`、`PoseAndFaceDetection`、`CLIPVisionLoader`、`LayerUtility: ImageMaskScaleAsV2`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
