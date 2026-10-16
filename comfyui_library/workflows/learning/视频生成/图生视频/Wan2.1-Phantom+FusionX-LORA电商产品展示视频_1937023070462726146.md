---
key: 视频生成/图生视频/Wan2.1-Phantom+FusionX-LORA电商产品展示视频_1937023070462726146.json
name: Wan2.1-Phantom+FusionX-LORA电商产品展示视频_1937023070462726146.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1937023070462726146.json
hash: 0c62ee1d5b8018f4
coverage: 1
learned_at: 2026-10-15 22:30:27
nodes: [LoadImage, LoadImage, LoadWanVideoT5TextEncoder, ImageResizeKJv2, ImageResizeKJv2, WanVideoEncode, WanVideoEncode, WanVideoDecode, WanVideoTeaCache, WanVideoSampler, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoModelLoader, DF_Integer, WanVideoPhantomEmbeds, WanVideoTextEncode, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoVAELoader, DF_Integer, DF_Integer, Text Multiline]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1-Phantom+FusionX-LORA电商产品展示视频_1937023070462726146.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1937023070462726146.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（22 个）：
- `LoadImage`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `WanVideoEncode`
- `WanVideoDecode`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `DF_Integer`
- `WanVideoPhantomEmbeds`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `DF_Integer`
- `DF_Integer`
- `Text Multiline`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`LoadImage`、`LoadWanVideoT5TextEncoder`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoDecode`、`WanVideoTeaCache`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`DF_Integer`、`WanVideoPhantomEmbeds`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`Text Multiline`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoLoraSelect
