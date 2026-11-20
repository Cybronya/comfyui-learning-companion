---
key: 数字人/数字人/MiniMax H3  30秒长视频短剧+自定义音频-V1.0_2116449796264386561.json
name: MiniMax H3  30秒长视频短剧+自定义音频-V1.0_2116449796264386561
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/MiniMax H3  30秒长视频短剧+自定义音频-V1.0_2116449796264386561.json
hash: ea84d430769d439e
coverage: 0.829268
learned_at: 2026-11-02 19:16:49
nodes: [CLIPLoader, VAELoader, ComfyMathExpression, VAELoader, DF_Int_to_Float, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, ConditioningZeroOut, LTXVSeparateAVLatent, BasicScheduler, KSamplerSelect, ModelPreviewOverrideKJ, LoadImage, PrimitiveInt, LTXVSeparateAVLatent, VAEDecodeAudio, RTXVideoFrameGeneration, ResolutionSelector, VAEDecode, JjkText, PrimitiveInt, UNETLoader, ModelAttentionBackend, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, LoraLoaderModelOnly, PrimitiveInt, ComfyMathExpression, MiniMaxH3ReferenceToVideo, SelfLiftAvatarH3Sampler, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_VideoCombine, LoadAudio, VHS_VideoCombine, MarkdownNote, Fast Groups Bypasser (rgthree), JjkText]
patterns: []
missing: []
---

# 数字人/数字人/MiniMax H3  30秒长视频短剧+自定义音频-V1.0_2116449796264386561.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/MiniMax H3  30秒长视频短剧+自定义音频-V1.0_2116449796264386561.json`

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
