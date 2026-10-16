---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2092554277284831233.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2092554277284831233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2092554277284831233.json
hash: 94fa405a1356a486
coverage: 1
learned_at: 2026-10-16 22:59:47
nodes: [WanVideoSetBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSetLoRAs, WanVideoBlockSwap, VHS_VideoCombine, LayerUtility: ImageMaskScaleAsV2, easy int, SeCModelLoader, SeCVideoSegmentation, GrowMask, WanVideoVAELoader, OnnxDetectionModelLoader, BlockifyMask, DrawMaskOnImage, PoseAndFaceDetection, DrawViTPose, WanVideoLoraSelectMulti, WanVideoSampler, VHS_VideoCombine, VHS_LoadVideo, LoadImage, VHS_VideoCombine, CLIPVisionLoader, VHS_VideoInfoLoaded, WanVideoDecode, ImageConcatMulti, GetImageSizeAndCount, WanVideoTorchCompileSettings, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoAnimateEmbeds, ImageConcatMulti, WanVideoTextEncodeCached, ImageBlend, ClothesSegment, WanVideoModelLoader, ImageFromBatch, Evaluate Integers]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2092554277284831233.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2092554277284831233.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoSetBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `GrowMask`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `BlockifyMask`
- `DrawMaskOnImage`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `WanVideoLoraSelectMulti`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `VHS_VideoInfoLoaded`
- `WanVideoDecode`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `WanVideoTorchCompileSettings`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `ImageConcatMulti`
- `WanVideoTextEncodeCached`
- `ImageBlend`
- `ClothesSegment`
- `WanVideoModelLoader`
- `ImageFromBatch`
- `Evaluate Integers`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`WanVideoSetBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`SeCModelLoader`、`SeCVideoSegmentation`、`GrowMask`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`BlockifyMask`、`DrawMaskOnImage`、`PoseAndFaceDetection`、`DrawViTPose`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`VHS_LoadVideo`、`LoadImage`、`CLIPVisionLoader`、`VHS_VideoInfoLoaded`、`WanVideoDecode`、`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`WanVideoClipVisionEncode`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`WanVideoTextEncodeCached`、`ImageBlend`、`ClothesSegment`、`WanVideoModelLoader`、`ImageFromBatch`、`Evaluate Integers`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
