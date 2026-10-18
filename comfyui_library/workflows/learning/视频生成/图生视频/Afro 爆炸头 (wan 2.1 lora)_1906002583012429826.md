---
key: 视频生成/图生视频/Afro 爆炸头 (wan 2.1 lora)_1906002583012429826.json
name: Afro 爆炸头 (wan 2.1 lora)_1906002583012429826.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Afro 爆炸头 (wan 2.1 lora)_1906002583012429826.json
hash: 31bb9670074b2b7b
coverage: 0.95
learned_at: 2026-10-15 22:29:26
nodes: [VHS_VideoCombine, WanVideoDecode, WanVideoImageClipEncode, WanVideoSLG, WanVideoTeaCache, WanVideoContextOptions, WanVideoEnhanceAVideo, easy int, easy imageSize, WanVideoBlockSwap, Note, ImageScaleToTotalPixels, WanVideoSampler, WanVideoTextEncode, LoadImage, WanVideoModelLoader, WanVideoLoraSelect, LoadWanVideoClipTextEncoder, WanVideoVAELoader, LoadWanVideoT5TextEncoder]
patterns: []
missing: []
---

# 视频生成/图生视频/Afro 爆炸头 (wan 2.1 lora)_1906002583012429826.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1906002583012429826.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（20 个）：
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoSLG`
- `WanVideoTeaCache`
- `WanVideoContextOptions`
- `WanVideoEnhanceAVideo`
- `easy int`
- `easy imageSize`
- `WanVideoBlockSwap`
- `Note`
- `ImageScaleToTotalPixels`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoImageClipEncode`、`WanVideoSLG`、`WanVideoTeaCache`、`WanVideoContextOptions`、`WanVideoEnhanceAVideo`、`easy int`、`easy imageSize`、`WanVideoBlockSwap`、`ImageScaleToTotalPixels`、`WanVideoSampler`、`WanVideoTextEncode`、`LoadImage`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
