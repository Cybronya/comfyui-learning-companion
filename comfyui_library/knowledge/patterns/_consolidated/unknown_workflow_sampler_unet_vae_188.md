---
name: unknown_workflow_sampler_unet_vae_188
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.823333
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/【API】Qwen-Image2.1文生图（提示词反推）_2111987215688622081.json, 图片生成/文生图/千问2.1！ 文生图！ 提示词自动优化！_2103393990568660994.json, 数字人/数字人/Qwen2.1- 文生图_2101941309354364929.json, 数字人/数字人/千问2.1！ 文生图！ 提示词自动优化！_2101851079326658561.json, 视频生成/文生视频/Qwen_Image_2.1_PE_文生图_2104447077903323137.json, 视频生成/文生视频/Qwen_Image_2.1_文生图-PE版_2106926003867185154.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_188

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/【API】Qwen-Image2.1文生图（提示词反推）_2111987215688622081.json、图片生成/文生图/千问2.1！ 文生图！ 提示词自动优化！_2103393990568660994.json、数字人/数字人/Qwen2.1- 文生图_2101941309354364929.json、数字人/数字人/千问2.1！ 文生图！ 提示词自动优化！_2101851079326658561.json、视频生成/文生视频/Qwen_Image_2.1_PE_文生图_2104447077903323137.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `TextGenerateLTX2Prompt` —— 4/6 个有
- `CR Prompt Text` —— 3/6 个有
- `FastGroupsBypassSwitch` —— 3/6 个有
- `JjkText` —— 3/6 个有
- `QwenImage21Cache` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `ComfySwitchNode` —— 2/6 个有
- `EmptyImage` —— 2/6 个有
- `QwenPERewriteT8` —— 2/6 个有
- `PlaySound|pysssss` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |
| 采样步数 | 45 | 40 - 50 | 6 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 45，观测区间 40 - 50，6 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
