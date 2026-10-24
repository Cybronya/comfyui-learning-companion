---
name: text_to_image_upscale_latent_upscale_lora_5
type: Text To Image
frequency: 8
level: strong
coverage: 0.914
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/打斗场面高清呈现｜MinimaxH3武戏图生视频特效_2096524592583106561.json, 视频生成/图生视频/舞姿自动生成｜Minimax H3人物特效跳舞机_2096575779445497858.json, 视频生成/图生视频/跳舞自动机动作生成｜Minimax H3人物特效图生视频_2096316917907804162.json, 视频生成/文生视频/MiniMax H3多参Taomate 3步Lora二采视频生成处理工具_2101407475479179265.json, 视频生成/文生视频/MiniMax H3多参角色替换LoRA二采放大工作流，文生视频视频生视频图生视频_2106867673660485633.json, 视频生成/文生视频/Minimax H3多参二采生视频｜Taomate 3 steplora助力_2101149197461446657.json, 视频生成/文生视频/多参生视频潜空间放大二采｜Minimax H3高质量版_2095969486913495042.json, 视频生成/文生视频/多参生视频潜空间放大｜Minimax H3 二采画质更稳_2096260116558467073.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_5

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/打斗场面高清呈现｜MinimaxH3武戏图生视频特效_2096524592583106561.json、视频生成/图生视频/舞姿自动生成｜Minimax H3人物特效跳舞机_2096575779445497858.json、视频生成/图生视频/跳舞自动机动作生成｜Minimax H3人物特效图生视频_2096316917907804162.json、视频生成/文生视频/MiniMax H3多参Taomate 3步Lora二采视频生成处理工具_2101407475479179265.json、视频生成/文生视频/MiniMax H3多参角色替换LoRA二采放大工作流，文生视频视频生视频图生视频_2106867673660485633.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 7/8 个有
- `PrimitiveFloat` —— 7/8 个有
- `BasicScheduler` —— 6/8 个有
- `SplitSigmas` —— 6/8 个有
- `Text` —— 6/8 个有
- `VHS_VideoCombine` —— 6/8 个有
- `CreateVideo` —— 5/8 个有
- `SaveVideo` —— 5/8 个有
- `RHHiddenNodes` —— 3/8 个有
- `CR Prompt Text` —— 2/8 个有
- `ClownsharKSampler_Beta` —— 2/8 个有
- `ConditioningZeroOut` —— 2/8 个有
- `SaveImage` —— 2/8 个有
- `SeedGenerator` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `DF_Get_image_size` —— 1/8 个有
- `FlashVSR_SM_KSampler` —— 1/8 个有
- `FlashVSR_SM_Model` —— 1/8 个有
- `GetImageRangeFromBatch` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `JWInteger` —— 1/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有
- `VideoCombineV2` —— 1/8 个有

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
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
