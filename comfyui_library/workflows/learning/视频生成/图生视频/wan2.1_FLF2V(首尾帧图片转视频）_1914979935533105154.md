---
key: 视频生成/图生视频/wan2.1_FLF2V(首尾帧图片转视频）_1914979935533105154.json
name: wan2.1_FLF2V(首尾帧图片转视频）_1914979935533105154.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1_FLF2V(首尾帧图片转视频）_1914979935533105154.json
hash: 2ee297b71dda9c71
coverage: 0.851852
learned_at: 2026-10-15 22:29:37
nodes: [WanVideoSLG, ImageResize+, WanVideoTeaCache, WanVideoSampler, GetNode, GetNode, AddLabel, AddLabel, EmptyImage, ImageConcatMulti, ImageConcatMulti, GetImageSizeAndCount, WanVideoDecode, LoadImage, LoadImage, WanVideoVAELoader, WanVideoClipVisionEncode, WanVideoTextEncode, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoBlockSwap, VHS_VideoCombine, SetNode, SetNode, WanVideoImageToVideoEncode, ImageResize+]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1_FLF2V(首尾帧图片转视频）_1914979935533105154.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1914979935533105154.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（27 个）：
- `WanVideoSLG`
- `ImageResize+`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `AddLabel`
- `AddLabel`
- `EmptyImage`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `LoadImage`
- `LoadImage`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncode`
- `LoadWanVideoClipTextEncoder` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `WanVideoImageToVideoEncode`
- `ImageResize+`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`WanVideoSLG`、`ImageResize+`、`WanVideoTeaCache`、`WanVideoSampler`、`AddLabel`、`EmptyImage`、`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoDecode`、`LoadImage`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoTextEncode`、`LoadWanVideoClipTextEncoder`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
