---
name: text_to_image_sampler_clip_unet_133
type: Text To Image
frequency: 6
level: weak
coverage: 0.882167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image文生图+FlashVSR超清放大-简单直观方便新手研究学习_1996121050985512961.json, 图片生成/文生图/z-image文生图_2094325413752426498.json, 图片生成/文生图/【老金驿站】Anima二次元专属出图工作流_2019258717857914882.json, 图片生成/文生图/千问qwen-image-2.1文生图工作流_2104553799485583362.json, 图片生成/文生图/千问qwen-image-2.1文生图工作流（不可商用）_2101941085793771521.json, 图片生成/文生图/千问文生图-加速高清放大_1988478559381577729.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_133

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/z-image文生图+FlashVSR超清放大-简单直观方便新手研究学习_1996121050985512961.json、图片生成/文生图/z-image文生图_2094325413752426498.json、图片生成/文生图/【老金驿站】Anima二次元专属出图工作流_2019258717857914882.json、图片生成/文生图/千问qwen-image-2.1文生图工作流_2104553799485583362.json、图片生成/文生图/千问qwen-image-2.1文生图工作流（不可商用）_2101941085793771521.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `CFGNorm` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `FlashVSRNode` —— 1/6 个有
- `FluxGuidance` —— 1/6 个有
- `ImageScaleBy` —— 1/6 个有
- `Seed Everywhere` —— 1/6 个有
- `VAEEncode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1360 | 896 - 1920 | 6 | 76% |
| 高度 | 1536 | 720 - 1960 | 6 | 66% |
| 采样步数 | 9 | 6 - 30 | 6 | 35% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 25% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 0.35 - 1 | 6 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1360，观测区间 896 - 1920，6 个样本
- 高度 中位数 1536，观测区间 720 - 1960，6 个样本
- 采样步数 中位数 9，观测区间 6 - 30，6 个样本，取值分散，一致性仅 35%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，6 个样本
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
