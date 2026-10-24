---
name: text_to_image_lora_sampler_clip_124
type: Text To Image
frequency: 12
level: strong
coverage: 0.87625
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMaxH3 HyperFlow｜8步多参考加首尾帧音频生成视频_2101501255758737410.json, 视频生成/图生视频/Minimax H3 I2v首帧参考｜图生视频一键直出_2092397758102724609.json, 视频生成/图生视频/Minimax H3尾帧参考图生视频｜高质量生成_2095562765640486913.json, 视频生成/图生视频/Minimax H3首尾帧both｜双参考图生视频生成_2095565532102742018.json, 视频生成/图生视频/Minimax H3首帧参考图生视频｜高质量生成_2095564155683168258.json, 视频生成/图生视频/加速版图生视频｜MiniMax H3人物场景特效生成_2094048249366802433.json, 视频生成/图生视频/图生视频加速版｜MiniMax H3人物场景特效生成_2093842351939743746.json, 视频生成/图生视频/官流直出美少女视频｜Minimax-H3 图生视频原汁原味_2096269567709499393.json, 视频生成/图生视频/首尾帧双向参考生成｜Minimax H3 I2v图生视频_2095810260463341570.json, 视频生成/图生视频/首帧参考图生视频｜Minimax H3 I2v起始帧生成_2095808793576824833.json, 视频生成/图生视频/高质量加速图生视频 Minimax H3 画质与速度兼顾快速出片_2094180356353249281.json, 视频生成/图生视频/高质量加速版图生视频｜Minimax H3一键高清生成_2094316328000778241.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_124

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3 HyperFlow｜8步多参考加首尾帧音频生成视频_2101501255758737410.json、视频生成/图生视频/Minimax H3 I2v首帧参考｜图生视频一键直出_2092397758102724609.json、视频生成/图生视频/Minimax H3尾帧参考图生视频｜高质量生成_2095562765640486913.json、视频生成/图生视频/Minimax H3首尾帧both｜双参考图生视频生成_2095565532102742018.json、视频生成/图生视频/Minimax H3首帧参考图生视频｜高质量生成_2095564155683168258.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 11/12 个有
- `PrimitiveFloat` —— 11/12 个有
- `ResolutionSelector` —— 11/12 个有
- `GetImageSize` —— 9/12 个有
- `ImageScaleToTotalPixels` —— 9/12 个有
- `PrimitiveStringMultiline` —— 9/12 个有
- `EasyCache` —— 7/12 个有
- `LoadImage` —— 6/12 个有
- `SDVN Load Image Url` —— 6/12 个有
- `MiniMaxH3SigmaShift` —— 3/12 个有
- `MiniMaxH3BlockCacheT8` —— 2/12 个有
- `ResizeImageMaskNode` —— 2/12 个有
- `AnySwitch` —— 1/12 个有
- `BlockSparseAttention` —— 1/12 个有
- `Fast Bypasser (rgthree)` —— 1/12 个有
- `MiniMaxH3ScheduledPictureReference` —— 1/12 个有
- `MiniMaxH3ScheduledReferenceToVideo` —— 1/12 个有
- `MiniMaxH3TurboLoRA` —— 1/12 个有
- `PixaromaDuration` —— 1/12 个有
- `PixaromaSizes` —— 1/12 个有

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
