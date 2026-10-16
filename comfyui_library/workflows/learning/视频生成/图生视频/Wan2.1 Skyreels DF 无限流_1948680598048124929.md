---
key: 视频生成/图生视频/Wan2.1 Skyreels DF 无限流_1948680598048124929.json
name: Wan2.1 Skyreels DF 无限流_1948680598048124929.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1948680598048124929.json
hash: befa741435fce0e8
coverage: 0.471698
learned_at: 2026-10-15 22:30:48
nodes: [GetNode, GetNode, WanVideoEmptyEmbeds, GetNode, WanVideoTeaCache, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoEmptyEmbeds, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, Note, SetNode, GetNode, CLIPTextEncode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, SetNode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoDecode, WanVideoDiffusionForcingSampler, VHS_VideoCombine, SetNode, GetNode, GetImageRangeFromBatch, WanVideoEncode, GetNode, GetNode, WanVideoDiffusionForcingSampler, GetNode, GetNode, WanVideoDecode, SetNode, GetImageRangeFromBatch, GetNode, VHS_VideoCombine, WanVideoEncode, GetNode, GetNode, WanVideoDiffusionForcingSampler, GetNode, GetNode, WanVideoDecode, SetNode, GetImageRangeFromBatch, VHS_VideoCombine, GetNode, GetNode, GetImageSizeAndCount, SimpleMath+, GetNode, GetNode, GetImageSizeAndCount, SimpleMath+, GetImageSizeAndCount, GetNode, SimpleMath+, GetImageRangeFromBatch, GetImageRangeFromBatch, GetImageRangeFromBatch, GetNode, ImageBatchMulti, VHS_VideoCombine, WanVideoTextEmbedBridge, WanVideoTextEmbedBridge, WanVideoTextEmbedBridge, SetNode, SetNode, WanVideoModelLoader, SetNode, WanVideoVAELoader, CLIPLoader, VHS_LoadVideo, SetNode, MarkdownNote, LoadImage, SetNode, ImageResizeKJ, Note, WanVideoExperimentalArgs, SetNode, WanVideoSLG, INTConstant, SetNode, Note, Note Plus (mtb), LoadImageFromUrl, MarkdownNote, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 Skyreels DF 无限流_1948680598048124929.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1948680598048124929.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（106 个）：
- `GetNode`
- `GetNode`
- `WanVideoEmptyEmbeds`
- `GetNode`
- `WanVideoTeaCache`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoEmptyEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `Note`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoDecode`
- `WanVideoDiffusionForcingSampler` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `WanVideoEncode`
- `GetNode`
- `GetNode`
- `WanVideoDiffusionForcingSampler` ★核心
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoEncode`
- `GetNode`
- `GetNode`
- `WanVideoDiffusionForcingSampler` ★核心
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `SimpleMath+`
- `GetImageSizeAndCount`
- `GetNode`
- `SimpleMath+`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageBatchMulti`
- `VHS_VideoCombine`
- `WanVideoTextEmbedBridge`
- `WanVideoTextEmbedBridge`
- `WanVideoTextEmbedBridge`
- `SetNode`
- `SetNode`
- `WanVideoModelLoader`
- `SetNode`
- `WanVideoVAELoader`
- `CLIPLoader`
- `VHS_LoadVideo`
- `SetNode`
- `MarkdownNote`
- `LoadImage`
- `SetNode`
- `ImageResizeKJ`
- `Note`
- `WanVideoExperimentalArgs`
- `SetNode`
- `WanVideoSLG`
- `INTConstant`
- `SetNode`
- `Note`
- `Note Plus (mtb)`
- `LoadImageFromUrl`
- `MarkdownNote`
- `Note`

## 知识

覆盖率 **47%**（50/106）

**有卡**：`WanVideoEmptyEmbeds`、`WanVideoTeaCache`、`CLIPTextEncode`、`WanVideoEncode`、`WanVideoDecode`、`WanVideoDiffusionForcingSampler`、`VHS_VideoCombine`、`GetImageRangeFromBatch`、`GetImageSizeAndCount`、`SimpleMath+`、`ImageBatchMulti`、`WanVideoTextEmbedBridge`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CLIPLoader`、`VHS_LoadVideo`、`LoadImage`、`ImageResizeKJ`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`INTConstant`、`Note Plus (mtb)`、`LoadImageFromUrl`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、WanVideoDiffusionForcingSampler、WanVideoDecode、WanVideoVAELoader、WanVideoEncode、GetImageSizeAndCount
