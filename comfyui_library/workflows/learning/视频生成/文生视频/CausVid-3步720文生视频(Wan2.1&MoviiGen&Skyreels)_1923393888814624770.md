---
key: 视频生成/文生视频/CausVid-3步720文生视频(Wan2.1&MoviiGen&Skyreels)_1923393888814624770.json
name: CausVid-3步720文生视频(Wan2.1&MoviiGen&Skyreels)_1923393888814624770
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/CausVid-3步720文生视频(Wan2.1&MoviiGen&Skyreels)_1923393888814624770.json
hash: da9ed4f6e0703df7
coverage: 0.95
learned_at: 2026-10-10 22:58:46
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoVACEEncode, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, WanVideoVACEModelSelect, INTConstant, WanVideoTextEncode, String Literal, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSampler, WanVideoBlockSwap, INTConstant, INTConstant, VHS_VideoCombine, WanVideoDecode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, WanVideoVACEModelSelect, INTConstant, WanVideoTextEncode, String Literal, WanVideoLoraSelect, WanVideoSampler, WanVideoTorchCompileSettings, VHS_VideoCombine, WanVideoDecode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoVACEEncode, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, WanVideoVACEModelSelect, INTConstant, WanVideoTextEncode, String Literal, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoBlockSwap, INTConstant, INTConstant, VHS_VideoCombine, WanVideoDecode, WanVideoModelLoader, WanVideoTorchCompileSettings, INTConstant, INTConstant, WanVideoBlockSwap, WanVideoVACEEncode]
patterns: []
missing: [String Literal, String Literal, String Literal]
discoveries: [次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/CausVid-3步720文生视频(Wan2.1&MoviiGen&Skyreels)_1923393888814624770.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/CausVid-3步720文生视频(Wan2.1&MoviiGen&Skyreels)_1923393888814624770.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（60 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoVACEEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoVACEModelSelect`
- `INTConstant`
- `WanVideoTextEncode`
- `String Literal`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoVACEModelSelect`
- `INTConstant`
- `WanVideoTextEncode`
- `String Literal`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoVACEEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoVACEModelSelect`
- `INTConstant`
- `WanVideoTextEncode`
- `String Literal`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `INTConstant`
- `INTConstant`
- `WanVideoBlockSwap`
- `WanVideoVACEEncode`

## 知识

覆盖率 **95%**（57/60）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoVACEEncode`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoVACEModelSelect`、`INTConstant`、`WanVideoTextEncode`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSampler`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoTorchCompileSettings`

**缺卡**（3）：`String Literal`、`String Literal`、`String Literal`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect、INTConstant

## 学习发现

- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
