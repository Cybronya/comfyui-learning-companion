---
name: unknown_workflow_sampler_clip_unet_82
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.9345
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image图片生成_1993961233665769474.json, 图片生成/文生图/Z-image文生图_2098605302726873090.json, 图片生成/文生图/ZIT基础文生图_2088289408716992513.json, 图片生成/文生图/ZImage turbo极致人感_1994819859462676481.json, 图片生成/文生图/Z_Image_Turbo-文生图_2063504172338737154.json, 图片生成/文生图/Z_image_turbo_int8_2079199590628282369.json, 图片生成/文生图/Zimage文生图基础_2060261069804892162.json, 图片生成/文生图/z-image-有无负面提示词对比_2016338426164944897.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_82

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Z-image图片生成_1993961233665769474.json、图片生成/文生图/Z-image文生图_2098605302726873090.json、图片生成/文生图/ZIT基础文生图_2088289408716992513.json、图片生成/文生图/ZImage turbo极致人感_1994819859462676481.json、图片生成/文生图/Z_Image_Turbo-文生图_2063504172338737154.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `EmptySD3LatentImage` —— 6/8 个有
- `ModelSamplingAuraFlow` —— 5/8 个有
- `PreviewImage` —— 3/8 个有
- `CR SDXL Aspect Ratio` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `JjkText` —— 1/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有
- `SDXLAspectRatio` —— 1/8 个有
- `Text` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 8 | 28% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 8 | 58% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，8 个样本，取值分散，一致性仅 28%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
