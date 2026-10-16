---
key: 视频生成/图生视频/角色替换  人物替换   动作迁移   动作模仿   wan2.2_2078347760310505474.json
name: 角色替换  人物替换   动作迁移   动作模仿   wan2.2_2078347760310505474.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2078347760310505474.json
hash: b629f132d47b11c3
coverage: 1
learned_at: 2026-10-15 22:41:51
nodes: [WanVideoAnimateEmbeds, VHS_LoadVideo, ImageConcatMulti, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, WanVideoDecode, WanVideoSampler, WanVideoTextEncodeCached, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, Evaluate Integers, DrawViTPose, WanVideoClipVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageMaskScaleAsV2, easy int, ImageFromBatch, SeCModelLoader, ClothesSegment, SeCVideoSegmentation, GrowMask, BlockifyMask, DrawMaskOnImage, WanVideoVAELoader, OnnxDetectionModelLoader, CLIPVisionLoader, PoseAndFaceDetection, VHS_VideoCombine, GetImageSizeAndCount, WanVideoTorchCompileSettings, WanVideoContextOptions, WanVideoLoraSelectMulti, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/角色替换  人物替换   动作迁移   动作模仿   wan2.2_2078347760310505474.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2078347760310505474.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoAnimateEmbeds`
- `VHS_LoadVideo`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `Evaluate Integers`
- `DrawViTPose`
- `WanVideoClipVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `ImageFromBatch`
- `SeCModelLoader`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `WanVideoTorchCompileSettings`
- `WanVideoContextOptions`
- `WanVideoLoraSelectMulti`
- `LoadImage`

## 知识

覆盖率 **100%**（36/36）

**有卡**：`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`Evaluate Integers`、`DrawViTPose`、`WanVideoClipVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`ImageFromBatch`、`SeCModelLoader`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`WanVideoContextOptions`、`WanVideoLoraSelectMulti`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
