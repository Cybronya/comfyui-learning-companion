---
name: unknown_workflow_sampler_clip_unet_227
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.806
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, KSamplerSelect, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Ideogram4（无审查版）_2071111233360715777.json, 图片生成/文生图/电商模特 最强本地文生图  养生 保健 模特 生成_2065154118913716226.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_227

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Ideogram4（无审查版）_2071111233360715777.json、图片生成/文生图/电商模特 最强本地文生图  养生 保健 模特 生成_2065154118913716226.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGOverride`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualModelGuider`
- `EmptyFlux2LatentImage`
- `Ideogram4Scheduler`
- `KSamplerSelect`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
