---
key: 视频生成/图生视频/(Singularity+Vdn+Lightx2v)MiniMax H3单采极速参考生视频V2_2096501713606889473.json
name: (Singularity+Vdn+Lightx2v)MiniMax H3单采极速参考生视频V2_2096501713606889473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(Singularity+Vdn+Lightx2v)MiniMax H3单采极速参考生视频V2_2096501713606889473.json
hash: d1d272f8c54131e0
coverage: 0.933333
learned_at: 2026-10-17 01:09:11
nodes: [VAELoader, VAELoader, BasicGuider, RandomNoise, SamplerCustomAdvanced, PrimitiveFloat, ComfyMathExpression, CLIPLoader, MiniMaxH3AVDecodeT8, SolAttnMiniMax, MiniMaxH3VDNExecutionPlanT8Advanced, CreateVideo, UNETLoader, CR Prompt Text, ResolutionSelector, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveVideo, MiniMaxH3VDNModelComposerT8Advanced, MarkdownNote, LoadImage, MiniMaxH3AudioConditioningT8, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/(Singularity+Vdn+Lightx2v)MiniMax H3单采极速参考生视频V2_2096501713606889473.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/(Singularity+Vdn+Lightx2v)MiniMax H3单采极速参考生视频V2_2096501713606889473.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Output → Other

**节点**（30 个）：
- `VAELoader`
- `VAELoader`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveFloat`
- `ComfyMathExpression`
- `CLIPLoader`
- `MiniMaxH3AVDecodeT8`
- `SolAttnMiniMax`
- `MiniMaxH3VDNExecutionPlanT8Advanced`
- `CreateVideo`
- `UNETLoader` ★核心
- `CR Prompt Text`
- `ResolutionSelector`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveVideo`
- `MiniMaxH3VDNModelComposerT8Advanced`
- `MarkdownNote`
- `LoadImage`
- `MiniMaxH3AudioConditioningT8`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`VAELoader`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`CLIPLoader`、`MiniMaxH3AVDecodeT8`、`SolAttnMiniMax`、`MiniMaxH3VDNExecutionPlanT8Advanced`、`CreateVideo`、`UNETLoader`、`CR Prompt Text`、`ResolutionSelector`、`LoraLoaderModelOnly`、`SaveVideo`、`MiniMaxH3VDNModelComposerT8Advanced`、`LoadImage`、`MiniMaxH3AudioConditioningT8`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3AVDecodeT8
