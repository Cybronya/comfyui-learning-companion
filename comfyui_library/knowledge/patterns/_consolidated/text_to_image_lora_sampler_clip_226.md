---
name: text_to_image_lora_sampler_clip_226
type: Text To Image
frequency: 9
level: strong
coverage: 0.873667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PathchSageAttentionKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMaxH3 HyperFlow｜8步多参考加首尾帧音频生成视频_2101501255758737410.json, 视频生成/图生视频/Minimax H3 I2v首帧参考｜图生视频一键直出_2092397758102724609.json, 视频生成/图生视频/Minimax H3尾帧参考图生视频｜高质量生成_2095562765640486913.json, 视频生成/图生视频/Minimax H3无色差版｜首尾帧参考生视频电商模特展示_2089376588533157889.json, 视频生成/图生视频/Minimax H3首尾帧both｜双参考图生视频生成_2095565532102742018.json, 视频生成/图生视频/Minimax H3首帧参考图生视频｜高质量生成_2095564155683168258.json, 视频生成/图生视频/加速版图生视频｜MiniMax H3人物场景特效生成_2094048249366802433.json, 视频生成/图生视频/首尾帧双向参考生成｜Minimax H3 I2v图生视频_2095810260463341570.json, 视频生成/图生视频/首帧参考图生视频｜Minimax H3 I2v起始帧生成_2095808793576824833.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_226

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3 HyperFlow｜8步多参考加首尾帧音频生成视频_2101501255758737410.json、视频生成/图生视频/Minimax H3 I2v首帧参考｜图生视频一键直出_2092397758102724609.json、视频生成/图生视频/Minimax H3尾帧参考图生视频｜高质量生成_2095562765640486913.json、视频生成/图生视频/Minimax H3无色差版｜首尾帧参考生视频电商模特展示_2089376588533157889.json、视频生成/图生视频/Minimax H3首尾帧both｜双参考图生视频生成_2095565532102742018.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
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
- `PathchSageAttentionKJ`
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
- `PrimitiveFloat` —— 8/9 个有
- `EasyCache` —— 7/9 个有
- `GetImageSize` —— 7/9 个有
- `ImageScaleToTotalPixels` —— 7/9 个有
- `PrimitiveStringMultiline` —— 7/9 个有
- `SDVN Load Image Url` —— 6/9 个有
- `LoadImage` —— 3/9 个有
- `MiniMaxH3SigmaShift` —— 3/9 个有
- `AnySwitch` —— 1/9 个有
- `BlockSparseAttention` —— 1/9 个有
- `Fast Bypasser (rgthree)` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `MiniMaxH3HybridLoader` —— 1/9 个有
- `MiniMaxH3ScheduledPictureReference` —— 1/9 个有
- `MiniMaxH3ScheduledReferenceToVideo` —— 1/9 个有
- `MiniMaxH3TurboLoRA` —— 1/9 个有
- `PixaromaDuration` —— 1/9 个有
- `PixaromaSizes` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `ResizeImageMaskNode` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
