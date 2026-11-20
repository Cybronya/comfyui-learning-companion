---
key: 平台全量/Wan2.1 视频转视频（视频风格、动作模仿）工作流_1991468942290010114.json
name: Wan2.1 视频转视频（视频风格、动作模仿）工作流_1991468942290010114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1 视频转视频（视频风格、动作模仿）工作流_1991468942290010114.json
hash: e023317f69b1dc74
coverage: 1
learned_at: 2026-11-14 01:04:30
nodes: [WanVideoModelLoader, WanVideoVAELoader, WanVideoTextEncode, LoadWanVideoT5TextEncoder, VHS_LoadVideo, ImageResizeKJ, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoEncode, WanVideoDecode, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/Wan2.1 视频转视频（视频风格、动作模仿）工作流_1991468942290010114.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1 视频转视频（视频风格、动作模仿）工作流_1991468942290010114.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（13 个）：
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `ImageResizeKJ`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `WanVideoDecode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`VHS_LoadVideo`、`ImageResizeKJ`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`WanVideoEncode`、`WanVideoDecode`、`ImageConcatMulti`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、ImageResizeKJ、ImageConcatMulti
