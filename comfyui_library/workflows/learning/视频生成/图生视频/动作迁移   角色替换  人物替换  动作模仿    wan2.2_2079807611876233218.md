---
key: 视频生成/图生视频/动作迁移   角色替换  人物替换  动作模仿    wan2.2_2079807611876233218.json
name: 动作迁移   角色替换  人物替换  动作模仿    wan2.2_2079807611876233218.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2079807611876233218.json
hash: 0e11fc8a4651353e
coverage: 1
learned_at: 2026-10-15 22:42:06
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoDecode, WanVideoContextOptions, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, ImageBlend, DrawViTPose, ImageConcatMulti, VHS_LoadVideo, LoadImage, LayerUtility: ImageMaskScaleAsV2, easy int, ImageFromBatch, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, ClothesSegment, SeCModelLoader, SeCVideoSegmentation, GrowMask, BlockifyMask, WanVideoVAELoader, OnnxDetectionModelLoader, DrawMaskOnImage, CLIPVisionLoader, PoseAndFaceDetection]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   角色替换  人物替换  动作模仿    wan2.2_2079807611876233218.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2079807611876233218.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageBlend`
- `DrawViTPose`
- `ImageConcatMulti`
- `VHS_LoadVideo`
- `LoadImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `easy int`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ClothesSegment`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `DrawMaskOnImage`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoContextOptions`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageBlend`、`DrawViTPose`、`ImageConcatMulti`、`VHS_LoadVideo`、`LoadImage`、`LayerUtility: ImageMaskScaleAsV2`、`easy int`、`ImageFromBatch`、`ClothesSegment`、`SeCModelLoader`、`SeCVideoSegmentation`、`GrowMask`、`BlockifyMask`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`DrawMaskOnImage`、`CLIPVisionLoader`、`PoseAndFaceDetection`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
