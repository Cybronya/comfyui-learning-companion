---
name: text_to_image_lora_sampler_clip_16
type: Text To Image
frequency: 20
level: strong
coverage: 0.8718
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/v2.0多参双采样图影音｜minimax h3电影感大片生成_2094317653564420098.json, 视频生成/图生视频/全能多参生视频自用版｜Minimax H3 人物场景类特效_2089349057071378433.json, 视频生成/图生视频/动作迁移图生视频｜Minimax视频动作迁移工作流_2087218060968161281.json, 视频生成/图生视频/去除ai感全能参考｜minimax h3转场运镜图生视频_2093435277451812865.json, 视频生成/图生视频/去除ai感转场运镜｜minimax h3全能参考图生视频_2093764750915231745.json, 视频生成/图生视频/声音）4步lora视频MinimaxH3-多参生视频（图片_2087336403087745025.json, 视频生成/图生视频/多元素参考生视频｜minimax h3图生视频直出_2092387092469993474.json, 视频生成/图生视频/多参双采样图影音电影感大片 minimax h3 v2.0视频制作_2094183296849768450.json, 视频生成/图生视频/多参格斗动作迁移背景替换8步加速 MiniMax-H3开源版视频生视频_2094024779476062210.json, 视频生成/图生视频/多参格斗动作迁移背景替换8步加速 MiniMax-H3开源版视频生视频_2097104058355113986.json, 视频生成/图生视频/多参格斗动作迁移背景替换｜MiniMax-H3开源8步加速_2093774376658366465.json, 视频生成/图生视频/多参格斗动作迁移背景替换｜MiniMax-H3开源8步加速_2094009514365374466.json, 视频生成/图生视频/极致电影质感｜Minimax-H3转场运镜图生视频_2093229463424299009.json, 视频生成/图生视频/格斗动作迁移背景替换8步加速 MiniMax-H3多参数图生视频方案_2093216713595768833.json, 视频生成/图生视频/电影级视频多参版v1.0｜minimax H3制作工作流_2093475759825440770.json, 视频生成/图生视频/电影质感极致呈现｜Minimax-H3运镜转场图生视频_2093071322497769473.json, 视频生成/文生视频/H3真实电影质感全能参考 文生视频图生视频_2100309862587654145.json, 视频生成/文生视频/真实电影质感｜MiniMax H3文生图生视频生成_2094051162357063682.json, 视频生成/文生视频/真实电影质感｜MiniMax H3文生图生视频直出_2093845276451753986.json, 视频生成/视频生视频/多参格斗动作迁移背景替换8步加速 MiniMax-H3开源版视频生视频_2106163123605561346.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_16

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/v2.0多参双采样图影音｜minimax h3电影感大片生成_2094317653564420098.json、视频生成/图生视频/全能多参生视频自用版｜Minimax H3 人物场景类特效_2089349057071378433.json、视频生成/图生视频/动作迁移图生视频｜Minimax视频动作迁移工作流_2087218060968161281.json、视频生成/图生视频/去除ai感全能参考｜minimax h3转场运镜图生视频_2093435277451812865.json、视频生成/图生视频/去除ai感转场运镜｜minimax h3全能参考图生视频_2093764750915231745.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 19/20 个有
- `PrimitiveFloat` —— 19/20 个有
- `VHS_LoadVideo` —— 19/20 个有
- `PrimitiveStringMultiline` —— 18/20 个有
- `MiniMaxH3BlockCacheT8` —— 16/20 个有
- `Fast Groups Bypasser (rgthree)` —— 12/20 个有
- `LoadAudio` —— 12/20 个有
- `PathchSageAttentionKJ` —— 12/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/20 个有
- `easy anythingIndexSwitch` —— 10/20 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/20 个有
- `Int` —— 7/20 个有
- `GetImageRangeFromBatch` —— 6/20 个有
- `GetVideoComponents` —— 6/20 个有
- `ImageConcatMulti` —— 6/20 个有
- `ImageResizeKJv2` —— 6/20 个有
- `MiniMaxH3ImageToVideo` —— 6/20 个有
- `PreviewImage` —— 6/20 个有
- `RMBG` —— 6/20 个有
- `VHS_GetImageCount` —— 6/20 个有
- `VRAM_Debug` —— 6/20 个有
- `easy showAnything` —— 6/20 个有
- `DisableNoise` —— 5/20 个有
- `H3SigmaRefiner` —— 5/20 个有
- `SplitSigmas` —— 5/20 个有
- `LoraLoaderBypassModelOnly` —— 2/20 个有
- `Load Lora` —— 1/20 个有
- `SaveImage` —— 1/20 个有
- `SimpleMath+` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（20/20 个样本）：Steps较低可能导致细节不足
