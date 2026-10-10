---
key: 视频生成/文生视频/万相Wan2.2图生视频2025KJ加速版工作流_1975384215250448386.json
name: 万相Wan2.2图生视频2025KJ加速版工作流_1975384215250448386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/万相Wan2.2图生视频2025KJ加速版工作流_1975384215250448386.json
hash: 7bc2590ee448d319
coverage: 0.8
learned_at: 2026-10-10 23:10:24
nodes: [MarkdownNote, CreateCFGScheduleFloatList, WanVideoModelLoader, WanVideoDecode, VHS_VideoCombine, WanVideoSampler, WanVideoSampler, WanVideoImageToVideoEncode, MarkdownNote, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, ImageResizeKJv2, easy seed, GetImageSizeAndCount, WanVideoTorchCompileSettings, MarkdownNote, Note, MarkdownNote, WanVideoSetBlockSwap, WanVideoSetLoRAs, INTConstant, INTConstant, LoadImage, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoVAELoader]
patterns: []
missing: [easy seed]
discoveries: [次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/万相Wan2.2图生视频2025KJ加速版工作流_1975384215250448386.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/万相Wan2.2图生视频2025KJ加速版工作流_1975384215250448386.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `MarkdownNote`
- `CreateCFGScheduleFloatList`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `MarkdownNote`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `ImageResizeKJv2`
- `easy seed`
- `GetImageSizeAndCount`
- `WanVideoTorchCompileSettings`
- `MarkdownNote`
- `Note`
- `MarkdownNote`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

## 知识

覆盖率 **80%**（24/30）

**有卡**：`CreateCFGScheduleFloatList`、`WanVideoModelLoader`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`INTConstant`、`LoadImage`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoVAELoader`

**缺卡**（1）：`easy seed`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

## 学习发现

- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
