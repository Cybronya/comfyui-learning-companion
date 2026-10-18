---
key: 视频生成/图生视频/动作迁移   动作模仿 角色替换  人物替换  wan2.2_2080943819062861825.json
name: 动作迁移   动作模仿 角色替换  人物替换  wan2.2_2080943819062861825.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移   动作模仿 角色替换  人物替换  wan2.2_2080943819062861825.json
hash: c693107711a980ee
coverage: 1
learned_at: 2026-10-15 22:42:18
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, ImageConcatMulti, WanVideoDecode, WanVideoContextOptions, CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoAnimateEmbeds, Evaluate Integers, WanVideoClipVisionEncode, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoBlockSwap, WanVideoTextEncodeCached, VHS_VideoCombine, ImageBlend, DrawViTPose, ImageConcatMulti, VHS_VideoCombine, LoadImage, VHS_LoadVideo, LayerUtility: ImageMaskScaleAsV2, SeCModelLoader, VHS_VideoInfoLoaded, ImageFromBatch, SeCVideoSegmentation, WanVideoVAELoader, OnnxDetectionModelLoader, PoseAndFaceDetection, GrowMask, BlockifyMask, DrawMaskOnImage, VHS_VideoCombine, ClothesSegment]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移   动作模仿 角色替换  人物替换  wan2.2_2080943819062861825.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2080943819062861825.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `ImageConcatMulti`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `ImageBlend`
- `DrawViTPose`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`
- `LayerUtility: ImageMaskScaleAsV2`
- `SeCModelLoader`
- `VHS_VideoInfoLoaded`
- `ImageFromBatch`
- `SeCVideoSegmentation`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `ClothesSegment`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoContextOptions`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`ImageBlend`、`DrawViTPose`、`LoadImage`、`VHS_LoadVideo`、`LayerUtility: ImageMaskScaleAsV2`、`SeCModelLoader`、`VHS_VideoInfoLoaded`、`ImageFromBatch`、`SeCVideoSegmentation`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`ClothesSegment`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
