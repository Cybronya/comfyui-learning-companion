---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2090689101451321345.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2090689101451321345
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2090689101451321345.json
hash: 56d1ee0f1827a018
coverage: 1
learned_at: 2026-10-16 22:30:59
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, WanVideoContextOptions, CLIPVisionLoader, PoseAndFaceDetection, VHS_VideoCombine, OnnxDetectionModelLoader, GrowMask, BlockifyMask, VHS_VideoInfoLoaded, easy int, WanVideoSampler, WanVideoVAELoader, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, ImageFromBatch, SeCModelLoader, VHS_VideoCombine, Evaluate Integers, SeCVideoSegmentation, ClothesSegment, ImageConcatMulti, DrawViTPose, DrawMaskOnImage, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, ImageConcatMulti, ImageBlend, VHS_LoadVideo, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2090689101451321345.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2090689101451321345.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
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
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageFromBatch`
- `SeCModelLoader`
- `VHS_VideoCombine`
- `Evaluate Integers`
- `SeCVideoSegmentation`
- `ClothesSegment`
- `ImageConcatMulti`
- `DrawViTPose`
- `DrawMaskOnImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcatMulti`
- `ImageBlend`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoContextOptions`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`GrowMask`、`BlockifyMask`、`VHS_VideoInfoLoaded`、`easy int`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageFromBatch`、`SeCModelLoader`、`Evaluate Integers`、`SeCVideoSegmentation`、`ClothesSegment`、`ImageConcatMulti`、`DrawViTPose`、`DrawMaskOnImage`、`LayerUtility: ImageMaskScaleAsV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageBlend`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
