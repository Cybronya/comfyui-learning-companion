---
name: unknown_workflow_lora_sampler_clip_111
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.783667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, Flux2Scheduler, GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/boogu_image_edit_turbo编辑_2080928439120515074.json, 图片生成/图生图/boogu_image单图编辑局部重绘换装_2096055509886529537.json, 图片生成/图生图/boogu_image单图编辑局部重绘换装_2096164208168751106.json, 图片生成/图生图/flux_2_klein_9b-图生图_2028319139701460993.json, 平台全量/boogu image edit turbo编辑_2077017630837399553.json, 数字人/数字人/260920 身材优化_2101508683275522049.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_111

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/boogu_image_edit_turbo编辑_2080928439120515074.json、图片生成/图生图/boogu_image单图编辑局部重绘换装_2096055509886529537.json、图片生成/图生图/boogu_image单图编辑局部重绘换装_2096164208168751106.json、图片生成/图生图/flux_2_klein_9b-图生图_2028319139701460993.json、平台全量/boogu image edit turbo编辑_2077017630837399553.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `Flux2Scheduler`
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
- `ConditioningZeroOut` —— 5/6 个有
- `EmptyLatentImage` —— 5/6 个有
- `GetImageSize` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `ColorMatchV2` —— 4/6 个有
- `FluxKontextImageScale` —— 4/6 个有
- `ImageScaleBy` —— 4/6 个有
- `TextEncodeBooguEdit` —— 4/6 个有
- `VAEDecodeTiled` —— 4/6 个有
- `easy float` —— 4/6 个有
- `CompressImages` —— 1/6 个有
- `EmptyFlux2LatentImage` —— 1/6 个有
- `JWInteger` —— 1/6 个有
- `LayerUtility: TextJoin` —— 1/6 个有
- `SaveText` —— 1/6 个有
- `easy imageScaleDownToSize` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1360 | 5 | 50% |
| 高度 | 512 | 512 - 768 | 5 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1360，5 个样本
- 高度 中位数 512，观测区间 512 - 768，5 个样本，取值集中（一致性 82%）
