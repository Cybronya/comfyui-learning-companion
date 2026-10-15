---
key: 视频生成/文生视频/【遇见AI】wan2.1文生视频基础流，不带加速_2061012769037701122.json
name: 【遇见AI】wan2.1文生视频基础流，不带加速_2061012769037701122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【遇见AI】wan2.1文生视频基础流，不带加速_2061012769037701122.json
hash: 12d0582d9c08762f
coverage: 1
learned_at: 2026-10-15 22:47:43
nodes: [WanVideoSampler, WanVideoDecode, WanVideoTextEncode, WanVideoEmptyEmbeds, VHS_VideoCombine, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader]
patterns: []
missing: []
---

# 视频生成/文生视频/【遇见AI】wan2.1文生视频基础流，不带加速_2061012769037701122.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【遇见AI】wan2.1文生视频基础流，不带加速_2061012769037701122.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（8 个）：
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoTextEncode`
- `WanVideoEmptyEmbeds`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`

## 知识

覆盖率 **100%**（8/8）

**有卡**：`WanVideoSampler`、`WanVideoDecode`、`WanVideoTextEncode`、`WanVideoEmptyEmbeds`、`VHS_VideoCombine`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、VHS_VideoCombine、WanVideoModelLoader、WanVideoEmptyEmbeds
