---
name: unknown_workflow_lora_sampler_clip_97
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7345
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [LayerMask: BiRefNetUltra, LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/图生图/2089629118886404097.json, 数字人/数字人/260920 身材优化_2101508683275522049.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_97

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2089629118886404097.json、数字人/数字人/260920 身材优化_2101508683275522049.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `CompressImages` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `LayerMask: BiRefNetUltra` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SaveText` —— 1/2 个有
- `easy imageScaleDownToSize` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerMask: BiRefNetUltra、LayerUtility: ImageScaleByAspectRatio V2
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
