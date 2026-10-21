---
name: text_to_image_video_lora_sampler_126
type: Text To Image
frequency: 5
level: strong
coverage: 0.6506
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, ExtendIntermediateSigmas, Fast Groups Bypasser (rgthree), GetNode, HeartMuLa_Transcribe, ImpactSwitch, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PreviewAny, PreviewImage, PrimitiveBoolean, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SoundFlow_GetLength, TTP_text_mix, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, VRGDG_AudioCrop, VRGDG_MiniMaxH3AudioDrive, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3三采数字人｜兼具质量速度场景特效图生视频_2089725152933277697.json, 视频生成/图生视频/兼具质量和速度的数字人｜场景特效图生视频生成_2094487993674461186.json, 视频生成/图生视频/质量与速度兼具的数字人｜口播视频高质量生成_2095938630001979394.json, 视频生成/图生视频/质量速度兼得的数字人｜图生视频场景特效一步到位_2096221676143992834.json, 视频生成/图生视频/速度质量双在线数字人｜场景类特效图生视频一键生成_2094711089618575362.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_126

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3三采数字人｜兼具质量速度场景特效图生视频_2089725152933277697.json、视频生成/图生视频/兼具质量和速度的数字人｜场景特效图生视频生成_2094487993674461186.json、视频生成/图生视频/质量与速度兼具的数字人｜口播视频高质量生成_2095938630001979394.json、视频生成/图生视频/质量速度兼得的数字人｜图生视频场景特效一步到位_2096221676143992834.json、视频生成/图生视频/速度质量双在线数字人｜场景类特效图生视频一键生成_2094711089618575362.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `ExtendIntermediateSigmas`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `HeartMuLa_Transcribe`
- `ImpactSwitch`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SoundFlow_GetLength`
- `TTP_text_mix`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VRGDG_AudioCrop`
- `VRGDG_MiniMaxH3AudioDrive`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 4/5 个有
- `LTXVSeparateAVLatent` —— 4/5 个有
- `MinimaxH3LatentUpscaler3D` —— 4/5 个有
- `easy ab` —— 4/5 个有
- `LoraLoaderBypassModelOnly` —— 2/5 个有
- `MiniMaxH3SigmaShift` —— 2/5 个有
- `ModelAttentionBackend` —— 2/5 个有
- `ComfySwitchNode` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `MiniMaxH3BlockCacheT8` —— 1/5 个有
- `PT_H3ConcatAVLatent` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `RunningHub Deepcleaner` —— 1/5 个有
- `VAEEncode` —— 1/5 个有
- `VAEEncodeAudio` —— 1/5 个有

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
