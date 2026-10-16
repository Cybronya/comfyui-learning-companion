---
key: 视频生成/图生视频/MinimaxH3双模双采（hybird+remix）(双larry加速）工作流_2092962796731461634.json
name: MinimaxH3双模双采（hybird+remix）(双larry加速）工作流_2092962796731461634
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MinimaxH3双模双采（hybird+remix）(双larry加速）工作流_2092962796731461634.json
hash: 5ac8ea2fca33f9cf
coverage: 0.94
learned_at: 2026-10-16 22:59:15
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, ModelPreviewOverrideKJ, ShellAgentPluginVideoCombineEncrypt, SamplerCustomAdvanced, BasicScheduler, H3SigmaRefiner, SplitSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConcatAVLatent, KSamplerSelect, BasicGuider, ModelPreviewOverrideKJ, BasicGuider, SplitSigmas, BasicScheduler, H3SigmaRefiner, easy cleanGpuUsed, MiniMaxH3MemoryEfficientSageAttentionPatch, ComfyMathExpression, LoadImage, PrimitiveStringMultiline, MiniMaxLowVRAMAttention, Seed (rgthree), MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, LoadImage, MarkdownNote, CLIPLoader, VAELoader, VAELoader, UNETLoader, MiniMaxH3ReferenceToVideo, RandomNoise, MiniMaxLowVRAMAttention, MiniMaxH3TurboLoRA, MiniMaxH3SigmaShift, ModelAttentionBackend, MiniMaxH3TurboLoRA, MiniMaxH3SigmaShift, ModelAttentionBackend, VAEDecode, VHS_VideoCombine, VAEDecodeAudio, MinimaxH3LatentUpscaler3D, ResolutionSelector, PrimitiveFloat]
patterns: []
missing: []
---

# 视频生成/图生视频/MinimaxH3双模双采（hybird+remix）(双larry加速）工作流_2092962796731461634.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MinimaxH3双模双采（hybird+remix）(双larry加速）工作流_2092962796731461634.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（50 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ModelPreviewOverrideKJ`
- `ShellAgentPluginVideoCombineEncrypt`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `H3SigmaRefiner`
- `SplitSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ModelPreviewOverrideKJ`
- `BasicGuider`
- `SplitSigmas`
- `BasicScheduler`
- `H3SigmaRefiner`
- `easy cleanGpuUsed`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ComfyMathExpression`
- `LoadImage`
- `PrimitiveStringMultiline`
- `MiniMaxLowVRAMAttention`
- `Seed (rgthree)`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader` ★核心
- `LoadImage`
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `MiniMaxLowVRAMAttention`
- `MiniMaxH3TurboLoRA`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `MiniMaxH3TurboLoRA`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VAEDecodeAudio` ★核心
- `MinimaxH3LatentUpscaler3D`
- `ResolutionSelector`
- `PrimitiveFloat`

## 知识

覆盖率 **94%**（47/50）

**有卡**：`LoadImage`、`ModelPreviewOverrideKJ`、`ShellAgentPluginVideoCombineEncrypt`、`SamplerCustomAdvanced`、`BasicScheduler`、`H3SigmaRefiner`、`SplitSigmas`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`KSamplerSelect`、`BasicGuider`、`easy cleanGpuUsed`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ComfyMathExpression`、`MiniMaxLowVRAMAttention`、`Seed (rgthree)`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`MiniMaxH3ReferenceToVideo`、`RandomNoise`、`MiniMaxH3TurboLoRA`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`VAEDecode`、`VHS_VideoCombine`、`VAEDecodeAudio`、`MinimaxH3LatentUpscaler3D`、`ResolutionSelector`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
