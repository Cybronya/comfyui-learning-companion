---
key: 视频生成/图生视频/MiniMax H3 REF2VA-Lightx2v-官方4步加速lora-V0.1-自动扩写提示词_全能参考生视频_2087793588594888705.json
name: MiniMax H3 REF2VA-Lightx2v-官方4步加速lora-V0.1-自动扩写提示词_全能参考生视频_2087793588594888705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 REF2VA-Lightx2v-官方4步加速lora-V0.1-自动扩写提示词_全能参考生视频_2087793588594888705.json
hash: 9f414af66e625991
coverage: 0.815789
learned_at: 2026-10-16 21:27:40
nodes: [CLIPLoader, UNETLoader, MathExpression|pysssss, Text, BasicScheduler, PathchSageAttentionKJ, RandomNoise, BasicGuider, VAELoader, VAELoader, VAEDecode, CreateVideo, SaveVideo, MarkdownNote, LoraLoaderModelOnly, SamplerCustomAdvanced, KSamplerSelect, VAEDecodeAudio, PrimitiveInt, LoadImage, PrimitiveStringMultiline, RH_Utils, CR Text Concatenate, CR Text Concatenate, Text, MultiTextConcatenate, MiniMaxH3ReferenceToVideo, LoadImage, LoadImage, LoadImage, easy showAnything, PrimitiveStringMultiline, easy showAnything, LoadImage, RH_LLMAPI_Pro_Node, LoadAudio, PrimitiveStringMultiline, ResolutionSelector]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3 REF2VA-Lightx2v-官方4步加速lora-V0.1-自动扩写提示词_全能参考生视频_2087793588594888705.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 REF2VA-Lightx2v-官方4步加速lora-V0.1-自动扩写提示词_全能参考生视频_2087793588594888705.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（38 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `MathExpression|pysssss`
- `Text`
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
- `VAEDecodeAudio` ★核心
- `PrimitiveInt`
- `LoadImage`
- `PrimitiveStringMultiline`
- `RH_Utils`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `Text`
- `MultiTextConcatenate`
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `ResolutionSelector`

## 知识

覆盖率 **82%**（31/38）

**有卡**：`CLIPLoader`、`UNETLoader`、`MathExpression|pysssss`、`Text`、`BasicScheduler`、`PathchSageAttentionKJ`、`RandomNoise`、`BasicGuider`、`VAELoader`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`LoraLoaderModelOnly`、`SamplerCustomAdvanced`、`KSamplerSelect`、`VAEDecodeAudio`、`LoadImage`、`RH_Utils`、`CR Text Concatenate`、`MultiTextConcatenate`、`MiniMaxH3ReferenceToVideo`、`RH_LLMAPI_Pro_Node`、`LoadAudio`、`ResolutionSelector`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
