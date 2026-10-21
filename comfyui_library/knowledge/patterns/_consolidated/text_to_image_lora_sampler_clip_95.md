---
name: text_to_image_lora_sampler_clip_95
type: Text To Image
frequency: 11
level: strong
coverage: 0.876909
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PathchSageAttentionKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMaxH3 HyperFlow｜8步多参考加首尾帧音频生成视频_2101501255758737410.json, 视频生成/图生视频/Minimax H3 I2v首帧参考｜图生视频一键直出_2092397758102724609.json, 视频生成/图生视频/Minimax H3多图参考视频流｜全节点中文注释齐全，新手也能看懂_2099470227150032898.json, 视频生成/图生视频/Minimax H3尾帧参考图生视频｜高质量生成_2095562765640486913.json, 视频生成/图生视频/Minimax H3首尾帧both｜双参考图生视频生成_2095565532102742018.json, 视频生成/图生视频/Minimax H3首帧参考图生视频｜高质量生成_2095564155683168258.json, 视频生成/图生视频/加速版图生视频｜MiniMax H3人物场景特效生成_2094048249366802433.json, 视频生成/图生视频/首尾帧双向参考生成｜Minimax H3 I2v图生视频_2095810260463341570.json, 视频生成/图生视频/首帧参考图生视频｜Minimax H3 I2v起始帧生成_2095808793576824833.json, 视频生成/文生视频/24GB通用版6倍加速参考生视频｜MiniMax H3文生图生视频生视频工作流_2087179601289236482.json, 视频生成/文生视频/48GB高配版6倍加速参考生视频｜MiniMax H3文生图生视频工作流_2087157477258383362.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_95

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3 HyperFlow｜8步多参考加首尾帧音频生成视频_2101501255758737410.json、视频生成/图生视频/Minimax H3 I2v首帧参考｜图生视频一键直出_2092397758102724609.json、视频生成/图生视频/Minimax H3多图参考视频流｜全节点中文注释齐全，新手也能看懂_2099470227150032898.json、视频生成/图生视频/Minimax H3尾帧参考图生视频｜高质量生成_2095562765640486913.json、视频生成/图生视频/Minimax H3首尾帧both｜双参考图生视频生成_2095565532102742018.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
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
- `EasyCache` —— 10/11 个有
- `PrimitiveFloat` —— 10/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `MiniMaxH3ImageToVideo` —— 8/11 个有
- `GetImageSize` —— 7/11 个有
- `ImageScaleToTotalPixels` —— 7/11 个有
- `SDVN Load Image Url` —— 6/11 个有
- `LoadImage` —— 5/11 个有
- `MiniMaxH3ReferenceToVideo` —— 3/11 个有
- `ImageResizeKJv2` —— 2/11 个有
- `LoadAudio` —— 2/11 个有
- `MiniMaxH3SigmaShift` —— 2/11 个有
- `AnySwitch` —— 1/11 个有
- `BlockSparseAttention` —— 1/11 个有
- `Fast Bypasser (rgthree)` —— 1/11 个有
- `MiniMaxH3ScheduledPictureReference` —— 1/11 个有
- `MiniMaxH3ScheduledReferenceToVideo` —— 1/11 个有
- `MiniMaxH3TurboLoRA` —— 1/11 个有
- `PixaromaDuration` —— 1/11 个有
- `PixaromaSizes` —— 1/11 个有
- `ResizeImageMaskNode` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
