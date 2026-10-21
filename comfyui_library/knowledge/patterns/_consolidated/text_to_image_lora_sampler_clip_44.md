---
name: text_to_image_lora_sampler_clip_44
type: Text To Image
frequency: 16
level: strong
coverage: 0.875625
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/G2.5 Sunburst文生图 4K画质经济型高效输出_2098290011564240898.json, 图片生成/文生图/GGPPTT-image2全能图片组件｜文生图图片编辑工作流_2097808293908541441.json, 图片生成/文生图/Image-2.5九图文生图版本 批量高质量生成_2098303034546806785.json, 图片生成/文生图/Image2.5文生图 顶级_2101616440351748097.json, 图片生成/文生图/Image2.5文生图 高质量图片生成工具_2100292745112936450.json, 图片生成/文生图/Image2.5文生图 高质量图片生成工具_2101592299229761537.json, 图片生成/文生图/Image2.5文生图顶级处理生成工作流工具_2102116515188400130.json, 图片生成/文生图/Image2.5文生图顶级工作流｜高质量图片生成｜文案配图一步到位_2101886755678015490.json, 图片生成/文生图/Image2.5文生图高质量图片生成工具｜高级感图像一键生成_2101936480737382401.json, 图片生成/文生图/Krea2写实4K直出｜文生图去ai感真实人像生成_2093105565953249281.json, 图片生成/文生图/aigc-image-2.5文生图九图连出｜太平风格批量出图_2106953497185972225.json, 图片生成/文生图/人像写真文生图｜Image 2图像模型图生图全能_2090822423569584129.json, 图片生成/文生图/人像写真文生图｜Image 2图像模型图生图直出_2090527437456236545.json, 图片生成/文生图/全能图片G-2.5低价版｜文生图局部重绘图片编辑_2101197387636236289.json, 图片生成/文生图/全能图片G-image-2.5 文生图与图生图双模图像处理_2098633491339636738.json, 图片生成/文生图/全能图片G-image-2.5｜文生图图生图一应俱全_2098719464136204289.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_44

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/G2.5 Sunburst文生图 4K画质经济型高效输出_2098290011564240898.json、图片生成/文生图/GGPPTT-image2全能图片组件｜文生图图片编辑工作流_2097808293908541441.json、图片生成/文生图/Image-2.5九图文生图版本 批量高质量生成_2098303034546806785.json、图片生成/文生图/Image2.5文生图 顶级_2101616440351748097.json、图片生成/文生图/Image2.5文生图 高质量图片生成工具_2100292745112936450.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 16 个 workflow 都包含：
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
- `孤海注释` —— 14/16 个有
- `RH_RhartImageG25SunburstTextToImage` —— 11/16 个有
- `LoadImage` —— 7/16 个有
- `PreviewImage` —— 4/16 个有
- `RH_RhartImageG25FlareTextToImage` —— 4/16 个有
- `RH_RhartImageG2ImageToImage` —— 4/16 个有
- `Fast Groups Muter (rgthree)` —— 3/16 个有
- `RH_RhartImageG25FlareImageToImage` —— 3/16 个有
- `RH_RhartImageG25SunburstImageToImage` —— 3/16 个有
- `RH_RhartImageG2TextToImage` —— 3/16 个有
- `CR Prompt Text` —— 2/16 个有
- `RH_RhartImageG2OfficialImageToImage` —— 2/16 个有
- `RH_RhartImageG2OfficialTextToImage` —— 2/16 个有
- `LayerUtility: TextBox` —— 1/16 个有
- `MuyeTextEditOutput` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高发问题（19/16 个样本）：Steps较低可能导致细节不足
