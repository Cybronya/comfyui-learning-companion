---
name: text_to_image_video_lora_sampler_43
type: Text To Image
frequency: 15
level: moderate
coverage: 0.8076
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLTXVLatentVideo, EmptyLatentImage, EnhancedLoadDiffusionModel, FluxKontextMultiReferenceLatentMethod, INTConstant, Int, KSampler, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LiconMSR, LoadImage, LoraLoaderModelOnly, LowVRAMCheckpointLoader, ManualSigmas, PreviewImage, RH_Captioner, RandomInt, RandomNoise, SamplerCustomAdvanced, Split String by Commas, StringReplace, Text, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader, VHS_VideoCombine, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy indexAnything, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/LTX-2.3_MSR V2 Gemma4开源版_2083136188516491265.json, 视频生成/图生视频/2079756676873408513.json, 视频生成/图生视频/LTX-2.3_MSR V2多参漫剧长镜头1_2083106849519398914.json, 视频生成/图生视频/2080241011628007425.json, 视频生成/图生视频/2081010266782912513.json, 视频生成/图生视频/2079758603824750594.json, 视频生成/图生视频/2080572501062672386.json, 视频生成/图生视频/LTX-2.3_MSR+V2漫剧自动多参分镜_2095747117393473538.json, 视频生成/图生视频/2079459174697754625.json, 视频生成/图生视频/2074464289334845442.json, 视频生成/图生视频/2074449807627874305.json, 视频生成/图生视频/2080283230909063170.json, 视频生成/图生视频/2073690383254646785.json, 视频生成/图生视频/2074389976934080514.json, 视频生成/图生视频/2073960338130817025.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_43

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3_MSR V2 Gemma4开源版_2083136188516491265.json、视频生成/图生视频/2079756676873408513.json、视频生成/图生视频/LTX-2.3_MSR V2多参漫剧长镜头1_2083106849519398914.json、视频生成/图生视频/2080241011628007425.json、视频生成/图生视频/2081010266782912513.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 15 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `EnhancedLoadDiffusionModel`
- `FluxKontextMultiReferenceLatentMethod`
- `INTConstant`
- `Int`
- `KSampler`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LiconMSR`
- `LoadImage`
- `LoraLoaderModelOnly`
- `LowVRAMCheckpointLoader`
- `ManualSigmas`
- `PreviewImage`
- `RH_Captioner`
- `RandomInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Split String by Commas`
- `StringReplace`
- `Text`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy indexAnything`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageConcatenate_UTK` —— 14/15 个有
- `CR Prompt Text` —— 13/15 个有
- `TextConcatenate_UTK` —— 13/15 个有
- `CR Float To Integer` —— 10/15 个有
- `FloatConstant` —— 10/15 个有
- `LTX2_NAG` —— 10/15 个有
- `PromptRelayEncode` —— 10/15 个有
- `SimpleMath+` —— 10/15 个有
- `CLIPVisionLoader` —— 5/15 个有
- `ExtractNFrames` —— 5/15 个有
- `GetNode` —— 5/15 个有
- `ImageResizeKJv2` —— 5/15 个有
- `ImageScaleToTotalPixels` —— 5/15 个有
- `JWInteger` —— 5/15 个有
- `SetNode` —— 5/15 个有
- `easy imageCount` —— 5/15 个有
- `DrawViTPose` —— 3/15 个有
- `OnnxDetectionModelLoader` —— 3/15 个有
- `PoseAndFaceDetection` —— 3/15 个有
- `WanAnimatePlus BlockSwap` —— 3/15 个有
- `WanVideoAnimateEmbeds` —— 3/15 个有
- `WanVideoClipVisionEncode` —— 3/15 个有
- `WanVideoDecode` —— 3/15 个有
- `WanVideoLoraSelectMulti` —— 3/15 个有
- `WanVideoModelLoader` —— 3/15 个有
- `WanVideoSampler` —— 3/15 个有
- `WanVideoSetBlockSwap` —— 3/15 个有
- `WanVideoSetLoRAs` —— 3/15 个有
- `WanVideoTextEncodeCached` —— 3/15 个有
- `WanVideoVAELoader` —— 3/15 个有
- `BatchImagesNode` —— 2/15 个有
- `CLIPVisionEncode` —— 2/15 个有
- `CheckpointLoaderSimple` —— 2/15 个有
- `DiffusionModelLoaderKJ` —— 2/15 个有
- `ModelSamplingSD3` —— 2/15 个有
- `SAM3_VideoTrack` —— 2/15 个有
- `SCAIL2ColoredMask` —— 2/15 个有
- `WanChunkFeedForward` —— 2/15 个有
- `WanContextWindowsManual` —— 2/15 个有
- `WanSCAILMultirefInfinity` —— 2/15 个有
- `WanVideoMemoryEfficientSageAttentionPatch` —— 2/15 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/15 个有
- `GIMMVFI_interpolate` —— 1/15 个有
- `llama_cpp_instruct_adv` —— 1/15 个有
- `llama_cpp_model_loader` —— 1/15 个有
- `llama_cpp_parameters` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 15 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 241 | 241 - 1280 | 15 | 7% |
| 高度 | 50 | 50 - 720 | 15 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 241，观测区间 241 - 1280，15 个样本，取值分散，一致性仅 7%
- 高度 中位数 50，观测区间 50 - 720，15 个样本，取值分散，一致性仅 0%
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
