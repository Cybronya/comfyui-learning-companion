---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2084511299454722050.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2084511299454722050
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2084511299454722050.json
hash: 0b93c105002b556b
coverage: 1
learned_at: 2026-10-16 20:35:50
nodes: [WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, ImageConcatMulti, LoadImage, LayerUtility: ImageMaskScaleAsV2, ImageFromBatch, SeCModelLoader, SeCVideoSegmentation, ClothesSegment, GrowMask, BlockifyMask, WanVideoVAELoader, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawMaskOnImage, CLIPVisionLoader, VHS_VideoCombine, WanVideoClipVisionEncode, Evaluate Integers, DrawViTPose, ImageBlend, WanVideoContextOptions, WanVideoLoraSelectMulti, WanVideoAnimateEmbeds, WanVideoTorchCompileSettings, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2084511299454722050.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2084511299454722050.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
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
- `LoadImage`
- `LayerUtility: ImageMaskScaleAsV2`
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
- `VHS_LoadVideo`

## 知识

覆盖率 **100%**（36/36）

**有卡**：`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`ImageConcatMulti`、`LoadImage`、`LayerUtility: ImageMaskScaleAsV2`、`ImageFromBatch`、`SeCModelLoader`、`SeCVideoSegmentation`、`ClothesSegment`、`GrowMask`、`BlockifyMask`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`CLIPVisionLoader`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`Evaluate Integers`、`DrawViTPose`、`ImageBlend`、`WanVideoContextOptions`、`WanVideoLoraSelectMulti`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
