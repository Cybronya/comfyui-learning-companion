---
name: unknown_workflow_lora_sampler_clip_129
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.738
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageScaleDownToSize]
problems: []
missing: []
members: [图片生成/文生图/f2_klein_9b_胸部放大器2.0_2026093999936774146.json, 图片生成/文生图/产品人物换背景光源一致F2-Klein-9B工作流_2084105106571743234.json, 数字人/数字人/260920 身材优化_2101508683275522049.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_129

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/f2_klein_9b_胸部放大器2.0_2026093999936774146.json、图片生成/文生图/产品人物换背景光源一致F2-Klein-9B工作流_2084105106571743234.json、数字人/数字人/260920 身材优化_2101508683275522049.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
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
- `easy imageScaleDownToSize`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `JWInteger` —— 2/3 个有
- `LayerUtility: ImageReel` —— 2/3 个有
- `LayerUtility: ImageReelComposit` —— 2/3 个有
- `CompressImages` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SaveText` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
