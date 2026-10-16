---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2082015579648643074.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2082015579648643074.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2082015579648643074.json
hash: 6830ebc9083031ce
coverage: 1
learned_at: 2026-10-15 22:42:26
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, LayerUtility: ImageMaskScaleAsV2, WanVideoAnimateEmbeds, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, ImageFromBatch, VHS_VideoInfoLoaded, ClothesSegment, SeCVideoSegmentation, GrowMask, BlockifyMask, OnnxDetectionModelLoader, easy int, WanVideoVAELoader, SeCModelLoader, CLIPVisionLoader, WanVideoClipVisionEncode, VHS_VideoCombine, PoseAndFaceDetection, DrawViTPose, Evaluate Integers, DrawMaskOnImage, WanVideoContextOptions, ImageBlend, WanVideoLoraSelectMulti, WanVideoDecode, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2082015579648643074.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2082015579648643074.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageMaskScaleAsV2`
- `WanVideoAnimateEmbeds`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageFromBatch`
- `VHS_VideoInfoLoaded`
- `ClothesSegment`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `OnnxDetectionModelLoader`
- `easy int`
- `WanVideoVAELoader`
- `SeCModelLoader`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `Evaluate Integers`
- `DrawMaskOnImage`
- `WanVideoContextOptions`
- `ImageBlend`
- `WanVideoLoraSelectMulti`
- `WanVideoDecode`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoAnimateEmbeds`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageConcatMulti`、`VHS_VideoCombine`、`ImageFromBatch`、`VHS_VideoInfoLoaded`、`ClothesSegment`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`OnnxDetectionModelLoader`、`easy int`、`WanVideoVAELoader`、`SeCModelLoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`PoseAndFaceDetection`、`DrawViTPose`、`Evaluate Integers`、`DrawMaskOnImage`、`WanVideoContextOptions`、`ImageBlend`、`WanVideoLoraSelectMulti`、`WanVideoDecode`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
