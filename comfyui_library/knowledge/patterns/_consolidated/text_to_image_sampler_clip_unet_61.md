---
name: text_to_image_sampler_clip_unet_61
type: Text To Image
frequency: 10
level: moderate
coverage: 0.9009
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Dark daze art（Z-image-dazz）_1998590663778271234.json, 图片生成/图生图/Flux 2 Dev 单图编辑 + 加速版_1994947122980118530.json, 图片生成/图生图/Flux2文生图_1993664157952180226.json, 图片生成/图生图/Z-image最新优化版（速度快）_1995420868127940610.json, 图片生成/文生图/2029542457939075073.json, 图片生成/文生图/2030250301340520450.json, 图片生成/文生图/Krea2 Turbo文生图（双采版）_2070846138026119169.json, 图片生成/文生图/Krea2 漫剧角色资产一键生成工作流｜文生四视图_2099740461484302337.json, 图片生成/文生图/Z-image文生图，二次元校园女生风格Lora_1998998879238508546.json, 图片生成/文生图/文生图（Z-image，带lora）_1998357719558029314.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_61

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Dark daze art（Z-image-dazz）_1998590663778271234.json、图片生成/图生图/Flux 2 Dev 单图编辑 + 加速版_1994947122980118530.json、图片生成/图生图/Flux2文生图_1993664157952180226.json、图片生成/图生图/Z-image最新优化版（速度快）_1995420868127940610.json、图片生成/文生图/2029542457939075073.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `PrimitiveStringMultiline` —— 5/10 个有
- `PreviewImage` —— 4/10 个有
- `LayerUtility: TextJoinV2` —— 3/10 个有
- `MuyeSizeSelector` —— 2/10 个有
- `FluxGuidance` —— 1/10 个有
- `Int` —— 1/10 个有
- `Primitive integer [Crystools]` —— 1/10 个有
- `StringFunction|pysssss` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 6 - 20 | 10 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 70% |
| 重绘幅度 | 1 | 0.4 - 1 | 10 | 81% |
| 宽度 | 1080 | 720 - 2000 | 10 | 69% |
| 高度 | 1600 | 1024 - 1920 | 10 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 6 - 20，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，10 个样本，取值集中（一致性 81%）
- 宽度 中位数 1080，观测区间 720 - 2000，10 个样本
- 高度 中位数 1600，观测区间 1024 - 1920，10 个样本
- 高发问题（5/10 个样本）：Steps较低可能导致细节不足
