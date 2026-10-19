---
name: text_to_image_lora_sampler_clip_23
type: Text To Image
frequency: 18
level: strong
coverage: 0.897
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3急速双采加无限时长长视频续写工作流工具_2100314628738871297.json, 视频生成/图生视频/MiniMax H3 SelfLift加速双采参考生视频｜武戏动态强_2108458056047742978.json, 视频生成/图生视频/MiniMax H3 SelfLift加速双采武戏动态强参考生视频方案_2108644932058697730.json, 视频生成/图生视频/MiniMax H3 SelfLift加速双采｜武戏动态强的参考生视频_2111123791060496385.json, 视频生成/图生视频/MiniMax H3加速双采SelfLift图生视频处理工作流_2101363088590196738.json, 视频生成/图生视频/MiniMax H3急速双采无限时长视频生成处理工作流_2101042811373178881.json, 视频生成/图生视频/MiniMax H3急速双采无限时长视频生成处理工作流_2101401984950693889.json, 视频生成/图生视频/Minimax H3加速双采self-lift流｜两次采样提质量，速度还不打折_2099494675802583042.json, 视频生成/图生视频/Minimax H3加速双采｜self-lift工作流高效出片_2101155630626201602.json, 视频生成/图生视频/Minimax H3多参视频生成不油不偏色及一致性好工作流，图生视频处理方案_2107954357282099202.json, 视频生成/图生视频/Minimax h3多参视频生成不油不偏色及一致性好 多模态输入_2109712427955871745.json, 视频生成/图生视频/Minimax-H3开源加速双采工作流｜self-lift图生视频生成_2097766070177320962.json, 视频生成/图生视频/Minimax-H3开源黑科技加速双采｜self-lift图生视频战斗特效_2097917181681029122.json, 视频生成/图生视频/黑科技self-lift双采加速｜高动态画面表现力惊人_2103101451823308801.json, 视频生成/图生视频/黑科技加速双采SelfLift Heng图生视频处理工作流_2101779733385146370.json, 视频生成/图生视频/黑科技加速双采self-lift图生视频｜Minimax-H3开源战斗特效版_2097956772765069313.json, 视频生成/文生视频/Aiden黑科技加速双采self-lift工作流｜文图视频三模生视频_2097969163804438530.json, 视频生成/文生视频/H3黑科技加速加星光2.6高清放大融合工作流_2100311534835691522.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/H3急速双采加无限时长长视频续写工作流工具_2100314628738871297.json、视频生成/图生视频/MiniMax H3 SelfLift加速双采参考生视频｜武戏动态强_2108458056047742978.json、视频生成/图生视频/MiniMax H3 SelfLift加速双采武戏动态强参考生视频方案_2108644932058697730.json、视频生成/图生视频/MiniMax H3 SelfLift加速双采｜武戏动态强的参考生视频_2111123791060496385.json、视频生成/图生视频/MiniMax H3加速双采SelfLift图生视频处理工作流_2101363088590196738.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
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
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 17/18 个有
- `CreateVideo` —— 16/18 个有
- `H3SigmaRefiner` —— 15/18 个有
- `VHS_VideoCombine` —— 11/18 个有
- `SaveImage` —— 10/18 个有
- `SaveVideo` —— 7/18 个有
- `LoraLoaderBypassModelOnly` —— 4/18 个有
- `AudioConcat` —— 3/18 个有
- `ExtendIntermediateSigmas` —— 3/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/18 个有
- `MiniMaxH3MotionContext` —— 3/18 个有
- `MiniMaxH3MotionContextSaveLatent` —— 3/18 个有
- `MiniMaxH3MotionContextTrim` —— 3/18 个有
- `SolAttnMiniMax` —— 3/18 个有
- `VHS_MergeImages` —— 3/18 个有
- `easy showAnything` —— 3/18 个有
- `LoadAudio` —— 2/18 个有
- `easy cleanGpuUsed` —— 2/18 个有
- `JWInteger` —— 1/18 个有
- `RH_Astra` —— 1/18 个有
- `SaveVideoNode` —— 1/18 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 1/18 个有

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
