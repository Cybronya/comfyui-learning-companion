---
name: text_to_image_lora_sampler_clip_173
type: Text To Image
frequency: 10
level: strong
coverage: 0.8507
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/全能图片G image2.5系列 文生图图生图单张成本低至7分钱_2098662218412941313.json, 图片生成/图生图/全能图片G-2.5低价版图片编辑｜角色设计与分镜生成出图，图生图成本打下来_2100423600812679170.json, 图片生成/图生图/全能图片G2.5图片编辑低价版 图生图处理工具_2100688455109009410.json, 图片生成/图生图/全能图片G2.5换装 虚拟试衣图生图处理工具_2099929509331034114.json, 图片生成/图生图/全能图片G2.5换装+虚拟试衣图生图处理工具_2101571060582928385.json, 图片生成/图生图/正面全身去头强制右侧高清特写面部特征文生图处理工具_2102164933382332417.json, 图片生成/图生图/精修图生图工作流，提升图片细节与质感的专业修图方案_2102889930006548481.json, 图片生成/文生图/全能图片G-2.5低价版｜文生图局部重绘图片编辑_2101197387636236289.json, 图片生成/文生图/全能图片G-image-2.5 文生图与图生图双模图像处理_2098633491339636738.json, 图片生成/文生图/全能图片G-image-2.5｜文生图图生图一应俱全_2098719464136204289.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_173

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/全能图片G image2.5系列 文生图图生图单张成本低至7分钱_2098662218412941313.json、图片生成/图生图/全能图片G-2.5低价版图片编辑｜角色设计与分镜生成出图，图生图成本打下来_2100423600812679170.json、图片生成/图生图/全能图片G2.5图片编辑低价版 图生图处理工具_2100688455109009410.json、图片生成/图生图/全能图片G2.5换装 虚拟试衣图生图处理工具_2099929509331034114.json、图片生成/图生图/全能图片G2.5换装+虚拟试衣图生图处理工具_2101571060582928385.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：85%

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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/10 个有
- `RH_RhartImageG25SunburstImageToImage` —— 8/10 个有
- `RH_RhartImageG25FlareImageToImage` —— 5/10 个有
- `RH_RhartImageG25FlareTextToImage` —— 5/10 个有
- `RH_RhartImageG25SunburstTextToImage` —— 5/10 个有
- `Fast Groups Muter (rgthree)` —— 4/10 个有
- `Image Comparer (rgthree)` —— 3/10 个有
- `MuyeTextEditOutput` —— 3/10 个有
- `CR Prompt Text` —— 1/10 个有
- `LLGPTImage25Generator` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `PainterFluxImageEdit` —— 1/10 个有

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
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
