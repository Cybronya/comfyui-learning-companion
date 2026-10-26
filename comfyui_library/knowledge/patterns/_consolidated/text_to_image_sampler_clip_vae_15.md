---
name: text_to_image_sampler_clip_vae_15
type: Text To Image
frequency: 8
level: moderate
coverage: 0.991125
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Boogu 满血版文生图_2068176743512502273.json, 图片生成/文生图/Boogu-Base 高清质感文生图_2068717818228592642.json, 图片生成/文生图/Boogu-Image Base基础文生图_2068063950163501058.json, 图片生成/文生图/Boogu-Image Turbo基础文生图2606_2068063045523435521.json, 图片生成/文生图/None Z-image-Turbo CFG解锁版（提高高频信息）_1999533655208980481.json, 图片生成/文生图/Nunchaku极速版Z-image文生图_2005527503991177218.json, 图片生成/文生图/Nunchaku超级加速版Z-image文生图v1_2005116765585764354.json, 图片生成/文生图/Z-Image-De-Turbo去蒸馏文生图（CFG3 25步）_1997621234118668290.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_15

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Boogu 满血版文生图_2068176743512502273.json、图片生成/文生图/Boogu-Base 高清质感文生图_2068717818228592642.json、图片生成/文生图/Boogu-Image Base基础文生图_2068063950163501058.json、图片生成/文生图/Boogu-Image Turbo基础文生图2606_2068063045523435521.json、图片生成/文生图/None Z-image-Turbo CFG解锁版（提高高频信息）_1999533655208980481.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `easy promptLine` —— 4/8 个有
- `NunchakuZImageDiTLoader` —— 2/8 个有
- `TTResolutionSelector` —— 2/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `ProcessString` —— 1/8 个有
- `SizeSelector` —— 1/8 个有
- `easy promptList` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1052 | 720 - 1920 | 8 | 66% |
| 高度 | 1180 | 1024 - 1920 | 8 | 73% |
| 采样步数 | 20 | 4 - 50 | 8 | 30% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4 | 8 | 49% |
| 采样算法 | ddim | - | 8 | 38% |
| 调度器 | simple | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1052，观测区间 720 - 1920，8 个样本
- 高度 中位数 1180，观测区间 1024 - 1920，8 个样本
- 采样步数 中位数 20，观测区间 4 - 50，8 个样本，取值分散，一致性仅 30%
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4，8 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 ddim，8 个样本，一致性 38%
- 调度器 最常用 simple，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
