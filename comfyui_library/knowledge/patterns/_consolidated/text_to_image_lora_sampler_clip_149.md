---
name: text_to_image_lora_sampler_clip_149
type: Text To Image
frequency: 8
level: strong
coverage: 0.893625
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3急速双采加无限时长长视频续写工作流工具_2100314628738871297.json, 视频生成/图生视频/MiniMax H3 SelfLift加速双采参考生视频｜武戏动态强_2108458056047742978.json, 视频生成/图生视频/MiniMax H3 SelfLift加速双采武戏动态强参考生视频方案_2108644932058697730.json, 视频生成/图生视频/MiniMax H3 SelfLift加速双采｜武戏动态强的参考生视频_2111123791060496385.json, 视频生成/图生视频/MiniMax H3 SelfLift双采对比普通双采图生视频处理工具_2101770093456871425.json, 视频生成/图生视频/MiniMax H3急速双采无限时长视频生成处理工作流_2101042811373178881.json, 视频生成/图生视频/MiniMax H3急速双采无限时长视频生成处理工作流_2101401984950693889.json, 视频生成/图生视频/h3 二阶+sigma+latent 采样组合｜数字人图生视频_2096896924396900353.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_149

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/H3急速双采加无限时长长视频续写工作流工具_2100314628738871297.json、视频生成/图生视频/MiniMax H3 SelfLift加速双采参考生视频｜武戏动态强_2108458056047742978.json、视频生成/图生视频/MiniMax H3 SelfLift加速双采武戏动态强参考生视频方案_2108644932058697730.json、视频生成/图生视频/MiniMax H3 SelfLift加速双采｜武戏动态强的参考生视频_2111123791060496385.json、视频生成/图生视频/MiniMax H3 SelfLift双采对比普通双采图生视频处理工具_2101770093456871425.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `MiniMaxChunkFeedForward` —— 7/8 个有
- `MiniMaxLowVRAMAttention` —— 7/8 个有
- `PrimitiveStringMultiline` —— 7/8 个有
- `SelfLiftH3Sampler` —— 7/8 个有
- `SaveImage` —— 5/8 个有
- `SaveVideo` —— 5/8 个有
- `VHS_VideoCombine` —— 5/8 个有
- `ExtendIntermediateSigmas` —— 4/8 个有
- `H3SigmaRefiner` —— 4/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/8 个有
- `SolAttnMiniMax` —— 4/8 个有
- `easy showAnything` —— 4/8 个有
- `AudioConcat` —— 3/8 个有
- `LoraLoaderBypassModelOnly` —— 3/8 个有
- `MiniMaxH3MotionContext` —— 3/8 个有
- `MiniMaxH3MotionContextSaveLatent` —— 3/8 个有
- `MiniMaxH3MotionContextTrim` —— 3/8 个有
- `VHS_MergeImages` —— 3/8 个有
- `BasicGuider` —— 2/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `LTXVConcatAVLatent` —— 2/8 个有
- `LTXVSeparateAVLatent` —— 2/8 个有
- `MinimaxH3LatentUpscaler3D` —— 2/8 个有
- `RandomNoise` —— 2/8 个有
- `SamplerCustomAdvanced` —— 2/8 个有
- `SplitSigmas` —— 2/8 个有
- `AddLabel` —— 1/8 个有
- `CR Text` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `GetImageSize` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `ManualSigmas` —— 1/8 个有
- `MiniMaxH3SigmaShift` —— 1/8 个有
- `RH_LLMAPI_Pro_Node` —— 1/8 个有
- `TextOverlay` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
