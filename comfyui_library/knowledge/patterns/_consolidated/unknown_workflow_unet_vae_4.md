---
name: unknown_workflow_unet_vae_4
type: Unknown Workflow
frequency: 14
level: weak
coverage: 0.866714
common_nodes: [CLIPLoader, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/guidao画风-moss_2116143813424148482.json, 图片生成/图生图/多参考图生成图片 1底图-4参考图_2113249722726182913.json, 图片生成/图生图/多参考图生成图片 1底图-5参考图_2112078134458806274.json, 图片生成/图生图/水墨武侠-moss_2115319736803352578.json, 图片生成/文生图/ERNIE-Image-Turbo文生图，测试用，感觉效果一般般_2046403986416214017.json, 图片生成/文生图/ERNIE-Image-Turbo（文生图）_2045418640316567553.json, 图片生成/文生图/ERNIE-Image-Turbo（文生图）_2059103096625782786.json, 图片生成/文生图/ERNIE-Image灵韵东方 • 文心一格造像师：定格知识增强的跨模态艺术巅峰_2044349388868292609.json, 图片生成/文生图/Erine Turbo文生图_2044755147204599809.json, 图片生成/文生图/MOSS-8步文生图_2115078986400358401.json, 图片生成/文生图/cos水墨武侠moss_2115245609451089921.json, 图片生成/文生图/ernie+klein双采_2045055189861801985.json, 图片生成/文生图/ernie+zit双采样_2045054582375587842.json, 图片生成/文生图/百度ernie+zit双采样_2045695437658656770.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_4

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/guidao画风-moss_2116143813424148482.json、图片生成/图生图/多参考图生成图片 1底图-4参考图_2113249722726182913.json、图片生成/图生图/多参考图生成图片 1底图-5参考图_2112078134458806274.json、图片生成/图生图/水墨武侠-moss_2115319736803352578.json、图片生成/文生图/ERNIE-Image-Turbo文生图，测试用，感觉效果一般般_2046403986416214017.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 12/14 个有
- `EmptyFlux2LatentImage` —— 12/14 个有
- `KSampler` —— 11/14 个有
- `PreviewImage` —— 11/14 个有
- `ConditioningZeroOut` —— 8/14 个有
- `LoraLoaderModelOnly` —— 8/14 个有
- `LoadImage` —— 6/14 个有
- `CR Text` —— 5/14 个有
- `KSamplerAdvanced` —— 3/14 个有
- `easy imageConcat` —— 3/14 个有
- `ModelSamplingAuraFlow` —— 2/14 个有
- `TextEncodeQwenImage21` —— 2/14 个有
- `VAEEncode` —— 2/14 个有
- `GetNode` —— 1/14 个有
- `INTConstant` —— 1/14 个有
- `RH_LLMAPI_NODE` —— 1/14 个有
- `SetNode` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 25 | 11 | 41% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 14 | 0% |
| 采样算法 | euler | - | 14 | 79% |
| 调度器 | simple | - | 14 | 79% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 25，11 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，14 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，14 个样本，一致性 79%
- 调度器 最常用 simple，14 个样本，一致性 79%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（9/14 个样本）：Steps较低可能导致细节不足
