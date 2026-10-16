---
key: 视频生成/图生视频/动作迁移调整版   动作模仿  角色替换  人物替换  wan2.2_2079476545160310785.json
name: 动作迁移调整版   动作模仿  角色替换  人物替换  wan2.2_2079476545160310785.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2079476545160310785.json
hash: 3559cf35596cc029
coverage: 0.974359
learned_at: 2026-10-15 22:42:02
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoDecode, CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, DrawViTPose, ImageConcatMulti, VHS_LoadVideo, LoadImage, LayerUtility: ImageMaskScaleAsV2, VHS_VideoInfoLoaded, easy int, easy showAnything, ImageFromBatch, ClothesSegment, SeCModelLoader, SeCVideoSegmentation, GrowMask, BlockifyMask, DrawMaskOnImage, WanVideoVAELoader, OnnxDetectionModelLoader, PoseAndFaceDetection, Evaluate Integers, VHS_VideoCombine, WanVideoContextOptions, ImageBlend, WanVideoClipVisionEncode, WanVideoTextEncodeCached, WanVideoLoraSelectMulti, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移调整版   动作模仿  角色替换  人物替换  wan2.2_2079476545160310785.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2079476545160310785.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `DrawViTPose`
- `ImageConcatMulti`
- `VHS_LoadVideo`
- `LoadImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `VHS_VideoInfoLoaded`
- `easy int`
- `easy showAnything`
- `ImageFromBatch`
- `ClothesSegment`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `Evaluate Integers`
- `VHS_VideoCombine`
- `WanVideoContextOptions`
- `ImageBlend`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncodeCached`
- `WanVideoLoraSelectMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`DrawViTPose`、`ImageConcatMulti`、`VHS_LoadVideo`、`LoadImage`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`easy int`、`ImageFromBatch`、`ClothesSegment`、`SeCModelLoader`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`Evaluate Integers`、`VHS_VideoCombine`、`WanVideoContextOptions`、`ImageBlend`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
