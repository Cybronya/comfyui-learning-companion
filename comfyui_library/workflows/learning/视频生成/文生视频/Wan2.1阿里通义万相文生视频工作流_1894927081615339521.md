---
key: 视频生成/文生视频/Wan2.1阿里通义万相文生视频工作流_1894927081615339521.json
name: Wan2.1阿里通义万相文生视频工作流_1894927081615339521.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1阿里通义万相文生视频工作流_1894927081615339521.json
hash: 3a3ff0d5483c496d
coverage: 1
learned_at: 2026-10-15 22:43:20
nodes: [WanVideoSampler, WanVideoDecode, WanVideoVAELoader, WanVideoEmptyEmbeds, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], WanVideoBlockSwap, WanVideoModelLoader, VHS_VideoCombine, Primitive string [Crystools], LoadWanVideoT5TextEncoder, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1阿里通义万相文生视频工作流_1894927081615339521.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1894927081615339521.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（13 个）：
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoEmptyEmbeds`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `Primitive string [Crystools]`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`WanVideoSampler`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoEmptyEmbeds`、`Primitive integer [Crystools]`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`VHS_VideoCombine`、`Primitive string [Crystools]`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、VHS_VideoCombine、WanVideoBlockSwap、WanVideoModelLoader
