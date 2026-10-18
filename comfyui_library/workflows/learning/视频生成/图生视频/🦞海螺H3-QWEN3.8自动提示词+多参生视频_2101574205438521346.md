---
key: 视频生成/图生视频/🦞海螺H3-QWEN3.8自动提示词+多参生视频_2101574205438521346.json
name: 🦞海螺H3-QWEN3.8自动提示词+多参生视频_2101574205438521346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/🦞海螺H3-QWEN3.8自动提示词+多参生视频_2101574205438521346.json
hash: 99b7224f56d28cb2
coverage: 0.848485
learned_at: 2026-10-17 02:15:18
nodes: [KSamplerSelect, BasicGuider, RandomNoise, MarkdownNote, BasicScheduler, VAELoader, VAELoader, VAEDecode, SamplerCustomAdvanced, VAEDecodeAudio, CLIPLoader, PrimitiveStringMultiline, UNETLoader, LoadImage, ResolutionSelector, LayerUtility: PurgeVRAM V2, PreviewAny, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, LoadImage, LoadImage, QwenH3PromptLocal, MuyeTextEditOutput, LoadImage, LoadImage, LoadImage, LoadImage, VHS_VideoCombine, PrimitiveStringMultiline, MiniMaxH3ReferenceToVideo, ModelPreviewOverrideKJ, PrimitiveFloat, ComfyMathExpression]
patterns: []
missing: []
---

# 视频生成/图生视频/🦞海螺H3-QWEN3.8自动提示词+多参生视频_2101574205438521346.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/🦞海螺H3-QWEN3.8自动提示词+多参生视频_2101574205438521346.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（33 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `MarkdownNote`
- `BasicScheduler`
- `VAELoader`
- `VAELoader`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeAudio` ★核心
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LoadImage`
- `ResolutionSelector`
- `LayerUtility: PurgeVRAM V2`
- `PreviewAny`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoadImage`
- `LoadImage`
- `QwenH3PromptLocal`
- `MuyeTextEditOutput`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `MiniMaxH3ReferenceToVideo`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `ComfyMathExpression`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`BasicScheduler`、`VAELoader`、`VAEDecode`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`CLIPLoader`、`UNETLoader`、`LoadImage`、`ResolutionSelector`、`LayerUtility: PurgeVRAM V2`、`LoraLoaderModelOnly`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`QwenH3PromptLocal`、`MuyeTextEditOutput`、`VHS_VideoCombine`、`MiniMaxH3ReferenceToVideo`、`ModelPreviewOverrideKJ`、`ComfyMathExpression`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
