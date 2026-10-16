---
key: 视频生成/图生视频/MInimaxH3_Ref2AV_bf16-lightx2v_1.0八步加速_2088188664793878530.json
name: MInimaxH3_Ref2AV_bf16-lightx2v_1.0八步加速_2088188664793878530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MInimaxH3_Ref2AV_bf16-lightx2v_1.0八步加速_2088188664793878530.json
hash: bf67dfe86ab5906d
coverage: 1
learned_at: 2026-10-16 21:43:24
nodes: [KSamplerSelect, BasicGuider, RandomNoise, VAEDecodeAudio, SamplerCustomAdvanced, CLIPLoader, VAEDecode, VAELoader, VAELoader, LoadImage, easy MiniMaxH3ReferenceToVideoBridge, EnhancedLoadDiffusionModel, LoraLoaderBypassModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, LoadImage, LoadImage, VHS_VideoCombine, Text, ResolutionSelector, ImageConcatenateMulti_UTK, BasicScheduler, RHHiddenNodes]
patterns: []
missing: []
---

# 视频生成/图生视频/MInimaxH3_Ref2AV_bf16-lightx2v_1.0八步加速_2088188664793878530.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MInimaxH3_Ref2AV_bf16-lightx2v_1.0八步加速_2088188664793878530.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（22 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `VAEDecodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `VAELoader`
- `VAELoader`
- `LoadImage`
- `easy MiniMaxH3ReferenceToVideoBridge`
- `EnhancedLoadDiffusionModel`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `Text`
- `ResolutionSelector`
- `ImageConcatenateMulti_UTK`
- `BasicScheduler`
- `RHHiddenNodes`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`VAEDecodeAudio`、`SamplerCustomAdvanced`、`CLIPLoader`、`VAEDecode`、`VAELoader`、`LoadImage`、`easy MiniMaxH3ReferenceToVideoBridge`、`EnhancedLoadDiffusionModel`、`LoraLoaderBypassModelOnly`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`VHS_VideoCombine`、`Text`、`ResolutionSelector`、`ImageConcatenateMulti_UTK`、`BasicScheduler`、`RHHiddenNodes`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio
