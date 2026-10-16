---
key: 视频生成/图生视频/wan2.2动作迁移动作模仿角色替换人物替换舞蹈复刻工作流_2092843457080549377.json
name: wan2.2动作迁移动作模仿角色替换人物替换舞蹈复刻工作流_2092843457080549377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2动作迁移动作模仿角色替换人物替换舞蹈复刻工作流_2092843457080549377.json
hash: 08ba905867e891c9
coverage: 0.95
learned_at: 2026-10-16 22:59:36
nodes: [WanVideoSetBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoTextEncodeCached, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: ImageMaskScaleAsV2, VHS_VideoInfoLoaded, easy int, SeCModelLoader, ClothesSegment, ImageFromBatch, SeCVideoSegmentation, WanVideoVAELoader, OnnxDetectionModelLoader, BlockifyMask, DrawMaskOnImage, CLIPVisionLoader, PoseAndFaceDetection, WanVideoClipVisionEncode, VHS_VideoCombine, Evaluate Integers, DrawViTPose, WanVideoContextOptions, WanVideoAnimateEmbeds, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, ImageBlend, ImageConcatMulti, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, ImageConcatMulti, VHS_LoadVideo, LoadImage, 孤海注释, 孤海注释, GrowMask]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2动作迁移动作模仿角色替换人物替换舞蹈复刻工作流_2092843457080549377.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/wan2.2动作迁移动作模仿角色替换人物替换舞蹈复刻工作流_2092843457080549377.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `WanVideoSetBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: ImageMaskScaleAsV2`
- `VHS_VideoInfoLoaded`
- `easy int`
- `SeCModelLoader`
- `ClothesSegment`
- `ImageFromBatch`
- `SeCVideoSegmentation`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `BlockifyMask`
- `DrawMaskOnImage`
- `CLIPVisionLoader`
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
- `ImageConcatMulti`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `VHS_LoadVideo`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `GrowMask`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`WanVideoSetBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`LayerUtility: ImageMaskScaleAsV2`、`VHS_VideoInfoLoaded`、`easy int`、`SeCModelLoader`、`ClothesSegment`、`ImageFromBatch`、`SeCVideoSegmentation`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`BlockifyMask`、`DrawMaskOnImage`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`WanVideoClipVisionEncode`、`Evaluate Integers`、`DrawViTPose`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`ImageBlend`、`ImageConcatMulti`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_LoadVideo`、`LoadImage`、`GrowMask`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
