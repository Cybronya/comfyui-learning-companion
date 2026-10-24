---
name: text_to_image_lora_sampler_clip_123
type: Text To Image
frequency: 12
level: strong
coverage: 0.856167
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/全行业广告制作加音频驱动加提示词生成器辅助扩写，数字人电商产品方案_2107226505611923457.json, 数字人/数字人/全行业广告制作助手｜音频驱动加提示词生成器辅助扩写_2106927316462039041.json, 视频生成/图生视频/H3多图生视频数字人带货 MiniMax开源版电商口播方案_2104675527998136322.json, 视频生成/图生视频/H3多图生视频数字人带货 MiniMax开源版电商口播方案_2104762447012917250.json, 视频生成/图生视频/H3多图生视频数字人带货 MiniMax开源版电商口播方案_2105440243649441794.json, 视频生成/图生视频/MiniMax H3 Digital Avatars for Video E co数字人视频带货方案_2108634054257111041.json, 视频生成/图生视频/MiniMax H3图生视频2K快速版，支持15秒长视频场景特效方案_2103610501115768833.json, 视频生成/图生视频/MiniMax H3图生视频fastH3加速 trim latent放大增强_2110250634422341633.json, 视频生成/图生视频/MiniMax H3图生视频fastH3加速 trim latent放大增强_2110365841622659073.json, 视频生成/图生视频/MiniMax H3图生视频首尾帧视频二采加速版 高质量动态生成_2105373937122242561.json, 视频生成/图生视频/MiniMax H3首尾帧二采加速版｜图生视频稳定出片_2105267559749734401.json, 视频生成/图生视频/全行业广告制作助手｜音频驱动加提示词生成器辅助扩写_2107981763464220673.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_123

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（数字人/数字人/全行业广告制作加音频驱动加提示词生成器辅助扩写，数字人电商产品方案_2107226505611923457.json、数字人/数字人/全行业广告制作助手｜音频驱动加提示词生成器辅助扩写_2106927316462039041.json、视频生成/图生视频/H3多图生视频数字人带货 MiniMax开源版电商口播方案_2104675527998136322.json、视频生成/图生视频/H3多图生视频数字人带货 MiniMax开源版电商口播方案_2104762447012917250.json、视频生成/图生视频/H3多图生视频数字人带货 MiniMax开源版电商口播方案_2105440243649441794.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 11/12 个有
- `VHS_VideoCombine` —— 10/12 个有
- `MinimaxH3LatentUpscaler3D` —— 9/12 个有
- `PrimitiveFloat` —— 9/12 个有
- `SaveImage` —— 9/12 个有
- `VAEDecodeAudio` —— 9/12 个有
- `GetNode` —— 8/12 个有
- `MiniMaxH3ReferenceToVideo` —— 8/12 个有
- `SetNode` —— 8/12 个有
- `ManualSigmas` —— 7/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/12 个有
- `MiniMaxH3SigmaShift` —— 5/12 个有
- `ModelAttentionBackend` —— 5/12 个有
- `PrimitiveStringMultiline` —— 5/12 个有
- `easy showAnything` —— 5/12 个有
- `MiniMaxH3ImageToVideo` —— 4/12 个有
- `SplitSigmas` —— 4/12 个有
- `CR Text` —— 3/12 个有
- `INTConstant` —— 3/12 个有
- `LTXVAudioVAEEncode` —— 3/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/12 个有
- `LoadAudio` —— 3/12 个有
- `MultiTextConcatenate` —— 3/12 个有
- `MuyeTextEditOutput` —— 3/12 个有
- `RHLLMChatNode` —— 3/12 个有
- `SetLatentNoiseMask` —— 3/12 个有
- `SolidMask` —— 3/12 个有
- `SoundFlow_GetLength` —— 3/12 个有
- `BlockSparseAttention` —— 2/12 个有
- `CreateVideo` —— 2/12 个有
- `ExtendIntermediateSigmas` —— 2/12 个有
- `SaveVideo` —— 2/12 个有
- `EmptyImage` —— 1/12 个有
- `PreviewImage` —— 1/12 个有

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
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
