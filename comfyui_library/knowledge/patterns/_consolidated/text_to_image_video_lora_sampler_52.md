---
name: text_to_image_video_lora_sampler_52
type: Text To Image
frequency: 13
level: strong
coverage: 0.884077
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, ResolutionSelector, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Minimax H3全能参考Selflift双采 Sage加速高质量直出_2110247054734880770.json, 视频生成/图生视频/Minimax H3全能参考Selflift双采 Sage加速高质量直出_2110372049079324674.json, 视频生成/图生视频/Minimax H3动作增强修复双采｜高动态脸部兼顾_2098773573254082561.json, 视频生成/图生视频/Minimax H3高质量高速度全能参考 Selflift双采Sage加速版_2110248726794162177.json, 视频生成/图生视频/Minimax H3高质量高速度全能参考 Selflift双采Sage加速版_2110362722650124289.json, 视频生成/图生视频/Minimax h3超级加速多图参考生视频 快速出片方案_2109357930280734721.json, 视频生成/图生视频/MinimaxH3全能参考高清放大｜9图12素材去噪加放大_2111315771795267585.json, 视频生成/图生视频/MinimaxH3双模双采hybird+remix｜双加速实验工作流_2094864494676762625.json, 视频生成/图生视频/hybird+remix双模双采｜MinimaxH3双加速实验生成_2095055333248032769.json, 视频生成/图生视频/双模双采hybird+remix｜MinimaxH3图生视频双larry加速_2093078463535210498.json, 视频生成/图生视频/双模双采加速｜MinimaxH3 hybrid+remix双larry工作流_2093241754479845378.json, 视频生成/图生视频/同模双采动态修复工作流｜H3图生视频画质增强生成_2097104202756608002.json, 视频生成/图生视频/多参生视频10秒直出｜Minimax二采768P升1080P高清_2090146522963992578.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_52

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/Minimax H3全能参考Selflift双采 Sage加速高质量直出_2110247054734880770.json、视频生成/图生视频/Minimax H3全能参考Selflift双采 Sage加速高质量直出_2110372049079324674.json、视频生成/图生视频/Minimax H3动作增强修复双采｜高动态脸部兼顾_2098773573254082561.json、视频生成/图生视频/Minimax H3高质量高速度全能参考 Selflift双采Sage加速版_2110248726794162177.json、视频生成/图生视频/Minimax H3高质量高速度全能参考 Selflift双采Sage加速版_2110362722650124289.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
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
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 12/13 个有
- `H3SigmaRefiner` —— 11/13 个有
- `PrimitiveStringMultiline` —— 11/13 个有
- `LoadAudio` —— 10/13 个有
- `BasicGuider` —— 9/13 个有
- `RandomNoise` —— 9/13 个有
- `SamplerCustomAdvanced` —— 9/13 个有
- `LTXVConcatAVLatent` —— 8/13 个有
- `LTXVSeparateAVLatent` —— 8/13 个有
- `MiniMaxH3ReferenceToVideo` —— 8/13 个有
- `VAEDecodeAudio` —— 8/13 个有
- `MinimaxH3LatentUpscaler3D` —— 7/13 个有
- `MiniMaxH3SigmaShift` —— 6/13 个有
- `MiniMaxH3TurboLoRA` —— 6/13 个有
- `ModelAttentionBackend` —— 6/13 个有
- `SaveImage` —— 6/13 个有
- `SplitSigmas` —— 6/13 个有
- `MiniMaxH3AVDecodeT8` —— 5/13 个有
- `MiniMaxH3AudioConditioningT8` —— 5/13 个有
- `ModelPreviewOverrideKJ` —— 5/13 个有
- `Seed (rgthree)` —— 5/13 个有
- `ShellAgentPluginVideoCombineEncrypt` —— 5/13 个有
- `easy cleanGpuUsed` —— 5/13 个有
- `ConditioningZeroOut` —— 4/13 个有
- `LayerUtility: PurgeVRAM V2` —— 4/13 个有
- `SelfLiftH3Sampler` —— 4/13 个有
- `LoraLoaderBypassModelOnly` —— 3/13 个有
- `GetNode` —— 2/13 个有
- `MiniMaxLowVRAMAttention` —— 2/13 个有
- `SetNode` —— 2/13 个有
- `SolAttnMiniMax` —— 2/13 个有
- `CR Prompt Text` —— 1/13 个有
- `MiniMaxH3BlockCacheT8` —— 1/13 个有
- `MiniMaxH3HybridArtifactBuilderT8Advanced` —— 1/13 个有
- `MiniMaxH3HybridLoader` —— 1/13 个有
- `MiniMaxH3HybridModelLoaderT8Advanced` —— 1/13 个有
- `MiniMaxH3HybridPairInspectorT8Advanced` —— 1/13 个有
- `MiniMaxH3VRAMPolicyT8Advanced` —— 1/13 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/13 个有
- `PainterVRAM` —— 1/13 个有
- `easy int` —— 1/13 个有

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
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
