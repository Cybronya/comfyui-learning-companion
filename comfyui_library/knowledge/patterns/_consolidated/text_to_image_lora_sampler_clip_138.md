---
name: text_to_image_lora_sampler_clip_138
type: Text To Image
frequency: 12
level: strong
coverage: 0.788333
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/写英文工作流｜数字人英文口播视频生成专用流_2114020800511696898.json, 视频生成/图生视频/10步+3步Latent Upscaler｜H3参考模式图生视频_2091180204667531265.json, 视频生成/图生视频/BUNNY_H3单采er_sde手动Sigma，文生视频节奏随心控_2110519304910364674.json, 视频生成/图生视频/H3 Taomate 3步加速 中远距离不崩脸视频生成_2099588330131382273.json, 视频生成/图生视频/H3 sigma强化超清放大｜1080P打斗不糊脸不崩视频_2094933026361921538.json, 视频生成/图生视频/H3一键角色替换 图生视频换人剪辑神器工作流推荐_2094810569621725186.json, 视频生成/图生视频/H3潜空间放大工作流｜图生视频画质提升_2090444142102011905.json, 视频生成/图生视频/H3视频衔接工作流｜多段视频无缝拼接生成_2095211983237894146.json, 视频生成/图生视频/sigma强化超清放大1080P｜Minimax H3脸不崩打斗不糊_2095111117046640641.json, 视频生成/图生视频/双采样高清画质流｜H3图生视频画质增强直出_2092695582556114946.json, 视频生成/图生视频/视频衔接无缝续接生成｜H3图生视频工作流_2095490694986166273.json, 视频生成/图生视频/角色替换生成｜H3图生视频一键处理工作流_2095096657456226306.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_138

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（数字人/数字人/写英文工作流｜数字人英文口播视频生成专用流_2114020800511696898.json、视频生成/图生视频/10步+3步Latent Upscaler｜H3参考模式图生视频_2091180204667531265.json、视频生成/图生视频/BUNNY_H3单采er_sde手动Sigma，文生视频节奏随心控_2110519304910364674.json、视频生成/图生视频/H3 Taomate 3步加速 中远距离不崩脸视频生成_2099588330131382273.json、视频生成/图生视频/H3 sigma强化超清放大｜1080P打斗不糊脸不崩视频_2094933026361921538.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 11/12 个有
- `ModelAttentionBackend` —— 11/12 个有
- `CreateVideo` —— 10/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/12 个有
- `MiniMaxH3SigmaShift` —— 10/12 个有
- `ModelPreviewOverrideKJ` —— 9/12 个有
- `SaveVideo` —— 9/12 个有
- `SplitSigmas` —— 9/12 个有
- `H3SigmaRefiner` —— 8/12 个有
- `LTXVConcatAVLatent` —— 8/12 个有
- `LTXVSeparateAVLatent` —— 8/12 个有
- `MinimaxH3LatentUpscaler3D` —— 7/12 个有
- `GetNode` —— 6/12 个有
- `MiniMaxLowVRAMAttention` —— 6/12 个有
- `SetNode` —— 6/12 个有
- `SaveImage` —— 5/12 个有
- `VHS_LoadVideo` —— 4/12 个有
- `VHS_VideoCombine` —— 4/12 个有
- `FlashVSRNode` —— 3/12 个有
- `ManualSigmas` —— 3/12 个有
- `MiniMaxChunkFeedForward` —— 3/12 个有
- `Sleep` —— 3/12 个有
- `SolAttnMiniMax` —— 3/12 个有
- `FL_UnloadAllModels` —— 2/12 个有
- `Float` —— 2/12 个有
- `GetImageRangeFromBatch` —— 2/12 个有
- `MiniMaxH3AddGuide` —— 2/12 个有
- `MinimaxH3LatentUpscalerNode2D` —— 2/12 个有
- `BlockSparseAttention` —— 1/12 个有
- `CR Text Concatenate` —— 1/12 个有
- `GetVideoComponents` —— 1/12 个有
- `LoadAudio` —— 1/12 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 1/12 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/12 个有
- `QZ_ResolutionPreset` —— 1/12 个有
- `RH_Astra` —— 1/12 个有
- `RunningHub Deepcleaner` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
