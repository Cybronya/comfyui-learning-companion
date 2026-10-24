---
name: unknown_workflow_sampler_unet_vae_92
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8389
common_nodes: [CLIPLoader, Easy_QwenEdit2509, FluxKontextMultiReferenceLatentMethod, KSampler, Krea2OstrisEditModelPatch, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2 动漫转真人_2102002514861314049.json, 图片生成/图生图/Krea2-动漫转真人V3_2094037108511035394.json, 图片生成/图生图/Krea2_漫转写实真人V2_2085011207811059713.json, 图片生成/图生图/Krea2_漫转写实真人V2_2085285424783773698.json, 图片生成/图生图/Krea2_漫转写实真人V2_2087387221463748610.json, 图片生成/图生图/Krea2_漫转写实真人V2_2089714152586702849.json, 图片生成/图生图/Krea2_漫转写实真人V3_2091170195137191937.json, 图片生成/图生图/Krea2_漫转写实真人V3_2098921299581161474.json, 图片生成/图生图/Krea2_漫转写实真人V3_2098979826014179329.json, 图片生成/图生图/Krea2_漫转写实真人V3_2099656062805831681.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_92

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Krea2 动漫转真人_2102002514861314049.json、图片生成/图生图/Krea2-动漫转真人V3_2094037108511035394.json、图片生成/图生图/Krea2_漫转写实真人V2_2085011207811059713.json、图片生成/图生图/Krea2_漫转写实真人V2_2085285424783773698.json、图片生成/图生图/Krea2_漫转写实真人V2_2087387221463748610.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `Easy_QwenEdit2509`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `Krea2OstrisEditModelPatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorCorrect` —— 6/10 个有
- `Lora Loader Stack (rgthree)` —— 6/10 个有
- `LoraLoaderModelOnly` —— 4/10 个有
- `EmptyImage` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `Int` —— 2/10 个有
- `CR Prompt Text` —— 1/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有
- `ImageMergeNode` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | beta57 | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 beta57，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
