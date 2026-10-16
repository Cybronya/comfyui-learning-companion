---
key: 视频生成/图生视频/人物替换  角色替换  动作模仿  动作迁移   wan2.2_2082695605587107842.json
name: 人物替换  角色替换  动作模仿  动作迁移   wan2.2_2082695605587107842.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2082695605587107842.json
hash: 2ec4861c48a0fd32
coverage: 0.95122
learned_at: 2026-10-15 22:42:34
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoVAELoader, WanVideoAnimateEmbeds, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoTextEncodeCached, LoadImage, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, GetImageSizeAndCount, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: ImageMaskScaleAsV2, easy int, SeCModelLoader, ImageFromBatch, ClothesSegment, SetNode, GetNode, VHS_LoadVideo, ImageConcatMulti, GrowMask, CLIPVisionLoader, OnnxDetectionModelLoader, PoseAndFaceDetection, BlockifyMask, DrawMaskOnImage, WanVideoClipVisionEncode, DrawViTPose, Evaluate Integers, WanVideoContextOptions, ImageBlend, WanVideoLoraSelectMulti, SeCVideoSegmentation, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/人物替换  角色替换  动作模仿  动作迁移   wan2.2_2082695605587107842.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2082695605587107842.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（41 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoAnimateEmbeds`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `LoadImage`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `SeCModelLoader`
- `ImageFromBatch`
- `ClothesSegment`
- `SetNode`
- `GetNode`
- `VHS_LoadVideo`
- `ImageConcatMulti`
- `GrowMask`
- `CLIPVisionLoader`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `BlockifyMask`
- `DrawMaskOnImage`
- `WanVideoClipVisionEncode`
- `DrawViTPose`
- `Evaluate Integers`
- `WanVideoContextOptions`
- `ImageBlend`
- `WanVideoLoraSelectMulti`
- `SeCVideoSegmentation`
- `VHS_VideoCombine`

## 知识

覆盖率 **95%**（39/41）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`LoadImage`、`VHS_VideoCombine`、`ImageConcatMulti`、`GetImageSizeAndCount`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`SeCModelLoader`、`ImageFromBatch`、`ClothesSegment`、`VHS_LoadVideo`、`GrowMask`、`CLIPVisionLoader`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`BlockifyMask`、`DrawMaskOnImage`、`WanVideoClipVisionEncode`、`DrawViTPose`、`Evaluate Integers`、`WanVideoContextOptions`、`ImageBlend`、`WanVideoLoraSelectMulti`、`SeCVideoSegmentation`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
