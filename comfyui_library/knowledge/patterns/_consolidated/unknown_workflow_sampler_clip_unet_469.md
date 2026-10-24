---
name: unknown_workflow_sampler_clip_unet_469
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.93
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/电商产品场景图生成_2065142735723646978.json, 图片生成/文生图/节点系列05-Seed (rgthree)_2034898646168248322.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_469

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/电商产品场景图生成_2065142735723646978.json、图片生成/文生图/节点系列05-Seed (rgthree)_2034898646168248322.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `Qwen2.5` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `Text` —— 1/2 个有
- `easy convertAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
