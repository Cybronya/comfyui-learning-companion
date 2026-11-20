---
key: 平台全量/H3图生视频H3_ Image-to-Video, Long-Form Video Acceler_2117453506549469186.json
name: H3图生视频H3_ Image-to-Video, Long-Form Video Acceler_2117453506549469186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/H3图生视频H3_ Image-to-Video, Long-Form Video Acceler_2117453506549469186.json
hash: 8725ceae25117aae
coverage: 0.756757
learned_at: 2026-11-14 00:31:35
nodes: [CLIPLoader, VAELoader, ComfyMathExpression, VAELoader, DF_Int_to_Float, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, ConditioningZeroOut, LTXVSeparateAVLatent, BasicScheduler, KSamplerSelect, ModelPreviewOverrideKJ, LoadImage, PrimitiveInt, LTXVSeparateAVLatent, SetNode, VAEDecodeAudio, GetNode, RTXVideoFrameGeneration, ResolutionSelector, VAEDecode, SetNode, JjkText, PrimitiveInt, UNETLoader, ModelAttentionBackend, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, LoraLoaderModelOnly, PrimitiveInt, ComfyMathExpression, MiniMaxH3ReferenceToVideo, GetNode, SelfLiftAvatarH3Sampler, LoadImage, Fast Groups Bypasser (rgthree), VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/H3图生视频H3_ Image-to-Video, Long-Form Video Acceler_2117453506549469186.json

> 来源文件 `comfyui_library/workflows/平台全量/H3图生视频H3_ Image-to-Video, Long-Form Video Acceler_2117453506549469186.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（37 个）：
- `CLIPLoader`
- `VAELoader`
- `ComfyMathExpression`
- `VAELoader`
- `DF_Int_to_Float`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `ConditioningZeroOut`
- `LTXVSeparateAVLatent`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `ModelPreviewOverrideKJ`
- `LoadImage`
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `SetNode`
- `VAEDecodeAudio` ★核心
- `GetNode`
- `RTXVideoFrameGeneration`
- `ResolutionSelector`
- `VAEDecode` ★核心
- `SetNode`
- `JjkText`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `ModelAttentionBackend`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `ComfyMathExpression`
- `MiniMaxH3ReferenceToVideo`
- `GetNode`
- `SelfLiftAvatarH3Sampler` ★核心
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`

## 知识

覆盖率 **76%**（28/37）

**有卡**：`CLIPLoader`、`VAELoader`、`ComfyMathExpression`、`DF_Int_to_Float`、`LayerUtility: PurgeVRAM V2`、`ConditioningZeroOut`、`LTXVSeparateAVLatent`、`BasicScheduler`、`KSamplerSelect`、`ModelPreviewOverrideKJ`、`LoadImage`、`VAEDecodeAudio`、`RTXVideoFrameGeneration`、`ResolutionSelector`、`VAEDecode`、`UNETLoader`、`ModelAttentionBackend`、`MiniMaxChunkFeedForward`、`MiniMaxLowVRAMAttention`、`LoraLoaderModelOnly`、`MiniMaxH3ReferenceToVideo`、`SelfLiftAvatarH3Sampler`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
