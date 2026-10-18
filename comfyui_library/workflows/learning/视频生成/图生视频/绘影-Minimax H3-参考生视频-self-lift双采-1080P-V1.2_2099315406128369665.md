---
key: 视频生成/图生视频/绘影-Minimax H3-参考生视频-self-lift双采-1080P-V1.2_2099315406128369665.json
name: 绘影-Minimax H3-参考生视频-self-lift双采-1080P-V1.2_2099315406128369665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/绘影-Minimax H3-参考生视频-self-lift双采-1080P-V1.2_2099315406128369665.json
hash: 3386a7ee6b7b4018
coverage: 0.895833
learned_at: 2026-10-17 01:45:19
nodes: [VAEDecode, VAEDecodeAudio, H3SigmaRefiner, ConditioningZeroOut, KSamplerSelect, VAELoader, ComfyMathExpression, MarkdownNote, BasicScheduler, LoraLoaderModelOnly, UNETLoader, MiniMaxH3SigmaShift, CLIPLoader, MiniMaxLowVRAMAttention, MiniMaxChunkFeedForward, PrimitiveFloat, VAELoader, LoadImage, ModelPreviewOverrideKJ, ResolutionSelector, SelfLiftH3Sampler, LoadImage, LoadImage, UNETLoader, ModelAttentionBackend, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadAudio, LoadAudio, LoadAudio, VHS_VideoCombine, LoadImage, PrimitiveStringMultiline, MarkdownNote, MarkdownNote, VHS_LoadVideo, VHS_LoadVideo, MiniMaxH3ReferenceToVideo, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/绘影-Minimax H3-参考生视频-self-lift双采-1080P-V1.2_2099315406128369665.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/绘影-Minimax H3-参考生视频-self-lift双采-1080P-V1.2_2099315406128369665.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（48 个）：
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `H3SigmaRefiner`
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `VAELoader`
- `ComfyMathExpression`
- `MarkdownNote`
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `MiniMaxH3SigmaShift`
- `CLIPLoader`
- `MiniMaxLowVRAMAttention`
- `MiniMaxChunkFeedForward`
- `PrimitiveFloat`
- `VAELoader`
- `LoadImage`
- `ModelPreviewOverrideKJ`
- `ResolutionSelector`
- `SelfLiftH3Sampler` ★核心
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `VHS_VideoCombine`
- `LoadImage`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `MarkdownNote`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `MiniMaxH3ReferenceToVideo`
- `VHS_LoadVideo`

## 知识

覆盖率 **90%**（43/48）

**有卡**：`VAEDecode`、`VAEDecodeAudio`、`H3SigmaRefiner`、`ConditioningZeroOut`、`KSamplerSelect`、`VAELoader`、`ComfyMathExpression`、`BasicScheduler`、`LoraLoaderModelOnly`、`UNETLoader`、`MiniMaxH3SigmaShift`、`CLIPLoader`、`MiniMaxLowVRAMAttention`、`MiniMaxChunkFeedForward`、`LoadImage`、`ModelPreviewOverrideKJ`、`ResolutionSelector`、`SelfLiftH3Sampler`、`ModelAttentionBackend`、`LoadAudio`、`VHS_VideoCombine`、`VHS_LoadVideo`、`MiniMaxH3ReferenceToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
