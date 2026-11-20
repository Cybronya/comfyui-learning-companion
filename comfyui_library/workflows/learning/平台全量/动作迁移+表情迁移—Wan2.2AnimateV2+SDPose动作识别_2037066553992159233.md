---
key: 平台全量/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose动作识别_2037066553992159233.json
name: 动作迁移+表情迁移—Wan2.2AnimateV2+SDPose动作识别_2037066553992159233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose动作识别_2037066553992159233.json
hash: 636332948acae64c
coverage: 0.447368
learned_at: 2026-11-14 01:45:10
nodes: [WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, WanVideoBlockSwap, WanVideoSetBlockSwap, PreviewImage, SetNode, GetNode, GetNode, Note, WanVideoVAELoader, WanVideoLoraSelectMulti, GetNode, Note, CLIPVisionLoader, GetNode, ImageConcatMulti, GetNode, SetNode, WanVideoDecode, WanVideoSampler, WanVideoTextEncodeCached, ImageConcatMulti, GetNode, OnnxDetectionModelLoader, GetImageSizeAndCount, GetNode, SetNode, VHS_VideoCombine, SDPoseOODLoader, SetNode, VHS_VideoCombine, YOLOModelLoader, VHS_VideoCombine, ImageResizeKJv2, GetNode, GetNode, GetNode, SDPoseOODProcessor, PoseAndFaceDetection, Note, VHS_VideoCombine, Note, SetNode, SetNode, Int, Int, Note, Text, SetNode, SetNode, VHS_VideoInfo, SetNode, SetNode, GetNode, GetNode, GetNode, Int, Note, Note, GetNode, WanVideoSetLoRAs, SetNode, WanVideoModelLoader, WanVideoBlockSwap, WanVideoAnimateEmbeds, Note, MarkdownNote, VHS_LoadVideo, LoadImage, LoadImage]
patterns: []
missing: []
---

# 平台全量/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose动作识别_2037066553992159233.json

> 来源文件 `comfyui_library/workflows/平台全量/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose动作识别_2037066553992159233.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（76 个）：
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `Note`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `Note`
- `CLIPVisionLoader`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `GetNode`
- `OnnxDetectionModelLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `SDPoseOODLoader`
- `SetNode`
- `VHS_VideoCombine`
- `YOLOModelLoader`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `SDPoseOODProcessor`
- `PoseAndFaceDetection`
- `Note`
- `VHS_VideoCombine`
- `Note`
- `SetNode`
- `SetNode`
- `Int`
- `Int`
- `Note`
- `Text`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `Note`
- `Note`
- `GetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoAnimateEmbeds`
- `Note`
- `MarkdownNote`
- `VHS_LoadVideo`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **45%**（34/76）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`OnnxDetectionModelLoader`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`SDPoseOODLoader`、`YOLOModelLoader`、`ImageResizeKJv2`、`SDPoseOODProcessor`、`PoseAndFaceDetection`、`Int`、`Text`、`VHS_VideoInfo`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
