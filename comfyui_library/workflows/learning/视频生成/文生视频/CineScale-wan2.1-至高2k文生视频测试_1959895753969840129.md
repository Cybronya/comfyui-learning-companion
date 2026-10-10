---
key: 视频生成/文生视频/CineScale-wan2.1-至高2k文生视频测试_1959895753969840129.json
name: CineScale-wan2.1-至高2k文生视频测试_1959895753969840129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/CineScale-wan2.1-至高2k文生视频测试_1959895753969840129.json
hash: da1cfce2c60539f5
coverage: 0.923077
learned_at: 2026-10-10 22:58:47
nodes: [WanVideoVAELoader, WanVideoDecode, WanVideoSetRadialAttention, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoSampler, WanVideoModelLoader, WanVideoEmptyEmbeds, WanVideoLoraSelect, VHS_VideoCombine, String Literal]
patterns: []
missing: [String Literal]
discoveries: [次要节点 `String Literal` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/CineScale-wan2.1-至高2k文生视频测试_1959895753969840129.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/CineScale-wan2.1-至高2k文生视频测试_1959895753969840129.json`

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

覆盖率 **92%**（12/13）

**有卡**：`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoSetRadialAttention`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoEmptyEmbeds`、`VHS_VideoCombine`

**缺卡**（1）：`String Literal`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、VHS_VideoCombine、WanVideoBlockSwap

## 学习发现

- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
