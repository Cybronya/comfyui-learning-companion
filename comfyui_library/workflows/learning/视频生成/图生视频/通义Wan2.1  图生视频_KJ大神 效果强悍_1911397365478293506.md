---
key: 视频生成/图生视频/通义Wan2.1  图生视频_KJ大神 效果强悍_1911397365478293506.json
name: 通义Wan2.1  图生视频_KJ大神 效果强悍_1911397365478293506.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/通义Wan2.1  图生视频_KJ大神 效果强悍_1911397365478293506.json
hash: 136571a4df3ff5f5
coverage: 0.894737
learned_at: 2026-10-15 22:29:31
nodes: [Note, Note, WanVideoBlockSwap, WanVideoTorchCompileSettings, CLIPVisionLoader, WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoSampler, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoDecode, LoadWanVideoT5TextEncoder, WanVideoVRAMManagement, WanVideoTextEncode, WanVideoModelLoader, WanVideoVAELoader, VHS_VideoCombine, LoadImage, ImageResizeKJ]
patterns: []
missing: []
---

# 视频生成/图生视频/通义Wan2.1  图生视频_KJ大神 效果强悍_1911397365478293506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1911397365478293506.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（19 个）：
- `Note`
- `Note`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `CLIPVisionLoader`
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `WanVideoSampler` ★核心
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVRAMManagement`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `LoadImage`
- `ImageResizeKJ`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`CLIPVisionLoader`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoVRAMManagement`、`WanVideoTextEncode`、`WanVideoModelLoader`、`WanVideoVAELoader`、`VHS_VideoCombine`、`LoadImage`、`ImageResizeKJ`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
