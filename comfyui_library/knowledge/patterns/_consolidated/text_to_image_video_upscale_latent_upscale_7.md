---
name: text_to_image_video_upscale_latent_upscale_7
type: Text To Image
frequency: 12
level: strong
coverage: 0.76975
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MinimaxH3LatentUpscaler3D, RandomNoise, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/高质量数字人MiniMax H3工作流，数字人生成处理方案_2106903069106720770.json, 视频生成/图生视频/H3 Easy工作台双采样｜提示词增强图生视频生成_2097078423951859713.json, 视频生成/图生视频/H3 最强去油双采样｜提示词全自动优化一步到位｜图生视频_2096829872772575233.json, 视频生成/图生视频/H3多参2采加Qwen3.8提示词优化版，图生视频高质量创作工具_2106069445222420481.json, 视频生成/图生视频/H3多参二采Qwen3.8提示词优化 角色一致性图生视频增强_2098660749190189058.json, 视频生成/图生视频/minimaxh3高质量数字人_口播视频生成省时省力_2106603151494303745.json, 视频生成/图生视频/最强去油双采样工作流｜H3提示词全自动优化图生视频_2096682501061300226.json, 视频生成/图生视频/电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2106533639197646850.json, 视频生成/图生视频/电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2106878349405671426.json, 视频生成/图生视频/电商带货版加H3多参2采加Qwen3.8提示词优化版，模特产品展示图生视频_2109442962584334337.json, 视频生成/图生视频/高质量数字人MiniMax_H3工作流，数字人生成处理方案_2108732703087616001.json, 视频生成/图生视频/高质量数字人minimax h3 数字人视频生成方案_2105028607759446018.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_7

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（数字人/数字人/高质量数字人MiniMax H3工作流，数字人生成处理方案_2106903069106720770.json、视频生成/图生视频/H3 Easy工作台双采样｜提示词增强图生视频生成_2097078423951859713.json、视频生成/图生视频/H3 最强去油双采样｜提示词全自动优化一步到位｜图生视频_2096829872772575233.json、视频生成/图生视频/H3多参2采加Qwen3.8提示词优化版，图生视频高质量创作工具_2106069445222420481.json、视频生成/图生视频/H3多参二采Qwen3.8提示词优化 角色一致性图生视频增强_2098660749190189058.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 12 个 workflow 都包含：
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
- `LoadImage` —— 11/12 个有
- `孤海注释` —— 10/12 个有
- `LoadAudio` —— 9/12 个有
- `SaveImage` —— 9/12 个有
- `CR Prompt Text` —— 8/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/12 个有
- `MiniMaxH3PromptEnhancerT8` —— 8/12 个有
- `PreviewAny` —— 8/12 个有
- `RH_Translator` —— 8/12 个有
- `VAEDecodeAudio` —— 8/12 个有
- `easy saveText` —— 8/12 个有
- `easy showAnything` —— 8/12 个有
- `Fast Groups Bypasser (rgthree)` —— 7/12 个有
- `H3SigmaRefiner` —— 7/12 个有
- `MiniMaxH3Easy` —— 7/12 个有
- `MiniMaxH3EasyModelAdapter` —— 7/12 个有
- `MiniMaxH3EasyOutput` —— 7/12 个有
- `MiniMaxH3EasySecondPassConditioning` —— 7/12 个有
- `ComfyMathExpression` —— 5/12 个有
- `GetNode` —— 5/12 个有
- `MiniMaxH3ReferenceToVideo` —— 5/12 个有
- `PrimitiveFloat` —— 5/12 个有
- `ResolutionSelector` —— 5/12 个有
- `SetNode` —— 5/12 个有
- `easy float` —— 5/12 个有
- `GoohaiMinimaxH3TiledSampler` —— 4/12 个有
- `LTXVAudioVAEEncode` —— 4/12 个有
- `ModelAttentionBackend` —— 4/12 个有
- `Seed (rgthree)` —— 4/12 个有
- `SetLatentNoiseMask` —— 4/12 个有
- `SolidMask` —— 4/12 个有
- `TrimAudioDuration` —— 4/12 个有
- `VHS_LoadVideo` —— 4/12 个有
- `easy indexTTSForceCleanup` —— 4/12 个有
- `Int` —— 3/12 个有
- `PreviewImage` —— 2/12 个有
- `EmptyImage` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（14/12 个样本）：Steps较低可能导致细节不足
