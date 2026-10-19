---
name: unknown_workflow_video_upscale_latent_upscale_4
type: Unknown Workflow
frequency: 30
level: moderate
coverage: 0.502467
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, JoinStrings, KSamplerSelect, LTX2AttentionTunerPatch, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/LTX2.3图片数字人v1_2106250175076458497.json, 数字人/数字人/LTX2.3数字人说话唱歌对口型+运镜+合并版_2085320561093341186.json, 数字人/数字人/数字人视频生成：LTX2.3 BGM+TTS优化版_2083187553284476929.json, 视频生成/图生视频/2078432143432314882.json, 视频生成/图生视频/LTX2.3+音频驱动_2084104031198343170.json, 视频生成/图生视频/2043611581572976641.json, 视频生成/图生视频/2043656293486956545.json, 视频生成/图生视频/2044745216434900994.json, 视频生成/图生视频/LTX2.3数字人、真人说话唱歌对口型！优化版！_2098723249088712705.json, 视频生成/图生视频/2060192236796727297.json, 视频生成/图生视频/2060281749111922689.json, 视频生成/图生视频/2060318631426347009.json, 视频生成/图生视频/LTX2.3数字人说话唱歌对口型优化升级kj版加速版_2108927748189286401.json, 视频生成/图生视频/2067555501503766529.json, 视频生成/图生视频/2067555732677029890.json, 视频生成/图生视频/2031003304490180610.json, 视频生成/图生视频/2044045789097369601.json, 视频生成/图生视频/2079447302481211393.json, 视频生成/图生视频/LTX2.3数字人说话唱歌对口型！优化升级kj版！_2095323014882746369.json, 视频生成/图生视频/2064388812364673025.json, 视频生成/图生视频/2069216975854854145.json, 视频生成/图生视频/数字人带货视频LTX2.3_2083076708705587201.json, 视频生成/图生视频/2082357953612566530.json, 视频生成/图生视频/数字人说话唱歌LTV2.0_图片对口型_2083114579193843713.json, 视频生成/图生视频/2060719943548751873.json, 视频生成/图生视频/2062353312200093697.json, 视频生成/图生视频/数字人说话带货视频-文本驱动-升级版_2082813113300250626.json, 视频生成/图生视频/2046477938211692546.json, 视频生成/文生视频/LTX2.3 数字人说话唱歌对口型 深度优化升级kj版_2056553193026449410.json, 视频生成/文生视频/图生视频 LTX2.3数字人说话唱歌对口型 优化升级kj版_2062723981005905921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_4

> 由 `engine/knowledge_consolidation` 从 30 个 workflow 归纳得出（数字人/数字人/LTX2.3图片数字人v1_2106250175076458497.json、数字人/数字人/LTX2.3数字人说话唱歌对口型+运镜+合并版_2085320561093341186.json、数字人/数字人/数字人视频生成：LTX2.3 BGM+TTS优化版_2083187553284476929.json、视频生成/图生视频/2078432143432314882.json、视频生成/图生视频/LTX2.3+音频驱动_2084104031198343170.json…）

- **类型**：Unknown Workflow
- **样本数**：30
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 30 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `JoinStrings`
- `KSamplerSelect`
- `LTX2AttentionTunerPatch`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 29/30 个有
- `GetImageSize` —— 29/30 个有
- `INTConstant` —— 29/30 个有
- `ImageResizeKJv2` —— 29/30 个有
- `LayerUtility: PurgeVRAM` —— 29/30 个有
- `PrimitiveStringMultiline` —— 29/30 个有
- `SimpleCalculatorKJ` —— 29/30 个有
- `VAELoaderKJ` —— 29/30 个有
- `LTXVChunkFeedForward` —— 25/30 个有
- `Compare` —— 24/30 个有
- `Int` —— 24/30 个有
- `LoraLoaderModelOnly` —— 24/30 个有
- `SimpleMath+` —— 24/30 个有
- `easy showAnything` —— 24/30 个有
- `InversionDemoLazySwitch` —— 23/30 个有
- `PreviewAudio` —— 19/30 个有
- `VHS_LoadAudioUpload` —— 19/30 个有
- `LoadAudio` —— 12/30 个有
- `IndexTTS2_Basic` —— 3/30 个有
- `JjkText` —— 3/30 个有
- `SaveAudio` —— 3/30 个有
- `AudioTrim` —— 1/30 个有
- `Float` —— 1/30 个有
- `GetAudioDurationFromAudio` —— 1/30 个有
- `LTX2MemoryEfficientSageAttentionPatch` —— 1/30 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/30 个有
- `LayerUtility: PurgeVRAM V2` —— 1/30 个有
- `LazySwitchKJ` —— 1/30 个有
- `PainterAudioLength` —— 1/30 个有
- `RH_GetAudioDuration` —— 1/30 个有
- `RH_LLMAPI_NODE` —— 1/30 个有
- `ShowAnything|Mie` —— 1/30 个有
- `SoundFlow_Mixer` —— 1/30 个有
- `Text` —— 1/30 个有
- `孤海注释` —— 1/30 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
