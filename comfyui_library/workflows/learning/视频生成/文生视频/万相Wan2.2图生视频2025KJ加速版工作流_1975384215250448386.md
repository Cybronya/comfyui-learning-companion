---
key: 视频生成/文生视频/万相Wan2.2图生视频2025KJ加速版工作流_1975384215250448386.json
name: 万相Wan2.2图生视频2025KJ加速版工作流_1975384215250448386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/万相Wan2.2图生视频2025KJ加速版工作流_1975384215250448386.json
hash: 7bc2590ee448d319
coverage: 0.833333
learned_at: 2026-10-15 22:47:45
nodes: [MarkdownNote, CreateCFGScheduleFloatList, WanVideoModelLoader, WanVideoDecode, VHS_VideoCombine, WanVideoSampler, WanVideoSampler, WanVideoImageToVideoEncode, MarkdownNote, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, ImageResizeKJv2, easy seed, GetImageSizeAndCount, WanVideoTorchCompileSettings, MarkdownNote, Note, MarkdownNote, WanVideoSetBlockSwap, WanVideoSetLoRAs, INTConstant, INTConstant, LoadImage, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoVAELoader]
patterns: []
missing: []
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

覆盖率 **83%**（25/30）

**有卡**：`CreateCFGScheduleFloatList`、`WanVideoModelLoader`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`easy seed`、`GetImageSizeAndCount`、`WanVideoTorchCompileSettings`、`INTConstant`、`LoadImage`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
