---
key: 平台全量/新 · 视频风格转绘 Ditto 2.0 【新优化版】_1982817001578070017.json
name: 新 · 视频风格转绘 Ditto 2.0 【新优化版】_1982817001578070017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/新 · 视频风格转绘 Ditto 2.0 【新优化版】_1982817001578070017.json
hash: d5f0fbaa0953ca45
coverage: 0.402778
learned_at: 2026-11-14 02:12:10
nodes: [SetNode, SetNode, SetNode, SetNode, GetImageSize, SetNode, SimpleMath+, SimpleMath+, SetNode, WanVideoVAELoader, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoModelLoader, GetNode, WanVideoVACEEncode, WanVideoTextEncode, WanVideoDecode, WanVideoSLG, LayerUtility: ImageScaleByAspectRatio V2, Primitive integer [Crystools], LoadWanVideoT5TextEncoder, SimpleMath+, SetNode, WanVideoSampler, WanVideoVACEModelSelect, WanVideoBlockSwap, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], VHS_LoadVideo, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, ImpactSwitch, SetNode, GetNode, VHS_VideoCombine, LoadImage, SaveAudio, WanVideoTorchCompileSettings, Primitive integer [Crystools], ImageConcanate, VHS_VideoCombine, GetNode, RHHiddenNodes, RHHiddenNodes]
patterns: []
missing: []
---

# 平台全量/新 · 视频风格转绘 Ditto 2.0 【新优化版】_1982817001578070017.json

> 来源文件 `comfyui_library/workflows/平台全量/新 · 视频风格转绘 Ditto 2.0 【新优化版】_1982817001578070017.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（72 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `SetNode`
- `SimpleMath+`
- `SimpleMath+`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoModelLoader`
- `GetNode`
- `WanVideoVACEEncode`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `WanVideoSLG`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Primitive integer [Crystools]`
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `VHS_LoadVideo`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `ImpactSwitch`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `LoadImage`
- `SaveAudio`
- `WanVideoTorchCompileSettings`
- `Primitive integer [Crystools]`
- `ImageConcanate`
- `VHS_VideoCombine`
- `GetNode`
- `RHHiddenNodes`
- `RHHiddenNodes`

## 知识

覆盖率 **40%**（29/72）

**有卡**：`GetImageSize`、`SimpleMath+`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoVACEEncode`、`WanVideoTextEncode`、`WanVideoDecode`、`WanVideoSLG`、`LayerUtility: ImageScaleByAspectRatio V2`、`Primitive integer [Crystools]`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`VHS_VideoCombine`、`LoadImage`、`SaveAudio`、`WanVideoTorchCompileSettings`、`ImageConcanate`、`RHHiddenNodes`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、GetImageSize
