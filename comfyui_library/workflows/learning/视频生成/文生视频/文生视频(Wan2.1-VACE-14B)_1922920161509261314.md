---
key: 视频生成/文生视频/文生视频(Wan2.1-VACE-14B)_1922920161509261314.json
name: 文生视频(Wan2.1-VACE-14B)_1922920161509261314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频(Wan2.1-VACE-14B)_1922920161509261314.json
hash: 0d2c8e287af4addf
coverage: 1
learned_at: 2026-10-15 22:48:41
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoVACEEncode, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, WanVideoVACEModelSelect, WanVideoBlockSwap, WanVideoSampler, INTConstant, INTConstant, INTConstant, WanVideoTextEncode, String Literal, VHS_VideoCombine, WanVideoDecode]
patterns: []
missing: []
---

# 视频生成/文生视频/文生视频(Wan2.1-VACE-14B)_1922920161509261314.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生视频(Wan2.1-VACE-14B)_1922920161509261314.json`

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

覆盖率 **100%**（19/19）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoVACEEncode`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`WanVideoSampler`、`INTConstant`、`WanVideoTextEncode`、`String Literal`、`VHS_VideoCombine`、`WanVideoDecode`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、INTConstant、VHS_VideoCombine
