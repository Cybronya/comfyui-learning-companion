---
name: unknown_workflow_sampler_unet_vae_132
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.57475
common_nodes: [CLIPLoader, EmptyLatentImage, GetNode, KSampler, LoadImage, QwenImage21Cache, SaveImage, SetNode, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问2.1！ 多图像编辑！ 提示词自动优化！_2103396759899828226.json, 图片生成/图生图/抠图，透明背景，Qwen2.1！_2102202740012306433.json, 图片生成/图生图/角色资产四视图极速版Qwen image 2.1 4(8)步加速_2103425351551635458.json, 图片生成/图生图/透明背景抠图！Qwen2.1_2102200839111790594.json, 数字人/数字人/Qwen2.1   图像编辑_2101937485273194498.json, 数字人/数字人/千问2.1！ 多图像编辑！ 提示词自动优化！_2101851811295612929.json, 视频生成/图生视频/抠图，透明背景，Qwen2.1！_2104061025187356673.json, 视频生成/图生视频/透明背景抠图！Qwen2.1_2104454506997174273.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_132

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/千问2.1！ 多图像编辑！ 提示词自动优化！_2103396759899828226.json、图片生成/图生图/抠图，透明背景，Qwen2.1！_2102202740012306433.json、图片生成/图生图/角色资产四视图极速版Qwen image 2.1 4(8)步加速_2103425351551635458.json、图片生成/图生图/透明背景抠图！Qwen2.1_2102200839111790594.json、数字人/数字人/Qwen2.1   图像编辑_2101937485273194498.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：57%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `GetNode`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FastGroupsBypassSwitch` —— 7/8 个有
- `JjkText` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `ResolutionSelector` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `TextCombinerTwo` —— 4/8 个有
- `GH_ImageVideoComparer` —— 3/8 个有
- `QwenPERewriteT8` —— 3/8 个有
- `BatchImagesNode` —— 2/8 个有
- `EmptyImage` —— 2/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 45 | 8 - 50 | 8 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | 1024 - 2048 | 8 | 71% |
| 高度 | 1024 | 1024 - 1280 | 8 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 45，观测区间 8 - 50，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 2048，8 个样本
- 高度 中位数 1024，观测区间 1024 - 1280，8 个样本，取值集中（一致性 92%）
