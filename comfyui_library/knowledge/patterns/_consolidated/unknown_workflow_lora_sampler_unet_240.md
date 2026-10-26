---
name: unknown_workflow_lora_sampler_unet_240
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.751
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen image 2.1海报设计强化LORA｜细节修复｜文字排版优化_2111603744281550850.json, 图片生成/文生图/Qwen-2.1-海报设计_2111467394572046338.json, 图片生成/文生图/Qwen-2.1-海报设计_2114257098417721346.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_240

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen image 2.1海报设计强化LORA｜细节修复｜文字排版优化_2111603744281550850.json、图片生成/文生图/Qwen-2.1-海报设计_2111467394572046338.json、图片生成/文生图/Qwen-2.1-海报设计_2114257098417721346.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Seed` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `LayerUtility: ImageReel` —— 2/3 个有
- `LayerUtility: ImageReelComposit` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `MuyeTextEditOutput` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1920 | 1200 - 1920 | 3 | 80% |
| 高度 | 1080 | 1080 - 1600 | 3 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，观测区间 1200 - 1920，3 个样本
- 高度 中位数 1080，观测区间 1080 - 1600，3 个样本，取值集中（一致性 80%）
