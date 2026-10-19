---
name: text_to_image_lora_sampler_clip_68
type: Text To Image
frequency: 12
level: strong
coverage: 0.868917
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3超长视频流 一次直出2分15秒135S长视频_2110360650903023617.json, 视频生成/图生视频/MiniMax-H3 Ref2va参考生视频标准版｜高质量_2095566940180930561.json, 视频生成/图生视频/MiniMaxH3参考生视频量化加速版｜文本图像音频视频全模态，图生视频更快出活_2100449477902553090.json, 视频生成/图生视频/MiniMaxH3参考生视频量化加速｜文本图像音频视频全能_2089438111041409026.json, 视频生成/图生视频/Minimax H3多参生视频sag backend block cache 2倍速加速版_2088271045022277634.json, 视频生成/图生视频/minimax最强动作武打视频生视频，战斗特效一步到位_2111187364122030082.json, 视频生成/图生视频/无限长视频流工作流，图生视频长视频生成方案_2106530579587096577.json, 视频生成/图生视频/无限长视频流工作流，图生视频长视频生成方案_2106881388426383362.json, 视频生成/图生视频/无限长视频流工作流，图生视频长视频生成方案_2109439827979628546.json, 视频生成/图生视频/无限长视频流生成 多镜头角色表演图生视频_2098817794715504642.json, 视频生成/文生视频/MiniMax H3超长视频流一次直出2分15秒视频135秒，图生视频长视频方案_2107164033324511233.json, 视频生成/文生视频/MiniMax H3超长视频流｜一次直出2分15秒135S成片｜文生图生全支持_2101875396814917633.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_68

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3超长视频流 一次直出2分15秒135S长视频_2110360650903023617.json、视频生成/图生视频/MiniMax-H3 Ref2va参考生视频标准版｜高质量_2095566940180930561.json、视频生成/图生视频/MiniMaxH3参考生视频量化加速版｜文本图像音频视频全模态，图生视频更快出活_2100449477902553090.json、视频生成/图生视频/MiniMaxH3参考生视频量化加速｜文本图像音频视频全能_2089438111041409026.json、视频生成/图生视频/Minimax H3多参生视频sag backend block cache 2倍速加速版_2088271045022277634.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 11/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/12 个有
- `AudioConcat` —— 8/12 个有
- `GetImageRangeFromBatch` —— 8/12 个有
- `ImageBatchMulti` —— 8/12 个有
- `MiniMaxH3AddGuide` —— 8/12 个有
- `VHS_VideoCombine` —— 8/12 个有
- `LayerColor: ColorAdapter` —— 7/12 个有
- `SaveAudio` —— 7/12 个有
- `SaveImage` —— 7/12 个有
- `LoadAudio` —— 5/12 个有
- `CreateVideo` —— 4/12 个有
- `SaveVideo` —— 4/12 个有
- `ModelAttentionBackend` —— 3/12 个有
- `VHS_LoadVideo` —— 3/12 个有
- `EmptyImage` —— 2/12 个有
- `MiniMaxH3BlockCacheT8` —— 2/12 个有
- `PreviewImage` —— 2/12 个有
- `BlockSparseAttention` —— 1/12 个有
- `ComfyMiniMaxH3Director` —— 1/12 个有
- `EasyCache` —— 1/12 个有
- `LoadVideo` —— 1/12 个有
- `ManualSigmas` —— 1/12 个有
- `ModelPreviewOverrideKJ` —— 1/12 个有
- `PathchSageAttentionKJ` —— 1/12 个有
- `SaveAudioAdvanced` —— 1/12 个有
- `SolAttnMiniMax` —— 1/12 个有
- `TrimAudioDuration` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（14/12 个样本）：Steps较低可能导致细节不足
