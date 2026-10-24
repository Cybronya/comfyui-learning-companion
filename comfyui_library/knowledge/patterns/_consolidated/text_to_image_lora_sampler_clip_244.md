---
name: text_to_image_lora_sampler_clip_244
type: Text To Image
frequency: 8
level: strong
coverage: 0.885
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/博主直播带货照片开口卖货 数字人口播视频生成_2099915240774389761.json, 视频生成/图生视频/参考生视频｜RH万相3.0视频生视频图生视频_2092209020676427778.json, 视频生成/图生视频/商品广告视频｜Seedance 2.5首帧生10秒竖版，电商带货利器_2099924708010577921.json, 视频生成/图生视频/照片开口卖货｜博主直播带货数字人，模特产品展示一键生成_2099932046675238914.json, 视频生成/图生视频/爆款短视频复刻｜一张图动作运镜节奏一键迁移MiniMax H3_2089825604421115906.json, 视频生成/文生视频/30秒直出低价版｜Wan3.0全能参考生视频生成_2093213787812876289.json, 视频生成/文生视频/多参视频生成｜Wan 3.0全节点注释三模合一_2092203862093549569.json, 视频生成/文生视频/多模态全能视频生成｜Seedance 2.5文生图生视频生视频工作流_2088341212158840834.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_244

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/博主直播带货照片开口卖货 数字人口播视频生成_2099915240774389761.json、视频生成/图生视频/参考生视频｜RH万相3.0视频生视频图生视频_2092209020676427778.json、视频生成/图生视频/商品广告视频｜Seedance 2.5首帧生10秒竖版，电商带货利器_2099924708010577921.json、视频生成/图生视频/照片开口卖货｜博主直播带货数字人，模特产品展示一键生成_2099932046675238914.json、视频生成/图生视频/爆款短视频复刻｜一张图动作运镜节奏一键迁移MiniMax H3_2089825604421115906.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 6/8 个有
- `LoadVideo` —— 4/8 个有
- `RH_AlibabaWan30ReferenceToVideo` —— 3/8 个有
- `RunningHub FlashTalk Loader` —— 2/8 个有
- `RunningHub FlashTalk Sampler` —— 2/8 个有
- `Text` —— 2/8 个有
- `CreateVideo` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `RHMiniMaxH3RefGen` —— 1/8 个有
- `RH_BytedanceSeedance25GlobalTokenImageToVideo` —— 1/8 个有
- `RH_BytedanceSeedance25TokenMultimodalVideo` —— 1/8 个有
- `SaveImage` —— 1/8 个有

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
