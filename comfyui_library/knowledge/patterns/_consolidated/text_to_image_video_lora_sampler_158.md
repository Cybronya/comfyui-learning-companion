---
name: text_to_image_video_lora_sampler_158
type: Text To Image
frequency: 3
level: strong
coverage: 0.806
common_nodes: [AudioCrop, AudioSeparation, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, CR Text, ConditioningZeroOut, DownloadAndLoadWav2VecModel, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, INTConstant, Int, Int Literal, JWIntegerToString, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, ModelSamplingFlux, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoaderV2, PreviewImage, PrimitiveInt, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SimpleMath+, Text, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy anythingIndexSwitch, easy showAnything]
problems: []
missing: [CR Text, Int Literal, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, Primitive integer [Crystools], SimpleMath+, easy anythingIndexSwitch]
members: [图片生成/文生图/1947858553363120130.json, 视频生成/图生视频/1947858553363120130.json, 视频生成/图生视频/1947973042778583042.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_158

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1947858553363120130.json、视频生成/图生视频/1947858553363120130.json、视频生成/图生视频/1947973042778583042.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Text`
- `ConditioningZeroOut`
- `DownloadAndLoadWav2VecModel`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `INTConstant`
- `Int`
- `Int Literal`
- `JWIntegerToString`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoaderV2`
- `PreviewImage`
- `PrimitiveInt`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SimpleMath+`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImpactStringSelector` —— 2/3 个有
- `Primitive integer [Crystools]` —— 2/3 个有
- `StringConcatenate` —— 2/3 个有
- `JjkText` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832 | 832 - 832 | 3 | 100% |
| 高度 | 1216 | 1216 - 1216 | 3 | 100% |
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 832，观测区间 832 - 832，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1216，观测区间 1216 - 1216，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Int Literal、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: PurgeVRAM、LayerUtility: PurgeVRAM V2
