---
name: text_to_image_lora_sampler_clip_120
type: Text To Image
frequency: 13
level: strong
coverage: 0.893154
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MiniMax H3多图参考官方提示词模板｜提速40%无劣化真人短剧剧情演绎数字人_2090475334801125378.json, 数字人/数字人/minimax开源版中文锁定语音H3稳定4步lora加速版优化版图生视频_2086193213840384002.json, 数字人/数字人/官方提示词模板提速40%｜MiniMax H3多图参考真人短剧演绎_2090193856364109826.json, 视频生成/图生视频/10Eros-Max Minimax BF16超级融合参考生视频-高质量加速版TEST3_2087401342334758913.json, 视频生成/图生视频/48GB高配版6倍加速参考生视频｜MiniMax H3图生视频工作流_2088219969338302466.json, 视频生成/图生视频/4步多图自用提速｜H3图生视频快速参考生成_2089040496692916225.json, 视频生成/图生视频/6倍加速24GB通用版优化版｜MiniMax H3图生视频数字人工作流_2087156243797471233.json, 视频生成/图生视频/MiniMax H3图生视频6倍加速48GB高配版｜速度狂飙_2113980295203606530.json, 视频生成/图生视频/MiniMax H3稳定加速版｜打斗脸部修复lora整合_2098767286873182210.json, 视频生成/图生视频/MiniMaxH3参考生视频量化加速｜文本图像音频视频全能_2089438111041409026.json, 视频生成/图生视频/MinimaxH3开源版全能多参｜视频参考标准加速集合版_2095262567538192386.json, 视频生成/文生视频/MiNiMaxH3全能参考文生视频图生视频视频生视频普通加速版_2088368737501143041.json, 视频生成/文生视频/全能参考文生图生视频生视频｜MiNiMaxH3视频生成工作流_2088334930496548865.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_120

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（数字人/数字人/MiniMax H3多图参考官方提示词模板｜提速40%无劣化真人短剧剧情演绎数字人_2090475334801125378.json、数字人/数字人/minimax开源版中文锁定语音H3稳定4步lora加速版优化版图生视频_2086193213840384002.json、数字人/数字人/官方提示词模板提速40%｜MiniMax H3多图参考真人短剧演绎_2090193856364109826.json、视频生成/图生视频/10Eros-Max Minimax BF16超级融合参考生视频-高质量加速版TEST3_2087401342334758913.json、视频生成/图生视频/48GB高配版6倍加速参考生视频｜MiniMax H3图生视频工作流_2088219969338302466.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 11/13 个有
- `KSamplerSelect` —— 11/13 个有
- `PrimitiveStringMultiline` —— 11/13 个有
- `SaveVideo` —— 11/13 个有
- `MiniMaxH3ReferenceToVideo` —— 9/13 个有
- `PathchSageAttentionKJ` —— 8/13 个有
- `LoadAudio` —— 7/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/13 个有
- `VHS_VideoCombine` —— 7/13 个有
- `EasyCache` —— 5/13 个有
- `LoraLoaderBypassModelOnly` —— 5/13 个有
- `MiniMaxH3AudioConditioningT8` —— 5/13 个有
- `VHS_LoadVideo` —— 5/13 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 4/13 个有
- `AudioCrop` —— 3/13 个有
- `ImageResizeKJv2` —— 3/13 个有
- `MiniMaxH3AVDecodeT8` —— 3/13 个有
- `忽略多组孤海` —— 3/13 个有
- `GetImageSize` —— 2/13 个有
- `MiniMaxH3BlockCacheT8` —— 2/13 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/13 个有
- `MiniMaxH3ImageToVideo` —— 2/13 个有
- `ResizeImageMaskNode` —— 2/13 个有
- `Textbox` —— 2/13 个有
- `ComfyMiniMaxH3Director` —— 1/13 个有
- `Label (rgthree)` —— 1/13 个有
- `ModelAttentionBackend` —— 1/13 个有
- `SolAttnMiniMax` —— 1/13 个有
- `SpectrumSDXL` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
