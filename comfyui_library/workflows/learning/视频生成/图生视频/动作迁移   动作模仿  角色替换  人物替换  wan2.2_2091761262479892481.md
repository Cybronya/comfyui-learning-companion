---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2091761262479892481.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2091761262479892481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2091761262479892481.json
hash: ae5a8473f1e3b98d
coverage: 1
learned_at: 2026-10-16 22:31:00
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: ImageMaskScaleAsV2, ImageFromBatch, GrowMask, WanVideoVAELoader, OnnxDetectionModelLoader, BlockifyMask, DrawMaskOnImage, VHS_VideoCombine, WanVideoContextOptions, WanVideoAnimateEmbeds, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, ImageConcatMulti, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, ImageConcatMulti, ImageBlend, WanVideoTextEncodeCached, CLIPVisionLoader, easy int, SeCModelLoader, SeCVideoSegmentation, ClothesSegment, PoseAndFaceDetection, Evaluate Integers, WanVideoClipVisionEncode, DrawViTPose, LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2091761262479892481.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2091761262479892481.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: ImageMaskScaleAsV2`
- `ImageFromBatch`
- `GrowMask`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `BlockifyMask`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `ImageConcatMulti`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageBlend`
- `WanVideoTextEncodeCached`
- `CLIPVisionLoader`
- `easy int`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `ClothesSegment`
- `PoseAndFaceDetection`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `DrawViTPose`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`LayerUtility: ImageMaskScaleAsV2`、`ImageFromBatch`、`GrowMask`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`BlockifyMask`、`DrawMaskOnImage`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`ImageConcatMulti`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`ImageBlend`、`WanVideoTextEncodeCached`、`CLIPVisionLoader`、`easy int`、`SeCModelLoader`、`SeCVideoSegmentation`、`ClothesSegment`、`PoseAndFaceDetection`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`DrawViTPose`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
