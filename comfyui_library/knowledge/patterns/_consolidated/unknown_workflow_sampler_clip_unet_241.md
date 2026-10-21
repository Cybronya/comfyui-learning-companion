---
name: unknown_workflow_sampler_clip_unet_241
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9045
common_nodes: [CFGOverride, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, ConditioningZeroOut, CustomCombo, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, JsonExtractString, KSamplerSelect, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, StringReplace, TTResolutionSelector, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/全民设计师！ideogram4单采工作流！_2064692811697582082.json, 图片生成/文生图/文生图Ideogram4_2080316909521817601.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_241

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/全民设计师！ideogram4单采工作流！_2064692811697582082.json、图片生成/文生图/文生图Ideogram4_2080316909521817601.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGOverride`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `ConditioningZeroOut`
- `CustomCombo`
- `DualModelGuider`
- `EmptyFlux2LatentImage`
- `Ideogram4Scheduler`
- `JsonExtractString`
- `KSamplerSelect`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringReplace`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `CLIPLoaderGGUF` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `Ideogram4DirectJSONBuilderModified` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
