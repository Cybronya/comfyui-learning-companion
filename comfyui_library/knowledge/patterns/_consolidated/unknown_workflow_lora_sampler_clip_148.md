---
name: unknown_workflow_lora_sampler_clip_148
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.854
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, FluxKVCache, GetNode, Image Comparer (rgthree), LayerUtility: ImageMaskScaleAs, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SZ_KleinTiledKSampler, SaveImage, SetNode, UNETLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy imageColorMatch, easy int]
problems: []
missing: []
members: [图片生成/图生图/图片涂抹感类细节重建高清放大-Flux2_Klein9B_2096505608341118977.json, 图片生成/图生图/图片涂抹感类细节重建高清放大-Flux2_Klein9B_2096812736561897473.json, 平台全量/Klein-涂抹感类高清放大-转载B站山竹老师_2053668433438490625.json, 平台全量/图片涂抹感类细节重建高清放大-Flux2 Klein9B_2061272156746637313.json, 平台全量/最强图像超清修复-版本答案-Flux.2-klein_2059874023806427138.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_148

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/图片涂抹感类细节重建高清放大-Flux2_Klein9B_2096505608341118977.json、图片生成/图生图/图片涂抹感类细节重建高清放大-Flux2_Klein9B_2096812736561897473.json、平台全量/Klein-涂抹感类高清放大-转载B站山竹老师_2053668433438490625.json、平台全量/图片涂抹感类细节重建高清放大-Flux2 Klein9B_2061272156746637313.json、平台全量/最强图像超清修复-版本答案-Flux.2-klein_2059874023806427138.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxKVCache`
- `GetNode`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SZ_KleinTiledKSampler`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy imageColorMatch`
- `easy int`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
