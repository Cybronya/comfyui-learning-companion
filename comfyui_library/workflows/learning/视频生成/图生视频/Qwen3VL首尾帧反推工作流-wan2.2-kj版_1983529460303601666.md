---
key: 视频生成/图生视频/Qwen3VL首尾帧反推工作流-wan2.2-kj版_1983529460303601666.json
name: Qwen3VL首尾帧反推工作流-wan2.2-kj版_1983529460303601666.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1983529460303601666.json
hash: 38572a8a9dd9ed75
coverage: 0.947368
learned_at: 2026-10-15 22:32:45
nodes: [JWInteger, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoSampler, WanVideoSampler, JWInteger, INTConstant, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, JWInteger, JWInteger, MarkdownNote, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, easy cleanGpuUsed, MultiplePathsInput, WanVideoTextEncode, ImageResize+, ImageResize+, WanVideoLoraSelect, WanVideoLoraSelect, easy showAnything, Qwen3_VQA, WanVideoDecode, VHS_VideoCombine, ImageLoader, ImageLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/Qwen3VL首尾帧反推工作流-wan2.2-kj版_1983529460303601666.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983529460303601666.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（38 个）：
- `JWInteger`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `JWInteger`
- `INTConstant`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `JWInteger`
- `JWInteger`
- `MarkdownNote`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `easy cleanGpuUsed`
- `MultiplePathsInput`
- `WanVideoTextEncode`
- `ImageResize+`
- `ImageResize+`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `easy showAnything`
- `Qwen3_VQA`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `ImageLoader`
- `ImageLoader`

## 知识

覆盖率 **95%**（36/38）

**有卡**：`JWInteger`、`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`INTConstant`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`easy cleanGpuUsed`、`MultiplePathsInput`、`WanVideoTextEncode`、`ImageResize+`、`Qwen3_VQA`、`WanVideoDecode`、`VHS_VideoCombine`、`ImageLoader`

**用到的条目**：WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
