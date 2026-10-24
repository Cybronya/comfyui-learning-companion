---
name: text_to_image_lora_sampler_clip_29
type: Text To Image
frequency: 22
level: strong
coverage: 0.890864
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/SeeThrough二次元PSD分层拆图｜live2D动画游戏创意图生图_2091647857257435137.json, 图片生成/图生图/openAI生图工作流｜图生图创意绘图模板直出_2097897249505374210.json, 图片生成/图生图/openAI生图工作流｜图生图图片生成处理_2097844315547594753.json, 图片生成/图生图/openAI生图工作流｜智能图生图创意绘制方案_2097898857920294913.json, 图片生成/图生图/ywt达人日常图生图｜生活感达人日常内容一键生成_2104524267881844738.json, 图片生成/图生图/上衣替换换衣服｜Image2服装替换展示图生图生成_2094802942401536001.json, 图片生成/图生图/二次元PSD分层拆图｜SeeThrough live2D动画游戏创意形象图生图_2089431325555126274.json, 图片生成/图生图/二次元PSD分层拆图｜SeeThrough拆23层live2D动画游戏_2091810480326270978.json, 图片生成/图生图/全功能图生图处理生成综合工作流工具包配置_2101020931924783105.json, 图片生成/图生图/全能G2图生图工作流｜多场景图像编辑处理生成_2096733211073273858.json, 图片生成/图生图/全能图片G2.0低价渠道版图生图工作流，通用图片生成与编辑_2102811484857393154.json, 图片生成/图生图/全能图片G2.0低价渠道版工作流，图生图图像处理方案_2107522530834739202.json, 图片生成/图生图/全能图片G2.0低价渠道版｜图生图成本打下来｜日常批量出图更划算_2102577836518367234.json, 图片生成/图生图/全能图片G2.0图生图 低价渠道高性价比出图_2104290534352310273.json, 图片生成/图生图/全能图片G2.0｜低价渠道版图生图处理直出_2090931490459840514.json, 图片生成/图生图/全能图片编辑助手｜图生图多场景通用一键处理_2105240455175819265.json, 图片生成/图生图/卡塔尔饰品海报一键生成｜图生图中东异域风情海报素材_2099160429791633409.json, 图片生成/图生图/图生图实用重绘工具｜全能图片2.0一键出图_2090818490918854657.json, 图片生成/图生图/埃及饰品海报图生图方案｜古埃及风饰品宣传图批量产出_2099164243470938113.json, 图片生成/图生图/建筑效果图重新渲染｜光源布光自由控制重出图_2101547236311257089.json, 图片生成/图生图/沙特饰品海报工作流｜图生图批量做沙特风珠宝宣传图_2099161734425694210.json, 图片生成/图生图/西班牙饰品海报制作神器｜图生图欧式风情饰品海报量产_2099166819130105858.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/SeeThrough二次元PSD分层拆图｜live2D动画游戏创意图生图_2091647857257435137.json、图片生成/图生图/openAI生图工作流｜图生图创意绘图模板直出_2097897249505374210.json、图片生成/图生图/openAI生图工作流｜图生图图片生成处理_2097844315547594753.json、图片生成/图生图/openAI生图工作流｜智能图生图创意绘制方案_2097898857920294913.json、图片生成/图生图/ywt达人日常图生图｜生活感达人日常内容一键生成_2104524267881844738.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 22 个 workflow 都包含：
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
- `RH_RhartImageG2ImageToImage` —— 19/22 个有
- `RH_RhartImageG2OfficialImageToImage` —— 3/22 个有
- `SeeThrough_GenerateDepth` —— 3/22 个有
- `SeeThrough_GenerateLayers` —— 3/22 个有
- `SeeThrough_LoadDepthModel` —— 3/22 个有
- `SeeThrough_LoadLayerDiffModel` —— 3/22 个有
- `SeeThrough_PostProcess` —— 3/22 个有
- `SeeThrough_SavePSD` —— 3/22 个有
- `Image Comparer (rgthree)` —— 2/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 22 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 22 | 100% |
| 采样算法 | er_sde | - | 22 | 100% |
| 调度器 | beta | - | 22 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |
| 宽度 | 80 | 80 - 80 | 22 | 100% |
| 高度 | 80 | 80 - 80 | 22 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，22 个样本，一致性 100%
- 调度器 最常用 beta，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高发问题（22/22 个样本）：Steps较低可能导致细节不足
