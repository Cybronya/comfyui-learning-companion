---
key: 视频生成/文生视频/Wan2.1-NAG反向应用_2072999737776971776.json
name: Wan2.1-NAG反向应用_2072999737776971776
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1-NAG反向应用_2072999737776971776.json
hash: 81d123fffb1273df
coverage: 0.933333
learned_at: 2026-10-11 20:38:42
nodes: [WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, WanVideoDecode, WanVideoBlockSwap, VHS_VideoCombine, WanVideoApplyNAG, WanVideoEmptyEmbeds, LoadWanVideoT5TextEncoder, String Literal, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoVAELoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoModelLoader]
patterns: []
missing: [String Literal]
discoveries: [次要节点 `String Literal` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.1-NAG反向应用_2072999737776971776.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.1-NAG反向应用_2072999737776971776.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（15 个）：
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoEmptyEmbeds`
- `LoadWanVideoT5TextEncoder`
- `String Literal`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`WanVideoTextEncodeSingle`、`WanVideoDecode`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoApplyNAG`、`WanVideoEmptyEmbeds`、`LoadWanVideoT5TextEncoder`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`

**缺卡**（1）：`String Literal`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、VHS_VideoCombine、WanVideoBlockSwap、WanVideoModelLoader

## 学习发现

- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
