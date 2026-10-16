---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2091945556028518401.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2091945556028518401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2091945556028518401.json
hash: c6e7d1b824cfde20
coverage: 1
learned_at: 2026-10-16 22:31:00
nodes: [WanVideoSetBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSetLoRAs, WanVideoBlockSwap, LoadImage, LayerUtility: ImageMaskScaleAsV2, VHS_VideoInfoLoaded, easy int, SeCModelLoader, ClothesSegment, ImageFromBatch, WanVideoVAELoader, OnnxDetectionModelLoader, DrawMaskOnImage, CLIPVisionLoader, WanVideoClipVisionEncode, Evaluate Integers, DrawViTPose, WanVideoContextOptions, WanVideoAnimateEmbeds, WanVideoTorchCompileSettings, WanVideoModelLoader, ImageBlend, ImageConcatMulti, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, WanVideoLoraSelectMulti, WanVideoTextEncodeCached, GrowMask, SeCVideoSegmentation, VHS_LoadVideo, PoseAndFaceDetection, BlockifyMask]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2091945556028518401.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2091945556028518401.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoSetBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `LoadImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `VHS_VideoInfoLoaded`
- `easy int`
- `SeCModelLoader`
- `ClothesSegment`
- `ImageFromBatch`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `DrawMaskOnImage`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `Evaluate Integers`
- `DrawViTPose`
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `ImageBlend`
- `ImageConcatMulti`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncodeCached`
- `GrowMask`
- `SeCVideoSegmentation`
- `VHS_LoadVideo`
- `PoseAndFaceDetection`
- `BlockifyMask`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`WanVideoSetBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`LoadImage`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`easy int`、`SeCModelLoader`、`ClothesSegment`、`ImageFromBatch`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`DrawMaskOnImage`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`Evaluate Integers`、`DrawViTPose`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`ImageBlend`、`ImageConcatMulti`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`、`GrowMask`、`SeCVideoSegmentation`、`VHS_LoadVideo`、`PoseAndFaceDetection`、`BlockifyMask`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
