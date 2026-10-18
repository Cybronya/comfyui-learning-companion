---
key: 视频生成/图生视频/(Singularity+Vdn文戏版)MiniMax H3单采极速参考生视频V2_2096495207192809474.json
name: (Singularity+Vdn文戏版)MiniMax H3单采极速参考生视频V2_2096495207192809474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(Singularity+Vdn文戏版)MiniMax H3单采极速参考生视频V2_2096495207192809474.json
hash: b28be2e6a93e46cd
coverage: 0.9
learned_at: 2026-10-17 01:09:11
nodes: [VAELoader, VAELoader, BasicGuider, RandomNoise, MarkdownNote, PrimitiveFloat, ComfyMathExpression, CLIPLoader, LoadImage, MiniMaxH3AudioConditioningT8, MiniMaxH3AVDecodeT8, SolAttnMiniMax, MiniMaxH3VDNExecutionPlanT8Advanced, CreateVideo, UNETLoader, SaveVideo, ResolutionSelector, MiniMaxH3VDNModelComposerT8Advanced, SamplerCustomAdvanced, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/(Singularity+Vdn文戏版)MiniMax H3单采极速参考生视频V2_2096495207192809474.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/(Singularity+Vdn文戏版)MiniMax H3单采极速参考生视频V2_2096495207192809474.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Output → Other

**节点**（20 个）：
- `VAELoader`
- `VAELoader`
- `BasicGuider`
- `RandomNoise`
- `MarkdownNote`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `CLIPLoader`
- `LoadImage`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3AVDecodeT8`
- `SolAttnMiniMax`
- `MiniMaxH3VDNExecutionPlanT8Advanced`
- `CreateVideo`
- `UNETLoader` ★核心
- `SaveVideo`
- `ResolutionSelector`
- `MiniMaxH3VDNModelComposerT8Advanced`
- `SamplerCustomAdvanced` ★核心
- `CR Prompt Text`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`VAELoader`、`BasicGuider`、`RandomNoise`、`ComfyMathExpression`、`CLIPLoader`、`LoadImage`、`MiniMaxH3AudioConditioningT8`、`MiniMaxH3AVDecodeT8`、`SolAttnMiniMax`、`MiniMaxH3VDNExecutionPlanT8Advanced`、`CreateVideo`、`UNETLoader`、`SaveVideo`、`ResolutionSelector`、`MiniMaxH3VDNModelComposerT8Advanced`、`SamplerCustomAdvanced`、`CR Prompt Text`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3AVDecodeT8、MiniMaxH3AudioConditioningT8
