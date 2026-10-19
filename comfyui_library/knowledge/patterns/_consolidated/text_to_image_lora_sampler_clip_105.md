---
name: text_to_image_lora_sampler_clip_105
type: Text To Image
frequency: 9
level: strong
coverage: 0.906889
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/SelfLift优化加速视频_2111462433582833666.json, 视频生成/图生视频/SelfLift优化速度流 视频生成加速方案_2108986698486079490.json, 视频生成/图生视频/绘影MiniMax H3参考生视频self-lift双采1080P，混合25-49模型加速方案_2103171255007531010.json, 视频生成/图生视频/绘影出品｜Minimax H3参考生视频self-lift双采1080P高清V1版_2103018117453672449.json, 视频生成/文生视频/MiniMax H3加速双采SelfLift图生视频处理工作流_2101739128789487617.json, 视频生成/文生视频/Minimax H3加速双采｜Self-Lift工作流提速出片两不误_2101510468241289218.json, 视频生成/文生视频/Minimax H3满血版黑科技加速 Self-lift双采工作流_2098704152372277249.json, 视频生成/文生视频/海螺H3融合模型加速双采｜self-lift文生视频工作流_2097819718035001346.json, 视频生成/文生视频/黑科技加速双采self-lift工作流｜文生视频快速生成_2097773293859328001.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_105

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/SelfLift优化加速视频_2111462433582833666.json、视频生成/图生视频/SelfLift优化速度流 视频生成加速方案_2108986698486079490.json、视频生成/图生视频/绘影MiniMax H3参考生视频self-lift双采1080P，混合25-49模型加速方案_2103171255007531010.json、视频生成/图生视频/绘影出品｜Minimax H3参考生视频self-lift双采1080P高清V1版_2103018117453672449.json、视频生成/文生视频/MiniMax H3加速双采SelfLift图生视频处理工作流_2101739128789487617.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：91%

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
- `MiniMaxH3ReferenceToVideo`
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
- `LoadAudio` —— 7/9 个有
- `SaveImage` —— 7/9 个有
- `SelfLiftH3Sampler` —— 7/9 个有
- `VHS_VideoCombine` —— 7/9 个有
- `CreateVideo` —— 5/9 个有
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
- `AudioCrop` —— 1/9 个有
- `LoraLoaderBypassModelOnly` —— 1/9 个有
- `VHS_LoadVideo` —— 1/9 个有

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
