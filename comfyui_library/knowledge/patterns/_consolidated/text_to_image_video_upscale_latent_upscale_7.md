---
name: text_to_image_video_upscale_latent_upscale_7
type: Text To Image
frequency: 7
level: strong
coverage: 0.677286
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3社区模型工作流｜高质量加速版图生视频_2095147029315018754.json, 视频生成/图生视频/MINIMAX H3多参二采新玩法9图3音混合参考生成视频工作流，图生视频处理方案_2108329037356683266.json, 视频生成/图生视频/MINIMAX-H3多参二采新玩法｜9图3音混合参考生成视频_2107978172766711810.json, 视频生成/图生视频/MINIMAX-H3最强工作流｜图生视频高质量全能生成_2097040443535089666.json, 视频生成/图生视频/高质量加速版0902｜H3社区模型图生视频生成_2095103895356919810.json, 视频生成/图生视频/高质量加速版图生视频｜H3社区模型一键生成_2095492025532637185.json, 视频生成/图生视频/高质量加速版｜H3社区模型工作流图生视频_2092733195283423233.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_7

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/H3社区模型工作流｜高质量加速版图生视频_2095147029315018754.json、视频生成/图生视频/MINIMAX H3多参二采新玩法9图3音混合参考生成视频工作流，图生视频处理方案_2108329037356683266.json、视频生成/图生视频/MINIMAX-H3多参二采新玩法｜9图3音混合参考生成视频_2107978172766711810.json、视频生成/图生视频/MINIMAX-H3最强工作流｜图生视频高质量全能生成_2097040443535089666.json、视频生成/图生视频/高质量加速版0902｜H3社区模型图生视频生成_2095103895356919810.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 6/7 个有
- `BasicScheduler` —— 4/7 个有
- `KSamplerSelect` —— 4/7 个有
- `LoadVideo` —— 4/7 个有
- `MiniMaxH3Easy` —— 4/7 个有
- `MiniMaxH3EasyLoader` —— 4/7 个有
- `MiniMaxH3EasyOutput` —— 4/7 个有
- `MiniMaxH3ReferenceToVideo` —— 4/7 个有
- `PrimitiveInt` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `VAEDecodeAudio` —— 4/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `Lora Loader Stack (rgthree)` —— 3/7 个有
- `LoraLoaderBypassModelOnly` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `SaveImage` —— 2/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `Florence2ModelLoader` —— 1/7 个有
- `Florence2Run` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `SeedVR2LoadDiTModel` —— 1/7 个有
- `SeedVR2LoadVAEModel` —— 1/7 个有
- `SeedVR2VideoUpscaler` —— 1/7 个有
- `VAEEncode` —— 1/7 个有
- `easy int` —— 1/7 个有
- `easy showAnything` —— 1/7 个有
- `忽略多组孤海` —— 1/7 个有

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
| Steps较低可能导致细节不足 | 9/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（9/7 个样本）：Steps较低可能导致细节不足
