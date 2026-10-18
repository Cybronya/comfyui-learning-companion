---
key: 视频生成/图生视频/WAN2.1街头霸王光波工作流_1894640699545944065.json
name: WAN2.1街头霸王光波工作流_1894640699545944065.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.1街头霸王光波工作流_1894640699545944065.json
hash: 9cc704a96d932bbd
coverage: 0.933333
learned_at: 2026-10-15 22:29:16
nodes: [WanVideoTeaCache, WanVideoSampler, VHS_VideoCombine, WanVideoLoraSelect, WanVideoModelLoader, WanVideoEnhanceAVideo, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoImageClipEncode, ImageResizeKJ, LoadImage, WanVideoTextEncode, WanVideoDecode, PreviewImage]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.1街头霸王光波工作流_1894640699545944065.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1894640699545944065.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（15 个）：
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoEnhanceAVideo`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoImageClipEncode`
- `ImageResizeKJ`
- `LoadImage`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `PreviewImage`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`WanVideoTeaCache`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoEnhanceAVideo`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoImageClipEncode`、`ImageResizeKJ`、`LoadImage`、`WanVideoTextEncode`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
