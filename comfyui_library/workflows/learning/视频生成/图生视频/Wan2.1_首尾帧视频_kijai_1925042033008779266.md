---
key: 视频生成/图生视频/Wan2.1_首尾帧视频_kijai_1925042033008779266.json
name: Wan2.1_首尾帧视频_kijai_1925042033008779266.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1925042033008779266.json
hash: 04da21ac56fec32c
coverage: 0.76
learned_at: 2026-10-15 22:29:51
nodes: [Note, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, Note, WanVideoBlockSwap, WanVideoClipVisionEncode, ImageResize+, PreviewImage, WanVideoModelLoader, MarkdownNote, WanVideoVAELoader, ImageResize+, LoadImage, LoadImage, LoadImage, LoadImage, WanVideoTextEncode, WanVideoDecode, WanVideoTeaCache, VHS_VideoCombine, PreviewImage, Note, WanVideoSLG, WanVideoSampler, WanVideoImageToVideoEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1_首尾帧视频_kijai_1925042033008779266.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1925042033008779266.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（25 个）：
- `Note`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `Note`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `ImageResize+`
- `PreviewImage`
- `WanVideoModelLoader`
- `MarkdownNote`
- `WanVideoVAELoader`
- `ImageResize+`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `WanVideoTeaCache`
- `VHS_VideoCombine`
- `PreviewImage`
- `Note`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`

## 知识

覆盖率 **76%**（19/25）

**有卡**：`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`ImageResize+`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadImage`、`WanVideoTextEncode`、`WanVideoDecode`、`WanVideoTeaCache`、`VHS_VideoCombine`、`WanVideoSLG`、`WanVideoSampler`、`WanVideoImageToVideoEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
