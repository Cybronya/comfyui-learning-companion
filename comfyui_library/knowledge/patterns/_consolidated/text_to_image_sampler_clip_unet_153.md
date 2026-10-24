---
name: text_to_image_sampler_clip_unet_153
type: Text To Image
frequency: 4
level: moderate
coverage: 0.9075
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MossImage文生分镜图生成工作流V1.0_2112470399945625601.json, 图片生成/文生图/Z-Image-Turbo 浮云2.3_2018528654661263361.json, 图片生成/文生图/boogu 文生图工作流_2072977078944886785.json, 图片生成/文生图/布谷boogu_image_turbo文生图_2074490110728560642.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_153

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/MossImage文生分镜图生成工作流V1.0_2112470399945625601.json、图片生成/文生图/Z-Image-Turbo 浮云2.3_2018528654661263361.json、图片生成/文生图/boogu 文生图工作流_2072977078944886785.json、图片生成/文生图/布谷boogu_image_turbo文生图_2074490110728560642.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `ImageStitch` —— 1/4 个有
- `MOSSImagePromptEnhancerT8` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1080 | 4 | 75% |
| 高度 | 1024 | 512 - 1920 | 4 | 55% |
| 采样步数 | 6 | 4 - 16 | 4 | 39% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 4 | 33% |
| 采样算法 | lcm | - | 4 | 50% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1080，4 个样本
- 高度 中位数 1024，观测区间 512 - 1920，4 个样本
- 采样步数 中位数 6，观测区间 4 - 16，4 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 lcm，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
