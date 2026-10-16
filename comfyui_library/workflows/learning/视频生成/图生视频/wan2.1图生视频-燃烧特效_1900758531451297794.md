---
key: 视频生成/图生视频/wan2.1图生视频-燃烧特效_1900758531451297794.json
name: wan2.1图生视频-燃烧特效_1900758531451297794.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1900758531451297794.json
hash: 2ef33495308bc72a
coverage: 1
learned_at: 2026-10-15 22:29:23
nodes: [LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoTextEncode, WanVideoImageClipEncode, WanVideoVAELoader, WanVideoModelLoader, WanVideoBlockSwap, WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoDecode, WanVideoLoraSelect, TextInput_, Int, WanVideoSampler, LoadImage, ImageResizeKJ, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1图生视频-燃烧特效_1900758531451297794.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1900758531451297794.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（17 个）：
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoTextEncode`
- `WanVideoImageClipEncode`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `TextInput_`
- `Int`
- `WanVideoSampler` ★核心
- `LoadImage`
- `ImageResizeKJ`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoTextEncode`、`WanVideoImageClipEncode`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`WanVideoLoraSelect`、`TextInput_`、`Int`、`WanVideoSampler`、`LoadImage`、`ImageResizeKJ`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
