---
key: 视频生成/图生视频/动作迁移 动作模仿 角色替换 人物替换 wan2.2_2062089104304726018.json
name: 动作迁移 动作模仿 角色替换 人物替换 wan2.2_2062089104304726018.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2062089104304726018.json
hash: 09bbfa30e1e3bb1e
coverage: 0.931818
learned_at: 2026-10-15 22:38:59
nodes: [ImageFromBatch, OnnxDetectionModelLoader, VHS_VideoInfoLoaded, easy int, easy int, PreviewImage, PreviewImage, easy showAnything, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, Evaluate Integers, ClothesSegment, ImageBlend, VHS_VideoCombine, DrawViTPose, PoseAndFaceDetection, SeCVideoSegmentation, DrawMaskOnImage, BlockifyMask, GrowMask, easy int, SeCModelLoader, ImageConcatMulti, VHS_LoadVideo, LoadImage, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, GetImageSizeAndCount, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, CLIPVisionLoader, WanVideoSampler, WanVideoContextOptions, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetBlockSwap, WanVideoAnimateEmbeds, WanVideoDecode]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移 动作模仿 角色替换 人物替换 wan2.2_2062089104304726018.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062089104304726018.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `ImageFromBatch`
- `OnnxDetectionModelLoader`
- `VHS_VideoInfoLoaded`
- `easy int`
- `easy int`
- `PreviewImage`
- `PreviewImage`
- `easy showAnything`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Evaluate Integers`
- `ClothesSegment`
- `ImageBlend`
- `VHS_VideoCombine`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `SeCVideoSegmentation`
- `DrawMaskOnImage`
- `BlockifyMask`
- `GrowMask`
- `easy int`
- `SeCModelLoader`
- `ImageConcatMulti`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetBlockSwap`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`

## 知识

覆盖率 **93%**（41/44）

**有卡**：`ImageFromBatch`、`OnnxDetectionModelLoader`、`VHS_VideoInfoLoaded`、`easy int`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`Evaluate Integers`、`ClothesSegment`、`ImageBlend`、`VHS_VideoCombine`、`DrawViTPose`、`PoseAndFaceDetection`、`SeCVideoSegmentation`、`DrawMaskOnImage`、`BlockifyMask`、`GrowMask`、`SeCModelLoader`、`ImageConcatMulti`、`VHS_LoadVideo`、`LoadImage`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`GetImageSizeAndCount`、`CLIPVisionLoader`、`WanVideoSampler`、`WanVideoContextOptions`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`WanVideoAnimateEmbeds`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
