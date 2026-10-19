---
name: text_to_image_lora_sampler_clip_71
type: Text To Image
frequency: 11
level: strong
coverage: 0.889909
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/10步+3步Latent Upscaler｜H3参考模式图生视频_2091180204667531265.json, 视频生成/图生视频/48GB高配版6倍加速参考生视频｜MiniMax H3图生视频工作流_2088219969338302466.json, 视频生成/图生视频/4步多图自用提速｜H3图生视频快速参考生成_2089040496692916225.json, 视频生成/图生视频/6倍加速24GB通用版优化版｜MiniMax H3图生视频数字人工作流_2087156243797471233.json, 视频生成/图生视频/8步加速1.0正式版｜minimax 1.0视频生视频图生视频工作流_2088345029642379265.json, 视频生成/图生视频/BUNNY_H3单采er_sde手动Sigma，文生视频节奏随心控_2110519304910364674.json, 视频生成/图生视频/H3 Taomate 3步加速 中远距离不崩脸视频生成_2099588330131382273.json, 视频生成/图生视频/H3多图参考视频生成全注释 多图参考入门级工作流_2099204538879266817.json, 视频生成/图生视频/I2V lora加速｜MiniMax H3首帧图生视频3分40秒_2091174539307872258.json, 视频生成/图生视频/MiniMax H3 SelfLift双采对比普通双采图生视频处理工具_2101770093456871425.json, 视频生成/图生视频/双采样高清画质流｜H3图生视频画质增强直出_2092695582556114946.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_71

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/10步+3步Latent Upscaler｜H3参考模式图生视频_2091180204667531265.json、视频生成/图生视频/48GB高配版6倍加速参考生视频｜MiniMax H3图生视频工作流_2088219969338302466.json、视频生成/图生视频/4步多图自用提速｜H3图生视频快速参考生成_2089040496692916225.json、视频生成/图生视频/6倍加速24GB通用版优化版｜MiniMax H3图生视频数字人工作流_2087156243797471233.json、视频生成/图生视频/8步加速1.0正式版｜minimax 1.0视频生视频图生视频工作流_2088345029642379265.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 10/11 个有
- `CreateVideo` —— 10/11 个有
- `KSamplerSelect` —— 10/11 个有
- `ResolutionSelector` —— 10/11 个有
- `SaveVideo` —— 10/11 个有
- `MiniMaxH3ReferenceToVideo` —— 9/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/11 个有
- `SaveImage` —— 5/11 个有
- `LoadAudio` —— 4/11 个有
- `MiniMaxLowVRAMAttention` —— 4/11 个有
- `ModelAttentionBackend` —— 4/11 个有
- `ModelPreviewOverrideKJ` —— 4/11 个有
- `PathchSageAttentionKJ` —— 4/11 个有
- `EasyCache` —— 3/11 个有
- `ManualSigmas` —— 3/11 个有
- `MiniMaxChunkFeedForward` —— 3/11 个有
- `MiniMaxH3SigmaShift` —— 3/11 个有
- `SplitSigmas` —— 3/11 个有
- `VHS_VideoCombine` —— 3/11 个有
- `H3SigmaRefiner` —— 2/11 个有
- `ImageResizeKJv2` —— 2/11 个有
- `LTXVConcatAVLatent` —— 2/11 个有
- `LTXVSeparateAVLatent` —— 2/11 个有
- `MiniMaxH3ImageToVideo` —— 2/11 个有
- `MinimaxH3LatentUpscaler3D` —— 2/11 个有
- `SolAttnPatch` —— 2/11 个有
- `AddLabel` —— 1/11 个有
- `ConditioningZeroOut` —— 1/11 个有
- `FlashVSRNode` —— 1/11 个有
- `ImageConcatMulti` —— 1/11 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 1/11 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/11 个有
- `SelfLiftH3Sampler` —— 1/11 个有
- `Sleep` —— 1/11 个有
- `SpectrumSDXL` —— 1/11 个有
- `ZNGB_ResizeImage` —— 1/11 个有

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
