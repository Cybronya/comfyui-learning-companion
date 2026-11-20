---
name: text_to_image_video_lora_sampler_65
type: Text To Image
frequency: 13
level: strong
coverage: 0.789615
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3多图生视频数字人带货 MiniMax开源版电商口播方案_2104675527998136322.json, 视频生成/图生视频/H3多图生视频数字人带货 MiniMax开源版电商口播方案_2104762447012917250.json, 视频生成/图生视频/H3多图生视频数字人带货 MiniMax开源版电商口播方案_2105440243649441794.json, 视频生成/图生视频/H3官流最强武戏 视频生成官方最佳方案稳定出片_2109173230555713537.json, 视频生成/图生视频/H3官流竖屏640p 无Lora15步图生视频处理工具_2113386469627879426.json, 视频生成/图生视频/H3官流终极版工作流，文生视频图生视频全覆盖方案_2109435565342019586.json, 视频生成/图生视频/H3工作流最优解 图生视频高质量稳定直出方案_2110367340926955522.json, 视频生成/图生视频/H3工作流最优解 视频生成最佳方案高效出片_2105350475045498881.json, 视频生成/图生视频/H3文戏SelfLift融合版｜24G显存720p 九参考图文戏更细腻_2105544997541072897.json, 视频生成/图生视频/H3融合模型专属双采 高遵循度无劣化战斗特效工具_2113345954777747457.json, 视频生成/图生视频/H3融合流专属双采 潜空间直达原汁口感视频生成工具_2113347638602063873.json, 视频生成/图生视频/H3角色替换工作流｜视频人物替换图生视频生成_2094905654396940289.json, 视频生成/图生视频/h3最优基础工作流汇总，文生视频图生视频全能_2111282762715062273.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_65

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/H3多图生视频数字人带货 MiniMax开源版电商口播方案_2104675527998136322.json、视频生成/图生视频/H3多图生视频数字人带货 MiniMax开源版电商口播方案_2104762447012917250.json、视频生成/图生视频/H3多图生视频数字人带货 MiniMax开源版电商口播方案_2105440243649441794.json、视频生成/图生视频/H3官流最强武戏 视频生成官方最佳方案稳定出片_2109173230555713537.json、视频生成/图生视频/H3官流竖屏640p 无Lora15步图生视频处理工具_2113386469627879426.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 12/13 个有
- `SaveImage` —— 12/13 个有
- `孤海注释` —— 12/13 个有
- `ManualSigmas` —— 10/13 个有
- `BlockSparseAttention` —— 9/13 个有
- `ModelAttentionBackend` —— 9/13 个有
- `PrimitiveStringMultiline` —— 9/13 个有
- `LTXVConcatAVLatent` —— 8/13 个有
- `LTXVSeparateAVLatent` —— 8/13 个有
- `MinimaxH3LatentUpscaler3D` —— 8/13 个有
- `ModelPreviewOverrideKJ` —— 8/13 个有
- `VHS_LoadVideo` —— 8/13 个有
- `GetNode` —— 7/13 个有
- `LoadAudio` —— 7/13 个有
- `SetNode` —— 7/13 个有
- `MiniMaxH3SigmaShift` —— 4/13 个有
- `SplitSigmas` —— 4/13 个有
- `CR Prompt Text` —— 3/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/13 个有
- `MiniMaxLowVRAMAttention` —— 3/13 个有
- `PreviewAny` —— 3/13 个有
- `ConditioningZeroOut` —— 2/13 个有
- `ExtendIntermediateSigmas` —— 2/13 个有
- `H3SigmaRefiner` —— 2/13 个有
- `MiniMaxChunkFeedForward` —— 2/13 个有
- `RH_LLMAPI_Pro_Node` —— 2/13 个有
- `SelfLiftAvatarH3Sampler` —— 2/13 个有
- `easy float` —— 2/13 个有
- `Any Switch (rgthree)` —— 1/13 个有
- `ComfyNumberConvert` —— 1/13 个有
- `ComfySwitchNode` —— 1/13 个有
- `CustomSigmas` —— 1/13 个有
- `FlashVSRNode` —— 1/13 个有
- `H3KitSemanticBridge` —— 1/13 个有
- `INTConstant` —— 1/13 个有
- `LTXVAudioVAEEncode` —— 1/13 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 1/13 个有
- `MiniMaxH3LowVRAMAttentionT8Advanced` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `SelfLiftAvatarH3TST` —— 1/13 个有
- `SetLatentNoiseMask` —— 1/13 个有
- `Sleep` —— 1/13 个有
- `SolidMask` —— 1/13 个有
- `SoundFlow_GetLength` —— 1/13 个有
- `TrimAudioDuration` —— 1/13 个有
- `ZML_MergeText` —— 1/13 个有
- `ZML_TextInput` —— 1/13 个有
- `ki_MiniMaxH3ReferenceToVideo` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（14/13 个样本）：Steps较低可能导致细节不足
