---
key: 视频生成/图生视频/Wan2.1_大摆锤舞蹈（胸部抖动优化版）_1948012879831269378.json
name: Wan2.1_大摆锤舞蹈（胸部抖动优化版）_1948012879831269378.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1_大摆锤舞蹈（胸部抖动优化版）_1948012879831269378.json
hash: 70b3a912547f641b
coverage: 0.676471
learned_at: 2026-10-15 22:30:46
nodes: [GetNode, GetNode, GetNode, GetNode, LoadWanVideoT5TextEncoder, WanVideoModelLoader, SetNode, SetNode, SetNode, GetNode, WanVideoTextEncode, ImageResizeKJv2, WanVideoTeaCache, easy showAnything, RHHiddenNodes, easy showAnything, Int, WanVideoDecode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, ColorMatch, RH_Captioner, RH_Prompter, LoadImage, VHS_VideoCombine, Int, Int, Int, WanVideoLoraSelect, WanVideoLoraSelect, JjkText, WanVideoSampler, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1_大摆锤舞蹈（胸部抖动优化版）_1948012879831269378.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1948012879831269378.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（34 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoTextEncode`
- `ImageResizeKJv2`
- `WanVideoTeaCache`
- `easy showAnything`
- `RHHiddenNodes`
- `easy showAnything`
- `Int`
- `WanVideoDecode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `ColorMatch`
- `RH_Captioner`
- `RH_Prompter`
- `LoadImage`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `Int`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `JjkText`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`

## 知识

覆盖率 **68%**（23/34）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoTextEncode`、`ImageResizeKJv2`、`WanVideoTeaCache`、`RHHiddenNodes`、`Int`、`WanVideoDecode`、`WanVideoVACEEncode`、`WanVideoVACEModelSelect`、`WanVideoVAELoader`、`ColorMatch`、`RH_Captioner`、`RH_Prompter`、`LoadImage`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoSampler`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
