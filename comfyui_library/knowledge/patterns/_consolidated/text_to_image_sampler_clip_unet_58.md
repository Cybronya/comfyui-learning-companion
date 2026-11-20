---
name: text_to_image_sampler_clip_unet_58
type: Text To Image
frequency: 11
level: moderate
coverage: 0.992455
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image Turbo 文生图_2009309148017598465.json, 图片生成/文生图/Z-Image 超强文生图_1993850615438704641.json, 图片生成/文生图/Z-Image-De文生图(Z-Image脱蒸馏版-效果更好)_1997646136397729793.json, 图片生成/文生图/Z-Image-De文生图_1997873304331517954.json, 图片生成/文生图/Z-Image-Turbo 身材优化+丰满LoRA_2004613231027126274.json, 图片生成/文生图/Z-Image-Turbo文生图标准工作流_2091176473360166914.json, 图片生成/文生图/Z-image turbo基础生图工作流_2028382510350082049.json, 图片生成/文生图/Z-image-文生图（自用测试版）_2052717804557742081.json, 图片生成/文生图/Z-image基础文生图，zimage文生图_1998203845559902209.json, 图片生成/文生图/Z-image文生图_2002645259123322881.json, 图片生成/文生图/Z-image文生图_2003370209052401665.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_58

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Z-Image Turbo 文生图_2009309148017598465.json、图片生成/文生图/Z-Image 超强文生图_1993850615438704641.json、图片生成/文生图/Z-Image-De文生图(Z-Image脱蒸馏版-效果更好)_1997646136397729793.json、图片生成/文生图/Z-Image-De文生图_1997873304331517954.json、图片生成/文生图/Z-Image-Turbo 身材优化+丰满LoRA_2004613231027126274.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 10/11 个有
- `LoraLoaderModelOnly` —— 6/11 个有
- `ModelSamplingAuraFlow` —— 5/11 个有
- `CR SDXL Aspect Ratio` —— 1/11 个有
- `ConditioningNoiseInjection` —— 1/11 个有
- `Float` —— 1/11 个有
- `ResolutionSelector` —— 1/11 个有
- `Textbox` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 20 | 11 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 11 | 67% |
| 采样算法 | euler | - | 11 | 64% |
| 调度器 | simple | - | 11 | 82% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 1200 | 512 - 1920 | 11 | 72% |
| 高度 | 1504 | 512 - 1920 | 11 | 63% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 20，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 64%
- 调度器 最常用 simple，11 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 1200，观测区间 512 - 1920，11 个样本
- 高度 中位数 1504，观测区间 512 - 1920，11 个样本
