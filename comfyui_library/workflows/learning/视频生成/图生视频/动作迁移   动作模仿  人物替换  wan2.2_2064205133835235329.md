---
key: 视频生成/图生视频/动作迁移   动作模仿  人物替换  wan2.2_2064205133835235329.json
name: 动作迁移   动作模仿  人物替换  wan2.2_2064205133835235329.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2064205133835235329.json
hash: ff01da3d0d33a7c1
coverage: 0.926829
learned_at: 2026-10-15 22:39:21
nodes: [WanVideoVAELoader, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, GetImageSizeAndCount, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoDecode, WanVideoAnimateEmbeds, WanVideoContextOptions, WanVideoClipVisionEncode, ImageConcatMulti, VHS_VideoCombine, ImageBlend, CLIPVisionLoader, VHS_LoadVideo, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoInfoLoaded, easy showAnything, easy int, LayerUtility: ImageMaskScaleAsV2, ImageFromBatch, PreviewImage, ClothesSegment, SeCVideoSegmentation, SeCModelLoader, WanVideoTextEncodeCached, GrowMask, BlockifyMask, DrawMaskOnImage, PreviewImage, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, WanVideoTorchCompileSettings, WanVideoModelLoader, Evaluate Integers]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  人物替换  wan2.2_2064205133835235329.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064205133835235329.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（41 个）：
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `WanVideoClipVisionEncode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageBlend`
- `CLIPVisionLoader`
- `VHS_LoadVideo`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `easy int`
- `LayerUtility: ImageMaskScaleAsV2`
- `ImageFromBatch`
- `PreviewImage`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `WanVideoTextEncodeCached`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `PreviewImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `Evaluate Integers`

## 知识

覆盖率 **93%**（38/41）

**有卡**：`WanVideoVAELoader`、`VHS_VideoCombine`、`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`WanVideoClipVisionEncode`、`ImageBlend`、`CLIPVisionLoader`、`VHS_LoadVideo`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfoLoaded`、`easy int`、`LayerUtility: ImageMaskScaleAsV2`、`ImageFromBatch`、`ClothesSegment`、`SeCVideoSegmentation`、`SeCModelLoader`、`WanVideoTextEncodeCached`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`Evaluate Integers`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
