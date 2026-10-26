---
name: text_to_image_lora_sampler_clip_129
type: Text To Image
frequency: 12
level: strong
coverage: 0.856
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/G image2图像编辑单图模式-全能图片图生图工作流_2087371568707096578.json, 图片生成/图生图/G-2.5全能图片图生图 高品质图像编辑版本_2098287173207420930.json, 图片生成/图生图/G-2.5全能图片图生图极速版 快速高效图像处理_2098291440265809921.json, 图片生成/图生图/G-image-2.5图生图极速API｜批量重绘快人一步_2098743047059230722.json, 图片生成/图生图/G-image-2.5图生图高品质API｜重绘质感不掉线_2098739267697733633.json, 图片生成/图生图/G-image2.0低价渠道一号｜图生图省钱跑量必收藏_2103736051213885441.json, 图片生成/图生图/G-image2.0低价渠道二号｜图生图批量出图成本打下来_2103740749375426562.json, 图片生成/图生图/G-image2五图参考低价版｜图生图多图融合_2094497916810514434.json, 图片生成/图生图/低价版G-image2｜短剧广告设计摄影图生图生成_2094726703590498305.json, 图片生成/图生图/单图模式图像编辑image2ENG全能图片G_2087115444502220802.json, 图片生成/文生图/人像写真文生图｜Image 2图像模型图生图全能_2090822423569584129.json, 图片生成/文生图/人像写真文生图｜Image 2图像模型图生图直出_2090527437456236545.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_129

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/G image2图像编辑单图模式-全能图片图生图工作流_2087371568707096578.json、图片生成/图生图/G-2.5全能图片图生图 高品质图像编辑版本_2098287173207420930.json、图片生成/图生图/G-2.5全能图片图生图极速版 快速高效图像处理_2098291440265809921.json、图片生成/图生图/G-image-2.5图生图极速API｜批量重绘快人一步_2098743047059230722.json、图片生成/图生图/G-image-2.5图生图高品质API｜重绘质感不掉线_2098739267697733633.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `RH_RhartImageG2ImageToImage` —— 8/12 个有
- `Fast Groups Muter (rgthree)` —— 4/12 个有
- `RH_RhartImageG2TextToImage` —— 4/12 个有
- `CR Prompt Text` —— 2/12 个有
- `Label (rgthree)` —— 2/12 个有
- `PreviewAny` —— 2/12 个有
- `RHSettingsNode` —— 2/12 个有
- `RH_RhartImageG25OfficialTokenFlareEdit` —— 2/12 个有
- `RH_RhartImageG25OfficialTokenSunburstEdit` —— 2/12 个有
- `RH_RhartImageG2OfficialImageToImage` —— 2/12 个有
- `RH_RhartImageG2OfficialTextToImage` —— 2/12 个有
- `Text` —— 2/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
