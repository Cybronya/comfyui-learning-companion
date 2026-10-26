---
name: image_to_image_lora_sampler_clip_82
type: Image To Image
frequency: 4
level: strong
coverage: 0.889
common_nodes: [CLIPTextEncode, FluxGuidance, KSampler, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/珠宝首饰电商洗图_改图_改产品颜色_改场景_2001175361377402881.json, 图片生成/文生图/电商产品_换图 换产品颜色或换场景_2001194927230943234.json, 数字人/数字人/真人转BJD人偶_V1.0_1989340531513847810.json, 数字人/数字人/胖人变瘦(一键变苗条)_1945686995257499649.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_82

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/珠宝首饰电商洗图_改图_改产品颜色_改场景_2001175361377402881.json、图片生成/文生图/电商产品_换图 换产品颜色或换场景_2001194927230943234.json、数字人/数字人/真人转BJD人偶_V1.0_1989340531513847810.json、数字人/数字人/胖人变瘦(一键变苗条)_1945686995257499649.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `FluxKontextImageScale` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ACE_TextTranslate` —— 2/4 个有
- `DualCLIPLoader` —— 2/4 个有
- `Note Plus (mtb)` —— 2/4 个有
- `NunchakuTextEncoderLoaderV2` —— 2/4 个有
- `JjkText` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 17.5 | 15 - 20 | 4 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 17.5，观测区间 15 - 20，4 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
