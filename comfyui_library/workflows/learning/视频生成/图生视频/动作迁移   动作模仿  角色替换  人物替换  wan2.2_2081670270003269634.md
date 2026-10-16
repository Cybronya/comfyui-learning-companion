---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2081670270003269634.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2081670270003269634.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2081670270003269634.json
hash: b3a148f88b110512
coverage: 0.974359
learned_at: 2026-10-15 22:42:24
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, WanVideoContextOptions, CLIPVisionLoader, PoseAndFaceDetection, VHS_VideoCombine, OnnxDetectionModelLoader, GrowMask, BlockifyMask, VHS_VideoInfoLoaded, easy int, SeCVideoSegmentation, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoVAELoader, LayerUtility: ImageMaskScaleAsV2, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, DrawMaskOnImage, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, ImageBlend, DrawViTPose, ImageConcatMulti, ClothesSegment, ImageFromBatch, SeCModelLoader, easy showAnything, VHS_LoadVideo, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2081670270003269634.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2081670270003269634.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `GrowMask`
- `BlockifyMask`
- `VHS_VideoInfoLoaded`
- `easy int`
- `SeCVideoSegmentation`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageBlend`
- `DrawViTPose`
- `ImageConcatMulti`
- `ClothesSegment`
- `ImageFromBatch`
- `SeCModelLoader`
- `easy showAnything`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoContextOptions`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`GrowMask`、`BlockifyMask`、`VHS_VideoInfoLoaded`、`easy int`、`SeCVideoSegmentation`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVAELoader`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`DrawMaskOnImage`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageBlend`、`DrawViTPose`、`ImageConcatMulti`、`ClothesSegment`、`ImageFromBatch`、`SeCModelLoader`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
