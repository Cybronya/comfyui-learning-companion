---
name: text_to_image_lora_sampler_clip_235
type: Text To Image
frequency: 8
level: strong
coverage: 0.845125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Image-2.5九图文生图版本 批量高质量生成_2098303034546806785.json, 图片生成/文生图/Image-2.5图片编辑极速版 全能图片G2.5快速处理_2098306932686802946.json, 图片生成/文生图/Image2.5 Seedance等API接入生图生视频，低成本文生图文生视频方案_2103934036086444034.json, 图片生成/文生图/aigc-image-2.5文生图九图连出｜太平风格批量出图_2106953497185972225.json, 图片生成/文生图/全能图片G-Image-2.5 Flare轻量快速版 文生图图生图编辑_2098705852541792258.json, 图片生成/文生图/全能图片G-Image-2.5 Sunburst高精旗舰版 文生图图生图编辑_2098702467142868994.json, 数字人/数字人/G Image 2.5全家桶 文生图与图像编辑多功能集成_2098292790764589058.json, 数字人/数字人/G Image 2.5全能图片 高一致性美学文生图与图像编辑_2098286878167490562.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_235

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Image-2.5九图文生图版本 批量高质量生成_2098303034546806785.json、图片生成/文生图/Image-2.5图片编辑极速版 全能图片G2.5快速处理_2098306932686802946.json、图片生成/文生图/Image2.5 Seedance等API接入生图生视频，低成本文生图文生视频方案_2103934036086444034.json、图片生成/文生图/aigc-image-2.5文生图九图连出｜太平风格批量出图_2106953497185972225.json、图片生成/文生图/全能图片G-Image-2.5 Flare轻量快速版 文生图图生图编辑_2098705852541792258.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/8 个有
- `PreviewImage` —— 4/8 个有
- `RH_RhartImageG25OfficialTokenFlareEdit` —— 4/8 个有
- `RH_RhartImageG25SunburstTextToImage` —— 4/8 个有
- `CR Prompt Text` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `RH_RhartImageG25OfficialTokenFlareTextToImage` —— 2/8 个有
- `RH_RhartImageG25OfficialTokenSunburstTextToImage` —— 2/8 个有
- `RH_RhartImageG25SunburstImageToImage` —— 2/8 个有
- `RH_RhartImageG25OfficialTokenSunburstEdit` —— 1/8 个有
- `RH_Screenwriter` —— 1/8 个有
- `WujiAPI` —— 1/8 个有
- `WujiClosedSourceGenerator` —— 1/8 个有
- `WujiUpscaler2` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
