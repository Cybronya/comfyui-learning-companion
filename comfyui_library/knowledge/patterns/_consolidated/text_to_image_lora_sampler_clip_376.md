---
name: text_to_image_lora_sampler_clip_376
type: Text To Image
frequency: 5
level: strong
coverage: 0.8766
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, Fast Groups Bypasser (rgthree), JjkText, KSampler, LoadImage, LoraLoaderModelOnly, RH_Nano_Banana2_Image2Image, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图与参考图生封面图详情页，海报制作与字体排版一体化_2104743204351471618.json, 数字人/数字人/全能图像Pro提示词玩法大全 电商主图详情页复刻工具_2099178316405239810.json, 数字人/数字人/全能图像Pro提示词玩法大全 电商主图详情页复刻工具_2099546664741720066.json, 数字人/数字人/全能图像Pro玩法宝典｜提示词合集一次拿全，电商主图详情页直接复刻_2099504783659986945.json, 数字人/数字人/文生图与参考图生封面图详情页，海报制作与字体排版一体化_2102892932557791233.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_376

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/文生图与参考图生封面图详情页，海报制作与字体排版一体化_2104743204351471618.json、数字人/数字人/全能图像Pro提示词玩法大全 电商主图详情页复刻工具_2099178316405239810.json、数字人/数字人/全能图像Pro提示词玩法大全 电商主图详情页复刻工具_2099546664741720066.json、数字人/数字人/全能图像Pro玩法宝典｜提示词合集一次拿全，电商主图详情页直接复刻_2099504783659986945.json、数字人/数字人/文生图与参考图生封面图详情页，海报制作与字体排版一体化_2102892932557791233.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 4/5 个有
- `GetImageSize+` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `JoinStringMulti` —— 2/5 个有
- `RH_LLMAPI_Pro_Node` —— 2/5 个有
- `easy anythingIndexSwitch` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `EmptyImage` —— 1/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
