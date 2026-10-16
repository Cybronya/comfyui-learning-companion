---
key: 视频生成/图生视频/MInimaxH3_Ref2AV_bf16-lightx2v_1.0八步加速V2_2088193284681322497.json
name: MInimaxH3_Ref2AV_bf16-lightx2v_1.0八步加速V2_2088193284681322497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MInimaxH3_Ref2AV_bf16-lightx2v_1.0八步加速V2_2088193284681322497.json
hash: 4ce6bd87a385a29e
coverage: 1
learned_at: 2026-10-16 21:43:24
nodes: [KSamplerSelect, BasicGuider, RandomNoise, VAEDecodeAudio, SamplerCustomAdvanced, CLIPLoader, VAEDecode, VAELoader, VAELoader, easy MiniMaxH3ReferenceToVideoBridge, EnhancedLoadDiffusionModel, LoraLoaderBypassModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, VHS_VideoCombine, ImageConcatenateMulti_UTK, BasicScheduler, LoadImage, LoadImage, LoadImage, Text, ResolutionSelector, RHHiddenNodes]
patterns: []
missing: []
---

# 视频生成/图生视频/MInimaxH3_Ref2AV_bf16-lightx2v_1.0八步加速V2_2088193284681322497.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MInimaxH3_Ref2AV_bf16-lightx2v_1.0八步加速V2_2088193284681322497.json`

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
- `easy MiniMaxH3ReferenceToVideoBridge`
- `EnhancedLoadDiffusionModel`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VHS_VideoCombine`
- `ImageConcatenateMulti_UTK`
- `BasicScheduler`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Text`
- `ResolutionSelector`
- `RHHiddenNodes`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`VAEDecodeAudio`、`SamplerCustomAdvanced`、`CLIPLoader`、`VAEDecode`、`VAELoader`、`easy MiniMaxH3ReferenceToVideoBridge`、`EnhancedLoadDiffusionModel`、`LoraLoaderBypassModelOnly`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`VHS_VideoCombine`、`ImageConcatenateMulti_UTK`、`BasicScheduler`、`LoadImage`、`Text`、`ResolutionSelector`、`RHHiddenNodes`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio
