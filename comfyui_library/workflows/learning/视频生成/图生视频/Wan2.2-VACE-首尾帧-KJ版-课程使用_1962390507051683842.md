---
key: 视频生成/图生视频/Wan2.2-VACE-首尾帧-KJ版-课程使用_1962390507051683842.json
name: Wan2.2-VACE-首尾帧-KJ版-课程使用_1962390507051683842.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-VACE-首尾帧-KJ版-课程使用_1962390507051683842.json
hash: 80ece92bba00429a
coverage: 0.782609
learned_at: 2026-10-15 22:31:30
nodes: [MarkdownNote, WanVideoVACEEncode, INTConstant, WanVideoVAELoader, WanVideoBlockSwap, Reroute, WanVideoTorchCompileSettings, Reroute, LoadWanVideoT5TextEncoder, WanVideoEasyCache, WanVideoEnhanceAVideo, WanVideoSLG, StringToFloatList, Note, WanVideoExperimentalArgs, easy int, easy int, WanVideoVACEStartToEndFrame, WanVideoModelLoader, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, VHS_VideoCombine, ImageResizeKJ, Reroute, WanVideoSampler, WanVideoSampler, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelectMulti, LoadImage, WanVideoTextEncode, ImageResizeKJ, Text Multiline, Wan22PromptSelector, easy showAnything, Text Concatenate, WanVideoVACEModelSelect, Reroute, Note, Note, LoadImage, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-VACE-首尾帧-KJ版-课程使用_1962390507051683842.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962390507051683842.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（46 个）：
- `MarkdownNote`
- `WanVideoVACEEncode`
- `INTConstant`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `Reroute`
- `WanVideoTorchCompileSettings`
- `Reroute`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEasyCache`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `StringToFloatList`
- `Note`
- `WanVideoExperimentalArgs`
- `easy int`
- `easy int`
- `WanVideoVACEStartToEndFrame`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `Reroute`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `LoadImage`
- `WanVideoTextEncode`
- `ImageResizeKJ`
- `Text Multiline`
- `Wan22PromptSelector`
- `easy showAnything`
- `Text Concatenate`
- `WanVideoVACEModelSelect`
- `Reroute`
- `Note`
- `Note`
- `LoadImage`
- `MarkdownNote`

## 知识

覆盖率 **78%**（36/46）

**有卡**：`WanVideoVACEEncode`、`INTConstant`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoEasyCache`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`StringToFloatList`、`WanVideoExperimentalArgs`、`easy int`、`WanVideoVACEStartToEndFrame`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`VHS_VideoCombine`、`ImageResizeKJ`、`WanVideoSampler`、`WanVideoLoraSelectMulti`、`LoadImage`、`WanVideoTextEncode`、`Text Multiline`、`Wan22PromptSelector`、`Text Concatenate`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoSetLoRAs
