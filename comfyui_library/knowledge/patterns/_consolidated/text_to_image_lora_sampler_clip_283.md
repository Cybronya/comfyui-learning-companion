---
name: text_to_image_lora_sampler_clip_283
type: Text To Image
frequency: 7
level: strong
coverage: 0.884714
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3AudioConditioningT8, ModelAttentionBackend, PrimitiveStringMultiline, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3 SelfLift工作流V1，文生视频视频生视频图生视频方案_2103940357879844865.json, 视频生成/文生视频/MiniMax H3 SelfLift版本｜768P通用生视频轻量出片｜文生视频_2099096873352126465.json, 视频生成/文生视频/MiniMax H3 SelfLift精修｜4K超清通用视频生成不糊帧｜文图双输入_2099102127078600705.json, 视频生成/文生视频/MiniMax H3 SelfLift通用生视频 768P多模态创作_2098829148855816193.json, 视频生成/文生视频/MiniMax H3 Sigma双采强化｜4K超清通用生视频旗舰版｜文图视频三合一_2099100789926096898.json, 视频生成/文生视频/MiniMax H3 Sigma强化双采通用生视频 4K超高清_2098832550188904449.json, 视频生成/文生视频/MiniMax H3双采Sigma强化版｜2K通用视频一站生成｜文生视频图生视频_2099091523861307393.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_283

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 SelfLift工作流V1，文生视频视频生视频图生视频方案_2103940357879844865.json、视频生成/文生视频/MiniMax H3 SelfLift版本｜768P通用生视频轻量出片｜文生视频_2099096873352126465.json、视频生成/文生视频/MiniMax H3 SelfLift精修｜4K超清通用视频生成不糊帧｜文图双输入_2099102127078600705.json、视频生成/文生视频/MiniMax H3 SelfLift通用生视频 768P多模态创作_2098829148855816193.json、视频生成/文生视频/MiniMax H3 Sigma双采强化｜4K超清通用生视频旗舰版｜文图视频三合一_2099100789926096898.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AudioConditioningT8`
- `ModelAttentionBackend`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 6/7 个有
- `ModelPreviewOverrideKJ` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `RH_DLSS5FrameInterpolation` —— 6/7 个有
- `SaveVideo` —— 6/7 个有
- `ConditioningZeroOut` —— 4/7 个有
- `ImageResizeKJv2` —— 4/7 个有
- `Int` —— 4/7 个有
- `LTXVSeparateAVLatent` —— 4/7 个有
- `MiniMaxChunkFeedForward` —— 4/7 个有
- `MiniMaxLowVRAMAttention` —— 4/7 个有
- `SeedVR2` —— 4/7 个有
- `SeedVR2BlockSwap` —— 4/7 个有
- `SelfLiftH3Sampler` —— 4/7 个有
- `BasicGuider` —— 3/7 个有
- `LTXVConcatAVLatent` —— 3/7 个有
- `MiniMaxH3SigmaShift` —— 3/7 个有
- `MinimaxH3LatentUpscaler3D` —— 3/7 个有
- `RandomNoise` —— 3/7 个有
- `SamplerCustomAdvanced` —— 3/7 个有
- `SaveImage` —— 3/7 个有
- `SplitSigmas` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `Float` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `VHS_VideoCombine` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
