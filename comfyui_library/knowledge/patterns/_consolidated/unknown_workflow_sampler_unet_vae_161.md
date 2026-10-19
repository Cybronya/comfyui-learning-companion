---
name: unknown_workflow_sampler_unet_vae_161
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.706333
common_nodes: [CLIPLoader, EmptyLatentImage, JjkText, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [Label (rgthree), easy cleanGpuUsed]
members: [图片生成/图生图/2101893576153190401.json, 图片生成/图生图/2101914691361660930.json, 图片生成/图生图/2102229892883640321.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_161

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2101893576153190401.json、图片生成/图生图/2101914691361660930.json、图片生成/图生图/2102229892883640321.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `MultiTextConcatenate` —— 1/3 个有
- `QwenImage21PromptEnhancerT8` —— 1/3 个有
- `SaveImageAdvanced` —— 1/3 个有
- `TextCombinerTwo` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 25 - 50 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 25 - 50，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)、easy cleanGpuUsed
