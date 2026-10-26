---
name: text_to_image_sampler_clip_unet_140
type: Text To Image
frequency: 5
level: moderate
coverage: 0.9866
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, TTResolutionSelector, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-极致艺术风格生成_2070006997050810370.json, 图片生成/文生图/Krea2-色彩HDR增强VAE-对比原版VAE效果_2074188352772984834.json, 图片生成/文生图/Krea2四视图生成流（文生图）2608_2096857346608816129.json, 图片生成/文生图/krea2 超真实人物生成2608_2096870221717000194.json, 视频生成/图生视频/Krea2-极致艺术风格生成_2070438497516875778.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_140

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Krea2-极致艺术风格生成_2070006997050810370.json、图片生成/文生图/Krea2-色彩HDR增强VAE-对比原版VAE效果_2074188352772984834.json、图片生成/文生图/Krea2四视图生成流（文生图）2608_2096857346608816129.json、图片生成/文生图/krea2 超真实人物生成2608_2096870221717000194.json、视频生成/图生视频/Krea2-极致艺术风格生成_2070438497516875778.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `Label (rgthree)` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `easy promptLine` —— 2/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `easy imageConcat` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1024 | 5 | 65% |
| 高度 | 512 | 512 - 1024 | 5 | 65% |
| 采样步数 | 8 | 8 - 10 | 5 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 60% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1024，5 个样本
- 高度 中位数 512，观测区间 512 - 1024，5 个样本
- 采样步数 中位数 8，观测区间 8 - 10，5 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
