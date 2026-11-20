---
name: unknown_workflow_lora_sampler_unet_256
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.886
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/refMod 8视角视图生成_2111837385603510274.json, 图片生成/文生图/Qwen-image2.1文生图3D国漫CG风格_2112960915317547010.json, 图片生成/文生图/Qwen-image2.1文生图赛璐璐平涂动漫风格_2112971703084208130.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_256

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/refMod 8视角视图生成_2111837385603510274.json、图片生成/文生图/Qwen-image2.1文生图3D国漫CG风格_2112960915317547010.json、图片生成/文生图/Qwen-image2.1文生图赛璐璐平涂动漫风格_2112971703084208130.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `easy promptLine` —— 1/3 个有
- `easy setNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1152 | 1024 - 1152 | 3 | 95% |
| 高度 | 2048 | 1024 - 2048 | 3 | 72% |
| 采样步数 | 9 | 9 - 25 | 3 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_cfg_pp | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1152，观测区间 1024 - 1152，3 个样本，取值集中（一致性 95%）
- 高度 中位数 2048，观测区间 1024 - 2048，3 个样本
- 采样步数 中位数 9，观测区间 9 - 25，3 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_cfg_pp，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
