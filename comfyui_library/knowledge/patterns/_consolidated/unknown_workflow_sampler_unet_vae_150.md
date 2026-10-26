---
name: unknown_workflow_sampler_unet_vae_150
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.885857
common_nodes: [CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Magic-Wan2.2-修手工作流_1995477299732656129.json, 图片生成/图生图/Qwen image2.1 加速版换脸_2102901567308521474.json, 图片生成/图生图/Qwen-image2.1 扩图工作流_2108906946001723394.json, 图片生成/图生图/Qwen-image2.1-扩图2.0_2104395498009489409.json, 图片生成/图生图/Qwen-image2.1-扩图工作流_2103452010099073025.json, 图片生成/图生图/Qwen-image2.1-换脸_2102751184430919681.json, 图片生成/图生图/Qwen_image2.1_加速版换脸_2104383930576228354.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_150

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Magic-Wan2.2-修手工作流_1995477299732656129.json、图片生成/图生图/Qwen image2.1 加速版换脸_2102901567308521474.json、图片生成/图生图/Qwen-image2.1 扩图工作流_2108906946001723394.json、图片生成/图生图/Qwen-image2.1-扩图2.0_2104395498009489409.json、图片生成/图生图/Qwen-image2.1-扩图工作流_2103452010099073025.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `TextEncodeQwenImage21` —— 6/7 个有
- `DrawMaskOnImage` —— 5/7 个有
- `MaskFillHoles` —— 4/7 个有
- `CR Prompt Text` —— 3/7 个有
- `ImagePadForOutpaint` —— 3/7 个有
- `CLIPTextEncode` —— 1/7 个有
- `DifferentialDiffusion` —— 1/7 个有
- `EmptyImage` —— 1/7 个有
- `InpaintModelConditioning` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 25 | 7 | 34% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 0.36 - 1 | 7 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 25，7 个样本，取值分散，一致性仅 34%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 0.36 - 1，7 个样本
- 高发问题（4/7 个样本）：Steps较低可能导致细节不足
