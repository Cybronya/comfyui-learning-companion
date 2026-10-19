---
name: unknown_workflow_sampler_unet_vae_129
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.848
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text Concatenate, easy boolean, easy float, CR Prompt Text]
members: [图片生成/图生图/2102180346572922881.json, 图片生成/图生图/2102282925260759042.json, 图片生成/文生图/BF16小字不崩-Qwen image 2.1图片编辑_2102769559072763906.json, 图片生成/文生图/QWEN-IMAGE-2.1_2104540875895431170.json, 图片生成/文生图/qwen2.1基础工作流  i2v  t2v_2102578292409847810.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_129

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2102180346572922881.json、图片生成/图生图/2102282925260759042.json、图片生成/文生图/BF16小字不崩-Qwen image 2.1图片编辑_2102769559072763906.json、图片生成/文生图/QWEN-IMAGE-2.1_2104540875895431170.json、图片生成/文生图/qwen2.1基础工作流  i2v  t2v_2102578292409847810.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 4/5 个有
- `SaveImageAdvanced` —— 4/5 个有
- `CR Prompt Text` —— 3/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `easy boolean` —— 1/5 个有
- `easy float` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 25 - 50 | 5 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 1024 - 1080 | 5 | 98% |
| 高度 | 1024 | 1024 - 1624 | 5 | 79% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 25 - 50，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1080，5 个样本，取值集中（一致性 98%）
- 高度 中位数 1024，观测区间 1024 - 1624，5 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、easy boolean、easy float、CR Prompt Text
