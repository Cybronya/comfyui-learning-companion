---
name: text_to_image_lora_sampler_clip_95
type: Text To Image
frequency: 14
level: strong
coverage: 0.881071
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/text to Image 2.0 RH性价比版全能图片G2文生图工作流_2088373457695363074.json, 图片生成/文生图/text to Image 2.0 RH性价比版文生图｜全能图片G2图片生成工作流_2088342587194302465.json, 图片生成/文生图/人像写真文生图｜Image 2图像模型图生图全能_2090822423569584129.json, 图片生成/文生图/人像写真文生图｜Image 2图像模型图生图直出_2090527437456236545.json, 图片生成/文生图/全能图片2.0文生图｜实用文字生成图片工具_2090819768029896706.json, 图片生成/文生图/全能图片G image 2.0文生图官方稳定版｜文生图放心冲_2111830361557786625.json, 图片生成/文生图/全能图片G-2.0文生图｜低价渠道API专用快速出图_2096294843915005953.json, 图片生成/文生图/全能图片G2.5图生图 最强生图模型文生图创作_2099903841104916481.json, 图片生成/文生图/全能图片G2.5文生图 最强生图模型图片生成_2099905456335572994.json, 图片生成/文生图/场景道具图单图文生图（真实感）_2106398654545358849.json, 图片生成/文生图/场景道具图批量文生图｜布景陈设素材一键出全套_2103107503109263362.json, 图片生成/文生图/海报分镜低成本｜全能图片G-2.0文生图API专用版_2096552763491704833.json, 视频生成/图生视频/全能图片2.0多宫格故事板 角色分镜批量出图_2098854307813740546.json, 视频生成/文生视频/小说原文转15秒漫剧｜Seedance2.5一键文生视频生成_2092553338125643778.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_95

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/text to Image 2.0 RH性价比版全能图片G2文生图工作流_2088373457695363074.json、图片生成/文生图/text to Image 2.0 RH性价比版文生图｜全能图片G2图片生成工作流_2088342587194302465.json、图片生成/文生图/人像写真文生图｜Image 2图像模型图生图全能_2090822423569584129.json、图片生成/文生图/人像写真文生图｜Image 2图像模型图生图直出_2090527437456236545.json、图片生成/文生图/全能图片2.0文生图｜实用文字生成图片工具_2090819768029896706.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 14 个 workflow 都包含：
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
- `孤海注释` —— 13/14 个有
- `RH_RhartImageG2TextToImage` —— 10/14 个有
- `CR Prompt Text` —— 6/14 个有
- `LoadImage` —— 5/14 个有
- `RH_RhartImageG2ImageToImage` —— 4/14 个有
- `RH_RhartImageG2OfficialImageToImage` —— 3/14 个有
- `RH_RhartImageG2OfficialTextToImage` —— 3/14 个有
- `Fast Groups Muter (rgthree)` —— 2/14 个有
- `ShowAnything|Mie` —— 2/14 个有
- `RHHiddenNodes` —— 1/14 个有
- `RHLLMChatNode` —— 1/14 个有
- `RH_BytedanceSeedance25TokenMultimodalVideo` —— 1/14 个有
- `SaveVideo` —— 1/14 个有
- `ShowText|pysssss` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
