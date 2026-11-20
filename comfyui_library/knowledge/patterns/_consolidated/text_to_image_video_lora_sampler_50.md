---
name: text_to_image_video_lora_sampler_50
type: Text To Image
frequency: 15
level: strong
coverage: 0.884
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, ResolutionSelector, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Minimax H3全能参考Selflift双采 Sage加速高质量直出_2110247054734880770.json, 视频生成/图生视频/Minimax H3全能参考Selflift双采 Sage加速高质量直出_2110372049079324674.json, 视频生成/图生视频/Minimax H3动作增强修复双采｜高动态脸部兼顾_2098773573254082561.json, 视频生成/图生视频/Minimax H3高质量高速度全能参考 Selflift双采Sage加速版_2110248726794162177.json, 视频生成/图生视频/Minimax H3高质量高速度全能参考 Selflift双采Sage加速版_2110362722650124289.json, 视频生成/图生视频/Minimax-H3lora)ENG8步多参生视频(双时钟图生极速2分钟出5秒ENG_2087129153064751106.json, 视频生成/图生视频/MinimaxH3全能参考高清放大｜9图12素材去噪加放大_2111315771795267585.json, 视频生成/图生视频/MinimaxH3双模双采hybird+remix｜双加速实验工作流_2094864494676762625.json, 视频生成/图生视频/Singularity真实人物双采流｜角色一致性高保真_2098716861327298562.json, 视频生成/图生视频/hybird+remix双模双采｜MinimaxH3双加速实验生成_2095055333248032769.json, 视频生成/图生视频/minmax潜空间放大姿势迁移｜图生视频新玩法_2097908550017306625.json, 视频生成/图生视频/双模双采hybird+remix｜MinimaxH3图生视频双larry加速_2093078463535210498.json, 视频生成/图生视频/双模双采加速｜MinimaxH3 hybrid+remix双larry工作流_2093241754479845378.json, 视频生成/图生视频/同模双采动态修复工作流｜H3图生视频画质增强生成_2097104202756608002.json, 视频生成/图生视频/多参生视频10秒直出｜Minimax二采768P升1080P高清_2090146522963992578.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_50

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/Minimax H3全能参考Selflift双采 Sage加速高质量直出_2110247054734880770.json、视频生成/图生视频/Minimax H3全能参考Selflift双采 Sage加速高质量直出_2110372049079324674.json、视频生成/图生视频/Minimax H3动作增强修复双采｜高动态脸部兼顾_2098773573254082561.json、视频生成/图生视频/Minimax H3高质量高速度全能参考 Selflift双采Sage加速版_2110248726794162177.json、视频生成/图生视频/Minimax H3高质量高速度全能参考 Selflift双采Sage加速版_2110362722650124289.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 14/15 个有
- `KSamplerSelect` —— 14/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 14/15 个有
- `PrimitiveFloat` —— 14/15 个有
- `H3SigmaRefiner` —— 12/15 个有
- `PrimitiveStringMultiline` —— 12/15 个有
- `BasicGuider` —— 11/15 个有
- `RandomNoise` —— 11/15 个有
- `SamplerCustomAdvanced` —— 11/15 个有
- `LTXVConcatAVLatent` —— 10/15 个有
- `LTXVSeparateAVLatent` —— 10/15 个有
- `LoadAudio` —— 10/15 个有
- `MiniMaxH3ReferenceToVideo` —— 9/15 个有
- `MinimaxH3LatentUpscaler3D` —— 9/15 个有
- `VAEDecodeAudio` —— 9/15 个有
- `MiniMaxH3SigmaShift` —— 8/15 个有
- `ModelAttentionBackend` —— 8/15 个有
- `SplitSigmas` —— 8/15 个有
- `MiniMaxH3TurboLoRA` —— 7/15 个有
- `ModelPreviewOverrideKJ` —— 7/15 个有
- `MiniMaxH3AVDecodeT8` —— 6/15 个有
- `MiniMaxH3AudioConditioningT8` —— 6/15 个有
- `SaveImage` —— 6/15 个有
- `Seed (rgthree)` —— 5/15 个有
- `ShellAgentPluginVideoCombineEncrypt` —— 5/15 个有
- `easy cleanGpuUsed` —— 5/15 个有
- `ConditioningZeroOut` —— 4/15 个有
- `LayerUtility: PurgeVRAM V2` —— 4/15 个有
- `LoraLoaderBypassModelOnly` —— 4/15 个有
- `SelfLiftH3Sampler` —— 4/15 个有
- `CR Prompt Text` —— 2/15 个有
- `GetNode` —— 2/15 个有
- `MiniMaxLowVRAMAttention` —— 2/15 个有
- `SetNode` —— 2/15 个有
- `SolAttnMiniMax` —— 2/15 个有
- `ManualSigmas` —— 1/15 个有
- `MiniMaxH3BlockCacheT8` —— 1/15 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/15 个有
- `MiniMaxH3HybridArtifactBuilderT8Advanced` —— 1/15 个有
- `MiniMaxH3HybridLoader` —— 1/15 个有
- `MiniMaxH3HybridModelLoaderT8Advanced` —— 1/15 个有
- `MiniMaxH3HybridPairInspectorT8Advanced` —— 1/15 个有
- `MiniMaxH3VRAMPolicyT8Advanced` —— 1/15 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/15 个有
- `easy int` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
