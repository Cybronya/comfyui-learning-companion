---
key: 视频生成/图生视频/Wan Animate2.2动作迁移V3(Move) 骨骼增强版_2073292954780917762.json
name: Wan Animate2.2动作迁移V3(Move) 骨骼增强版_2073292954780917762.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2073292954780917762.json
hash: fd40077ec56ac3a7
coverage: 0.5
learned_at: 2026-10-15 22:41:03
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, GetNode, GetNode, WanVideoTextEncodeCached, Note, Note, Note, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, SetNode, WanVideoVAELoader, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, GetNode, GetImageSizeAndCount, ImageConcatMulti, WanVideoDecode, WanVideoSampler, WanVideoBlockSwap, GetNode, LayerUtility: PurgeVRAM, GetNode, WanVideoClipVisionEncode, GetNode, SetNode, ImageResizeKJv2, SetNode, WanVideoModelLoader, WanVideoLoraSelectMulti, LoadImage, JWInteger, CR Prompt Text, SetNode, Reroute, easy anythingIndexSwitch, SetNode, SetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, PoseAndFaceDetection, EmptyImage, Primitive integer [Crystools], OnnxDetectionModelLoader, WanVideoAnimateEmbeds, JWInteger, PoseDetectionOneToAllAnimation, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan Animate2.2动作迁移V3(Move) 骨骼增强版_2073292954780917762.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073292954780917762.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（62 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `Note`
- `Note`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `LoadImage`
- `JWInteger`
- `CR Prompt Text`
- `SetNode`
- `Reroute`
- `easy anythingIndexSwitch`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `PoseAndFaceDetection`
- `EmptyImage`
- `Primitive integer [Crystools]`
- `OnnxDetectionModelLoader`
- `WanVideoAnimateEmbeds`
- `JWInteger`
- `PoseDetectionOneToAllAnimation`
- `MarkdownNote`

## 知识

覆盖率 **50%**（31/62）

**有卡**：`ImageConcatMulti`、`WanVideoTextEncodeCached`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoBlockSwap`、`LayerUtility: PurgeVRAM`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`LoadImage`、`JWInteger`、`CR Prompt Text`、`easy anythingIndexSwitch`、`VHS_VideoCombine`、`VHS_LoadVideo`、`PoseAndFaceDetection`、`EmptyImage`、`Primitive integer [Crystools]`、`OnnxDetectionModelLoader`、`WanVideoAnimateEmbeds`、`PoseDetectionOneToAllAnimation`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
