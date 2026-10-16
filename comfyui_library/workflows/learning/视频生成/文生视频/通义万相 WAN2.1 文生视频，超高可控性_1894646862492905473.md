---
key: 视频生成/文生视频/通义万相 WAN2.1 文生视频，超高可控性_1894646862492905473.json
name: 通义万相 WAN2.1 文生视频，超高可控性_1894646862492905473.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1894646862492905473.json
hash: 3b6bc17f2e0c8064
coverage: 0.75
learned_at: 2026-10-15 22:43:20
nodes: [WanVideoDecode, WanVideoVAELoader, WanVideoSampler, WanVideoTextEncode, WanVideoEmptyEmbeds, WanVideoModelLoader, VHS_VideoCombine, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, Note, Note, Note]
patterns: []
missing: []
---

# 视频生成/文生视频/通义万相 WAN2.1 文生视频，超高可控性_1894646862492905473.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1894646862492905473.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（12 个）：
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `Note`
- `Note`

## 知识

覆盖率 **75%**（9/12）

**有卡**：`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoEmptyEmbeds`、`WanVideoModelLoader`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、VHS_VideoCombine、WanVideoBlockSwap、WanVideoModelLoader
