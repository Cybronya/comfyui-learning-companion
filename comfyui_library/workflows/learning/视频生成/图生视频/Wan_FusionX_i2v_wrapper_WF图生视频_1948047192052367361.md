---
key: 视频生成/图生视频/Wan_FusionX_i2v_wrapper_WF图生视频_1948047192052367361.json
name: Wan_FusionX_i2v_wrapper_WF图生视频_1948047192052367361.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan_FusionX_i2v_wrapper_WF图生视频_1948047192052367361.json
hash: b5e4ba9ccb83633d
coverage: 0.888889
learned_at: 2026-10-15 22:30:47
nodes: [WanVideoBlockSwap, MarkdownNote, MarkdownNote, WanVideoTextEncode, WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, WanVideoVAELoader, CLIPVisionLoader, LoadImage, VHS_VideoCombine, WanVideoSampler, WanVideoModelLoader, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, WanVideoDecode, ImageResizeKJv2, ImageResizeKJv2, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan_FusionX_i2v_wrapper_WF图生视频_1948047192052367361.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1948047192052367361.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（18 个）：
- `WanVideoBlockSwap`
- `MarkdownNote`
- `MarkdownNote`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoadImage`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`CLIPVisionLoader`、`LoadImage`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`ImageResizeKJv2`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
