---
name: image_to_image_lora_sampler_clip_141
type: Image To Image
frequency: 2
level: weak
coverage: 0.635
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningZeroOut, GetNode, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-Base，图生图洗图_2068968208014594050.json, 图片生成/图生图/动漫转真人+zimage细节增强+Seed放大_2009102080778182657.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_141

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Z-Base，图生图洗图_2068968208014594050.json、图片生成/图生图/动漫转真人+zimage细节增强+Seed放大_2009102080778182657.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 1/2 个有
- `Display Any (rgthree)` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Float` —— 1/2 个有
- `Int` —— 1/2 个有
- `Joy_caption_two_advanced` —— 1/2 个有
- `Joy_caption_two_load` —— 1/2 个有
- `Joy_extra_options` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 50% |
| 调度器 | linear_quadratic | - | 2 | 50% |
| 重绘幅度 | 0.65 | - | 2 | 46% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 50%
- 调度器 最常用 linear_quadratic，2 个样本，一致性 50%
- 重绘幅度 中位数 0.65，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
