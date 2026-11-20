---
name: text_to_image_lora_sampler_clip_194
type: Text To Image
frequency: 10
level: strong
coverage: 0.8058
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/lightx2v不同版加速Lora测试｜Minimax H3图生视频对比_2096727729675788289.json, 视频生成/图生视频/lightx2v正式版参考模式｜minimax_h3视频生视频图生视频工作流_2088211325951504385.json, 视频生成/图生视频/minimax h3 r2v Latent Upscaler｜图生视频二采放大_2092058189146710017.json, 视频生成/图生视频/minimax h3最强动作迁移｜视频图生视频直出_2092048558504628226.json, 视频生成/图生视频/minimax_h3_r2v复杂镜头运动｜视频生视频运镜_2095302998342848513.json, 视频生成/图生视频/r2v故事板分镜生成｜minimax_h3图生视频直出_2092737402887561218.json, 视频生成/图生视频/sigma强化超清放大1080P｜Minimax H3脸不崩打斗不糊_2095111117046640641.json, 视频生成/图生视频/二次采样放大文戏工作流｜MiniMax_H3图生视频精修_2096324113731248129.json, 视频生成/图生视频/双模双采小脸不崩｜Minimax H3高动态不崩脸视频_2093486007596437506.json, 视频生成/图生视频/双模双采资源面板短剧助手 MiniMax H3 全能参考生成视频_2094255084355022849.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_194

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/lightx2v不同版加速Lora测试｜Minimax H3图生视频对比_2096727729675788289.json、视频生成/图生视频/lightx2v正式版参考模式｜minimax_h3视频生视频图生视频工作流_2088211325951504385.json、视频生成/图生视频/minimax h3 r2v Latent Upscaler｜图生视频二采放大_2092058189146710017.json、视频生成/图生视频/minimax h3最强动作迁移｜视频图生视频直出_2092048558504628226.json、视频生成/图生视频/minimax_h3_r2v复杂镜头运动｜视频生视频运镜_2095302998342848513.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：81%

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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/10 个有
- `ModelAttentionBackend` —— 9/10 个有
- `MiniMaxH3SigmaShift` —— 8/10 个有
- `CreateVideo` —— 7/10 个有
- `LTXVConcatAVLatent` —— 7/10 个有
- `LTXVSeparateAVLatent` —— 7/10 个有
- `MinimaxH3LatentUpscaler3D` —— 7/10 个有
- `ModelPreviewOverrideKJ` —— 7/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `SaveVideo` —— 7/10 个有
- `SplitSigmas` —— 7/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/10 个有
- `GetNode` —— 5/10 个有
- `SetNode` —— 5/10 个有
- `H3SigmaRefiner` —— 4/10 个有
- `VHS_VideoCombine` —— 4/10 个有
- `CR Prompt Text` —— 3/10 个有
- `ManualSigmas` —— 3/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `MiniMaxLowVRAMAttention` —— 2/10 个有
- `SolAttnMiniMax` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `easy cleanGpuUsed` —— 2/10 个有
- `AddLabel` —— 1/10 个有
- `Anything Everywhere` —— 1/10 个有
- `Anything Everywhere3` —— 1/10 个有
- `DF_Integer` —— 1/10 个有
- `Float` —— 1/10 个有
- `ImageConcatMulti` —— 1/10 个有
- `MiniMaxH3AddGuide` —— 1/10 个有
- `MiniMaxH3MediaLoaderFantastic` —— 1/10 个有
- `MiniMaxH3ReferenceSplitter` —— 1/10 个有
- `MinimaxH3LatentUpscalerNode2D` —— 1/10 个有
- `RTXVideoSuperResolution` —— 1/10 个有
- `UniBlockSwapTE` —— 1/10 个有

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
