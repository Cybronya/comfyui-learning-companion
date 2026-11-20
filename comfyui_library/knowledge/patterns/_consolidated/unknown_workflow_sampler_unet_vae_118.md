---
name: unknown_workflow_sampler_unet_vae_118
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8701
common_nodes: [CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image2.1 加速版换脸_2102901567308521474.json, 图片生成/图生图/Qwen-image2.1 扩图工作流_2108906946001723394.json, 图片生成/图生图/Qwen-image2.1-万物移除工作流_2103849501856456706.json, 图片生成/图生图/Qwen-image2.1-万物移除工作流_2105587801839464450.json, 图片生成/图生图/Qwen-image2.1-万物移除工作流_2108374498859896834.json, 图片生成/图生图/Qwen-image2.1-扩图2.0_2104395498009489409.json, 图片生成/图生图/Qwen-image2.1-扩图工作流_2103452010099073025.json, 图片生成/图生图/Qwen-image2.1-换脸_2102751184430919681.json, 图片生成/图生图/Qwen_image2.1_加速版换脸_2104383930576228354.json, 平台全量/Qwen-image2.1-万物移除_2105640398470336514.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_118

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen image2.1 加速版换脸_2102901567308521474.json、图片生成/图生图/Qwen-image2.1 扩图工作流_2108906946001723394.json、图片生成/图生图/Qwen-image2.1-万物移除工作流_2103849501856456706.json、图片生成/图生图/Qwen-image2.1-万物移除工作流_2105587801839464450.json、图片生成/图生图/Qwen-image2.1-万物移除工作流_2108374498859896834.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DrawMaskOnImage` —— 9/10 个有
- `CR Prompt Text` —— 7/10 个有
- `LoraLoaderModelOnly` —— 5/10 个有
- `CR Text` —— 4/10 个有
- `Int` —— 4/10 个有
- `Mask Fill Holes` —— 4/10 个有
- `ImagePadForOutpaint` —— 3/10 个有
- `MaskFillHoles` —— 3/10 个有
- `EmptyImage` —— 1/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 6 - 25 | 10 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 6 - 25，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
