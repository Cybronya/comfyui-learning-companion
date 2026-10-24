---
name: text_to_image_sampler_clip_unet_106
type: Text To Image
frequency: 6
level: strong
coverage: 0.973833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, Krea2StyleReference, Krea2StyleTransfer, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea 2风格迁移工作流_2079112632136720385.json, 图片生成/图生图/Krea2 单图风格迁移_2073675891854630914.json, 图片生成/图生图/Krea2-单图风格参考_2074069678892343297.json, 图片生成/图生图/Krea2-风格迁移（按风格生成）_2074121611355181058.json, 图片生成/图生图/Krea2真风格迁移（单图）_2073676868842246145.json, 图片生成/文生图/Krea2-单图风格参考_2073947155995389954.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_106

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Krea 2风格迁移工作流_2079112632136720385.json、图片生成/图生图/Krea2 单图风格迁移_2073675891854630914.json、图片生成/图生图/Krea2-单图风格参考_2074069678892343297.json、图片生成/图生图/Krea2-风格迁移（按风格生成）_2074121611355181058.json、图片生成/图生图/Krea2真风格迁移（单图）_2073676868842246145.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `Krea2StyleReference`
- `Krea2StyleTransfer`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `CR Text` —— 2/6 个有
- `Krea2SizePreset` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `ResolutionSelector` —— 2/6 个有
- `ImageConcanate` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `LayerUtility: ImageReel` —— 1/6 个有
- `LayerUtility: ImageReelComposit` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `SeedNode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler_ancestral | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 976 | 512 - 1024 | 6 | 72% |
| 高度 | 1024 | 512 - 1280 | 6 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 976，观测区间 512 - 1024，6 个样本
- 高度 中位数 1024，观测区间 512 - 1280，6 个样本
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
