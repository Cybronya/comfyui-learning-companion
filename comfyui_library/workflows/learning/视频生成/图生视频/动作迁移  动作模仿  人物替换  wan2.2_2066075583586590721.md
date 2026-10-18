---
key: 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2066075583586590721.json
name: 动作迁移  动作模仿  人物替换  wan2.2_2066075583586590721.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2066075583586590721.json
hash: e28cfe052b4ab9d6
coverage: 0.926829
learned_at: 2026-10-15 22:39:46
nodes: [LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoInfoLoaded, easy showAnything, easy int, GrowMask, BlockifyMask, PreviewImage, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, GetImageSizeAndCount, WanVideoDecode, WanVideoVAELoader, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoSetBlockSwap, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoTextEncodeCached, WanVideoClipVisionEncode, CLIPVisionLoader, Evaluate Integers, WanVideoContextOptions, ImageConcatMulti, OnnxDetectionModelLoader, LoadImage, LayerUtility: ImageMaskScaleAsV2, PreviewImage, SeCModelLoader, SeCVideoSegmentation, ClothesSegment, ImageFromBatch, PoseAndFaceDetection, DrawMaskOnImage, DrawViTPose, ImageBlend, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移  动作模仿  人物替换  wan2.2_2066075583586590721.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2066075583586590721.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（41 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `easy int`
- `GrowMask`
- `BlockifyMask`
- `PreviewImage`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `Evaluate Integers`
- `WanVideoContextOptions`
- `ImageConcatMulti`
- `OnnxDetectionModelLoader`
- `LoadImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `PreviewImage`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `ClothesSegment`
- `ImageFromBatch`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `DrawViTPose`
- `ImageBlend`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 知识

覆盖率 **93%**（38/41）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfoLoaded`、`easy int`、`GrowMask`、`BlockifyMask`、`ImageConcatMulti`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoSetBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`Evaluate Integers`、`WanVideoContextOptions`、`OnnxDetectionModelLoader`、`LoadImage`、`LayerUtility: ImageMaskScaleAsV2`、`SeCModelLoader`、`SeCVideoSegmentation`、`ClothesSegment`、`ImageFromBatch`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`DrawViTPose`、`ImageBlend`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
