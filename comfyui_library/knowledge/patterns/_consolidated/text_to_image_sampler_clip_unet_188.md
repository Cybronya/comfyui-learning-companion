---
name: text_to_image_sampler_clip_unet_188
type: Text To Image
frequency: 3
level: strong
coverage: 0.972333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, Krea2SizePreset, Krea2StyleReference, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-风格参考(单双图)_2074801670466392066.json, 图片生成/文生图/那颗星星 _ Krea2真风格迁移（单图）_2072977936545828865.json, 图片生成/文生图/那颗星星 _ Krea2真风格迁移（双图）_2072977960210096130.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_188

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea2-风格参考(单双图)_2074801670466392066.json、图片生成/文生图/那颗星星 _ Krea2真风格迁移（单图）_2072977936545828865.json、图片生成/文生图/那颗星星 _ Krea2真风格迁移（双图）_2072977960210096130.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `Krea2SizePreset`
- `Krea2StyleReference`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Krea2StyleTransfer` —— 2/3 个有
- `Krea2TwoStyleReferences` —— 2/3 个有
- `Krea2TwoStyleTransfer` —— 2/3 个有
- `GoohaiUniversalSlider` —— 1/3 个有
- `MuyeTextEditOutput` —— 1/3 个有
- `孤海注释` —— 1/3 个有
- `忽略多组孤海` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 928 | 928 - 928 | 3 | 100% |
| 高度 | 1160 | 1160 - 1160 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 928，观测区间 928 - 928，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1160，观测区间 1160 - 1160，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
