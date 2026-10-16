---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2072907655127064578.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2072907655127064578.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2072907655127064578.json
hash: a7fff37f1a62d4ba
coverage: 1
learned_at: 2026-10-15 22:40:58
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, LayerUtility: ImageMaskScaleAsV2, WanVideoAnimateEmbeds, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, ImageConcatMulti, VHS_LoadVideo, LoadImage, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, ImageFromBatch, VHS_VideoInfoLoaded, ClothesSegment, SeCVideoSegmentation, GrowMask, BlockifyMask, OnnxDetectionModelLoader, easy int, WanVideoVAELoader, SeCModelLoader, CLIPVisionLoader, WanVideoClipVisionEncode, VHS_VideoCombine, PoseAndFaceDetection, DrawViTPose, Evaluate Integers, DrawMaskOnImage, WanVideoContextOptions, ImageBlend, WanVideoLoraSelectMulti, WanVideoDecode]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2072907655127064578.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2072907655127064578.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageMaskScaleAsV2`
- `WanVideoAnimateEmbeds`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `VHS_LoadVideo`
- `LoadImage`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageFromBatch`
- `VHS_VideoInfoLoaded`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `OnnxDetectionModelLoader`
- `easy int`
- `WanVideoVAELoader`
- `SeCModelLoader`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `Evaluate Integers`
- `DrawMaskOnImage`
- `WanVideoContextOptions`
- `ImageBlend`
- `WanVideoLoraSelectMulti`
- `WanVideoDecode`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoAnimateEmbeds`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageConcatMulti`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoCombine`、`ImageFromBatch`、`VHS_VideoInfoLoaded`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`OnnxDetectionModelLoader`、`easy int`、`WanVideoVAELoader`、`SeCModelLoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`PoseAndFaceDetection`、`DrawViTPose`、`Evaluate Integers`、`DrawMaskOnImage`、`WanVideoContextOptions`、`ImageBlend`、`WanVideoLoraSelectMulti`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
