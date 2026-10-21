---
name: text_to_image_lora_sampler_clip_18
type: Text To Image
frequency: 25
level: strong
coverage: 0.89328
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, ResolutionSelector, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Minimax H3全能参考Selflift双采 Sage加速高质量直出_2110247054734880770.json, 视频生成/图生视频/Minimax H3全能参考Selflift双采 Sage加速高质量直出_2110372049079324674.json, 视频生成/图生视频/Minimax H3多参视频生成不油不偏色及一致性好工作流，图生视频处理方案_2107954357282099202.json, 视频生成/图生视频/Minimax H3高质量高速度全能参考 Selflift双采Sage加速版_2110248726794162177.json, 视频生成/图生视频/Minimax H3高质量高速度全能参考 Selflift双采Sage加速版_2110362722650124289.json, 视频生成/图生视频/Minimax h3多参视频生成不油不偏色及一致性好 多模态输入_2109712427955871745.json, 视频生成/图生视频/Minimax-H3开源加速双采工作流｜self-lift图生视频生成_2097766070177320962.json, 视频生成/图生视频/Minimax-H3开源黑科技加速双采｜self-lift图生视频战斗特效_2097917181681029122.json, 视频生成/图生视频/Minimax参考图模式 多模态输入视频生成_2109765711622139905.json, 视频生成/图生视频/SelfLift双采BF16max多宫格单图专用三音色参考工作流，图生视频方案_2106481893637181442.json, 视频生成/图生视频/SelfLift双采BF16max多宫格单图专用双音色参考工作流，图生视频方案_2106512263355125761.json, 视频生成/图生视频/selfift双采BF16max多宫格单图专用｜三音色参考自由切换_2106225447443984385.json, 视频生成/图生视频/多参考图生视频｜Minimax H3一键生成直出_2092083542187667457.json, 视频生成/图生视频/多图参考生视频｜MiniMaxH3图生视频一键生成_2092741832886276098.json, 视频生成/图生视频/老李多参生视频 多参考图输入视频生成方案_2104710161666498561.json, 视频生成/图生视频/黑科技self-lift双采加速｜高动态画面表现力惊人_2103101451823308801.json, 视频生成/文生视频/H3 SelfLift五图音频数字人 15秒广告视频生成_2099191168692219906.json, 视频生成/文生视频/H3 SelfLift五图音频数字人 15秒广告视频生成_2099573312807591938.json, 视频生成/文生视频/H3二采数字人SelfLift单图三人音频参考 多角色口播_2099189481143365633.json, 视频生成/文生视频/H3二采数字人SelfLift单图三人音频参考 多角色口播_2099571650248400898.json, 视频生成/文生视频/H3二采数字人SelfLift单图双人音频参考 多人口播_2099192888298139649.json, 视频生成/文生视频/H3二采数字人SelfLift单图双人音频参考 多人口播_2099574994182434818.json, 视频生成/文生视频/MiniMax H3 SelfLift加速双采文戏武戏参考生视频处理工具_2101730945995993089.json, 视频生成/文生视频/MiniMax H3-SelfLift加速双采｜文戏不油武戏动态强_2101550350955270145.json, 视频生成/文生视频/Minimax H3满血版黑科技加速 Self-lift双采工作流_2098704152372277249.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（视频生成/图生视频/Minimax H3全能参考Selflift双采 Sage加速高质量直出_2110247054734880770.json、视频生成/图生视频/Minimax H3全能参考Selflift双采 Sage加速高质量直出_2110372049079324674.json、视频生成/图生视频/Minimax H3多参视频生成不油不偏色及一致性好工作流，图生视频处理方案_2107954357282099202.json、视频生成/图生视频/Minimax H3高质量高速度全能参考 Selflift双采Sage加速版_2110248726794162177.json、视频生成/图生视频/Minimax H3高质量高速度全能参考 Selflift双采Sage加速版_2110362722650124289.json…）

- **类型**：Text To Image
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 25 个 workflow 都包含：
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
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 23/25 个有
- `VHS_VideoCombine` —— 23/25 个有
- `ConditioningZeroOut` —— 22/25 个有
- `SelfLiftH3Sampler` —— 22/25 个有
- `H3SigmaRefiner` —— 20/25 个有
- `LoadAudio` —— 19/25 个有
- `SaveImage` —— 19/25 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 18/25 个有
- `MiniMaxChunkFeedForward` —— 16/25 个有
- `MiniMaxLowVRAMAttention` —— 16/25 个有
- `LayerUtility: PurgeVRAM V2` —— 13/25 个有
- `MiniMaxH3AVDecodeT8` —— 13/25 个有
- `MiniMaxH3AudioConditioningT8` —— 13/25 个有
- `MiniMaxH3ReferenceToVideo` —— 12/25 个有
- `VAEDecodeAudio` —— 12/25 个有
- `ModelAttentionBackend` —— 9/25 个有
- `ModelPreviewOverrideKJ` —— 9/25 个有
- `BasicGuider` —— 6/25 个有
- `CreateVideo` —— 6/25 个有
- `RandomNoise` —— 6/25 个有
- `SamplerCustomAdvanced` —— 6/25 个有
- `LoraLoaderBypassModelOnly` —— 4/25 个有
- `VHS_LoadVideo` —— 3/25 个有
- `easy showAnything` —— 3/25 个有
- `ExtendIntermediateSigmas` —— 2/25 个有
- `Fast Groups Bypasser (rgthree)` —— 2/25 个有
- `SaveVideo` —— 2/25 个有
- `SolAttnMiniMax` —— 2/25 个有
- `AudioCrop` —— 1/25 个有
- `CR Text` —— 1/25 个有
- `Label (rgthree)` —— 1/25 个有
- `Text` —— 1/25 个有
- `easy cleanGpuUsed` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 25 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 25 | 100% |
| 采样算法 | er_sde | - | 25 | 100% |
| 调度器 | beta | - | 25 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |
| 宽度 | 80 | 80 - 80 | 25 | 100% |
| 高度 | 80 | 80 - 80 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，25 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，25 个样本，一致性 100%
- 调度器 最常用 beta，25 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高发问题（25/25 个样本）：Steps较低可能导致细节不足
