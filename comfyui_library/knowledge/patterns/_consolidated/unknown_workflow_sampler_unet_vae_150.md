---
name: unknown_workflow_sampler_unet_vae_150
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6462
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/qwen2.1 文生图_2102025901952299009.json, 图片生成/文生图/qwen2.1文生图_2104275580962304002.json, 图片生成/文生图/千问 qwen image 2.1 单图编辑+全节点注释_2101953275674320897.json, 图片生成/文生图/千问 qwen image 2.1 多图编辑 图片编辑 +全节点注释_2101953245253033985.json, 图片生成/文生图/千问 qwen image 2.1 文生图+全节点注释_2101953220728938497.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_150

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/qwen2.1 文生图_2102025901952299009.json、图片生成/文生图/qwen2.1文生图_2104275580962304002.json、图片生成/文生图/千问 qwen image 2.1 单图编辑+全节点注释_2101953275674320897.json、图片生成/文生图/千问 qwen image 2.1 多图编辑 图片编辑 +全节点注释_2101953245253033985.json、图片生成/文生图/千问 qwen image 2.1 文生图+全节点注释_2101953220728938497.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 4/5 个有
- `QwenImage21Cache` —— 4/5 个有
- `TextGenerateLTX2Prompt` —— 4/5 个有
- `Anything Everywhere3` —— 3/5 个有
- `CR Prompt Text` —— 3/5 个有
- `CR Text` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `BatchImagesNode` —— 1/5 个有
- `RH_LLMAPI_Pro_Node` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1024 | 5 | 89% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 40 | 25 - 50 | 5 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1024，5 个样本，取值集中（一致性 89%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 25 - 50，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
