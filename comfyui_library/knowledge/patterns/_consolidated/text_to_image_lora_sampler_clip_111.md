---
name: text_to_image_lora_sampler_clip_111
type: Text To Image
frequency: 13
level: strong
coverage: 0.863385
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3超长视频流 一次直出2分15秒135S长视频_2110360650903023617.json, 视频生成/图生视频/MiniMax-H3 Ref2va参考生视频标准版｜高质量_2095566940180930561.json, 视频生成/图生视频/MiniMax-H3-多图参考视频生成（Lightx2v加速）_2086208730663841794.json, 视频生成/图生视频/MiniMaxH3四关键帧视频生成｜KeyFrames X4工作流_2094875841221185538.json, 视频生成/图生视频/Minimax H3三图参考无参考音｜图生视频多图参考_2089732304192237570.json, 视频生成/图生视频/Minimax H3多参生视频sag backend block cache 2倍速加速版_2088271045022277634.json, 视频生成/图生视频/Minimax-H3多参长视频736p直出｜原版图生视频工作流_2097088563040051202.json, 视频生成/图生视频/无限长视频流工作流，图生视频长视频生成方案_2106530579587096577.json, 视频生成/图生视频/无限长视频流工作流，图生视频长视频生成方案_2106881388426383362.json, 视频生成/图生视频/无限长视频流工作流，图生视频长视频生成方案_2109439827979628546.json, 视频生成/图生视频/无限长视频流生成 多镜头角色表演图生视频_2098817794715504642.json, 视频生成/文生视频/MiniMax H3超长视频流一次直出2分15秒视频135秒，图生视频长视频方案_2107164033324511233.json, 视频生成/文生视频/MiniMax H3超长视频流｜一次直出2分15秒135S成片｜文生图生全支持_2101875396814917633.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_111

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3超长视频流 一次直出2分15秒135S长视频_2110360650903023617.json、视频生成/图生视频/MiniMax-H3 Ref2va参考生视频标准版｜高质量_2095566940180930561.json、视频生成/图生视频/MiniMax-H3-多图参考视频生成（Lightx2v加速）_2086208730663841794.json、视频生成/图生视频/MiniMaxH3四关键帧视频生成｜KeyFrames X4工作流_2094875841221185538.json、视频生成/图生视频/Minimax H3三图参考无参考音｜图生视频多图参考_2089732304192237570.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：86%

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
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 12/13 个有
- `孤海注释` —— 12/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/13 个有
- `VHS_VideoCombine` —— 9/13 个有
- `MiniMaxH3AddGuide` —— 8/13 个有
- `AudioConcat` —— 7/13 个有
- `GetImageRangeFromBatch` —— 7/13 个有
- `ImageBatchMulti` —— 7/13 个有
- `LayerColor: ColorAdapter` —— 7/13 个有
- `SaveAudio` —— 7/13 个有
- `SaveImage` —— 7/13 个有
- `CreateVideo` —— 4/13 个有
- `SaveVideo` —— 4/13 个有
- `LoadAudio` —— 3/13 个有
- `ModelAttentionBackend` —— 3/13 个有
- `MiniMaxH3SigmaShift` —— 2/13 个有
- `EmptyImage` —— 1/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `INTConstant` —— 1/13 个有
- `LoadVideo` —— 1/13 个有
- `LoadVideoUI` —— 1/13 个有
- `MiniMaxH3BlockCacheT8` —— 1/13 个有
- `MiniMaxH3MotionContext` —— 1/13 个有
- `MiniMaxH3MotionContextTrim` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `TrimAudioDuration` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（15/13 个样本）：Steps较低可能导致细节不足
