---
key: 视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2087445019107090434.json
name: MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2087445019107090434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2087445019107090434.json
hash: b7f9d560803164da
coverage: 0.956522
learned_at: 2026-10-07 00:34:08
nodes: [KSamplerSelect, BasicGuider, SamplerCustomAdvanced, MiniMaxH3ImageToVideo, VAEDecode, BasicScheduler, VAELoader, VAELoader, CLIPLoader, Int, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderBypassModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, EnhancedLoadDiffusionModel, RandomNoise, VAEDecodeAudio, CreateVideo, LoadImage, LoadImage, Text, SaveVideo, VHS_VideoCombine, RHHiddenNodes]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2087445019107090434.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2087445019107090434.json`

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

覆盖率 **96%**（22/23）

**有卡**：`KSamplerSelect`、`BasicGuider`、`SamplerCustomAdvanced`、`MiniMaxH3ImageToVideo`、`VAEDecode`、`BasicScheduler`、`VAELoader`、`CLIPLoader`、`Int`、`LoraLoaderBypassModelOnly`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`EnhancedLoadDiffusionModel`、`RandomNoise`、`VAEDecodeAudio`、`CreateVideo`、`LoadImage`、`Text`、`SaveVideo`、`VHS_VideoCombine`、`RHHiddenNodes`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio、LoraLoaderBypassModelOnly

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
