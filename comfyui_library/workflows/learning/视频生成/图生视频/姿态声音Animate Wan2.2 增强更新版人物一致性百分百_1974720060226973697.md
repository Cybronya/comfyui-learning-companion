---
key: 视频生成/图生视频/姿态声音Animate Wan2.2 增强更新版人物一致性百分百_1974720060226973697.json
name: 姿态声音Animate Wan2.2 增强更新版人物一致性百分百_1974720060226973697.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/姿态声音Animate Wan2.2 增强更新版人物一致性百分百_1974720060226973697.json
hash: e1408fff3d97e292
coverage: 0.666667
learned_at: 2026-10-15 22:32:06
nodes: [GetNode, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoTextEncodeCached, PoseRetargetPromptHelper, WanVideoLoraSelectMulti, WanVideoModelLoader, PoseAndFaceDetection, OnnxDetectionModelLoader, DrawViTPose, easy showAnything, SetNode, easy showAnything, SetNode, WanVideoSetLoRAs, JWInteger, JWInteger, VHS_VideoCombine, SetNode, GetNode, WanVideoClipVisionEncode, WanVideoDecode, GetNode, GetNode, VHS_LoadVideo, VHS_LoadVideo, JWInteger, CR Prompt Text, GetImageSizeAndCount, WanVideoVAELoader, CLIPVisionLoader, WanVideoSampler, GetNode, VHS_VideoCombine, Reroute, ImageResizeKJv2, Reroute, ImageResizeKJv2, SetNode, Note, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/姿态声音Animate Wan2.2 增强更新版人物一致性百分百_1974720060226973697.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1974720060226973697.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（42 个）：
- `GetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `PoseRetargetPromptHelper`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `DrawViTPose`
- `easy showAnything`
- `SetNode`
- `easy showAnything`
- `SetNode`
- `WanVideoSetLoRAs`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `JWInteger`
- `CR Prompt Text`
- `GetImageSizeAndCount`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoSampler` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `Reroute`
- `ImageResizeKJv2`
- `Reroute`
- `ImageResizeKJv2`
- `SetNode`
- `Note`
- `LoadImage`

## 知识

覆盖率 **67%**（28/42）

**有卡**：`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`PoseRetargetPromptHelper`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`DrawViTPose`、`WanVideoSetLoRAs`、`JWInteger`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`VHS_LoadVideo`、`CR Prompt Text`、`GetImageSizeAndCount`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoSampler`、`ImageResizeKJv2`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
