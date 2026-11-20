---
name: unknown_workflow_lora_sampler_clip_107
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7768
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, Flux2Scheduler, GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/boogu_image_edit_turbo编辑_2080928439120515074.json, 图片生成/图生图/boogu_image单图编辑局部重绘换装_2096055509886529537.json, 图片生成/图生图/boogu_image单图编辑局部重绘换装_2096164208168751106.json, 图片生成/图生图/flux_2_klein_9b-图生图_2028319139701460993.json, 数字人/数字人/260920 身材优化_2101508683275522049.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_107

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/boogu_image_edit_turbo编辑_2080928439120515074.json、图片生成/图生图/boogu_image单图编辑局部重绘换装_2096055509886529537.json、图片生成/图生图/boogu_image单图编辑局部重绘换装_2096164208168751106.json、图片生成/图生图/flux_2_klein_9b-图生图_2028319139701460993.json、数字人/数字人/260920 身材优化_2101508683275522049.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 4/5 个有
- `EmptyLatentImage` —— 4/5 个有
- `GetImageSize` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `ColorMatchV2` —— 3/5 个有
- `FluxKontextImageScale` —— 3/5 个有
- `ImageScaleBy` —— 3/5 个有
- `TextEncodeBooguEdit` —— 3/5 个有
- `VAEDecodeTiled` —— 3/5 个有
- `easy float` —— 3/5 个有
- `CompressImages` —— 1/5 个有
- `EmptyFlux2LatentImage` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `LayerUtility: TextJoin` —— 1/5 个有
- `SaveText` —— 1/5 个有
- `easy imageScaleDownToSize` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1360 | 4 | 49% |
| 高度 | 512 | 512 - 768 | 4 | 81% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1360，4 个样本，取值分散，一致性仅 49%
- 高度 中位数 512，观测区间 512 - 768，4 个样本，取值集中（一致性 81%）
