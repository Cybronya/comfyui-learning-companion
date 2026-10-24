---
name: text_to_image_sampler_clip_unet_68
type: Text To Image
frequency: 10
level: moderate
coverage: 0.9917
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z_image_Doodle style 风格工作流_2014354573992927233.json, 图片生成/文生图/zimage奇幻天宫_2087361360895242241.json, 图片生成/文生图/zimage广告图直出_2016732158576041986.json, 图片生成/文生图/zimage文生图+lora仙逆姚惜雪_2005983053098991617.json, 图片生成/文生图/zimage文生图+全息翼界lora_2014158819462488066.json, 图片生成/文生图/⚡ Boogu-Turbo 极速高写实文生图_2068717870527369217.json, 图片生成/文生图/【GUGU】Z-image文生图工作流_1993849344558383105.json, 图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_2098225838008389634.json, 图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_2099331628756725762.json, 图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_2099337911668924418.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_68

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/z_image_Doodle style 风格工作流_2014354573992927233.json、图片生成/文生图/zimage奇幻天宫_2087361360895242241.json、图片生成/文生图/zimage广告图直出_2016732158576041986.json、图片生成/文生图/zimage文生图+lora仙逆姚惜雪_2005983053098991617.json、图片生成/文生图/zimage文生图+全息翼界lora_2014158819462488066.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/10 个有
- `CR Text` —— 3/10 个有
- `QZ_ResolutionPreset` —— 3/10 个有
- `ZImageLoraModelOnly` —— 2/10 个有
- `FluxResolutionNode` —— 1/10 个有
- `JjkText` —— 1/10 个有
- `PIP_StringConcatenation` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 10 | 10 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 90% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1052 | 960 - 1920 | 10 | 71% |
| 高度 | 1080 | 1024 - 1920 | 10 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 10，10 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 90%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，观测区间 960 - 1920，10 个样本
- 高度 中位数 1080，观测区间 1024 - 1920，10 个样本
