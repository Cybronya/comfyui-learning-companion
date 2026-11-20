---
name: text_to_image_lora_sampler_clip_168
type: Text To Image
frequency: 10
level: strong
coverage: 0.6235
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, INTConstant, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResizeShortestToNode, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MINImax-H3全自动视频编辑流 人物替换迁移一步到位_2094818687348989954.json, 平台全量/二采重绘v2超级加强清晰度天花板｜minimax h3视频生视频工作流_2088123445790986241.json, 视频生成/图生视频/MiniMax-H3全功能疾速多参高清二采加速｜角色一致性视频生视频图生视频_2089701921434193922.json, 视频生成/图生视频/Minimax H3二采重绘效率流｜秒变清晰不丢一致性，出片效率起飞_2099519441183789057.json, 视频生成/图生视频/MinimaxH3全能参考提示词自动反推版！ENGENG开源视频模型真神！！_2087149888927780865.json, 视频生成/图生视频/单模型无编解码二采放大｜Minimax H3全能参考自动反推提示词 13 浏览 0 点赞 0 收藏_2092299427519225857.json, 视频生成/图生视频/双采高清人脸视频生成｜Minimax自动提示词加最新加速lora_2090470050162630658.json, 视频生成/图生视频/多参二采加速｜minimax-h3全功能疾速高清 鸭鸭图私密版直出_2089425542838841345.json, 视频生成/文生视频/minimaxH3混合模型sigma强化｜潜空间放大高清直出_2094545098968227842.json, 视频生成/文生视频/sigma强化不油腻混合模型｜minimaxH3潜空间放大高清直出_2094790731905986562.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_168

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/MINImax-H3全自动视频编辑流 人物替换迁移一步到位_2094818687348989954.json、平台全量/二采重绘v2超级加强清晰度天花板｜minimax h3视频生视频工作流_2088123445790986241.json、视频生成/图生视频/MiniMax-H3全功能疾速多参高清二采加速｜角色一致性视频生视频图生视频_2089701921434193922.json、视频生成/图生视频/Minimax H3二采重绘效率流｜秒变清晰不丢一致性，出片效率起飞_2099519441183789057.json、视频生成/图生视频/MinimaxH3全能参考提示词自动反推版！ENGENG开源视频模型真神！！_2087149888927780865.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeShortestToNode`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 8/10 个有
- `RHLLMChatNode` —— 8/10 个有
- `VHS_LoadVideo` —— 8/10 个有
- `easy clearCacheAll` —— 8/10 个有
- `easy showAnything` —— 8/10 个有
- `孤海注释` —— 8/10 个有
- `EasyCache` —— 7/10 个有
- `LoadAudio` —— 7/10 个有
- `ModelAttentionBackend` —— 7/10 个有
- `LoraLoaderBypassModelOnly` —— 5/10 个有
- `PT_H3ConcatAVLatent` —— 5/10 个有
- `SaveVideo` —— 5/10 个有
- `StringFunction|pysssss` —— 5/10 个有
- `VAEEncode` —— 5/10 个有
- `VAEEncodeAudio` —— 5/10 个有
- `VHS_VideoCombine` —— 5/10 个有
- `LTXVConcatAVLatent` —— 4/10 个有
- `LTXVSeparateAVLatent` —— 4/10 个有
- `MinimaxH3LatentUpscaler3D` —— 4/10 个有
- `SplitSigmas` —— 4/10 个有
- `TrimAudioDuration` —— 4/10 个有
- `AudioCrop` —— 3/10 个有
- `H3SigmaRefiner` —— 3/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/10 个有
- `ModelPreviewOverrideKJ` —— 3/10 个有
- `MuyeTextEditOutput` —— 3/10 个有
- `PathchSageAttentionKJ` —— 3/10 个有
- `SolAttnMiniMax` —— 3/10 个有
- `easy float` —— 3/10 个有
- `DuckHideNode` —— 2/10 个有
- `HAIGC_SaveImagesToZip` —— 2/10 个有
- `Label (rgthree)` —— 2/10 个有
- `SaveImage` —— 2/10 个有
- `easy imageSize` —— 2/10 个有
- `CR String To Number` —— 1/10 个有
- `GetImageRangeFromBatch` —— 1/10 个有
- `LoadVideo` —— 1/10 个有
- `VHS_VideoInfo` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
