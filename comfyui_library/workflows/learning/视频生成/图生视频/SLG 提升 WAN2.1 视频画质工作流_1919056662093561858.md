---
key: 视频生成/图生视频/SLG 提升 WAN2.1 视频画质工作流_1919056662093561858.json
name: SLG 提升 WAN2.1 视频画质工作流_1919056662093561858.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1919056662093561858.json
hash: e0f3303fbf2864d8
coverage: 0.944444
learned_at: 2026-10-15 22:29:41
nodes: [LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoImageToVideoEncode, CLIPVisionLoader, WanVideoEnhanceAVideo, WanVideoDecode, WanVideoClipVisionEncode, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoVAELoader, WanVideoTeaCache, Reroute, WanVideoSampler, WanVideoSLG, ImageResizeKJ, LoadImage, WanVideoTextEncode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/SLG 提升 WAN2.1 视频画质工作流_1919056662093561858.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1919056662093561858.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（18 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `CLIPVisionLoader`
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `WanVideoClipVisionEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoTeaCache`
- `Reroute`
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `ImageResizeKJ`
- `LoadImage`
- `WanVideoTextEncode`
- `VHS_VideoCombine`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`CLIPVisionLoader`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoTeaCache`、`WanVideoSampler`、`WanVideoSLG`、`ImageResizeKJ`、`LoadImage`、`WanVideoTextEncode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
