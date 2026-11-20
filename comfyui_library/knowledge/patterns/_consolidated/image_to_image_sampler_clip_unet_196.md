---
name: image_to_image_sampler_clip_unet_196
type: Image To Image
frequency: 3
level: strong
coverage: 0.808333
common_nodes: [AddLabel, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, ImagesConcanateToGrid, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, PreviewAny, PreviewImage, PrimitiveFloat, ReferenceLatent, SaveImage, Seed (rgthree), Text, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy batchAnything, easy convertAnything, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/工作流基础系列1.3-Klein单图编辑工作流-Denoise值的影响-使用For循环_2043865301527306241.json, 平台全量/节点系列24-Images Concanate To Grid节点_2030198451295756290.json, 平台全量/节点系列27-CR Text Concatenate文本拼接节点_2044285908324716545.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_196

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/工作流基础系列1.3-Klein单图编辑工作流-Denoise值的影响-使用For循环_2043865301527306241.json、平台全量/节点系列24-Images Concanate To Grid节点_2030198451295756290.json、平台全量/节点系列27-CR Text Concatenate文本拼接节点_2044285908324716545.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `AddLabel`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `ImagesConcanateToGrid`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveFloat`
- `ReferenceLatent`
- `SaveImage`
- `Seed (rgthree)`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy batchAnything`
- `easy convertAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `SamplerCustomAdvanced` —— 2/3 个有
- `StringConcatenate` —— 2/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `Image Batch` —— 1/3 个有
- `JjkText` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
