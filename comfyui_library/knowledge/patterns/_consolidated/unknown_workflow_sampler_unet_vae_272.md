---
name: unknown_workflow_sampler_unet_vae_272
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.782667
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen image2.1 文生图_2099195780748890113.json, 图片生成/文生图/Qwen2.1文生图_2102393926710816769.json, 图片生成/文生图/[Qwen Image 2.1] 极简提示词自然街拍生成 _ 随性抓拍 _ 日系胶片 _ 街拍 __2105186958128533506.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_272

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen image2.1 文生图_2099195780748890113.json、图片生成/文生图/Qwen2.1文生图_2102393926710816769.json、图片生成/文生图/[Qwen Image 2.1] 极简提示词自然街拍生成 _ 随性抓拍 _ 日系胶片 _ 街拍 __2105186958128533506.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
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
- `Anything Everywhere3` —— 2/3 个有
- `QwenImage21Cache` —— 2/3 个有
- `RHLLMChatNode` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `JjkText` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `Text` —— 1/3 个有
- `TextGenerateLTX2Prompt` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 25 | 25 - 40 | 3 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 40，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
