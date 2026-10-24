---
key: 图片生成/图生图/Wan2.2-Animate_去AI感新版动作迁移，美女跳舞（体型自适应 脸部更一致）_1971077076524638209.json
name: Wan2.2-Animate_去AI感新版动作迁移，美女跳舞（体型自适应 脸部更一致）_1971077076524638209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2-Animate_去AI感新版动作迁移，美女跳舞（体型自适应 脸部更一致）_1971077076524638209.json
hash: 27483affdab2ff9e
coverage: 0.534247
learned_at: 2026-10-23 11:28:07
nodes: [WanVideoSampler, WanVideoVAELoader, GetImageSizeAndCount, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, ImageConcatMulti, WanVideoClipVisionEncode, CLIPVisionLoader, ImageConcatMulti, VHS_VideoCombine, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, Int, PoseRetargetPromptHelper, DrawViTPose, GetNode, GetNode, GetNode, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, LoadImage, ImageResizeKJv2, Anything Everywhere, MarkdownNote, WanVideoModelLoader, WanVideoLoraSelectMulti, Note, GetNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GetNode, WanVideoAnimateEmbeds, GetNode, VHS_VideoCombine, GetNode, GetNode, DrawMaskOnImage, BlockifyMask, GrowMask, GetNode, WanVideoDecode, Int, easy showAnything, SetNode, GetNode, SetNode, GetNode, GetNode, DownloadAndLoadSAM2Model, Sam2Segmentation, SetNode, Anything Everywhere, GetNode, OnnxDetectionModelLoader, PoseAndFaceDetection, RHHiddenNodes, WanVideoTextEncodeCached, PrimitiveStringMultiline, Int, VHS_LoadVideo, Int]
patterns: []
missing: []
---

# 图片生成/图生图/Wan2.2-Animate_去AI感新版动作迁移，美女跳舞（体型自适应 脸部更一致）_1971077076524638209.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2-Animate_去AI感新版动作迁移，美女跳舞（体型自适应 脸部更一致）_1971077076524638209.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（73 个）：
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `ImageConcatMulti`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Int`
- `PoseRetargetPromptHelper`
- `DrawViTPose`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `LoadImage`
- `ImageResizeKJv2`
- `Anything Everywhere`
- `MarkdownNote`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `DrawMaskOnImage`
- `BlockifyMask`
- `GrowMask`
- `GetNode`
- `WanVideoDecode`
- `Int`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `SetNode`
- `Anything Everywhere`
- `GetNode`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `RHHiddenNodes`
- `WanVideoTextEncodeCached`
- `PrimitiveStringMultiline`
- `Int`
- `VHS_LoadVideo`
- `Int`

## 知识

覆盖率 **53%**（39/73）

**有卡**：`WanVideoSampler`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`ImageConcatMulti`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`VHS_VideoCombine`、`Int`、`PoseRetargetPromptHelper`、`DrawViTPose`、`LayerUtility: PurgeVRAM V2`、`easy cleanGpuUsed`、`LoadImage`、`ImageResizeKJv2`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoAnimateEmbeds`、`DrawMaskOnImage`、`BlockifyMask`、`GrowMask`、`WanVideoDecode`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`RHHiddenNodes`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
