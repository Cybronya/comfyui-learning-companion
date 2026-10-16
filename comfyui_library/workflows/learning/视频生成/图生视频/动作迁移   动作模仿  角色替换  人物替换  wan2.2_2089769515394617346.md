---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2089769515394617346.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2089769515394617346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2089769515394617346.json
hash: 6bd33edcfe199dc4
coverage: 1
learned_at: 2026-10-16 22:02:27
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoDecode, CLIPVisionLoader, VHS_VideoCombine, VHS_VideoInfoLoaded, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, DrawViTPose, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, ImageBlend, WanVideoVAELoader, OnnxDetectionModelLoader, easy int, SeCModelLoader, ImageFromBatch, LayerUtility: ImageMaskScaleAsV2, ClothesSegment, VHS_LoadVideo, LoadImage, GrowMask, BlockifyMask, SeCVideoSegmentation, PoseAndFaceDetection, DrawMaskOnImage, WanVideoContextOptions, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2089769515394617346.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2089769515394617346.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `DrawViTPose`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageBlend`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `easy int`
- `SeCModelLoader`
- `ImageFromBatch`
- `LayerUtility: ImageMaskScaleAsV2`
- `ClothesSegment`
- `VHS_LoadVideo`
- `LoadImage`
- `GrowMask`
- `BlockifyMask`
- `SeCVideoSegmentation`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `WanVideoContextOptions`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`CLIPVisionLoader`、`VHS_VideoCombine`、`VHS_VideoInfoLoaded`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`DrawViTPose`、`ImageConcatMulti`、`ImageBlend`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`easy int`、`SeCModelLoader`、`ImageFromBatch`、`LayerUtility: ImageMaskScaleAsV2`、`ClothesSegment`、`VHS_LoadVideo`、`LoadImage`、`GrowMask`、`BlockifyMask`、`SeCVideoSegmentation`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`WanVideoContextOptions`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
