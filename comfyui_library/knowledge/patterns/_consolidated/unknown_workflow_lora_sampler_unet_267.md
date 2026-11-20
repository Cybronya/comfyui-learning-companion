---
name: unknown_workflow_lora_sampler_unet_267
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.781333
common_nodes: [CFGNorm, CLIPLoader, Compare, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, ImageConcanate, ImageScaleToTotalPixels, ImpactSwitch, Int, InversionDemoLazySwitch, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, RHHiddenNodes, SaveImage, SetNode, TextEncodeQwenImageEdit, TextInput_, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问鞋模大师 适配电商 效果超越全能图片V1_1971500943906947074.json, 图片生成/图生图/鞋模工作流，适配电商（效果超好）_1989146354058407938.json, 平台全量/千问鞋模大师 适配电商 效果超越全能图片V1_1970926881845481473.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_267

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/千问鞋模大师 适配电商 效果超越全能图片V1_1971500943906947074.json、图片生成/图生图/鞋模工作流，适配电商（效果超好）_1989146354058407938.json、平台全量/千问鞋模大师 适配电商 效果超越全能图片V1_1970926881845481473.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Compare`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `ImpactSwitch`
- `Int`
- `InversionDemoLazySwitch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RHHiddenNodes`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEdit`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1152 | 1152 - 1152 | 3 | 100% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1152，观测区间 1152 - 1152，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
