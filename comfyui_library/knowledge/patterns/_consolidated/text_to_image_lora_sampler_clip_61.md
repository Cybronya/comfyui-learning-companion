---
name: text_to_image_lora_sampler_clip_61
type: Text To Image
frequency: 16
level: strong
coverage: 0.876313
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/产品正侧视图压缩工作流｜商品图片快速处理生成_2097532280968400898.json, 图片生成/图生图/全功能图生图处理生成综合工作流工具包配置_2101020931924783105.json, 图片生成/图生图/全能G2图生图工作流｜多场景图像编辑处理生成_2096733211073273858.json, 图片生成/图生图/全能图像G image2.0三图编辑 三张参考图输入改图_2105124015596728322.json, 图片生成/图生图/全能图像G image2.0多图编辑｜四到十图低价版_2095583907658944513.json, 图片生成/图生图/全能图像Image2.5三图编辑 多图合成处理_2098301067544055810.json, 图片生成/图生图/全能图片 G-Image-2.0｜人物面部三视图高清直出｜图生图_2096889065525309441.json, 图片生成/图生图/全能图片G-2.0图生图低价渠道高性价比出图方案_2104821488074444802.json, 图片生成/图生图/全能图片G2.0低价渠道版 图生图高效处理生成工具_2113730029988433922.json, 图片生成/图生图/全能图片G2.0低价渠道版图生图工作流，通用图片生成与编辑_2102811484857393154.json, 图片生成/图生图/全能图片G2.0低价渠道版工作流，图生图图像处理方案_2107522530834739202.json, 图片生成/图生图/全能图片G2.0低价渠道版｜图生图成本打下来｜日常批量出图更划算_2102577836518367234.json, 图片生成/图生图/全能图片G2.0图生图 低价渠道高性价比出图_2104290534352310273.json, 图片生成/图生图/全能图片G2.0｜低价渠道版图生图处理直出_2090931490459840514.json, 图片生成/图生图/全能图片G2图生图0.1元版处理生成工具_2102487881666351105.json, 图片生成/图生图/地表最强全能图片G2图生图｜GP-T-Image-2单次0.1元｜改图超划算_2102222773492994049.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_61

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/产品正侧视图压缩工作流｜商品图片快速处理生成_2097532280968400898.json、图片生成/图生图/全功能图生图处理生成综合工作流工具包配置_2101020931924783105.json、图片生成/图生图/全能G2图生图工作流｜多场景图像编辑处理生成_2096733211073273858.json、图片生成/图生图/全能图像G image2.0三图编辑 三张参考图输入改图_2105124015596728322.json、图片生成/图生图/全能图像G image2.0多图编辑｜四到十图低价版_2095583907658944513.json…）

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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 15/16 个有
- `RH_RhartImageG2ImageToImage` —— 14/16 个有
- `CR Text` —— 3/16 个有
- `Fast Groups Bypasser (rgthree)` —— 2/16 个有
- `Float` —— 2/16 个有
- `PreviewImage` —— 2/16 个有
- `RTXVideoSuperResolution` —— 2/16 个有
- `DisplayImageFromURL` —— 1/16 个有
- `ImageScale` —— 1/16 个有
- `RH_RhartImageG25SunburstImageToImage` —— 1/16 个有
- `RotateImageNode` —— 1/16 个有

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
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
