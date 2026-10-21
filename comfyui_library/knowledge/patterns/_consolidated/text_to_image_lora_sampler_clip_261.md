---
name: text_to_image_lora_sampler_clip_261
type: Text To Image
frequency: 4
level: strong
coverage: 0.88375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScaleBy, JjkText, KSampler, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/4K高清直出工作流｜Krea2_文生图生成_2092937515861889025.json, 图片生成/文生图/Krea2文生图双采 高质量画面两次采样优化_2105119424356376577.json, 图片生成/文生图/Krea2文生图双采 高质量画面两次采样优化_2105390862208430081.json, 图片生成/文生图/Krea2文生图双采样｜文生图画质翻倍｜一张提示词两张好图_2104832511506468866.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_261

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/4K高清直出工作流｜Krea2_文生图生成_2092937515861889025.json、图片生成/文生图/Krea2文生图双采 高质量画面两次采样优化_2105119424356376577.json、图片生成/文生图/Krea2文生图双采 高质量画面两次采样优化_2105390862208430081.json、图片生成/文生图/Krea2文生图双采样｜文生图画质翻倍｜一张提示词两张好图_2104832511506468866.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageScaleBy`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ConditioningKrea2Rebalance` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `ImageBlend` —— 3/4 个有
- `ImageScale` —— 3/4 个有
- `ImageUpscaleWithModel` —— 3/4 个有
- `KSamplerAdvanced` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `RH_Translator` —— 3/4 个有
- `ResolutionSelector` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `easy seed` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `easy clearCacheAll` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `PDRatioSelector` —— 1/4 个有
- `VAEDecodeTiled` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
