---
name: unknown_workflow_lora_sampler_unet_186
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7508
common_nodes: [CLIPLoader, ConditioningZeroOut, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/电商模特指定图片换背景FireRed_2029026525802143745.json, 平台全量/电商模特换服装 FireRed_2028291580733427714.json, 平台全量/电商模特换首饰 FireRed 1.1_2034444255673978881.json, 平台全量/电商海报改文字 FireRed_2031561485498982401.json, 数字人/数字人/YJ-APP-FireRed-多图编辑_2034470620423004161.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_186

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/电商模特指定图片换背景FireRed_2029026525802143745.json、平台全量/电商模特换服装 FireRed_2028291580733427714.json、平台全量/电商模特换首饰 FireRed 1.1_2034444255673978881.json、平台全量/电商海报改文字 FireRed_2031561485498982401.json、数字人/数字人/YJ-APP-FireRed-多图编辑_2034470620423004161.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `EmptyLatentImage` —— 1/5 个有
- `FastCanvas` —— 1/5 个有
- `FastCanvasTool` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `Switch` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 5 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1080 | - | 1 | 100% |
| 高度 | 1920 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
