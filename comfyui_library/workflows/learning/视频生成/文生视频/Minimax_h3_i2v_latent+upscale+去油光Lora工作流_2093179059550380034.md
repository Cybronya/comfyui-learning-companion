---
key: 视频生成/文生视频/Minimax_h3_i2v_latent+upscale+去油光Lora工作流_2093179059550380034.json
name: Minimax_h3_i2v_latent+upscale+去油光Lora工作流_2093179059550380034
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax_h3_i2v_latent+upscale+去油光Lora工作流_2093179059550380034.json
hash: f5f35fae6290305a
coverage: 0.809524
learned_at: 2026-10-11 21:30:27
nodes: [VAEDecode, ManualSigmas, KSamplerSelect, ManualSigmas, MarkdownNote, BasicGuider, BasicGuider, VAEDecodeAudio, SamplerCustomAdvanced, ComfyMathExpression, ManualSigmas, VHS_VideoCombine, RandomNoise, MiniMaxH3ImageToVideo, SamplerCustomAdvanced, ResolutionSelector, PrimitiveFloat, MarkdownNote, SplitSigmas, BasicScheduler, MiniMaxH3ImageToVideo, LTXVSeparateAVLatent, ModelPreviewOverrideKJ, MarkdownNote, LoraLoaderModelOnly, UNETLoader, PrimitiveStringMultiline, CLIPLoader, VAELoader, VAELoader, ResolutionSelector, PrimitiveFloat, MinimaxH3LatentUpscaler3D, LTXVConcatAVLatent, Note, Label (rgthree), LoadImage, ImageResizeKJv2, VAEDecodeAudio, LoraLoaderModelOnly, MiniMaxH3SigmaShift, ModelAttentionBackend]
patterns: []
missing: [Label (rgthree)]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Minimax_h3_i2v_latent+upscale+去油光Lora工作流_2093179059550380034.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Minimax_h3_i2v_latent+upscale+去油光Lora工作流_2093179059550380034.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（42 个）：
- `VAEDecode` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `MarkdownNote`
- `BasicGuider`
- `BasicGuider`
- `VAEDecodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `ComfyMathExpression`
- `ManualSigmas`
- `VHS_VideoCombine`
- `RandomNoise`
- `MiniMaxH3ImageToVideo`
- `SamplerCustomAdvanced` ★核心
- `ResolutionSelector`
- `PrimitiveFloat`
- `MarkdownNote`
- `SplitSigmas`
- `BasicScheduler`
- `MiniMaxH3ImageToVideo`
- `LTXVSeparateAVLatent`
- `ModelPreviewOverrideKJ`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `ResolutionSelector`
- `PrimitiveFloat`
- `MinimaxH3LatentUpscaler3D`
- `LTXVConcatAVLatent`
- `Note`
- `Label (rgthree)`
- `LoadImage`
- `ImageResizeKJv2`
- `VAEDecodeAudio` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`

## 知识

覆盖率 **81%**（34/42）

**有卡**：`VAEDecode`、`ManualSigmas`、`KSamplerSelect`、`BasicGuider`、`VAEDecodeAudio`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`VHS_VideoCombine`、`RandomNoise`、`MiniMaxH3ImageToVideo`、`ResolutionSelector`、`SplitSigmas`、`BasicScheduler`、`LTXVSeparateAVLatent`、`ModelPreviewOverrideKJ`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`MinimaxH3LatentUpscaler3D`、`LTXVConcatAVLatent`、`LoadImage`、`ImageResizeKJv2`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`

**缺卡**（1）：`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
