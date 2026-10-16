---
key: 视频生成/图生视频/【Wan2.1系列】图生视频工作流_1914283396808306690.json
name: 【Wan2.1系列】图生视频工作流_1914283396808306690.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1914283396808306690.json
hash: 9c915a0c67f485c0
coverage: 0.9375
learned_at: 2026-10-15 22:29:36
nodes: [WanVideoDecode, VHS_VideoCombine, WanVideoSampler, LoadWanVideoT5TextEncoder, WanVideoImageToVideoEncode, WanVideoBlockSwap, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoModelLoader, WanVideoVAELoader, ImageResizeKJ, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoTextEncode, LoadImage, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/【Wan2.1系列】图生视频工作流_1914283396808306690.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1914283396808306690.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（16 个）：
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoImageToVideoEncode`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `ImageResizeKJ`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `LoadImage`
- `MarkdownNote`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoModelLoader`、`WanVideoVAELoader`、`ImageResizeKJ`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoTextEncode`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
