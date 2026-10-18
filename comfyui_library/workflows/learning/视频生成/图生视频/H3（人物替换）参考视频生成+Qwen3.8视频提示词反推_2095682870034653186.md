---
key: 视频生成/图生视频/H3（人物替换）参考视频生成+Qwen3.8视频提示词反推_2095682870034653186.json
name: H3（人物替换）参考视频生成+Qwen3.8视频提示词反推_2095682870034653186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/H3（人物替换）参考视频生成+Qwen3.8视频提示词反推_2095682870034653186.json
hash: 9635021e5d6679e3
coverage: 0.88
learned_at: 2026-10-17 01:09:20
nodes: [SaveImage, LoadImage, LoadImage, VAELoader, ManualSigmas, VAEDecode, VAEDecodeAudio, SplitSigmas, CLIPLoader, ManualSigmas, ManualSigmas, RandomNoise, LTXVSeparateAVLatent, UNETLoader, ShellAgentPluginOutputText, BasicScheduler, BasicGuider, KSamplerSelect, VAELoader, easy showAnything, MiniMaxH3PromptEnhancerT8, BasicGuider, VAEDecode, VAEDecodeAudio, LoadVideo, PrimitiveFloat, MarkdownNote, MuyeTextEditOutput, ModelPreviewOverrideKJ, SamplerCustomAdvanced, MinimaxH3LatentUpscaler3D, LTXVConcatAVLatent, SamplerCustomAdvanced, VHS_VideoCombine, Label (rgthree), ComfyMathExpression, PreviewAny, MiniMaxH3ReferenceToVideo, ResolutionSelector, ImageResizeKJv2, PrimitiveStringMultiline, MarkdownNote, VHS_LoadVideo, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Float to Int, MiniMaxH3SigmaShift, ModelAttentionBackend]
patterns: []
missing: []
---

# 视频生成/图生视频/H3（人物替换）参考视频生成+Qwen3.8视频提示词反推_2095682870034653186.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/H3（人物替换）参考视频生成+Qwen3.8视频提示词反推_2095682870034653186.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `ManualSigmas`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SplitSigmas`
- `CLIPLoader`
- `ManualSigmas`
- `ManualSigmas`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `UNETLoader` ★核心
- `ShellAgentPluginOutputText`
- `BasicScheduler`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAELoader`
- `easy showAnything`
- `MiniMaxH3PromptEnhancerT8`
- `BasicGuider`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `LoadVideo`
- `PrimitiveFloat`
- `MarkdownNote`
- `MuyeTextEditOutput`
- `ModelPreviewOverrideKJ`
- `SamplerCustomAdvanced` ★核心
- `MinimaxH3LatentUpscaler3D`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `Label (rgthree)`
- `ComfyMathExpression`
- `PreviewAny`
- `MiniMaxH3ReferenceToVideo`
- `ResolutionSelector`
- `ImageResizeKJv2`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `VHS_LoadVideo`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Float to Int`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`

## 知识

覆盖率 **88%**（44/50）

**有卡**：`SaveImage`、`LoadImage`、`VAELoader`、`ManualSigmas`、`VAEDecode`、`VAEDecodeAudio`、`SplitSigmas`、`CLIPLoader`、`RandomNoise`、`LTXVSeparateAVLatent`、`UNETLoader`、`ShellAgentPluginOutputText`、`BasicScheduler`、`BasicGuider`、`KSamplerSelect`、`MiniMaxH3PromptEnhancerT8`、`LoadVideo`、`MuyeTextEditOutput`、`ModelPreviewOverrideKJ`、`SamplerCustomAdvanced`、`MinimaxH3LatentUpscaler3D`、`LTXVConcatAVLatent`、`VHS_VideoCombine`、`Label (rgthree)`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`ResolutionSelector`、`ImageResizeKJv2`、`VHS_LoadVideo`、`Float to Int`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、SaveImage、LoadImage、UNETLoader、KSamplerSelect
