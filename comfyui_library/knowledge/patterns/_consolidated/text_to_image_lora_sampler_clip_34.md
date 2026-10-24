---
name: text_to_image_lora_sampler_clip_34
type: Text To Image
frequency: 21
level: strong
coverage: 0.883667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/G image2图像编辑单图模式-全能图片图生图工作流_2087371568707096578.json, 图片生成/图生图/G-2.5全能图片图生图 高品质图像编辑版本_2098287173207420930.json, 图片生成/图生图/G-2.5全能图片图生图极速版 快速高效图像处理_2098291440265809921.json, 图片生成/图生图/G-image-2.5图生图极速API｜批量重绘快人一步_2098743047059230722.json, 图片生成/图生图/G-image-2.5图生图高品质API｜重绘质感不掉线_2098739267697733633.json, 图片生成/图生图/G-image2.0低价渠道一号｜图生图省钱跑量必收藏_2103736051213885441.json, 图片生成/图生图/G-image2.0低价渠道二号｜图生图批量出图成本打下来_2103740749375426562.json, 图片生成/图生图/G-image2低价版图生图｜低成本高质量出图方案_2098715664189054978.json, 图片生成/图生图/G2图像编辑低价官方版-图生图工作流_2087389684388425730.json, 图片生成/图生图/G2图生图处理生成工具包集_2100669057442869249.json, 图片生成/图生图/H3人物三视图和场景图生成优化版V3工具-参考双图_2101865637562904577.json, 图片生成/图生图/MiniMax H3人物三视图可生成场景图生图处理工具_2102137579343794177.json, 图片生成/图生图/Minimax H3人物三视图和场景图生成 超清优化版_2105125698879975425.json, 图片生成/图生图/Minimax H3人物三视图和场景图生成超清优化版 角色设定批量产出_2109367390558580737.json, 图片生成/图生图/人物三视图场景图｜Minimax H3超清优化版图生图_2092918394403250177.json, 图片生成/图生图/全能图片G Image2.5图生图 高质量改图方案_2110368621951279106.json, 图片生成/图生图/单图模式图像编辑image2ENG全能图片G_2087115444502220802.json, 图片生成/图生图/商用版人物介绍产品四宫格 全能图片2图生图排版_2094236619254616065.json, 图片生成/图生图/商用版全能图片2｜人物介绍产品四宫格图生图生成_2094355396973649921.json, 图片生成/图生图/超清优化人物三视图场景图｜Minimax H3图生图生成_2092718678612729857.json, 图片生成/文生图/H3人物三视图和场景图生成优化版V3工具_2100664259473657857.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_34

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/G image2图像编辑单图模式-全能图片图生图工作流_2087371568707096578.json、图片生成/图生图/G-2.5全能图片图生图 高品质图像编辑版本_2098287173207420930.json、图片生成/图生图/G-2.5全能图片图生图极速版 快速高效图像处理_2098291440265809921.json、图片生成/图生图/G-image-2.5图生图极速API｜批量重绘快人一步_2098743047059230722.json、图片生成/图生图/G-image-2.5图生图高品质API｜重绘质感不掉线_2098739267697733633.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 21 个 workflow 都包含：
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
- `RH_RhartImageG2ImageToImage` —— 13/21 个有
- `CR Prompt Text` —— 11/21 个有
- `CR Text Concatenate` —— 9/21 个有
- `KOOK_SaveJPGImage` —— 9/21 个有
- `RH_RhartImageG25OfficialTokenSunburstEdit` —— 3/21 个有
- `Text` —— 3/21 个有
- `Label (rgthree)` —— 2/21 个有
- `RH_RhartImageG25OfficialTokenFlareEdit` —— 2/21 个有
- `RH_RhartImageNG31FlashImageToImage` —— 2/21 个有
- `RH_RhartImageNG31FlashOfficialImageToImage` —— 2/21 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 21 | 100% |
| 高度 | 80 | 80 - 80 | 21 | 100% |
| 采样步数 | 4 | 4 - 4 | 21 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 21 | 100% |
| 采样算法 | er_sde | - | 21 | 100% |
| 调度器 | beta | - | 21 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，21 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，21 个样本，一致性 100%
- 调度器 最常用 beta，21 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 高发问题（21/21 个样本）：Steps较低可能导致细节不足
