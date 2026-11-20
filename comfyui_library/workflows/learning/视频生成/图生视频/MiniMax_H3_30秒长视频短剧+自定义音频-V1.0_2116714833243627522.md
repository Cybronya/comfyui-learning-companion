---
key: 视频生成/图生视频/MiniMax_H3_30秒长视频短剧+自定义音频-V1.0_2116714833243627522.json
name: MiniMax_H3_30秒长视频短剧+自定义音频-V1.0_2116714833243627522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax_H3_30秒长视频短剧+自定义音频-V1.0_2116714833243627522.json
hash: 8f690d09033b0796
coverage: 0.829268
learned_at: 2026-11-02 19:18:04
nodes: [CLIPLoader, VAELoader, ComfyMathExpression, VAELoader, DF_Int_to_Float, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, ConditioningZeroOut, LTXVSeparateAVLatent, BasicScheduler, KSamplerSelect, ModelPreviewOverrideKJ, LoadImage, PrimitiveInt, LTXVSeparateAVLatent, VAEDecodeAudio, RTXVideoFrameGeneration, ResolutionSelector, VAEDecode, JjkText, PrimitiveInt, UNETLoader, ModelAttentionBackend, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, LoraLoaderModelOnly, PrimitiveInt, ComfyMathExpression, MiniMaxH3ReferenceToVideo, SelfLiftAvatarH3Sampler, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_VideoCombine, LoadAudio, VHS_VideoCombine, MarkdownNote, Fast Groups Bypasser (rgthree), JjkText]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax_H3_30秒长视频短剧+自定义音频-V1.0_2116714833243627522.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax_H3_30秒长视频短剧+自定义音频-V1.0_2116714833243627522.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（41 个）：
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
- `VAEDecodeAudio` ★核心
- `RTXVideoFrameGeneration`
- `ResolutionSelector`
- `VAEDecode` ★核心
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
- `SelfLiftAvatarH3Sampler` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `LoadAudio`
- `VHS_VideoCombine`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `JjkText`

## 知识

覆盖率 **83%**（34/41）

**有卡**：`CLIPLoader`、`VAELoader`、`ComfyMathExpression`、`DF_Int_to_Float`、`LayerUtility: PurgeVRAM V2`、`ConditioningZeroOut`、`LTXVSeparateAVLatent`、`BasicScheduler`、`KSamplerSelect`、`ModelPreviewOverrideKJ`、`LoadImage`、`VAEDecodeAudio`、`RTXVideoFrameGeneration`、`ResolutionSelector`、`VAEDecode`、`UNETLoader`、`ModelAttentionBackend`、`MiniMaxChunkFeedForward`、`MiniMaxLowVRAMAttention`、`LoraLoaderModelOnly`、`MiniMaxH3ReferenceToVideo`、`SelfLiftAvatarH3Sampler`、`VHS_VideoCombine`、`LoadAudio`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
