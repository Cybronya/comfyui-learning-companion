---
name: text_to_image_lora_sampler_clip_639
type: Text To Image
frequency: 2
level: weak
coverage: 0.927
common_nodes: [BetterFilmGrain, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfySwitchNode, ConditioningZeroOut, EmptyLatentImage, ImageSharpen, KOOK_SaveJPGImage, KSampler, LayerColor: ColorBalance, LayerUtility: ImageBlendAdvance, LoadImage, LoraLoaderModelOnly, ResolutionSelector, TextConcat, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2 4K直出文生图工作流_2082008537349312514.json, 图片生成/文生图/krea2 4K直出文生图，写实高清画质一站搞定_2111273798757605378.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_639

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/krea2 4K直出文生图工作流_2082008537349312514.json、图片生成/文生图/krea2 4K直出文生图，写实高清画质一站搞定_2111273798757605378.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `BetterFilmGrain`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageSharpen`
- `KOOK_SaveJPGImage`
- `KSampler`
- `LayerColor: ColorBalance`
- `LayerUtility: ImageBlendAdvance`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `TextConcat`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 2.75 | - | 2 | 36% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 724 | - | 2 | 11% |
| 高度 | 1064 | - | 2 | 8% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 2.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 724，样本不足，未给区间，2 个样本，取值分散，一致性仅 11%
- 高度 中位数 1064，样本不足，未给区间，2 个样本，取值分散，一致性仅 8%
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
