---
key: 视频生成/文生视频/minimaxH3UltraFastestTrue4_v80LightningSpeed_2098097827569295361.json
name: minimaxH3UltraFastestTrue4_v80LightningSpeed_2098097827569295361
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/minimaxH3UltraFastestTrue4_v80LightningSpeed_2098097827569295361.json
hash: c87b3f5de15e9daf
coverage: 0.873684
learned_at: 2026-10-15 22:47:26
nodes: [CreateVideo, BasicGuider, ComfyMathExpression, PrimitiveFloat, PrimitiveStringMultiline, MiniMaxH3SigmaShift, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), VAEDecode, Label (rgthree), VAEDecodeAudio, Label (rgthree), Label (rgthree), ModelAttentionBackend, Label (rgthree), Label (rgthree), LoadAudio, Label (rgthree), LoadImage, LoadImage, RandomNoise, Label (rgthree), Label (rgthree), Label (rgthree), MarkdownNote, MarkdownNote, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), MiniMaxH3ReferenceToVideo, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), MarkdownNote, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), VHS_LoadVideo, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), LoadImage, SaveVideo, Label (rgthree), Label (rgthree), MarkdownNote, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), VAELoader, VAELoader, CLIPLoader, KSamplerSelect, SamplerCustomAdvanced, Label (rgthree), MarkdownNote, Label (rgthree), Label (rgthree), LoadImage, Label (rgthree), MarkdownNote, ModelPreviewOverrideKJ, BasicScheduler, Label (rgthree), Label (rgthree), PrimitiveFloat, ResolutionSelector, LoadImage, SpectrumApplyMiniMaxH3, Fast Groups Bypasser (rgthree), RTXVideoSuperResolution, MarkdownNote, LoadImage, UNETLoader, LTX_lora_loader, PrimitiveStringMultiline, LoraLoaderModelOnly, Label (rgthree)]
patterns: []
missing: []
---

# 视频生成/文生视频/minimaxH3UltraFastestTrue4_v80LightningSpeed_2098097827569295361.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/minimaxH3UltraFastestTrue4_v80LightningSpeed_2098097827569295361.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（95 个）：
- `CreateVideo`
- `BasicGuider`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `MiniMaxH3SigmaShift`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `VAEDecode` ★核心
- `Label (rgthree)`
- `VAEDecodeAudio` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `ModelAttentionBackend`
- `Label (rgthree)`
- `Label (rgthree)`
- `LoadAudio`
- `Label (rgthree)`
- `LoadImage`
- `LoadImage`
- `RandomNoise`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `MarkdownNote`
- `MarkdownNote`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `MiniMaxH3ReferenceToVideo`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `MarkdownNote`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `VHS_LoadVideo`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `LoadImage`
- `SaveVideo`
- `Label (rgthree)`
- `Label (rgthree)`
- `MarkdownNote`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `Label (rgthree)`
- `MarkdownNote`
- `Label (rgthree)`
- `Label (rgthree)`
- `LoadImage`
- `Label (rgthree)`
- `MarkdownNote`
- `ModelPreviewOverrideKJ`
- `BasicScheduler`
- `Label (rgthree)`
- `Label (rgthree)`
- `PrimitiveFloat`
- `ResolutionSelector`
- `LoadImage`
- `SpectrumApplyMiniMaxH3`
- `Fast Groups Bypasser (rgthree)`
- `RTXVideoSuperResolution`
- `MarkdownNote`
- `LoadImage`
- `UNETLoader` ★核心
- `LTX_lora_loader`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `Label (rgthree)`

## 知识

覆盖率 **87%**（83/95）

**有卡**：`CreateVideo`、`BasicGuider`、`ComfyMathExpression`、`MiniMaxH3SigmaShift`、`Label (rgthree)`、`VAEDecode`、`VAEDecodeAudio`、`ModelAttentionBackend`、`LoadAudio`、`LoadImage`、`RandomNoise`、`MiniMaxH3ReferenceToVideo`、`VHS_LoadVideo`、`SaveVideo`、`VAELoader`、`CLIPLoader`、`KSamplerSelect`、`SamplerCustomAdvanced`、`ModelPreviewOverrideKJ`、`BasicScheduler`、`ResolutionSelector`、`SpectrumApplyMiniMaxH3`、`RTXVideoSuperResolution`、`UNETLoader`、`LTX_lora_loader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
