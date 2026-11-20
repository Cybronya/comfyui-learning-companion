---
name: unknown_workflow_video_lora_sampler_767
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.85975
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/角色PV动画制作_2096613890909102081.json, 视频生成/图生视频/速享minimaxh3 pika_2116488588115406850.json, 视频生成/图生视频/速享minimaxh3_pika_2116670120620814337.json, 视频生成/图生视频/速享minimaxh3_pika_2116681952676900866.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_767

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/角色PV动画制作_2096613890909102081.json、视频生成/图生视频/速享minimaxh3 pika_2116488588115406850.json、视频生成/图生视频/速享minimaxh3_pika_2116670120620814337.json、视频生成/图生视频/速享minimaxh3_pika_2116681952676900866.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ManualSigmas` —— 3/4 个有
- `BasicScheduler` —— 1/4 个有
- `H3SigmaRefiner` —— 1/4 个有
- `JsonExtractString` —— 1/4 个有
- `MiniMaxH3SigmaShift` —— 1/4 个有
- `RegexReplace` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `SolAttnPatch` —— 1/4 个有
- `StringConcatenate` —— 1/4 个有
- `TextGenerate` —— 1/4 个有
- `easy convertAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
