---
key: 平台全量/视频-动作声音迁移Animate Wan2.2_1976300726697725954.json
name: 视频-动作声音迁移Animate Wan2.2_1976300726697725954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-动作声音迁移Animate Wan2.2_1976300726697725954.json
hash: e88fdd827614ebba
coverage: 0.666667
learned_at: 2026-11-14 02:34:05
nodes: [GetNode, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoTextEncodeCached, PoseRetargetPromptHelper, WanVideoLoraSelectMulti, WanVideoModelLoader, PoseAndFaceDetection, OnnxDetectionModelLoader, DrawViTPose, easy showAnything, SetNode, easy showAnything, SetNode, WanVideoSetLoRAs, JWInteger, JWInteger, VHS_VideoCombine, SetNode, GetNode, WanVideoClipVisionEncode, WanVideoDecode, GetNode, GetNode, VHS_LoadVideo, VHS_LoadVideo, JWInteger, CR Prompt Text, GetImageSizeAndCount, WanVideoVAELoader, CLIPVisionLoader, WanVideoSampler, GetNode, VHS_VideoCombine, Reroute, ImageResizeKJv2, Reroute, ImageResizeKJv2, SetNode, Note, LoadImage]
patterns: []
missing: []
---

# 平台全量/视频-动作声音迁移Animate Wan2.2_1976300726697725954.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-动作声音迁移Animate Wan2.2_1976300726697725954.json`

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

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
