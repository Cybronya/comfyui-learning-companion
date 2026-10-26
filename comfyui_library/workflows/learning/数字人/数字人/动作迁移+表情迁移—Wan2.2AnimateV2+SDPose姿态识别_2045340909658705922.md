---
key: 数字人/数字人/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2045340909658705922.json
name: 动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2045340909658705922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2045340909658705922.json
hash: b3bd01a57109f2ee
coverage: 0.445946
learned_at: 2026-10-26 02:00:38
nodes: [WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, WanVideoBlockSwap, WanVideoSetBlockSwap, SetNode, GetNode, GetNode, Note, WanVideoVAELoader, WanVideoLoraSelectMulti, GetNode, Note, CLIPVisionLoader, GetNode, ImageConcatMulti, GetNode, SetNode, WanVideoDecode, WanVideoSampler, WanVideoTextEncodeCached, ImageConcatMulti, GetNode, OnnxDetectionModelLoader, GetImageSizeAndCount, GetNode, SetNode, VHS_VideoCombine, SDPoseOODLoader, SetNode, VHS_VideoCombine, YOLOModelLoader, VHS_VideoCombine, ImageResizeKJv2, GetNode, GetNode, GetNode, SDPoseOODProcessor, PoseAndFaceDetection, Note, VHS_VideoCombine, Note, SetNode, SetNode, Int, Int, Note, Text, SetNode, SetNode, VHS_VideoInfo, SetNode, SetNode, GetNode, GetNode, GetNode, Int, Note, Note, GetNode, WanVideoSetLoRAs, SetNode, WanVideoModelLoader, WanVideoBlockSwap, WanVideoAnimateEmbeds, LoadImage, Note, VHS_LoadVideo, PreviewImage]
patterns: []
missing: []
---

# 数字人/数字人/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2045340909658705922.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2045340909658705922.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（74 个）：
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
- `VHS_LoadVideo`
- `PreviewImage`

## 知识

覆盖率 **45%**（33/74）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`OnnxDetectionModelLoader`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`SDPoseOODLoader`、`YOLOModelLoader`、`ImageResizeKJv2`、`SDPoseOODProcessor`、`PoseAndFaceDetection`、`Int`、`Text`、`VHS_VideoInfo`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoAnimateEmbeds`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
