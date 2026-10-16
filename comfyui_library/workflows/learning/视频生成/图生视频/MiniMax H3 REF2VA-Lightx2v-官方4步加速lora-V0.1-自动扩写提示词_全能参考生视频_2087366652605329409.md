---
key: 视频生成/图生视频/MiniMax H3 REF2VA-Lightx2v-官方4步加速lora-V0.1-自动扩写提示词_全能参考生视频_2087366652605329409.json
name: MiniMax H3 REF2VA-Lightx2v-官方4步加速lora-V0.1-自动扩写提示词_全能参考生视频_2087366652605329409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 REF2VA-Lightx2v-官方4步加速lora-V0.1-自动扩写提示词_全能参考生视频_2087366652605329409.json
hash: a95632480ef766c4
coverage: 0.8
learned_at: 2026-10-16 21:27:40
nodes: [CLIPLoader, UNETLoader, MathExpression|pysssss, RH_Utils, Text, CR Text Concatenate, CR Text Concatenate, Text, PrimitiveStringMultiline, MultiTextConcatenate, easy showAnything, BasicScheduler, PathchSageAttentionKJ, RandomNoise, BasicGuider, VAELoader, VAELoader, VAEDecode, CreateVideo, SaveVideo, MarkdownNote, LoraLoaderModelOnly, SamplerCustomAdvanced, KSamplerSelect, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, ResolutionSelector, MiniMaxH3ReferenceToVideo, PrimitiveInt, easy showAnything, VAEDecodeAudio, PrimitiveStringMultiline, RH_LLMAPI_Pro_Node]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3 REF2VA-Lightx2v-官方4步加速lora-V0.1-自动扩写提示词_全能参考生视频_2087366652605329409.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 REF2VA-Lightx2v-官方4步加速lora-V0.1-自动扩写提示词_全能参考生视频_2087366652605329409.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（35 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `MathExpression|pysssss`
- `RH_Utils`
- `Text`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `Text`
- `PrimitiveStringMultiline`
- `MultiTextConcatenate`
- `easy showAnything`
- `BasicScheduler`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `BasicGuider`
- `VAELoader`
- `VAELoader`
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveInt`
- `easy showAnything`
- `VAEDecodeAudio` ★核心
- `PrimitiveStringMultiline`
- `RH_LLMAPI_Pro_Node`

## 知识

覆盖率 **80%**（28/35）

**有卡**：`CLIPLoader`、`UNETLoader`、`MathExpression|pysssss`、`RH_Utils`、`Text`、`CR Text Concatenate`、`MultiTextConcatenate`、`BasicScheduler`、`PathchSageAttentionKJ`、`RandomNoise`、`BasicGuider`、`VAELoader`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`LoraLoaderModelOnly`、`SamplerCustomAdvanced`、`KSamplerSelect`、`LoadImage`、`ResolutionSelector`、`MiniMaxH3ReferenceToVideo`、`VAEDecodeAudio`、`RH_LLMAPI_Pro_Node`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
