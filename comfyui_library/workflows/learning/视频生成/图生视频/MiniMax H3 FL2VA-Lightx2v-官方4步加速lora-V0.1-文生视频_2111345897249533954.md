---
key: 视频生成/图生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-文生视频_2111345897249533954.json
name: MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-文生视频_2111345897249533954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-文生视频_2111345897249533954.json
hash: a5a7662ca7c6498d
coverage: 0.8
learned_at: 2026-10-18 00:43:26
nodes: [KSamplerSelect, SamplerCustomAdvanced, BasicGuider, RandomNoise, VAEDecode, VAEDecodeAudio, MiniMaxH3ImageToVideo, VAELoader, VAELoader, CLIPLoader, UNETLoader, MarkdownNote, LoraLoaderModelOnly, RHMiniMaxH3PromptOptimizerCompact, ComfyMathExpression, StringFunction|pysssss, ResolutionSelector, PrimitiveStringMultiline, PrimitiveFloat, StringFunction|pysssss, easy showAnything, easy showAnything, VHS_VideoCombine, BasicScheduler, PathchSageAttentionKJ]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-文生视频_2111345897249533954.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-文生视频_2111345897249533954.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（25 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `RandomNoise`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `MiniMaxH3ImageToVideo`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `RHMiniMaxH3PromptOptimizerCompact`
- `ComfyMathExpression`
- `StringFunction|pysssss`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `StringFunction|pysssss`
- `easy showAnything`
- `easy showAnything`
- `VHS_VideoCombine`
- `BasicScheduler`
- `PathchSageAttentionKJ`

## 知识

覆盖率 **80%**（20/25）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicGuider`、`RandomNoise`、`VAEDecode`、`VAEDecodeAudio`、`MiniMaxH3ImageToVideo`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`RHMiniMaxH3PromptOptimizerCompact`、`ComfyMathExpression`、`StringFunction|pysssss`、`ResolutionSelector`、`VHS_VideoCombine`、`BasicScheduler`、`PathchSageAttentionKJ`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
