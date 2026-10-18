---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2080717614837489666.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2080717614837489666.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2080717614837489666.json
hash: 548fab91c9748883
coverage: 1
learned_at: 2026-10-15 22:42:17
nodes: [WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, ImageConcatMulti, VHS_LoadVideo, LoadImage, LayerUtility: ImageMaskScaleAsV2, VHS_VideoInfoLoaded, ImageFromBatch, SeCModelLoader, SeCVideoSegmentation, ClothesSegment, GrowMask, BlockifyMask, WanVideoVAELoader, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawMaskOnImage, CLIPVisionLoader, VHS_VideoCombine, WanVideoClipVisionEncode, Evaluate Integers, DrawViTPose, ImageBlend, WanVideoContextOptions, WanVideoLoraSelectMulti, WanVideoAnimateEmbeds, WanVideoTorchCompileSettings, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2080717614837489666.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2080717614837489666.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `VHS_LoadVideo`
- `LoadImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `VHS_VideoInfoLoaded`
- `ImageFromBatch`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `ClothesSegment`
- `GrowMask`
- `BlockifyMask`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `Evaluate Integers`
- `DrawViTPose`
- `ImageBlend`
- `WanVideoContextOptions`
- `WanVideoLoraSelectMulti`
- `WanVideoAnimateEmbeds`
- `WanVideoTorchCompileSettings`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageConcatMulti`、`VHS_LoadVideo`、`LoadImage`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`ImageFromBatch`、`SeCModelLoader`、`SeCVideoSegmentation`、`ClothesSegment`、`GrowMask`、`BlockifyMask`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`CLIPVisionLoader`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`Evaluate Integers`、`DrawViTPose`、`ImageBlend`、`WanVideoContextOptions`、`WanVideoLoraSelectMulti`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
