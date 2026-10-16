---
key: 视频生成/图生视频/自动提示词_WAN2.1-CanAI_1932714999003369473.json
name: 自动提示词_WAN2.1-CanAI_1932714999003369473.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1932714999003369473.json
hash: 366876dba12be6d7
coverage: 0.638889
learned_at: 2026-10-15 22:30:12
nodes: [LoadWanVideoT5TextEncoder, Anything Everywhere, LoadWanVideoClipTextEncoder, WanVideoEnhanceAVideo, Anything Everywhere, Anything Everywhere, LayerUtility: PurgeVRAM V2, SaveLatent, GetNode, WanVideoImageClipEncode, Anything Everywhere, Anything Everywhere, MathExpression|pysssss, Int, Florence2ModelLoader, WanVideoTorchCompileSettings, Anything Everywhere, LayerUtility: ImageScaleByAspectRatio V2, WanVideoModelLoader, Seed Everywhere, VHS_VideoCombine, WanVideoExperimentalArgs, SetNode, WanVideoVAELoader, Anything Everywhere, WanVideoSLG, WanVideoDecode, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, WanVideoTextEncode, WanVideoSampler, LoadImage, StringFunction|pysssss, Florence2Run]
patterns: []
missing: []
---

# 视频生成/图生视频/自动提示词_WAN2.1-CanAI_1932714999003369473.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1932714999003369473.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（36 个）：
- `LoadWanVideoT5TextEncoder`
- `Anything Everywhere`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoEnhanceAVideo`
- `Anything Everywhere`
- `Anything Everywhere`
- `LayerUtility: PurgeVRAM V2`
- `SaveLatent`
- `GetNode`
- `WanVideoImageClipEncode`
- `Anything Everywhere`
- `Anything Everywhere`
- `MathExpression|pysssss`
- `Int`
- `Florence2ModelLoader`
- `WanVideoTorchCompileSettings`
- `Anything Everywhere`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoModelLoader`
- `Seed Everywhere`
- `VHS_VideoCombine`
- `WanVideoExperimentalArgs`
- `SetNode`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `WanVideoSLG`
- `WanVideoDecode`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `LoadImage`
- `StringFunction|pysssss`
- `Florence2Run`

## 知识

覆盖率 **64%**（23/36）

**有卡**：`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoEnhanceAVideo`、`LayerUtility: PurgeVRAM V2`、`SaveLatent`、`WanVideoImageClipEncode`、`MathExpression|pysssss`、`Int`、`Florence2ModelLoader`、`WanVideoTorchCompileSettings`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoModelLoader`、`Seed Everywhere`、`VHS_VideoCombine`、`WanVideoExperimentalArgs`、`WanVideoVAELoader`、`WanVideoSLG`、`WanVideoDecode`、`WanVideoTextEncode`、`WanVideoSampler`、`LoadImage`、`StringFunction|pysssss`、`Florence2Run`

**用到的条目**：LoadImage、WanVideoSampler、Seed Everywhere、SaveLatent、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode
