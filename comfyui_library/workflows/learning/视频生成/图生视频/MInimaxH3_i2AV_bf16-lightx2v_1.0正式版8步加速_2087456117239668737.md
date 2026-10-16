---
key: 视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0正式版8步加速_2087456117239668737.json
name: MInimaxH3_i2AV_bf16-lightx2v_1.0正式版8步加速_2087456117239668737
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0正式版8步加速_2087456117239668737.json
hash: 0bdd80dc18e8e473
coverage: 1
learned_at: 2026-10-16 21:27:39
nodes: [RandomNoise, KSamplerSelect, BasicGuider, SamplerCustomAdvanced, VAEDecodeAudio, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, VAELoader, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, BasicScheduler, EnhancedLoadDiffusionModel, VAELoader, LoraLoaderBypassModelOnly, Int, Text, RHHiddenNodes, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0正式版8步加速_2087456117239668737.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0正式版8步加速_2087456117239668737.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Other

**节点**（20 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `VAELoader`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `BasicScheduler`
- `EnhancedLoadDiffusionModel`
- `VAELoader`
- `LoraLoaderBypassModelOnly` ★核心
- `Int`
- `Text`
- `RHHiddenNodes`
- `LoadImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`RandomNoise`、`KSamplerSelect`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`VAELoader`、`MiniMaxH3ImageToVideo`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BasicScheduler`、`EnhancedLoadDiffusionModel`、`LoraLoaderBypassModelOnly`、`Int`、`Text`、`RHHiddenNodes`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio、LoraLoaderBypassModelOnly
