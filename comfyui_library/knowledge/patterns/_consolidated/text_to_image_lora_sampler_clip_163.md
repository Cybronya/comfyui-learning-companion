---
name: text_to_image_lora_sampler_clip_163
type: Text To Image
frequency: 10
level: strong
coverage: 0.8427
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/产品正侧视图压缩工作流｜商品图片快速处理生成_2097532280968400898.json, 图片生成/图生图/人物皮肤质感优化搭配克莱因高清放大，人像写真级图生图高清修复_2102894507539910658.json, 图片生成/图生图/人物皮肤质感优化搭配克莱因高清放大，人像写真级图生图高清修复_2104741711716114434.json, 图片生成/图生图/人物皮肤质感克莱因高清 人像写真高清放大处理_2099939435751239681.json, 图片生成/图生图/人物皮肤质感克莱因高清_人像写真高清放大处理_2100182790968012801.json, 图片生成/图生图/人物皮肤质感克莱因高清_人像写真高清放大处理_2101482977904644097.json, 图片生成/图生图/人物皮肤质感克莱因高清_人像写真高清放大处理_2101868155126771713.json, 图片生成/图生图/人物皮肤质感克莱因高清_人像写真高清放大处理_2102212532319641601.json, 图片生成/图生图/人物皮肤质感加克莱因高清工作流，精修图生图高清放大处理方案_2105813111113601026.json, 图片生成/图生图/克莱因高清人物皮肤质感流｜毛孔光泽都真实，人像出图高级感_2099540747157594114.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_163

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/产品正侧视图压缩工作流｜商品图片快速处理生成_2097532280968400898.json、图片生成/图生图/人物皮肤质感优化搭配克莱因高清放大，人像写真级图生图高清修复_2102894507539910658.json、图片生成/图生图/人物皮肤质感优化搭配克莱因高清放大，人像写真级图生图高清修复_2104741711716114434.json、图片生成/图生图/人物皮肤质感克莱因高清 人像写真高清放大处理_2099939435751239681.json、图片生成/图生图/人物皮肤质感克莱因高清_人像写真高清放大处理_2100182790968012801.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 9/10 个有
- `Image Comparer (rgthree)` —— 9/10 个有
- `LoadImage` —— 9/10 个有
- `workflow>klein高清` —— 8/10 个有
- `workflow>人物皮肤高清` —— 6/10 个有
- `孤海注释` —— 5/10 个有
- `PreviewImage` —— 4/10 个有
- `EmptyImage` —— 3/10 个有
- `workflow>krea2高清` —— 3/10 个有
- `DisplayImageFromURL` —— 1/10 个有
- `ImageScale` —— 1/10 个有
- `RotateImageNode` —— 1/10 个有
- `workflow>克莱因高清` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
