---
name: image_to_image_lora_sampler_unet_222
type: Image To Image
frequency: 2
level: weak
coverage: 0.8335
common_nodes: [CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/krea2二次元转真人_2052586481721589761.json, 图片生成/图生图/图案提取 + 神级迁移！Qwen+Klein 王炸组合_2032784566385123329.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_222

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/krea2二次元转真人_2052586481721589761.json、图片生成/图生图/图案提取 + 神级迁移！Qwen+Klein 王炸组合_2032784566385123329.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 1/2 个有
- `Krea2OstrisEditModelPatch` —— 1/2 个有
- `PainterFluxImageEdit` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `VOSR2ModelLoader` —— 1/2 个有
- `VOSR2Upscale` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | - | 2 | 86% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta57 | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta57，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
