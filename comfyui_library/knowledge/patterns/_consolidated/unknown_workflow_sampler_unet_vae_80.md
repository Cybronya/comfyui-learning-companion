---
name: unknown_workflow_sampler_unet_vae_80
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.783556
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen Image2.1文生图_2103745897376079874.json, 图片生成/文生图/(V2)-qwen-image2.1-文生图_2102577741005676545.json, 图片生成/文生图/QWEN IMAGE 2.1 文生图，带提示词增强_2103073606212341761.json, 图片生成/文生图/Qwen Image2.1 全能_2101873993291751425.json, 图片生成/文生图/Qwen Image2.1文生图_2101668523557875714.json, 图片生成/文生图/Qwen Image2.1文生图_2101858341764034561.json, 图片生成/文生图/Qwen Image2.1文生图_2103745897376079874.json, 图片生成/文生图/Qwen Image2.1文生图_2107782937193308162.json, 数字人/数字人/Qwen Image2.1 全能_2102320159447937026.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_80

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image2.1文生图_2103745897376079874.json、图片生成/文生图/(V2)-qwen-image2.1-文生图_2102577741005676545.json、图片生成/文生图/QWEN IMAGE 2.1 文生图，带提示词增强_2103073606212341761.json、图片生成/文生图/Qwen Image2.1 全能_2101873993291751425.json、图片生成/文生图/Qwen Image2.1文生图_2101668523557875714.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 8/9 个有
- `RegexExtract` —— 8/9 个有
- `ResolutionSelector` —— 8/9 个有
- `SaveImageAdvanced` —— 8/9 个有
- `TextGenerate` —— 8/9 个有
- `JsonExtractString` —— 7/9 个有
- `PreviewAny` —— 7/9 个有
- `StringCompare` —— 7/9 个有
- `Text` —— 5/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `StringConcatenate` —— 3/9 个有
- `LoadImage` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `PrimitiveBoolean` —— 2/9 个有
- `RegexMatch` —— 2/9 个有
- `ComfyMathExpression` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `TextGenerateLTX2Prompt` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1088 | 9 | 98% |
| 高度 | 1024 | 1024 - 1920 | 9 | 75% |
| 采样步数 | 40 | 25 - 40 | 9 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1088，9 个样本，取值集中（一致性 98%）
- 高度 中位数 1024，观测区间 1024 - 1920，9 个样本
- 采样步数 中位数 40，观测区间 25 - 40，9 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
