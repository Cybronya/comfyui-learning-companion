---
name: text_to_image_upscale_lora_sampler_25
type: Text To Image
frequency: 5
level: strong
coverage: 0.9188
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, CreateVideo, DF_Int_to_Float, EasyCache, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetVideoComponents, ImageResizeKJv2, ImpactSwitch, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LoadAudio, LoadImage, LoadVideo, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, RandomNoise, RandomSeedNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowAnything|Mie, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAEEncodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/h3 singularity提示词优化反推加速双采｜非高低噪声采样_2111064379713220609.json, 视频生成/图生视频/h3 singularity提示词优化反推，加速双采视频生视频_2111198491438575618.json, 视频生成/图生视频/h3 singularity模型提示词优化反推加速双采非高低噪声 视频生成优化_2109705983533600769.json, 视频生成/文生视频/MiniMax H3 Singularity VDN加速双采高步数图生视频处理工具_2102458025251532801.json, 视频生成/文生视频/h3提示词优化反推加速双采 视频生成优化方案_2108669589306568706.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_25

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/h3 singularity提示词优化反推加速双采｜非高低噪声采样_2111064379713220609.json、视频生成/图生视频/h3 singularity提示词优化反推，加速双采视频生视频_2111198491438575618.json、视频生成/图生视频/h3 singularity模型提示词优化反推加速双采非高低噪声 视频生成优化_2109705983533600769.json、视频生成/文生视频/MiniMax H3 Singularity VDN加速双采高步数图生视频处理工具_2102458025251532801.json、视频生成/文生视频/h3提示词优化反推加速双采 视频生成优化方案_2108669589306568706.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `CreateVideo`
- `DF_Int_to_Float`
- `EasyCache`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetVideoComponents`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `RandomSeedNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowAnything|Mie`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `DapaoH3LocalPromptNode` —— 4/5 个有
- `DapaoH3PromptBoxNode` —— 4/5 个有
- `PreviewAny` —— 4/5 个有
- `SaveAudio` —— 4/5 个有
- `SaveImage` —— 4/5 个有
- `T8_IndexTTS25_EmotionControl` —— 4/5 个有
- `T8_IndexTTS25_Generate` —— 4/5 个有
- `T8_IndexTTS25_ModelLoader` —— 4/5 个有
- `BasicScheduler` —— 3/5 个有
- `ManualSigmas` —— 3/5 个有
- `MiniMaxH3VDNRuntimeAuditT8Advanced` —— 3/5 个有
- `SolAttnMiniMax` —— 3/5 个有
- `GoohaiUniversalSlider` —— 2/5 个有
- `MiniMaxH3SparkAttentionAuto` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
