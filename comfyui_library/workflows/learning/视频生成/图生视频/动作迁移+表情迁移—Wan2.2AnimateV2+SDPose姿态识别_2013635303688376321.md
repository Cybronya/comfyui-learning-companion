---
key: 视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2013635303688376321.json
name: 动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2013635303688376321.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2013635303688376321.json
hash: 5280e96449b8b66b
coverage: 0.447368
learned_at: 2026-10-15 22:34:32
nodes: [WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, WanVideoBlockSwap, WanVideoSetBlockSwap, PreviewImage, SetNode, GetNode, GetNode, Note, WanVideoVAELoader, WanVideoLoraSelectMulti, GetNode, Note, CLIPVisionLoader, GetNode, ImageConcatMulti, GetNode, SetNode, WanVideoDecode, WanVideoSampler, WanVideoTextEncodeCached, ImageConcatMulti, GetNode, OnnxDetectionModelLoader, GetImageSizeAndCount, GetNode, SetNode, VHS_VideoCombine, SDPoseOODLoader, SetNode, VHS_VideoCombine, YOLOModelLoader, VHS_VideoCombine, ImageResizeKJv2, GetNode, GetNode, GetNode, SDPoseOODProcessor, PoseAndFaceDetection, Note, VHS_VideoCombine, Note, SetNode, SetNode, Int, Int, Note, Text, SetNode, SetNode, VHS_VideoInfo, SetNode, SetNode, GetNode, GetNode, GetNode, Int, Note, Note, GetNode, WanVideoSetLoRAs, SetNode, WanVideoModelLoader, WanVideoBlockSwap, WanVideoAnimateEmbeds, LoadImage, Note, MarkdownNote, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2013635303688376321.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2013635303688376321.json`

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
- `LoadImage`
- `Note`
- `MarkdownNote`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **45%**（34/76）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`OnnxDetectionModelLoader`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`SDPoseOODLoader`、`YOLOModelLoader`、`ImageResizeKJv2`、`SDPoseOODProcessor`、`PoseAndFaceDetection`、`Int`、`Text`、`VHS_VideoInfo`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoAnimateEmbeds`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
