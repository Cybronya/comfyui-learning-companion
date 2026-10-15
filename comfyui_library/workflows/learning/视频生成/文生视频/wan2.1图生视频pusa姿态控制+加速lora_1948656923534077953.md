---
key: 视频生成/文生视频/wan2.1图生视频pusa姿态控制+加速lora_1948656923534077953.json
name: wan2.1图生视频pusa姿态控制+加速lora_1948656923534077953
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.1图生视频pusa姿态控制+加速lora_1948656923534077953.json
hash: 378beb5e03bc137e
coverage: 1
learned_at: 2026-10-15 22:47:34
nodes: [LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoVAELoader, WanVideoModelLoader, WanVideoDecode, WanVideoSampler, ImageResizeKJv2, WanVideoEncode, WanVideoEmptyEmbeds, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoTextEncode, LoadImage, WanVideoLoraSelect, VHS_VideoCombine, Text Multiline]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.1图生视频pusa姿态控制+加速lora_1948656923534077953.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.1图生视频pusa姿态控制+加速lora_1948656923534077953.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（16 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `WanVideoEncode`
- `WanVideoEmptyEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `LoadImage`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `Text Multiline`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoSampler`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoEmptyEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`LoadImage`、`VHS_VideoCombine`、`Text Multiline`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoLoraSelect
