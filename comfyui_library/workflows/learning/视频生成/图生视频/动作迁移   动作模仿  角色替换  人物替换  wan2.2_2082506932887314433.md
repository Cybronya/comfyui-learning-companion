---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2082506932887314433.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2082506932887314433.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2082506932887314433.json
hash: ea4bf263cc700fe6
coverage: 1
learned_at: 2026-10-15 22:42:32
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, WanVideoContextOptions, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoTextEncodeCached, ImageBlend, DrawViTPose, ImageConcatMulti, LoadImage, LayerUtility: ImageMaskScaleAsV2, VHS_VideoInfoLoaded, easy int, SeCModelLoader, ImageFromBatch, ClothesSegment, SeCVideoSegmentation, GrowMask, BlockifyMask, DrawMaskOnImage, OnnxDetectionModelLoader, WanVideoVAELoader, CLIPVisionLoader, PoseAndFaceDetection, VHS_VideoCombine, VHS_VideoCombine, GetImageSizeAndCount, VHS_LoadVideo, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2082506932887314433.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2082506932887314433.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
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
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageBlend`
- `DrawViTPose`
- `ImageConcatMulti`
- `LoadImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `VHS_VideoInfoLoaded`
- `easy int`
- `SeCModelLoader`
- `ImageFromBatch`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `OnnxDetectionModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `VHS_LoadVideo`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（40/40）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoContextOptions`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageBlend`、`DrawViTPose`、`ImageConcatMulti`、`LoadImage`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`easy int`、`SeCModelLoader`、`ImageFromBatch`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`GetImageSizeAndCount`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
