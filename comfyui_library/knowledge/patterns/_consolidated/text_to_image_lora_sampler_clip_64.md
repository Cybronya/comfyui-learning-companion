---
name: text_to_image_lora_sampler_clip_64
type: Text To Image
frequency: 18
level: strong
coverage: 0.914611
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/低显存专用MiniMax H3双采多参 图生视频影视处理工具_2113040884995547137.json, 视频生成/图生视频/低显存也能跑 MiniMax H3双采参考生视频方案_2104650144351346689.json, 视频生成/图生视频/低显存友好方案｜时间分块前馈分块MiniMax H3双采参考生视频_2101157041715900417.json, 视频生成/图生视频/动态最强单采生成｜Dasiwa-MiniMax H3参考生视频_2095562835513405441.json, 视频生成/图生视频/动态最强参考生视频｜MiniMax H3 V1版图生视频_2095050766850551809.json, 视频生成/图生视频/参考生视频最强战斗效果｜MiniMax H3多图参考图生视频_2096673588765093890.json, 视频生成/图生视频/双时钟双采加速｜Latent Upscaler参考生视频H3版_2092746811000844289.json, 视频生成/图生视频/双时钟双采加速｜Minimax H3 Latent Upscaler图生视频_2091203656212373506.json, 视频生成/图生视频/双采V3图生视频工作流｜双倍采样画质更稳_2114176763180969986.json, 视频生成/图生视频/时间分块前馈分块降显存｜MiniMax H3双采参考生视频_2101187630208737281.json, 视频生成/图生视频/格莱美慢镜头质感 MiniMax H3双采参考生视频动态可控_2104360820577759233.json, 视频生成/图生视频/长视频Pov第一视角 MiniMax H3多参双采参考生视频_2105001173613899778.json, 视频生成/图生视频/长视频Pov第一视角 MiniMax H3多参双采参考生视频_2105078692375519233.json, 视频生成/图生视频/长视频Pov第一视角 MiniMax H3多参双采参考生视频_2105444809631686658.json, 视频生成/文生视频/30秒长视频文武双修均衡版高清 视频生成方案_2105053597879848962.json, 视频生成/文生视频/H3长视频优化版｜文生视频视频生视频图生视频全支持_2106981562544902146.json, 视频生成/文生视频/多参双采30秒直出 MiniMax H3参考生视频最强均衡版_2104298425591353346.json, 视频生成/文生视频/长视频优化版H3工作流，文生视频视频生视频图生视频方案_2107243300871827458.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_64

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/低显存专用MiniMax H3双采多参 图生视频影视处理工具_2113040884995547137.json、视频生成/图生视频/低显存也能跑 MiniMax H3双采参考生视频方案_2104650144351346689.json、视频生成/图生视频/低显存友好方案｜时间分块前馈分块MiniMax H3双采参考生视频_2101157041715900417.json、视频生成/图生视频/动态最强单采生成｜Dasiwa-MiniMax H3参考生视频_2095562835513405441.json、视频生成/图生视频/动态最强参考生视频｜MiniMax H3 V1版图生视频_2095050766850551809.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 17/18 个有
- `SolAttnMiniMax` —— 17/18 个有
- `VHS_VideoCombine` —— 15/18 个有
- `PrimitiveFloat` —— 14/18 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 13/18 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 13/18 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 13/18 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 12/18 个有
- `easy cleanGpuUsed` —— 12/18 个有
- `CreateVideo` —— 10/18 个有
- `Float` —— 10/18 个有
- `SaveVideo` —— 10/18 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 9/18 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 9/18 个有
- `SaveImage` —— 9/18 个有
- `easy anythingIndexSwitch` —— 9/18 个有
- `RunningHub Deepcleaner` —— 8/18 个有
- `Astra` —— 7/18 个有
- `JWFloat` —— 4/18 个有
- `MiniMaxH3ChunkedTwoPassPlanT8Advanced` —— 4/18 个有
- `MiniMaxH3ChunkedTwoPassUpscaleT8Advanced` —— 4/18 个有
- `PreviewAny` —— 4/18 个有
- `ConcatTextOfUtils` —— 1/18 个有
- `Fast Muter (rgthree)` —— 1/18 个有
- `GetNode` —— 1/18 个有
- `ImageCrop` —— 1/18 个有
- `ImageFromBatch` —— 1/18 个有
- `PrimitiveInt` —— 1/18 个有
- `SetNode` —— 1/18 个有
- `TrimAudioDuration` —— 1/18 个有
- `VHS_LoadVideo` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高发问题（19/18 个样本）：Steps较低可能导致细节不足
