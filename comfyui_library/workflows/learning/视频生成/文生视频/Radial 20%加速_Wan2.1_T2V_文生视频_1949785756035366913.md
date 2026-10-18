---
key: 视频生成/文生视频/Radial 20%加速_Wan2.1_T2V_文生视频_1949785756035366913.json
name: Radial 20%加速_Wan2.1_T2V_文生视频_1949785756035366913.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Radial 20%加速_Wan2.1_T2V_文生视频_1949785756035366913.json
hash: b3f97c8f3922d423
coverage: 0.8
learned_at: 2026-10-15 22:43:33
nodes: [Note, Note, DownloadAndLoadGIMMVFIModel, WanVideoVAELoader, GIMMVFI_interpolate, WanVideoSLG, WanVideoTorchCompileSettings, WanVideoExperimentalArgs, WanVideoDecode, WanVideoEasyCache, WanVideoSetRadialAttention, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoEnhanceAVideo, WanVideoSampler, Note, Note, easy showAnything, MMAudioModelLoader, MMAudioSampler, PrimitiveBoolean, InversionDemoLazySwitch, LoadAudio, Evaluate Integers, VHS_VideoCombine, MMAudioFeatureUtilsLoader, RH_Translator, Int, easy showAnything, Note, WanVideoModelLoader, PreviewAudio, VHS_VideoCombine, WanVideoTextEncode, Note, LoadWanVideoT5TextEncoder, SeargePromptText, WanVideoEmptyEmbeds, Int, Int]
patterns: []
missing: []
---

# 视频生成/文生视频/Radial 20%加速_Wan2.1_T2V_文生视频_1949785756035366913.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1949785756035366913.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（40 个）：
- `Note`
- `Note`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoVAELoader`
- `GIMMVFI_interpolate`
- `WanVideoSLG`
- `WanVideoTorchCompileSettings`
- `WanVideoExperimentalArgs`
- `WanVideoDecode`
- `WanVideoEasyCache`
- `WanVideoSetRadialAttention`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoEnhanceAVideo`
- `WanVideoSampler` ★核心
- `Note`
- `Note`
- `easy showAnything`
- `MMAudioModelLoader`
- `MMAudioSampler` ★核心
- `PrimitiveBoolean`
- `InversionDemoLazySwitch`
- `LoadAudio`
- `Evaluate Integers`
- `VHS_VideoCombine`
- `MMAudioFeatureUtilsLoader`
- `RH_Translator`
- `Int`
- `easy showAnything`
- `Note`
- `WanVideoModelLoader`
- `PreviewAudio`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `Note`
- `LoadWanVideoT5TextEncoder`
- `SeargePromptText`
- `WanVideoEmptyEmbeds`
- `Int`
- `Int`

## 知识

覆盖率 **80%**（32/40）

**有卡**：`DownloadAndLoadGIMMVFIModel`、`WanVideoVAELoader`、`GIMMVFI_interpolate`、`WanVideoSLG`、`WanVideoTorchCompileSettings`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`WanVideoEasyCache`、`WanVideoSetRadialAttention`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`MMAudioModelLoader`、`MMAudioSampler`、`PrimitiveBoolean`、`InversionDemoLazySwitch`、`LoadAudio`、`Evaluate Integers`、`VHS_VideoCombine`、`MMAudioFeatureUtilsLoader`、`RH_Translator`、`Int`、`WanVideoModelLoader`、`PreviewAudio`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`SeargePromptText`、`WanVideoEmptyEmbeds`

**用到的条目**：WanVideoSampler、MMAudioSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、SeargePromptText
