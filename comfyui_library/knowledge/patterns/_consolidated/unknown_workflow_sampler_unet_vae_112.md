---
name: unknown_workflow_sampler_unet_vae_112
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.575167
common_nodes: [CLIPLoader, EmptyLatentImage, FastGroupsBypassSwitch, GetNode, JjkText, KSampler, LoadImage, PreviewImage, QwenImage21Cache, ResolutionSelector, SaveImage, SetNode, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/2102200839111790594.json, 图片生成/图生图/2102202740012306433.json, 数字人/数字人/Qwen2.1   图像编辑_2101937485273194498.json, 数字人/数字人/千问2.1！ 多图像编辑！ 提示词自动优化！_2101851811295612929.json, 视频生成/图生视频/抠图，透明背景，Qwen2.1！_2104061025187356673.json, 视频生成/图生视频/透明背景抠图！Qwen2.1_2104454506997174273.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_112

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/2102200839111790594.json、图片生成/图生图/2102202740012306433.json、数字人/数字人/Qwen2.1   图像编辑_2101937485273194498.json、数字人/数字人/千问2.1！ 多图像编辑！ 提示词自动优化！_2101851811295612929.json、视频生成/图生视频/抠图，透明背景，Qwen2.1！_2104061025187356673.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `FastGroupsBypassSwitch`
- `GetNode`
- `JjkText`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `TextCombinerTwo` —— 4/6 个有
- `GH_ImageVideoComparer` —— 3/6 个有
- `BatchImagesNode` —— 2/6 个有
- `EmptyImage` —— 2/6 个有
- `QwenPERewriteT8` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |
| 采样步数 | 45 | 45 - 50 | 6 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 45，观测区间 45 - 50，6 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
