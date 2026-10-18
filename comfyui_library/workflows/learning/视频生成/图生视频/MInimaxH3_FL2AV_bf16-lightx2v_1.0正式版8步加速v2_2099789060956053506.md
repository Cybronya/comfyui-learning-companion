---
key: 视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2099789060956053506.json
name: MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2099789060956053506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2099789060956053506.json
hash: 7f98e0014ab80289
coverage: 1
learned_at: 2026-10-17 01:59:07
nodes: [KSamplerSelect, BasicGuider, SamplerCustomAdvanced, MiniMaxH3ImageToVideo, VAEDecode, BasicScheduler, VAELoader, VAELoader, CLIPLoader, Int, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderBypassModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, EnhancedLoadDiffusionModel, RandomNoise, VAEDecodeAudio, CreateVideo, LoadImage, LoadImage, Text, SaveVideo, VHS_VideoCombine, RHHiddenNodes]
patterns: []
missing: []
---

# 视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2099789060956053506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2099789060956053506.json`

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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `EnhancedLoadDiffusionModel`
- `RandomNoise`
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `LoadImage`
- `LoadImage`
- `Text`
- `SaveVideo`
- `VHS_VideoCombine`
- `RHHiddenNodes`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`KSamplerSelect`、`BasicGuider`、`SamplerCustomAdvanced`、`MiniMaxH3ImageToVideo`、`VAEDecode`、`BasicScheduler`、`VAELoader`、`CLIPLoader`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderBypassModelOnly`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`EnhancedLoadDiffusionModel`、`RandomNoise`、`VAEDecodeAudio`、`CreateVideo`、`LoadImage`、`Text`、`SaveVideo`、`VHS_VideoCombine`、`RHHiddenNodes`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio、LoraLoaderBypassModelOnly
