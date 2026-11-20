---
name: image_to_image_sampler_clip_unet_103
type: Image To Image
frequency: 5
level: strong
coverage: 0.8566
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, PreviewImage, RH_Translator, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/电商产品任意更换颜色 万能真实换色  服饰指定换色 保持材质不变_2052695533499756546.json, 图片生成/图生图/电商产品任意更换颜色_万能真实换色_服饰指定换色_保持材质不变_2096800408797794305.json, 图片生成/图生图/电商产品任意更换颜色_万能真实换色_服饰指定换色_保持材质不变_2097143368966041602.json, 图片生成/文生图/去除水印_2090086272101605377.json, 图片生成/文生图/电商改色丨Flux丨AI改色图生成_2100864143933919233.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_103

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/电商产品任意更换颜色 万能真实换色  服饰指定换色 保持材质不变_2052695533499756546.json、图片生成/图生图/电商产品任意更换颜色_万能真实换色_服饰指定换色_保持材质不变_2096800408797794305.json、图片生成/图生图/电商产品任意更换颜色_万能真实换色_服饰指定换色_保持材质不变_2097143368966041602.json、图片生成/文生图/去除水印_2090086272101605377.json、图片生成/文生图/电商改色丨Flux丨AI改色图生成_2100864143933919233.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Colored Image (mtb)` —— 4/5 个有
- `ImageConcatMulti` —— 4/5 个有
- `ImageCrop` —— 4/5 个有
- `ImageResize+` —— 4/5 个有
- `ImpactInt` —— 4/5 个有
- `MathExpression|pysssss` —— 4/5 个有
- `FluxKontextImageScale` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
