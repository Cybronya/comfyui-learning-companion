---
key: 视频生成/图生视频/Wan2.2图生视频-Kijai优化版_1950147247079079938.json
name: Wan2.2图生视频-Kijai优化版_1950147247079079938.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2图生视频-Kijai优化版_1950147247079079938.json
hash: 89c5ef97bb0eca36
coverage: 0.962963
learned_at: 2026-10-15 22:30:53
nodes: [WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoImageToVideoEncode, WanVideoVAELoader, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, Int, Int, WanVideoModelLoader, WanVideoModelLoader, SimpleMath+, WanVideoSampler, WanVideoSampler, Int, Int, ImageResize+, WanVideoTextEncode, VHS_VideoCombine, LoadImage, MarkdownNote, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频-Kijai优化版_1950147247079079938.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950147247079079938.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（27 个）：
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `Int`
- `Int`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `Int`
- `Int`
- `ImageResize+`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `LoadImage`
- `MarkdownNote`
- `Int`

## 知识

覆盖率 **96%**（26/27）

**有卡**：`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`Int`、`WanVideoModelLoader`、`SimpleMath+`、`WanVideoSampler`、`ImageResize+`、`WanVideoTextEncode`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect
