---
name: text_to_image_upscale_latent_upscale_lora_3
type: Text To Image
frequency: 10
level: strong
coverage: 0.8285
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MinimaxH3LatentUpscaler3D, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 SelfLift双采对比普通双采图生视频处理工具_2101770093456871425.json, 视频生成/图生视频/MiniMax H3全能插件加音频设计 视频加音效一站式方案_2105420482479742977.json, 视频生成/图生视频/MiniMax H3全能插件升级｜音频设计加持视频创作_2105253049693458433.json, 视频生成/图生视频/MiniMax H3六图可选图生视频混合模型潜空间高清直出工作流，图生视频方案_2107977180578930690.json, 视频生成/图生视频/MiniMax H3双采潜空间放大图生视频处理工作流_2101380889010855937.json, 视频生成/图生视频/MiniMax H3首尾帧3步快速生成图生视频处理工具_2101395032807923714.json, 视频生成/图生视频/minimaxh3selflift二采音频参考｜三重加持稳定出片_2106239244355325953.json, 视频生成/图生视频/minimaxh3音频参考加持，selflift二采流程一键出片_2110442485200809985.json, 视频生成/图生视频/全能多模态二采放大｜H3加速sigma强化工作流_2092350860545314817.json, 视频生成/文生视频/MiniMax H3 SelfLift加二采加音频参考工作流，文生视频视频生视频图生视频_2106518365966786562.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_3

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 SelfLift双采对比普通双采图生视频处理工具_2101770093456871425.json、视频生成/图生视频/MiniMax H3全能插件加音频设计 视频加音效一站式方案_2105420482479742977.json、视频生成/图生视频/MiniMax H3全能插件升级｜音频设计加持视频创作_2105253049693458433.json、视频生成/图生视频/MiniMax H3六图可选图生视频混合模型潜空间高清直出工作流，图生视频方案_2107977180578930690.json、视频生成/图生视频/MiniMax H3双采潜空间放大图生视频处理工作流_2101380889010855937.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MinimaxH3LatentUpscaler3D`
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 9/10 个有
- `MiniMaxH3ReferenceToVideo` —— 9/10 个有
- `ModelAttentionBackend` —— 9/10 个有
- `ModelPreviewOverrideKJ` —— 9/10 个有
- `CreateVideo` —— 8/10 个有
- `SaveImage` —— 8/10 个有
- `SplitSigmas` —— 7/10 个有
- `VHS_VideoCombine` —— 7/10 个有
- `MiniMaxChunkFeedForward` —— 6/10 个有
- `MiniMaxH3SigmaShift` —— 6/10 个有
- `MiniMaxLowVRAMAttention` —— 6/10 个有
- `GetNode` —— 5/10 个有
- `LoadAudio` —— 5/10 个有
- `SaveVideo` —— 5/10 个有
- `SetNode` —— 5/10 个有
- `ConditioningZeroOut` —— 4/10 个有
- `Fast Groups Bypasser (rgthree)` —— 4/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/10 个有
- `PlaySound|pysssss` —— 3/10 个有
- `SelfLiftAvatarH3Sampler` —— 3/10 个有
- `ManualSigmas` —— 2/10 个有
- `MiniMaxH3Unified` —— 2/10 个有
- `SolAttnMiniMax` —— 2/10 个有
- `Vignette` —— 2/10 个有
- `AddLabel` —— 1/10 个有
- `Fast Groups Muter (rgthree)` —— 1/10 个有
- `GetVideoComponents` —— 1/10 个有
- `ImageConcatMulti` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `LoadVideo` —— 1/10 个有
- `MiniMaxH3BlockCacheT8` —— 1/10 个有
- `MiniMaxH3ImageToVideo` —— 1/10 个有
- `SelfLiftH3Sampler` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
