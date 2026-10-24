---
name: text_to_image_video_lora_sampler_146
type: Text To Image
frequency: 4
level: strong
coverage: 0.748
common_nodes: [BasicGuider, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, ImageScaleToMaxDimension, JjkText, KSampler, KSamplerSelect, LTXAVTextEncoderLoader, LTXVConditioning, LTXVLoopingSampler, LTXVSpatioTemporalTiledVAEDecode, LoadImage, LoraLoaderModelOnly, MiniMaxH3SigmaShift, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SolAttnPatch, SpectrumApplyMiniMaxH3, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncodeTiled, VAELoader, VHS_VideoCombine, VisualizeSigmasKJ, easy cleanGpuUsed, easy clearCacheAll, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/4步加速多参考注入｜MiniMax H3视频生成+LTX放大_2093843847783739394.json, 视频生成/图生视频/LTX放大工作流视频生成4步加速ref-多参考注入MiniMax_2086205211500175361.json, 视频生成/图生视频/ref多参考注入4步加速｜MiniMax H3战斗特效+LTX放大_2094049739330375681.json, 视频生成/文生视频/导演台双采SLA加速｜MiniMax H3 Latent Upscaler视频生成_2093122877859127297.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_146

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/4步加速多参考注入｜MiniMax H3视频生成+LTX放大_2093843847783739394.json、视频生成/图生视频/LTX放大工作流视频生成4步加速ref-多参考注入MiniMax_2086205211500175361.json、视频生成/图生视频/ref多参考注入4步加速｜MiniMax H3战斗特效+LTX放大_2094049739330375681.json、视频生成/文生视频/导演台双采SLA加速｜MiniMax H3 Latent Upscaler视频生成_2093122877859127297.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `ImageScaleToMaxDimension`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVConditioning`
- `LTXVLoopingSampler`
- `LTXVSpatioTemporalTiledVAEDecode`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3SigmaShift`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SolAttnPatch`
- `SpectrumApplyMiniMaxH3`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 3/4 个有
- `LTXVAudioVAELoader` —— 3/4 个有
- `ManualSigmas` —— 3/4 个有
- `MiniMaxH3ReferenceToVideo` —— 3/4 个有
- `VHS_LoadAudio` —— 3/4 个有
- `MiniMaxH3ImageToVideo` —— 1/4 个有
- `ResizeImageMaskNode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
