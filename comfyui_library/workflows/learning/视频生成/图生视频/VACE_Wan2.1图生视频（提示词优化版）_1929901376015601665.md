---
key: 视频生成/图生视频/VACE_Wan2.1图生视频（提示词优化版）_1929901376015601665.json
name: VACE_Wan2.1图生视频（提示词优化版）_1929901376015601665.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/VACE_Wan2.1图生视频（提示词优化版）_1929901376015601665.json
hash: fbbc0da71a758d61
coverage: 0.65625
learned_at: 2026-10-15 22:30:02
nodes: [GetNode, GetNode, GetNode, GetNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, SetNode, SetNode, SetNode, WanVideoVACEModelSelect, GetNode, WanVideoTextEncode, LoadImage, WanVideoVACEEncode, WanVideoSLG, Int, Int, Int, ImageResizeKJv2, WanVideoTeaCache, WanVideoDecode, WanVideoExperimentalArgs, VHS_VideoCombine, easy showAnything, RH_Captioner, RHHiddenNodes, RH_Prompter, easy showAnything, JjkText, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/VACE_Wan2.1图生视频（提示词优化版）_1929901376015601665.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1929901376015601665.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（32 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoVACEModelSelect`
- `GetNode`
- `WanVideoTextEncode`
- `LoadImage`
- `WanVideoVACEEncode`
- `WanVideoSLG`
- `Int`
- `Int`
- `Int`
- `ImageResizeKJv2`
- `WanVideoTeaCache`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `VHS_VideoCombine`
- `easy showAnything`
- `RH_Captioner`
- `RHHiddenNodes`
- `RH_Prompter`
- `easy showAnything`
- `JjkText`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **66%**（21/32）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoTextEncode`、`LoadImage`、`WanVideoVACEEncode`、`WanVideoSLG`、`Int`、`ImageResizeKJv2`、`WanVideoTeaCache`、`WanVideoDecode`、`WanVideoExperimentalArgs`、`VHS_VideoCombine`、`RH_Captioner`、`RHHiddenNodes`、`RH_Prompter`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、RH_Prompter
