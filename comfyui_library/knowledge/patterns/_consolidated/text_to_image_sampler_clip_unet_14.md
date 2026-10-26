---
name: text_to_image_sampler_clip_unet_14
type: Text To Image
frequency: 22
level: moderate
coverage: 0.867636
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Turbo 浮云2.3_2018528654661263361.json, 图片生成/文生图/Z-Image-Turbo文生图_1993942538386161666.json, 图片生成/文生图/Z-Image-turbo-人物角色定像_2032331811874938881.json, 图片生成/文生图/Z-Image文生图基础工作流_1997889845496283138.json, 图片生成/文生图/Z-image文生图_1996854775096516609.json, 图片生成/文生图/Z-image文生图_2002734393544306690.json, 图片生成/文生图/Z-image文生图写实，真实感_1999363958169628673.json, 图片生成/文生图/Z-image文生图新王-支持中文_1995027322610888706.json, 图片生成/文生图/Z-image文生图新王-支持中文_1995287563680276482.json, 图片生成/文生图/Z-image文生图极速高质量_1996077196244631554.json, 图片生成/文生图/ZImage 光速高清文生图_1988965178039480322.json, 图片生成/文生图/ZImage3.0-SUPER 文生图_2017812013216436226.json, 图片生成/文生图/Zimage图像模型（支持真人的国产加速模型）_2028268832682418177.json, 图片生成/文生图/Zimage文生图_1993848041241329666.json, 图片生成/文生图/Zimage文生图_2013426591489069057.json, 图片生成/文生图/Zimage超越Flux2的国产图像模型（支持真人的国产加速模型）_1993888771909369858.json, 图片生成/文生图/Zimage超越Flux2的国产图像模型（支持真人的国产加速模型）_1995004425267818497.json, 图片生成/文生图/Zimage超越Flux2的国产图像模型（支持真人的国产加速模型）_2038275878496505858.json, 图片生成/文生图/Zimage（支持真人的国产加速模型）_2027694676630835201.json, 图片生成/文生图/Zimage（支持真人的国产加速模型）_2027695408717238273.json, 图片生成/文生图/zimage文生图_2004814222078996481.json, 图片生成/文生图/文生图_2028064937913880578.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_14

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/文生图/Z-Image-Turbo 浮云2.3_2018528654661263361.json、图片生成/文生图/Z-Image-Turbo文生图_1993942538386161666.json、图片生成/文生图/Z-Image-turbo-人物角色定像_2032331811874938881.json、图片生成/文生图/Z-Image文生图基础工作流_1997889845496283138.json、图片生成/文生图/Z-image文生图_1996854775096516609.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 18/22 个有
- `PrimitiveInt` —— 12/22 个有
- `PrimitiveStringMultiline` —— 8/22 个有
- `LoraLoader` —— 3/22 个有
- `CR Prompt Text` —— 2/22 个有
- `AnyAspectRatio` —— 1/22 个有
- `Fast Groups Bypasser (rgthree)` —— 1/22 个有
- `Load Lora` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 35 | 22 | 37% |
| Prompt 约束强度(CFG) | 1 | 1 - 5.5 | 22 | 12% |
| 采样算法 | euler | - | 22 | 86% |
| 调度器 | simple | - | 22 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |
| 宽度 | 1052 | 512 - 1920 | 22 | 57% |
| 高度 | 1280 | 512 - 1920 | 22 | 60% |
| LoRA 模型强度 | 0.6 | 0.6 - 1 | 3 | 74% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 35，22 个样本，取值分散，一致性仅 37%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5.5，22 个样本，取值分散，一致性仅 12%
- 采样算法 最常用 euler，22 个样本，一致性 86%
- 调度器 最常用 simple，22 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，观测区间 512 - 1920，22 个样本
- 高度 中位数 1280，观测区间 512 - 1920，22 个样本
- LoRA 模型强度 中位数 0.6，观测区间 0.6 - 1，3 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
