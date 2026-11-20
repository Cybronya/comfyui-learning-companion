---
name: unknown_workflow_sampler_checkpoint_vae_29
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9125
common_nodes: [Anything Everywhere3, Anything Everywhere?, CheckpointLoaderSimple, EmptyImage, EmptyLatentImage, Fast Bypasser (rgthree), KSampler, LoadImage, Mute / Bypass Repeater (rgthree), SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, WujiCleaner, easy boolean, easy cleanGpuUsed, easy imageSwitch, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【千问Qwen】RapidAIO_图片编辑(I2I)_V19_光天化日_2020687970847690753.json, 图片生成/图生图/【千问Qwen】RapidAIO_图片编辑(I2I)_V23_光天化日_2020767161542778881.json, 图片生成/图生图/【绅士加密】千问Qwen_RapidAIO_图片编辑(I2I)_V19+TTtools_2020842049825673218.json, 图片生成/图生图/【绅士加密】千问Qwen_RapidAIO_图片编辑(I2I)_V23+TTtools_1980527707945615361.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_29

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【千问Qwen】RapidAIO_图片编辑(I2I)_V19_光天化日_2020687970847690753.json、图片生成/图生图/【千问Qwen】RapidAIO_图片编辑(I2I)_V23_光天化日_2020767161542778881.json、图片生成/图生图/【绅士加密】千问Qwen_RapidAIO_图片编辑(I2I)_V19+TTtools_2020842049825673218.json、图片生成/图生图/【绅士加密】千问Qwen_RapidAIO_图片编辑(I2I)_V23+TTtools_1980527707945615361.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere3`
- `Anything Everywhere?`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLatentImage`
- `Fast Bypasser (rgthree)`
- `KSampler`
- `LoadImage`
- `Mute / Bypass Repeater (rgthree)`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `WujiCleaner`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy imageSwitch`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Latent Input Switch` —— 2/4 个有
- `Int` —— 2/4 个有
- `TT_img_enc` —— 2/4 个有
- `easy float` —— 2/4 个有
- `easy getNode` —— 2/4 个有
- `easy imageScaleDownBy` —— 2/4 个有
- `easy imageSize` —— 2/4 个有
- `easy setNode` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 952 | 904 - 1000 | 4 | 95% |
| 高度 | 1100 | 1000 - 1200 | 4 | 91% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | sa_solver | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 952，观测区间 904 - 1000，4 个样本，取值集中（一致性 95%）
- 高度 中位数 1100，观测区间 1000 - 1200，4 个样本，取值集中（一致性 91%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
