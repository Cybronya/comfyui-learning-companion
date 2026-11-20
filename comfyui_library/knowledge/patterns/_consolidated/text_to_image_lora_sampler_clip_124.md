---
name: text_to_image_lora_sampler_clip_124
type: Text To Image
frequency: 13
level: strong
coverage: 0.711231
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, ModelPreviewOverrideKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/H3 All-in-One Accelerated V3 一体化加速视频工作流_2099231445800808450.json, 视频生成/文生视频/H3 All-in-One Accelerated V3一体化加速工作流_2099556074457231362.json, 视频生成/文生视频/H3 氛围感短视频｜文生视频图生视频双双在线_2096866829003218946.json, 视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107191447593246721.json, 视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107333167064637441.json, 视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107444165738057730.json, 视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107958839365689345.json, 视频生成/文生视频/H3官流mpov版不用加速LoRA工作流，文生视频视频生视频图生视频方案_2107987502211620866.json, 视频生成/文生视频/H3官流终极版 视频生成官方最佳方案稳定出片_2105387723480719362.json, 视频生成/文生视频/H3突破15秒长视频不劣化工作流拆解系列_2100272112148766722.json, 视频生成/文生视频/H3突破15秒长视频不劣化｜工作流拆解系列生成_2095301463194034178.json, 视频生成/文生视频/minimax-H3 官方版去油提质｜长视频续接无限延长手动版_2096903551057481730.json, 视频生成/文生视频/去油提画质长视频续接｜MiniMax H3官方版无限延长手动生成_2096782492383666177.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_124

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/文生视频/H3 All-in-One Accelerated V3 一体化加速视频工作流_2099231445800808450.json、视频生成/文生视频/H3 All-in-One Accelerated V3一体化加速工作流_2099556074457231362.json、视频生成/文生视频/H3 氛围感短视频｜文生视频图生视频双双在线_2096866829003218946.json、视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107191447593246721.json、视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107333167064637441.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelPreviewOverrideKJ`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 11/13 个有
- `LoadImage` —— 11/13 个有
- `MiniMaxH3ReferenceToVideo` —— 11/13 个有
- `ModelAttentionBackend` —— 11/13 个有
- `PrimitiveFloat` —— 11/13 个有
- `PrimitiveStringMultiline` —— 11/13 个有
- `孤海注释` —— 11/13 个有
- `LoadAudio` —— 10/13 个有
- `SaveImage` —— 10/13 个有
- `VAEDecodeAudio` —— 9/13 个有
- `VHS_VideoCombine` —— 9/13 个有
- `GetNode` —— 8/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/13 个有
- `SetNode` —— 8/13 个有
- `ManualSigmas` —— 7/13 个有
- `BlockSparseAttention` —— 6/13 个有
- `Fast Groups Bypasser (rgthree)` —— 6/13 个有
- `VHS_LoadVideo` —— 6/13 个有
- `PreviewImage` —— 5/13 个有
- `CreateVideo` —— 4/13 个有
- `ExtendIntermediateSigmas` —— 4/13 个有
- `GetImageRangeFromBatch` —— 4/13 个有
- `H3SigmaRefiner` —— 4/13 个有
- `MiniMaxH3AVDecodeT8` —— 4/13 个有
- `MiniMaxH3AddGuide` —— 4/13 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 4/13 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 4/13 个有
- `SaveVideo` —— 4/13 个有
- `easy showAnything` —— 4/13 个有
- `EmptyImage` —— 3/13 个有
- `CR Text` —— 2/13 个有
- `ComfySwitchNode` —— 2/13 个有
- `ImageAddNoise` —— 2/13 个有
- `MiniMaxH3SigmaShift` —— 2/13 个有
- `MiniMaxH3Unified` —— 2/13 个有
- `PrimitiveBoolean` —— 2/13 个有
- `SolAttnMiniMax` —— 2/13 个有
- `忽略多组孤海` —— 1/13 个有

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
| Steps较低可能导致细节不足 | 14/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（14/13 个样本）：Steps较低可能导致细节不足
