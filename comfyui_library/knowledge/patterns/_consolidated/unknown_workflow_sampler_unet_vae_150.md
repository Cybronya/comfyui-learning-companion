---
name: unknown_workflow_sampler_unet_vae_150
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.7725
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [easy int, CR Seed]
members: [图片生成/图生图/2102372164333821954.json, 图片生成/文生图/Qwen-Image 2.1｜5倍加速全能工作流_2102372164333821954.json, 图片生成/文生图/qwen+image+2.1多图编辑_2102637659226206209.json, 数字人/数字人/Qwen Image 2.1 图像编辑 Image Edit_2101822303028989953.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_150

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2102372164333821954.json、图片生成/文生图/Qwen-Image 2.1｜5倍加速全能工作流_2102372164333821954.json、图片生成/文生图/qwen+image+2.1多图编辑_2102637659226206209.json、数字人/数字人/Qwen Image 2.1 图像编辑 Image Edit_2101822303028989953.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 3/4 个有
- `BatchImagesNode` —— 2/4 个有
- `CR Seed` —— 2/4 个有
- `DrawMaskOnImage` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `easy int` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `SaveImageAdvanced` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 16.5 | 8 - 25 | 4 | 48% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 16.5，观测区间 8 - 25，4 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy int、CR Seed
