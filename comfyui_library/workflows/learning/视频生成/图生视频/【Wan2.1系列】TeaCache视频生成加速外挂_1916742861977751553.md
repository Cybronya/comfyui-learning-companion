---
key: 视频生成/图生视频/【Wan2.1系列】TeaCache视频生成加速外挂_1916742861977751553.json
name: 【Wan2.1系列】TeaCache视频生成加速外挂_1916742861977751553.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1916742861977751553.json
hash: 9fce1a1956d807cb
coverage: 0.95122
learned_at: 2026-10-15 22:29:39
nodes: [LoadWanVideoT5TextEncoder, WanVideoDecode, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoVAELoader, WanVideoTeaCache, WanVideoModelLoader, LoadImage, ImageResizeKJ, WanVideoImageToVideoEncode, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, WanVideoSampler, WanVideoDecode, LoadImage, ImageResizeKJ, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, WanVideoSampler, WanVideoDecode, ImageResizeKJ, LoadImage, WanVideoTeaCache, WanVideoTeaCache, WanVideoTextEncode, WanVideoSampler, Fast Groups Bypasser (rgthree), VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/【Wan2.1系列】TeaCache视频生成加速外挂_1916742861977751553.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1916742861977751553.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（41 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoTeaCache`
- `WanVideoModelLoader`
- `LoadImage`
- `ImageResizeKJ`
- `WanVideoImageToVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `LoadImage`
- `ImageResizeKJ`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageResizeKJ`
- `LoadImage`
- `WanVideoTeaCache`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MarkdownNote`

## 知识

覆盖率 **95%**（39/41）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoTeaCache`、`WanVideoModelLoader`、`LoadImage`、`ImageResizeKJ`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`WanVideoSampler`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
