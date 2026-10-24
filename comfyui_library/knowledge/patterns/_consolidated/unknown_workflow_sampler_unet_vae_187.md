---
name: unknown_workflow_sampler_unet_vae_187
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.897
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, SaveImageAdvanced, Text, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen Image2.1文生图_2103745897376079874.json, 图片生成/图生图/【开源】Qwen image 2.1 图片编辑_2102011288636452865.json, 图片生成/文生图/Qwen Image2.1文生图_2101668523557875714.json, 图片生成/文生图/Qwen Image2.1文生图_2101858341764034561.json, 图片生成/文生图/Qwen Image2.1文生图_2107782937193308162.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_187

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image2.1文生图_2103745897376079874.json、图片生成/图生图/【开源】Qwen image 2.1 图片编辑_2102011288636452865.json、图片生成/文生图/Qwen Image2.1文生图_2101668523557875714.json、图片生成/文生图/Qwen Image2.1文生图_2101858341764034561.json、图片生成/文生图/Qwen Image2.1文生图_2107782937193308162.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `SaveImageAdvanced`
- `Text`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JsonExtractString` —— 4/5 个有
- `PreviewAny` —— 4/5 个有
- `RegexExtract` —— 4/5 个有
- `StringCompare` —— 4/5 个有
- `TextGenerate` —— 4/5 个有
- `LoadImage` —— 2/5 个有
- `BatchImagesNode` —— 1/5 个有
- `TextGenerateLTX2Prompt` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 40 | 25 - 40 | 5 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 25 - 40，5 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
