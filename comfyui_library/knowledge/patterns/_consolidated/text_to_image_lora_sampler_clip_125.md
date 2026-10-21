---
name: text_to_image_lora_sampler_clip_125
type: Text To Image
frequency: 9
level: strong
coverage: 0.897556
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/SelfLift优化加速视频_2111462433582833666.json, 视频生成/图生视频/SelfLift优化速度流 视频生成加速方案_2108986698486079490.json, 视频生成/图生视频/绘影MiniMax H3参考生视频self-lift双采1080P，混合25-49模型加速方案_2103171255007531010.json, 视频生成/图生视频/绘影出品｜Minimax H3参考生视频self-lift双采1080P高清V1版_2103018117453672449.json, 视频生成/图生视频/黑科技加速双采SelfLift Heng图生视频处理工作流_2101779733385146370.json, 视频生成/图生视频/黑科技加速双采self-lift图生视频｜Minimax-H3开源战斗特效版_2097956772765069313.json, 视频生成/文生视频/Aiden黑科技加速双采self-lift工作流｜文图视频三模生视频_2097969163804438530.json, 视频生成/文生视频/H3加速双采SelfLift工作流 图生视频高效生成_2099944178082992130.json, 视频生成/文生视频/H3黑科技加速加星光2.6高清放大融合工作流_2100311534835691522.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_125

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/SelfLift优化加速视频_2111462433582833666.json、视频生成/图生视频/SelfLift优化速度流 视频生成加速方案_2108986698486079490.json、视频生成/图生视频/绘影MiniMax H3参考生视频self-lift双采1080P，混合25-49模型加速方案_2103171255007531010.json、视频生成/图生视频/绘影出品｜Minimax H3参考生视频self-lift双采1080P高清V1版_2103018117453672449.json、视频生成/图生视频/黑科技加速双采SelfLift Heng图生视频处理工作流_2101779733385146370.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 8/9 个有
- `SelfLiftH3Sampler` —— 7/9 个有
- `VHS_VideoCombine` —— 7/9 个有
- `SaveImage` —— 6/9 个有
- `CreateVideo` —— 5/9 个有
- `LoadAudio` —— 5/9 个有
- `ImageFromBatch` —— 2/9 个有
- `ImageScaleBy` —— 2/9 个有
- `LTXVConcatAVLatent` —— 2/9 个有
- `MiniMaxH3SigmaShift` —— 2/9 个有
- `SaveVideo` —— 2/9 个有
- `SelfLiftAvatarH3Sampler` —— 2/9 个有
- `SetLatentNoiseMask` —— 2/9 个有
- `SolidMask` —— 2/9 个有
- `VAEEncodeAudio` —— 2/9 个有
- `VOSR2ModelLoader` —— 2/9 个有
- `VOSR2Upscale` —— 2/9 个有
- `VedaSparseAttention` —— 2/9 个有
- `JWInteger` —— 1/9 个有
- `RH_Astra` —— 1/9 个有
- `SaveVideoNode` —— 1/9 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
