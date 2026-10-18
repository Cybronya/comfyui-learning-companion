---
key: 视频生成/图生视频/WAN2.1 首尾帧 生成视频_1919985178293239809.json
name: WAN2.1 首尾帧 生成视频_1919985178293239809.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.1 首尾帧 生成视频_1919985178293239809.json
hash: ade0c6206d81e297
coverage: 0.5
learned_at: 2026-10-15 22:29:42
nodes: [SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, AddLabel, ImageConcatMulti, SetNode, SetNode, GetNode, SetNode, WanVideoImageToVideoEncode, GetNode, GetNode, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, GetNode, AddLabel, EmptyImage, ImageConcatMulti, GetNode, SetNode, WanVideoSampler, SetNode, LoadImage, SetNode, WanVideoClipVisionEncode, GetNode, VHS_VideoCombine, VHS_VideoCombine, GetImageSizeAndCount, MarkdownNote, MarkdownNote, MarkdownNote, WanVideoBlockSwap, LoadImage, MarkdownNote, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, MarkdownNote, ImageResizeKJ, ImageResizeKJ, WanVideoTextEncode, WanVideoDecode, LoadWanVideoClipTextEncoder]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.1 首尾帧 生成视频_1919985178293239809.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1919985178293239809.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（50 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `AddLabel`
- `ImageConcatMulti`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `GetNode`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `GetNode`
- `AddLabel`
- `EmptyImage`
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `WanVideoSampler` ★核心
- `SetNode`
- `LoadImage`
- `SetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `WanVideoBlockSwap`
- `LoadImage`
- `MarkdownNote`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `MarkdownNote`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `LoadWanVideoClipTextEncoder` ★核心

## 知识

覆盖率 **50%**（25/50）

**有卡**：`AddLabel`、`ImageConcatMulti`、`WanVideoImageToVideoEncode`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`EmptyImage`、`WanVideoSampler`、`LoadImage`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`ImageResizeKJ`、`WanVideoTextEncode`、`WanVideoDecode`、`LoadWanVideoClipTextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
