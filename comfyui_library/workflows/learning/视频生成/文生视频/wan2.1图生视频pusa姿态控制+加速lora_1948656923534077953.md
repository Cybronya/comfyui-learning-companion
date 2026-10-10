---
key: 视频生成/文生视频/wan2.1图生视频pusa姿态控制+加速lora_1948656923534077953.json
name: wan2.1图生视频pusa姿态控制+加速lora_1948656923534077953
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.1图生视频pusa姿态控制+加速lora_1948656923534077953.json
hash: 378beb5e03bc137e
coverage: 0.9375
learned_at: 2026-10-10 23:09:32
nodes: [LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoVAELoader, WanVideoModelLoader, WanVideoDecode, WanVideoSampler, ImageResizeKJv2, WanVideoEncode, WanVideoEmptyEmbeds, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoTextEncode, LoadImage, WanVideoLoraSelect, VHS_VideoCombine, Text Multiline]
patterns: []
missing: [Text Multiline]
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
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

覆盖率 **94%**（15/16）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoSampler`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoEmptyEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`LoadImage`、`VHS_VideoCombine`

**缺卡**（1）：`Text Multiline`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoLoraSelect

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
