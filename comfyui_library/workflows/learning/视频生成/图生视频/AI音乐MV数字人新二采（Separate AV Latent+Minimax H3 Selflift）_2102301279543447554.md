---
key: 视频生成/图生视频/AI音乐MV数字人新二采（Separate AV Latent+Minimax H3 Selflift）_2102301279543447554.json
name: AI音乐MV数字人新二采（Separate AV Latent+Minimax H3 Selflift）_2102301279543447554
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AI音乐MV数字人新二采（Separate AV Latent+Minimax H3 Selflift）_2102301279543447554.json
hash: 69cdda81e70e329d
coverage: 0.886364
learned_at: 2026-10-17 02:28:43
nodes: [MiniMaxChunkFeedForward, CLIPLoader, VAELoader, VAELoader, Reroute, SoundFlow_GetLength, ComfyMathExpression, ComfyNumberConvert, LTXVSeparateAVLatent, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, LoadImage, TrimAudioDuration, LoadAudio, PrimitiveFloat, PrimitiveFloat, ResolutionSelector, LoadImage, Textbox, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, LTXVAudioVAEEncode, UNETLoader, LoraLoaderModelOnly, SelfLiftAvatarH3Sampler, MiniMaxLowVRAMAttention, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerSelect, LTXVSeparateAVLatent, ConditioningZeroOut, BasicScheduler, PreviewAny, VAEDecode]
patterns: []
missing: []
---

# 视频生成/图生视频/AI音乐MV数字人新二采（Separate AV Latent+Minimax H3 Selflift）_2102301279543447554.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/AI音乐MV数字人新二采（Separate AV Latent+Minimax H3 Selflift）_2102301279543447554.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Other

**节点**（44 个）：
- `MiniMaxChunkFeedForward`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `Reroute`
- `SoundFlow_GetLength`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `LTXVSeparateAVLatent`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `LoadImage`
- `TrimAudioDuration`
- `LoadAudio`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ResolutionSelector`
- `LoadImage`
- `Textbox`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `LTXVAudioVAEEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SelfLiftAvatarH3Sampler` ★核心
- `MiniMaxLowVRAMAttention`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `ConditioningZeroOut`
- `BasicScheduler`
- `PreviewAny`
- `VAEDecode` ★核心

## 知识

覆盖率 **89%**（39/44）

**有卡**：`MiniMaxChunkFeedForward`、`CLIPLoader`、`VAELoader`、`SoundFlow_GetLength`、`ComfyMathExpression`、`ComfyNumberConvert`、`LTXVSeparateAVLatent`、`SolidMask`、`SetLatentNoiseMask`、`LTXVConcatAVLatent`、`LoadImage`、`TrimAudioDuration`、`LoadAudio`、`ResolutionSelector`、`Textbox`、`VHS_VideoCombine`、`MiniMaxH3ReferenceToVideo`、`ModelAttentionBackend`、`LTXVAudioVAEEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`SelfLiftAvatarH3Sampler`、`MiniMaxLowVRAMAttention`、`KSamplerSelect`、`ConditioningZeroOut`、`BasicScheduler`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
