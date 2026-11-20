---
name: text_to_image_video_upscale_latent_upscale_6
type: Text To Image
frequency: 9
level: strong
coverage: 0.717889
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MinimaxH3LatentUpscaler3D, RandomNoise, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/高质量数字人MiniMax H3工作流，数字人生成处理方案_2106903069106720770.json, 视频生成/图生视频/H3 Easy工作台双采样｜提示词增强图生视频生成_2097078423951859713.json, 视频生成/图生视频/H3 最强去油双采样｜提示词全自动优化一步到位｜图生视频_2096829872772575233.json, 视频生成/图生视频/H3多参2采加Qwen3.8提示词优化版，图生视频高质量创作工具_2106069445222420481.json, 视频生成/图生视频/H3多参二采Qwen3.8提示词优化 角色一致性图生视频增强_2098660749190189058.json, 视频生成/图生视频/最强去油双采样工作流｜H3提示词全自动优化图生视频_2096682501061300226.json, 视频生成/图生视频/电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2106533639197646850.json, 视频生成/图生视频/电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2106878349405671426.json, 视频生成/图生视频/电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2109442962584334337.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_6

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（数字人/数字人/高质量数字人MiniMax H3工作流，数字人生成处理方案_2106903069106720770.json、视频生成/图生视频/H3 Easy工作台双采样｜提示词增强图生视频生成_2097078423951859713.json、视频生成/图生视频/H3 最强去油双采样｜提示词全自动优化一步到位｜图生视频_2096829872772575233.json、视频生成/图生视频/H3多参2采加Qwen3.8提示词优化版，图生视频高质量创作工具_2106069445222420481.json、视频生成/图生视频/H3多参二采Qwen3.8提示词优化 角色一致性图生视频增强_2098660749190189058.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
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
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 8/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/9 个有
- `MiniMaxH3PromptEnhancerT8` —— 8/9 个有
- `PreviewAny` —— 8/9 个有
- `RH_Translator` —— 8/9 个有
- `VAEDecodeAudio` —— 8/9 个有
- `easy saveText` —— 8/9 个有
- `easy showAnything` —— 8/9 个有
- `孤海注释` —— 8/9 个有
- `SaveImage` —— 7/9 个有
- `LoadAudio` —— 6/9 个有
- `ComfyMathExpression` —— 5/9 个有
- `GetNode` —— 5/9 个有
- `MiniMaxH3ReferenceToVideo` —— 5/9 个有
- `PrimitiveFloat` —— 5/9 个有
- `ResolutionSelector` —— 5/9 个有
- `SetNode` —— 5/9 个有
- `easy float` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `H3SigmaRefiner` —— 4/9 个有
- `MiniMaxH3Easy` —— 4/9 个有
- `MiniMaxH3EasyModelAdapter` —— 4/9 个有
- `MiniMaxH3EasyOutput` —— 4/9 个有
- `MiniMaxH3EasySecondPassConditioning` —— 4/9 个有
- `VHS_LoadVideo` —— 4/9 个有
- `easy indexTTSForceCleanup` —— 4/9 个有
- `Int` —— 3/9 个有
- `GoohaiMinimaxH3TiledSampler` —— 1/9 个有
- `LTXVAudioVAEEncode` —— 1/9 个有
- `ModelAttentionBackend` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `Seed (rgthree)` —— 1/9 个有
- `SetLatentNoiseMask` —— 1/9 个有
- `SolidMask` —— 1/9 个有
- `TrimAudioDuration` —— 1/9 个有

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
| Steps较低可能导致细节不足 | 11/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（11/9 个样本）：Steps较低可能导致细节不足
