---
key: 视频生成/图生视频/通宵全力搭建！最新ai视频生成王炸！！万相2.1 图生视频工作流_1895025130055794689.json
name: 通宵全力搭建！最新ai视频生成王炸！！万相2.1 图生视频工作流_1895025130055794689.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1895025130055794689.json
hash: 102ea6b19e623fef
coverage: 0.846154
learned_at: 2026-10-15 22:29:17
nodes: [WanVideoBlockSwap, WanVideoDecode, WanVideoTextEncode, Note, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoVAELoader, LoadImage, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, VHS_VideoCombine, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/通宵全力搭建！最新ai视频生成王炸！！万相2.1 图生视频工作流_1895025130055794689.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1895025130055794689.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（13 个）：
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `Note`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `LoadImage`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `Note`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`LoadImage`、`WanVideoImageClipEncode`、`WanVideoModelLoader`、`WanVideoSampler`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
