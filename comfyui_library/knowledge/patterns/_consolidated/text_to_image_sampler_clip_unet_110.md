---
name: text_to_image_sampler_clip_unet_110
type: Text To Image
frequency: 6
level: moderate
coverage: 0.807
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2031225025554030594.json, 图片生成/文生图/2031284119526711298.json, 图片生成/文生图/SD放大_2037862505682313218.json, 图片生成/文生图/Z-image文生图工作流_2075475394177880066.json, 图片生成/文生图/z-image文生图+全节点注释_2055922381788598273.json, 图片生成/文生图/z-image文生图_2055928133613826049.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_110

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/2031225025554030594.json、图片生成/文生图/2031284119526711298.json、图片生成/文生图/SD放大_2037862505682313218.json、图片生成/文生图/Z-image文生图工作流_2075475394177880066.json、图片生成/文生图/z-image文生图+全节点注释_2055922381788598273.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `ImageUpscaleWithModel` —— 5/6 个有
- `UpscaleModelLoader` —— 5/6 个有
- `CR Text` —— 4/6 个有
- `easy promptList` —— 3/6 个有
- `LoadImage` —— 2/6 个有
- `PreviewTextNode` —— 2/6 个有
- `RHHiddenNodes` —— 2/6 个有
- `UltimateSDUpscale` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 10 | 6 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 25% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1052 | 720 - 1536 | 6 | 74% |
| 高度 | 1536 | 1024 - 1920 | 6 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 10，6 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，观测区间 720 - 1536，6 个样本
- 高度 中位数 1536，观测区间 1024 - 1920，6 个样本，取值集中（一致性 81%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
