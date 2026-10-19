---
name: unknown_workflow_sampler_unet_vae_127
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7812
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, PreviewAny, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen Image2.1文生图_2103745897376079874.json, 图片生成/文生图/(V2)-qwen-image2.1-文生图_2102577741005676545.json, 图片生成/文生图/QWEN IMAGE 2.1 文生图，带提示词增强_2103073606212341761.json, 图片生成/文生图/Qwen Image2.1文生图_2103745897376079874.json, 图片生成/文生图/Qwen-image2.1-文生图+提示词增强_2103929675339886594.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_127

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image2.1文生图_2103745897376079874.json、图片生成/文生图/(V2)-qwen-image2.1-文生图_2102577741005676545.json、图片生成/文生图/QWEN IMAGE 2.1 文生图，带提示词增强_2103073606212341761.json、图片生成/文生图/Qwen Image2.1文生图_2103745897376079874.json、图片生成/文生图/Qwen-image2.1-文生图+提示词增强_2103929675339886594.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `PreviewAny`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `SaveImageAdvanced` —— 4/5 个有
- `TextGenerate` —— 4/5 个有
- `JsonExtractString` —— 3/5 个有
- `PrimitiveStringMultiline` —— 3/5 个有
- `RegexExtract` —— 3/5 个有
- `StringCompare` —— 2/5 个有
- `StringConcatenate` —— 2/5 个有
- `Text` —— 2/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `ModelAttentionBackend` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `SeedNode` —— 1/5 个有
- `TextGenerateLTX2Prompt` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1080 | 5 | 98% |
| 高度 | 1024 | 1024 - 1920 | 5 | 70% |
| 采样步数 | 25 | 8 - 40 | 5 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1080，5 个样本，取值集中（一致性 98%）
- 高度 中位数 1024，观测区间 1024 - 1920，5 个样本
- 采样步数 中位数 25，观测区间 8 - 40，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
