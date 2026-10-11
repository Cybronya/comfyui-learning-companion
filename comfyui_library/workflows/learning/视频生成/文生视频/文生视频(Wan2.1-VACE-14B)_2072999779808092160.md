---
key: 视频生成/文生视频/文生视频(Wan2.1-VACE-14B)_2072999779808092160.json
name: 文生视频(Wan2.1-VACE-14B)_2072999779808092160
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频(Wan2.1-VACE-14B)_2072999779808092160.json
hash: cfe645cfddc8ae96
coverage: 0.947368
learned_at: 2026-10-11 20:38:47
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoVACEEncode, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, WanVideoVACEModelSelect, WanVideoBlockSwap, WanVideoSampler, INTConstant, INTConstant, INTConstant, WanVideoTextEncode, String Literal, VHS_VideoCombine, WanVideoDecode]
patterns: []
missing: [String Literal]
discoveries: [次要节点 `String Literal` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/文生视频(Wan2.1-VACE-14B)_2072999779808092160.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生视频(Wan2.1-VACE-14B)_2072999779808092160.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（19 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoVACEEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanVideoTextEncode`
- `String Literal`
- `VHS_VideoCombine`
- `WanVideoDecode`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoVACEEncode`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`WanVideoSampler`、`INTConstant`、`WanVideoTextEncode`、`VHS_VideoCombine`、`WanVideoDecode`

**缺卡**（1）：`String Literal`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、INTConstant、VHS_VideoCombine

## 学习发现

- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
