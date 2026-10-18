---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2067213881965109249.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2067213881965109249.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2067213881965109249.json
hash: c234d4391d682a80
coverage: 0.926829
learned_at: 2026-10-15 22:39:58
nodes: [ImageConcatMulti, VHS_VideoCombine, VHS_LoadVideo, LoadImage, SeCModelLoader, ImageFromBatch, ClothesSegment, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, VHS_VideoInfoLoaded, easy showAnything, easy int, PreviewImage, SeCVideoSegmentation, GrowMask, BlockifyMask, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawMaskOnImage, PreviewImage, DrawViTPose, ImageBlend, VHS_VideoCombine, WanVideoLoraSelectMulti, ImageConcatMulti, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetLoRAs, Evaluate Integers, WanVideoContextOptions, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoAnimateEmbeds, WanVideoVAELoader, WanVideoTextEncodeCached, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2067213881965109249.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067213881965109249.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（41 个）：
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `SeCModelLoader`
- `ImageFromBatch`
- `ClothesSegment`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageMaskScaleAsV2`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `easy int`
- `PreviewImage`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `PreviewImage`
- `DrawViTPose`
- `ImageBlend`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`
- `ImageConcatMulti`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `Evaluate Integers`
- `WanVideoContextOptions`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoAnimateEmbeds`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`

## 知识

覆盖率 **93%**（38/41）

**有卡**：`ImageConcatMulti`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`、`SeCModelLoader`、`ImageFromBatch`、`ClothesSegment`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`easy int`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`DrawViTPose`、`ImageBlend`、`WanVideoLoraSelectMulti`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`Evaluate Integers`、`WanVideoContextOptions`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoAnimateEmbeds`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
