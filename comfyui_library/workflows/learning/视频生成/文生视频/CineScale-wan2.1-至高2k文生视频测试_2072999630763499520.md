---
key: 视频生成/文生视频/CineScale-wan2.1-至高2k文生视频测试_2072999630763499520.json
name: CineScale-wan2.1-至高2k文生视频测试_2072999630763499520
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/CineScale-wan2.1-至高2k文生视频测试_2072999630763499520.json
hash: efe32432f161202e
coverage: 1
learned_at: 2026-10-15 22:44:06
nodes: [WanVideoVAELoader, WanVideoDecode, WanVideoSetRadialAttention, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoSampler, WanVideoModelLoader, WanVideoEmptyEmbeds, WanVideoLoraSelect, VHS_VideoCombine, String Literal]
patterns: []
missing: []
---

# 视频生成/文生视频/CineScale-wan2.1-至高2k文生视频测试_2072999630763499520.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/CineScale-wan2.1-至高2k文生视频测试_2072999630763499520.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（13 个）：
- `WanVideoVAELoader`
- `WanVideoDecode`
- `WanVideoSetRadialAttention`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `String Literal`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoSetRadialAttention`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoEmptyEmbeds`、`VHS_VideoCombine`、`String Literal`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、VHS_VideoCombine、WanVideoBlockSwap
