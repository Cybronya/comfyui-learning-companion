---
key: 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2094127397753933825.json
name: 动作迁移   动作模仿  角色替换  人物替换  wan2.2_2094127397753933825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2094127397753933825.json
hash: 9a93735bf2bd7aac
coverage: 1
learned_at: 2026-10-16 23:42:51
nodes: [LayerUtility: ImageScaleByAspectRatio V2, WanVideoSetLoRAs, WanVideoBlockSwap, VHS_VideoCombine, easy int, SeCModelLoader, ClothesSegment, ImageFromBatch, SeCVideoSegmentation, GrowMask, WanVideoVAELoader, OnnxDetectionModelLoader, BlockifyMask, DrawMaskOnImage, PoseAndFaceDetection, WanVideoClipVisionEncode, VHS_VideoCombine, Evaluate Integers, DrawViTPose, WanVideoContextOptions, WanVideoAnimateEmbeds, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, ImageBlend, WanVideoDecode, VHS_LoadVideo, LoadImage, CLIPVisionLoader, LayerUtility: ImageMaskScaleAsV2, WanVideoTextEncodeCached, ImageConcatMulti, WanVideoSetBlockSwap, ImageConcatMulti, GetImageSizeAndCount, WanVideoSampler, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2094127397753933825.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿  角色替换  人物替换  wan2.2_2094127397753933825.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `easy int`
- `SeCModelLoader`
- `ClothesSegment`
- `ImageFromBatch`
- `SeCVideoSegmentation`
- `GrowMask`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `BlockifyMask`
- `DrawMaskOnImage`
- `PoseAndFaceDetection`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `Evaluate Integers`
- `DrawViTPose`
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `ImageBlend`
- `WanVideoDecode`
- `VHS_LoadVideo`
- `LoadImage`
- `CLIPVisionLoader`
- `LayerUtility: ImageMaskScaleAsV2`
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `WanVideoSetBlockSwap`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`easy int`、`SeCModelLoader`、`ClothesSegment`、`ImageFromBatch`、`SeCVideoSegmentation`、`GrowMask`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`BlockifyMask`、`DrawMaskOnImage`、`PoseAndFaceDetection`、`WanVideoClipVisionEncode`、`Evaluate Integers`、`DrawViTPose`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`ImageBlend`、`WanVideoDecode`、`VHS_LoadVideo`、`LoadImage`、`CLIPVisionLoader`、`LayerUtility: ImageMaskScaleAsV2`、`WanVideoTextEncodeCached`、`ImageConcatMulti`、`WanVideoSetBlockSwap`、`GetImageSizeAndCount`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
