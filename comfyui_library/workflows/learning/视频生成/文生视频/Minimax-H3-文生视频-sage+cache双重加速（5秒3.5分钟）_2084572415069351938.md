---
key: 视频生成/文生视频/Minimax-H3-文生视频-sage+cache双重加速（5秒3.5分钟）_2084572415069351938.json
name: Minimax-H3-文生视频-sage+cache双重加速（5秒3.5分钟）_2084572415069351938
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax-H3-文生视频-sage+cache双重加速（5秒3.5分钟）_2084572415069351938.json
hash: c3f8aafa6b185340
coverage: 0.863636
learned_at: 2026-10-15 22:46:41
nodes: [VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, BasicGuider, ResolutionSelector, PathchSageAttentionKJ, EasyCache, CLIPLoader, VAELoader, VAELoader, ComfyMathExpression, SamplerCustomAdvanced, RandomNoise, UNETLoader, MiniMaxH3ImageToVideo, SaveVideo, PrimitiveFloat, PrimitiveFloat, CreateVideo, CR Prompt Text, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/文生视频/Minimax-H3-文生视频-sage+cache双重加速（5秒3.5分钟）_2084572415069351938.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Minimax-H3-文生视频-sage+cache双重加速（5秒3.5分钟）_2084572415069351938.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（22 个）：
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `ResolutionSelector`
- `PathchSageAttentionKJ`
- `EasyCache`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `UNETLoader` ★核心
- `MiniMaxH3ImageToVideo`
- `SaveVideo`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `CreateVideo`
- `CR Prompt Text`
- `MarkdownNote`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`ResolutionSelector`、`PathchSageAttentionKJ`、`EasyCache`、`CLIPLoader`、`VAELoader`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`RandomNoise`、`UNETLoader`、`MiniMaxH3ImageToVideo`、`SaveVideo`、`CreateVideo`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio
