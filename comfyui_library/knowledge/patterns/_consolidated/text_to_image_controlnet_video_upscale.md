---
name: text_to_image_controlnet_video_upscale
type: Text To Image
frequency: 4
level: strong
coverage: 0.559
common_nodes: [ACN_AdvancedControlNetApply, ADE_AnimateDiffLoaderWithContext, ADE_AnimateDiffSamplingSettings, ADE_ApplyAnimateDiffModelSimple, ADE_IterationOptsFreeInit, ADE_LoadAnimateDiffModel, ADE_StandardStaticContextOptions, ADE_UseEvolvedSampling, AddMask, Any Switch (rgthree), BasicScheduler, CLIPSetLastLayer, CLIPTextEncode, CR Text, CheckpointLoaderSimple, CheckpointLoaderSimpleWithNoiseSelect, ConstrainImageforVideo|pysssss, ControlNetLoader, DWPreprocessor, EmptyImage, EmptyLatentImage, Fast Groups Muter (rgthree), FloatConstant, FreeU_V2, GetImageSizeAndCount, GetNode, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), GrowMask, HEDPreprocessor, INTConstant, ImageCompositeMasked, ImageConcatMulti, ImageScale, ImpactImageInfo, InvertMask, KSampler, LatentUpscaleBy, LineArtPreprocessor, LoadImage, LoraLoader, LoraLoaderModelOnly, LoraLoader|pysssss, MaskToImage, ModelSamplingDiscrete, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), MyOpenPoseNode, OpenposePreprocessor, Primitive string multiline [Crystools], RepeatImageBatch, ResizeMask, SAMModelLoader (segment anything), SamplerCustom, SamplerLCMCycle, Seed (rgthree), SetLatentNoiseMask, SetNode, VAEDecode, VAEEncode, VAELoader, VHS_DuplicateMasks, VHS_LoadVideo, VHS_SplitImages, VHS_VideoCombine, easy cleanGpuUsed, easy if, smZ CLIPTextEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/视频转绘真人转动漫风格_1912845933527400449.json, 平台全量/视频转绘真人转动漫风格_1912881889969958913.json, 平台全量/视频转绘真人转动漫风格_1977339549393264641.json, 平台全量/视频转绘真人转动漫（指定角色Lora）_1872221952633925633.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_video_upscale

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/视频转绘真人转动漫风格_1912845933527400449.json、平台全量/视频转绘真人转动漫风格_1912881889969958913.json、平台全量/视频转绘真人转动漫风格_1977339549393264641.json、平台全量/视频转绘真人转动漫（指定角色Lora）_1872221952633925633.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 4 个 workflow 都包含：
- `ACN_AdvancedControlNetApply`
- `ADE_AnimateDiffLoaderWithContext`
- `ADE_AnimateDiffSamplingSettings`
- `ADE_ApplyAnimateDiffModelSimple`
- `ADE_IterationOptsFreeInit`
- `ADE_LoadAnimateDiffModel`
- `ADE_StandardStaticContextOptions`
- `ADE_UseEvolvedSampling`
- `AddMask`
- `Any Switch (rgthree)`
- `BasicScheduler`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `CheckpointLoaderSimpleWithNoiseSelect`
- `ConstrainImageforVideo|pysssss`
- `ControlNetLoader`
- `DWPreprocessor`
- `EmptyImage`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `FloatConstant`
- `FreeU_V2`
- `GetImageSizeAndCount`
- `GetNode`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMask`
- `HEDPreprocessor`
- `INTConstant`
- `ImageCompositeMasked`
- `ImageConcatMulti`
- `ImageScale`
- `ImpactImageInfo`
- `InvertMask`
- `KSampler`
- `LatentUpscaleBy`
- `LineArtPreprocessor`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `LoraLoader|pysssss`
- `MaskToImage`
- `ModelSamplingDiscrete`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `MyOpenPoseNode`
- `OpenposePreprocessor`
- `Primitive string multiline [Crystools]`
- `RepeatImageBatch`
- `ResizeMask`
- `SAMModelLoader (segment anything)`
- `SamplerCustom`
- `SamplerLCMCycle`
- `Seed (rgthree)`
- `SetLatentNoiseMask`
- `SetNode`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_DuplicateMasks`
- `VHS_LoadVideo`
- `VHS_SplitImages`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy if`
- `smZ CLIPTextEncode`

**可变部分**（部分 workflow 才有）：
- `BOOLConstant` —— 3/4 个有
- `CLIPVisionLoader` —— 3/4 个有
- `EditBasicPipe` —— 3/4 个有
- `FromBasicPipe` —— 3/4 个有
- `IPAdapterAdvanced` —— 3/4 个有
- `IPAdapterModelLoader` —— 3/4 个有
- `ImpactSimpleDetectorSEGS_for_AD` —— 3/4 个有
- `MaskBlur+` —— 3/4 个有
- `PrepImageForClipVision` —— 3/4 个有
- `RebatchLatents` —— 3/4 个有
- `SAMLoader` —— 3/4 个有
- `SEGSDetailerForAnimateDiff` —— 3/4 个有
- `SEGSPaste` —— 3/4 个有
- `TEEDPreprocessor` —— 3/4 个有
- `ToBasicPipe` —— 3/4 个有
- `UltralyticsDetectorProvider` —— 3/4 个有
- `JWInteger` —— 2/4 个有
- `ExpressionEditor` —— 1/4 个有
- `Fast Actions Button (rgthree)` —— 1/4 个有
- `ImageListToImageBatch` —— 1/4 个有
- `MarigoldDepthEstimation` —— 1/4 个有
- `RebatchImages` —— 1/4 个有
- `SingleBooleanTrigger` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | ddim | - | 4 | 100% |
| 调度器 | sgm_uniform | - | 4 | 100% |
| 重绘幅度 | 1 | 0.35 - 1 | 4 | 66% |
| ControlNet 权重 | 0.6 | 0.4 - 0.6 | 4 | 84% |
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 768 | 768 - 768 | 4 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ddim，4 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，4 个样本
- ControlNet 权重 中位数 0.6，观测区间 0.4 - 0.6，4 个样本，取值集中（一致性 84%）
- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 768，观测区间 768 - 768，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
