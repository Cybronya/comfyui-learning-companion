---
name: image_to_image_sampler_clip_unet_125
type: Image To Image
frequency: 4
level: moderate
coverage: 0.97625
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Magic-Wan-V2加速图生图_1991143691563696129.json, 图片生成/文生图/Magic-Wan-V2图生图_1991113183234732033.json, 图片生成/文生图/Z-Image-Turbo图生图_1994260211968000002.json, 图片生成/文生图/Z-iMage-turbo基础工作流（文生图+图生图）_2026897908511023106.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_125

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Magic-Wan-V2加速图生图_1991143691563696129.json、图片生成/文生图/Magic-Wan-V2图生图_1991113183234732033.json、图片生成/文生图/Z-Image-Turbo图生图_1994260211968000002.json、图片生成/文生图/Z-iMage-turbo基础工作流（文生图+图生图）_2026897908511023106.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 3/4 个有
- `Seed (rgthree)` —— 3/4 个有
- `EmptySD3LatentImage` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `ModelSamplingSD3` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `Florence2ModelLoader` —— 1/4 个有
- `Florence2Run` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 25 | 4 | 33% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | deis | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.75 | 0.58 - 1 | 4 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 25，4 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.75，观测区间 0.58 - 1，4 个样本，取值集中（一致性 81%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
