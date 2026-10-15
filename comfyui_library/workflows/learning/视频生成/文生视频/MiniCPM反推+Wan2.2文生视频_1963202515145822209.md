---
key: 视频生成/文生视频/MiniCPM反推+Wan2.2文生视频_1963202515145822209.json
name: MiniCPM反推+Wan2.2文生视频_1963202515145822209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniCPM反推+Wan2.2文生视频_1963202515145822209.json
hash: a2af59cb0a9783db
coverage: 0.769231
learned_at: 2026-10-15 22:45:27
nodes: [GetNode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoDecode, PrimitiveNode, PrimitiveNode, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoSampler, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSampler, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetRadialAttention, WanVideoSetRadialAttention, PrimitiveNode, PrimitiveNode, WanVideoContextOptions, easy seed, PrimitiveNode, StringToFloatList, FloatToSigmas, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTorchCompileSettings, easy globalSeed, WanVideoEmptyEmbeds, String Literal, LoadVideo, ShowText, AILab_MiniCPM_4_V]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniCPM反推+Wan2.2文生视频_1963202515145822209.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniCPM反推+Wan2.2文生视频_1963202515145822209.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（39 个）：
- `GetNode`
- `SetNode`
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoDecode`
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSetRadialAttention`
- `WanVideoSetRadialAttention`
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoContextOptions`
- `easy seed`
- `PrimitiveNode`
- `StringToFloatList`
- `FloatToSigmas`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `easy globalSeed`
- `WanVideoEmptyEmbeds`
- `String Literal`
- `LoadVideo`
- `ShowText`
- `AILab_MiniCPM_4_V`

## 知识

覆盖率 **77%**（30/39）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSetRadialAttention`、`WanVideoContextOptions`、`easy seed`、`StringToFloatList`、`FloatToSigmas`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`easy globalSeed`、`WanVideoEmptyEmbeds`、`String Literal`、`LoadVideo`、`ShowText`、`AILab_MiniCPM_4_V`

**用到的条目**：WanVideoSampler、easy globalSeed、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
