---
key: 视频生成/图生视频/【遇见AI】wan2.1 Skyreels V3 V2V视频延长_2067528007627141122.json
name: 【遇见AI】wan2.1 Skyreels V3 V2V视频延长_2067528007627141122.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2067528007627141122.json
hash: ec3588f9a1f0d3b8
coverage: 0.947368
learned_at: 2026-10-15 22:40:04
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, VHS_VideoCombine, WanVideoSampler, MarkdownNote, LoadImage, LoadImage, WanVideoLoraSelect, ImageResizeKJv2, GetImageRangeFromBatch, WanVideoEncode, WanVideoEmptyEmbeds, VHS_LoadVideo, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/【遇见AI】wan2.1 Skyreels V3 V2V视频延长_2067528007627141122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067528007627141122.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（19 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `WanVideoLoraSelect`
- `ImageResizeKJv2`
- `GetImageRangeFromBatch`
- `WanVideoEncode`
- `WanVideoEmptyEmbeds`
- `VHS_LoadVideo`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WanVideoModelLoader`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSampler`、`LoadImage`、`WanVideoLoraSelect`、`ImageResizeKJv2`、`GetImageRangeFromBatch`、`WanVideoEncode`、`WanVideoEmptyEmbeds`、`VHS_LoadVideo`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect、WanVideoSetLoRAs
