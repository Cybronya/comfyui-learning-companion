---
key: 视频生成/图生视频/Wan2.1-KJ首尾帧图生视频_1911321308582608897.json
name: Wan2.1-KJ首尾帧图生视频_1911321308582608897.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1-KJ首尾帧图生视频_1911321308582608897.json
hash: 06cc3ded0d5f8a3c
coverage: 0.657895
learned_at: 2026-10-15 22:29:31
nodes: [ImageResize+, LoadImage, ImageResize+, SetNode, SetNode, WanVideoClipVisionEncode, WanVideoBlockSwap, WanVideoVRAMManagement, LoadWanVideoT5TextEncoder, Note, WanVideoSLG, WanVideoTeaCache, WanVideoExperimentalArgs, WanVideoSampler, GetImageSizeAndCount, Note, Note, VHS_VideoCombine, WanVideoImageToVideoEncode, LoadImage, WanVideoTextEncode, LoadWanVideoClipTextEncoder, WanVideoModelLoader, AddLabel, AddLabel, GetNode, GetNode, PreviewImage, PreviewImage, PreviewImage, PreviewImage, WanVideoDecode, ImageConcatMulti, PreviewImage, Note, WanVideoVAELoader, EmptyImage, ImageConcatMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1-KJ首尾帧图生视频_1911321308582608897.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1911321308582608897.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（38 个）：
- `ImageResize+`
- `LoadImage`
- `ImageResize+`
- `SetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `WanVideoBlockSwap`
- `WanVideoVRAMManagement`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `WanVideoSLG`
- `WanVideoTeaCache`
- `WanVideoExperimentalArgs`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `WanVideoTextEncode`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoModelLoader`
- `AddLabel`
- `AddLabel`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `WanVideoDecode`
- `ImageConcatMulti`
- `PreviewImage`
- `Note`
- `WanVideoVAELoader`
- `EmptyImage`
- `ImageConcatMulti`

## 知识

覆盖率 **66%**（25/38）

**有卡**：`ImageResize+`、`LoadImage`、`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`WanVideoVRAMManagement`、`LoadWanVideoT5TextEncoder`、`WanVideoSLG`、`WanVideoTeaCache`、`WanVideoExperimentalArgs`、`WanVideoSampler`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`LoadWanVideoClipTextEncoder`、`WanVideoModelLoader`、`AddLabel`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoVAELoader`、`EmptyImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
