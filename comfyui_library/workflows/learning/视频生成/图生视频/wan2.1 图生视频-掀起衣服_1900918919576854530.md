---
key: 视频生成/图生视频/wan2.1 图生视频-掀起衣服_1900918919576854530.json
name: wan2.1 图生视频-掀起衣服_1900918919576854530.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1900918919576854530.json
hash: 2463b0b43fb50a3f
coverage: 1
learned_at: 2026-10-15 22:29:23
nodes: [LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoTextEncode, WanVideoVAELoader, WanVideoModelLoader, WanVideoBlockSwap, WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoLoraSelect, TextInput_, WanVideoImageClipEncode, WanVideoDecode, Int, ImageResizeKJ, WanVideoSampler, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1 图生视频-掀起衣服_1900918919576854530.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1900918919576854530.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（17 个）：
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `WanVideoLoraSelect`
- `TextInput_`
- `WanVideoImageClipEncode`
- `WanVideoDecode`
- `Int`
- `ImageResizeKJ`
- `WanVideoSampler` ★核心
- `LoadImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoTextEncode`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoLoraSelect`、`TextInput_`、`WanVideoImageClipEncode`、`WanVideoDecode`、`Int`、`ImageResizeKJ`、`WanVideoSampler`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
