---
key: 视频生成/图生视频/wan2.2 lora_1996855253331058690.json
name: wan2.2 lora_1996855253331058690.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 lora_1996855253331058690.json
hash: 1aa9b7a35a4d1d17
coverage: 1
learned_at: 2026-10-15 22:33:28
nodes: [LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoDecode, MathExpression|pysssss, Primitive integer [Crystools], WanVideoImageToVideoEncode, WanVideoVAELoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSampler, LoadAudio, WanVideoLoraSelect, WanVideoSampler, WanVideoModelLoader, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTextEncode, WanVideoLoraSelect, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 lora_1996855253331058690.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1996855253331058690.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `WanVideoImageToVideoEncode`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `LoadAudio`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `LoadImage`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoDecode`、`MathExpression|pysssss`、`Primitive integer [Crystools]`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSampler`、`LoadAudio`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTextEncode`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect
