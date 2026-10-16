---
key: 视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速_2087442235926335490.json
name: MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速_2087442235926335490
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速_2087442235926335490.json
hash: 06e7e2535484e7b9
coverage: 1
learned_at: 2026-10-16 21:27:39
nodes: [KSamplerSelect, BasicGuider, SamplerCustomAdvanced, MiniMaxH3ImageToVideo, VAEDecode, BasicScheduler, VAELoader, VAELoader, CLIPLoader, Int, LoraLoaderBypassModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, EnhancedLoadDiffusionModel, RandomNoise, VHS_VideoCombine, VAEDecodeAudio, CreateVideo, SaveVideo, LoadImage, Text, LayerUtility: ImageScaleByAspectRatio V2, RHHiddenNodes, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速_2087442235926335490.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速_2087442235926335490.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3ImageToVideo`
- `VAEDecode` ★核心
- `BasicScheduler`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `Int`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `EnhancedLoadDiffusionModel`
- `RandomNoise`
- `VHS_VideoCombine`
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `SaveVideo`
- `LoadImage`
- `Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RHHiddenNodes`
- `LoadImage`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`KSamplerSelect`、`BasicGuider`、`SamplerCustomAdvanced`、`MiniMaxH3ImageToVideo`、`VAEDecode`、`BasicScheduler`、`VAELoader`、`CLIPLoader`、`Int`、`LoraLoaderBypassModelOnly`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`EnhancedLoadDiffusionModel`、`RandomNoise`、`VHS_VideoCombine`、`VAEDecodeAudio`、`CreateVideo`、`SaveVideo`、`LoadImage`、`Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`RHHiddenNodes`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio、LoraLoaderBypassModelOnly
