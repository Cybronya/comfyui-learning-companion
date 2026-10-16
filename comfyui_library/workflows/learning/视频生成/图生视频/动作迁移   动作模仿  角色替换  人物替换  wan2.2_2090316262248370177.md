---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2090316262248370177.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2090316262248370177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2090316262248370177.json
hash: b9939fc56337fde0
coverage: 1
learned_at: 2026-10-16 22:02:27
nodes: [LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, LoadImage, VHS_LoadVideo, LayerUtility: ImageMaskScaleAsV2, SeCModelLoader, ImageFromBatch, easy int, ClothesSegment, SeCVideoSegmentation, GrowMask, VHS_VideoInfoLoaded, OnnxDetectionModelLoader, BlockifyMask, WanVideoVAELoader, CLIPVisionLoader, DrawMaskOnImage, PoseAndFaceDetection, WanVideoClipVisionEncode, VHS_VideoCombine, DrawViTPose, Evaluate Integers, WanVideoAnimateEmbeds, WanVideoContextOptions, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoTextEncodeCached, ImageBlend, ImageConcatMulti, WanVideoSampler, VHS_VideoCombine, WanVideoDecode, GetImageSizeAndCount, ImageConcatMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2090316262248370177.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2090316262248370177.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`
- `LayerUtility: ImageMaskScaleAsV2`
- `SeCModelLoader`
- `ImageFromBatch`
- `easy int`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `GrowMask`
- `VHS_VideoInfoLoaded`
- `OnnxDetectionModelLoader`
- `BlockifyMask`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `PoseAndFaceDetection`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `DrawViTPose`
- `Evaluate Integers`
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageBlend`
- `ImageConcatMulti`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `ImageConcatMulti`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`LoadImage`、`VHS_LoadVideo`、`LayerUtility: ImageMaskScaleAsV2`、`SeCModelLoader`、`ImageFromBatch`、`easy int`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`VHS_VideoInfoLoaded`、`OnnxDetectionModelLoader`、`BlockifyMask`、`WanVideoVAELoader`、`CLIPVisionLoader`、`DrawMaskOnImage`、`PoseAndFaceDetection`、`WanVideoClipVisionEncode`、`DrawViTPose`、`Evaluate Integers`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`ImageBlend`、`ImageConcatMulti`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
