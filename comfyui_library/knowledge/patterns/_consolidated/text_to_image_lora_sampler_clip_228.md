---
name: text_to_image_lora_sampler_clip_228
type: Text To Image
frequency: 3
level: strong
coverage: 0.777
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, RH_RhartImageG25SunburstImageToImage, RH_RhartImageG25SunburstTextToImage, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/GI2.5 Sunburst文生图图生图集合流｜新奇创意一把抓，文生图图生图双模式_2100484050002735106.json, 数字人/数字人/G Image 2.5全家桶 文生图与图像编辑多功能集成_2098292790764589058.json, 数字人/数字人/G Image 2.5全能图片 高一致性美学文生图与图像编辑_2098286878167490562.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_228

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/GI2.5 Sunburst文生图图生图集合流｜新奇创意一把抓，文生图图生图双模式_2100484050002735106.json、数字人/数字人/G Image 2.5全家桶 文生图与图像编辑多功能集成_2098292790764589058.json、数字人/数字人/G Image 2.5全能图片 高一致性美学文生图与图像编辑_2098286878167490562.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RH_RhartImageG25SunburstImageToImage`
- `RH_RhartImageG25SunburstTextToImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `RH_RhartImageG25OfficialTokenFlareEdit` —— 2/3 个有
- `RH_RhartImageG25OfficialTokenFlareTextToImage` —— 2/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `MuyeTextEditOutput` —— 1/3 个有
- `PlaySound|pysssss` —— 1/3 个有
- `RH_RhartImageG25OfficialTokenSunburstEdit` —— 1/3 个有
- `RH_RhartImageG25OfficialTokenSunburstTextToImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
