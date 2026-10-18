---
key: 视频生成/图生视频/H3多参视频生成+Qwen3.8全自动撰写H3提示词_2095738490674827265.json
name: H3多参视频生成+Qwen3.8全自动撰写H3提示词_2095738490674827265
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/H3多参视频生成+Qwen3.8全自动撰写H3提示词_2095738490674827265.json
hash: b840402232f8c3ee
coverage: 0.906977
learned_at: 2026-10-17 01:09:19
nodes: [SaveImage, VAELoader, ManualSigmas, VAEDecode, VAEDecodeAudio, SplitSigmas, CLIPLoader, ManualSigmas, ManualSigmas, RandomNoise, LTXVSeparateAVLatent, UNETLoader, ShellAgentPluginOutputText, BasicScheduler, BasicGuider, KSamplerSelect, VAELoader, easy showAnything, MiniMaxH3PromptEnhancerT8, BasicGuider, VAEDecode, VAEDecodeAudio, ModelPreviewOverrideKJ, SamplerCustomAdvanced, MinimaxH3LatentUpscaler3D, LTXVConcatAVLatent, SamplerCustomAdvanced, VHS_VideoCombine, ComfyMathExpression, PreviewAny, MiniMaxH3SigmaShift, ModelAttentionBackend, LoadImage, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, Label (rgthree), Label (rgthree), MuyeTextEditOutput, Float to Int, MarkdownNote, ResolutionSelector, Label (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/H3多参视频生成+Qwen3.8全自动撰写H3提示词_2095738490674827265.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/H3多参视频生成+Qwen3.8全自动撰写H3提示词_2095738490674827265.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `SaveImage`
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
- `ModelPreviewOverrideKJ`
- `SamplerCustomAdvanced` ★核心
- `MinimaxH3LatentUpscaler3D`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `ComfyMathExpression`
- `PreviewAny`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `Label (rgthree)`
- `Label (rgthree)`
- `MuyeTextEditOutput`
- `Float to Int`
- `MarkdownNote`
- `ResolutionSelector`
- `Label (rgthree)`

## 知识

覆盖率 **91%**（39/43）

**有卡**：`SaveImage`、`VAELoader`、`ManualSigmas`、`VAEDecode`、`VAEDecodeAudio`、`SplitSigmas`、`CLIPLoader`、`RandomNoise`、`LTXVSeparateAVLatent`、`UNETLoader`、`ShellAgentPluginOutputText`、`BasicScheduler`、`BasicGuider`、`KSamplerSelect`、`MiniMaxH3PromptEnhancerT8`、`ModelPreviewOverrideKJ`、`SamplerCustomAdvanced`、`MinimaxH3LatentUpscaler3D`、`LTXVConcatAVLatent`、`VHS_VideoCombine`、`ComfyMathExpression`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`LoadImage`、`MiniMaxH3ReferenceToVideo`、`Label (rgthree)`、`MuyeTextEditOutput`、`Float to Int`、`ResolutionSelector`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、SaveImage、LoadImage、UNETLoader、KSamplerSelect
