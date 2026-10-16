---
key: 视频生成/图生视频/wan2.2动作迁移 动作模仿 角色替换 人物替换 复刻舞蹈 复刻动作_2082772420339003394.json
name: wan2.2动作迁移 动作模仿 角色替换 人物替换 复刻舞蹈 复刻动作_2082772420339003394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2动作迁移 动作模仿 角色替换 人物替换 复刻舞蹈 复刻动作_2082772420339003394.json
hash: 2391220fd0f8fb89
coverage: 1
learned_at: 2026-10-16 01:17:13
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, WanVideoContextOptions, CLIPVisionLoader, PoseAndFaceDetection, VHS_VideoCombine, OnnxDetectionModelLoader, GrowMask, BlockifyMask, VHS_VideoInfoLoaded, easy int, SeCVideoSegmentation, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoVAELoader, LayerUtility: ImageMaskScaleAsV2, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoSetLoRAs, DrawMaskOnImage, WanVideoBlockSwap, WanVideoTextEncodeCached, ImageBlend, DrawViTPose, VHS_VideoCombine, ClothesSegment, ImageFromBatch, SeCModelLoader, Evaluate Integers, ImageConcatMulti, VHS_VideoCombine, ImageConcatMulti, GetImageSizeAndCount, VHS_LoadVideo, ImageConcatMulti, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2动作迁移 动作模仿 角色替换 人物替换 复刻舞蹈 复刻动作_2082772420339003394.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/wan2.2动作迁移 动作模仿 角色替换 人物替换 复刻舞蹈 复刻动作_2082772420339003394.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
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
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `DrawMaskOnImage`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageBlend`
- `DrawViTPose`
- `VHS_VideoCombine`
- `ClothesSegment`
- `ImageFromBatch`
- `SeCModelLoader`
- `Evaluate Integers`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `VHS_LoadVideo`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **100%**（40/40）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoContextOptions`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`GrowMask`、`BlockifyMask`、`VHS_VideoInfoLoaded`、`easy int`、`SeCVideoSegmentation`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVAELoader`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`DrawMaskOnImage`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageBlend`、`DrawViTPose`、`ClothesSegment`、`ImageFromBatch`、`SeCModelLoader`、`Evaluate Integers`、`ImageConcatMulti`、`GetImageSizeAndCount`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
