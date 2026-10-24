---
name: text_to_image_video_lora_sampler_169
type: Text To Image
frequency: 3
level: strong
coverage: 0.659
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyNumberConvert, EmptyLTXVLatentVideo, EmptyLatentImage, INTConstant, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LTX2AttentionTunerPatch, LTX2SamplingPreviewOverride, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveFloat, PromptRelayEncode, RandomNoise, SamplerCustomAdvanced, SimpleCalculatorKJ, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/LTX2.3+MSR多主体生视频｜图生视频一键直出_2092011625753698306.json, 视频生成/图生视频/LTX2.5多参视频生成MSR2BFS图生视频工作流_2088203562252853249.json, 视频生成/图生视频/多主体生视频｜LTX2.3+MSR图生视频生成_2092155116446117890.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_169

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/LTX2.3+MSR多主体生视频｜图生视频一键直出_2092011625753698306.json、视频生成/图生视频/LTX2.5多参视频生成MSR2BFS图生视频工作流_2088203562252853249.json、视频生成/图生视频/多主体生视频｜LTX2.3+MSR图生视频生成_2092155116446117890.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyNumberConvert`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `INTConstant`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTX2AttentionTunerPatch`
- `LTX2SamplingPreviewOverride`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PromptRelayEncode`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleCalculatorKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 2/3 个有
- `ComfyMathExpression` —— 2/3 个有
- `ComfySwitchNode` —— 2/3 个有
- `DualCLIPLoader` —— 2/3 个有
- `GetImageSizeAndCount` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `LTX2MemoryEfficientSageAttentionPatch` —— 2/3 个有
- `LTX2_NAG` —— 2/3 个有
- `LTXVLatentUpsampler` —— 2/3 个有
- `LatentUpscaleModelLoader` —— 2/3 个有
- `ManualSigmas` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `LTXVDualCFGGuider` —— 1/3 个有
- `LTXVImgToVideoInplace` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
