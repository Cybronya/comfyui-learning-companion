---
key: 视频生成/图生视频/Wan2.1-Phantom+FusionX-LORA电商版_1935608698565742593.json
name: Wan2.1-Phantom+FusionX-LORA电商版_1935608698565742593.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1-Phantom+FusionX-LORA电商版_1935608698565742593.json
hash: e9bf052589cec525
coverage: 1
learned_at: 2026-10-15 22:30:23
nodes: [LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoEncode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, Text Multiline, WanVideoDecode, WanVideoTeaCache, WanVideoVAELoader, VHS_VideoCombine, WanVideoTextEncode, LoadImage, WanVideoPhantomEmbeds, DF_Integer, LoadImage, ImageResizeKJv2, ImageResizeKJv2, DF_Integer, DF_Integer, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1-Phantom+FusionX-LORA电商版_1935608698565742593.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1935608698565742593.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（21 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoEncode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `Text Multiline`
- `WanVideoDecode`
- `WanVideoTeaCache`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `LoadImage`
- `WanVideoPhantomEmbeds`
- `DF_Integer`
- `LoadImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `DF_Integer`
- `DF_Integer`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **100%**（21/21）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoEncode`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`Text Multiline`、`WanVideoDecode`、`WanVideoTeaCache`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoTextEncode`、`LoadImage`、`WanVideoPhantomEmbeds`、`DF_Integer`、`ImageResizeKJv2`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoLoraSelect
