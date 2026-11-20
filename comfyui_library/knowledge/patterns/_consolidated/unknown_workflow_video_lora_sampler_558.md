---
name: unknown_workflow_video_lora_sampler_558
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8215
common_nodes: [AudioCrop, BasicScheduler, CLIPTextEncode, CM_IntToFloat, CR Text, DapaoSmartMemoryOptimizerNode, Display Int (rgthree), DualCLIPLoader, EmptyImage, EmptyLTXVLatentVideo, Get resolution [Crystools], KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, PrimitiveString, SamplerCustom, SetLatentNoiseMask, SimpleMath+, SolidMask, SoundFlow_GetLength, Switch any [Crystools], ToInt, UNETLoader, VAEDecode, VAELoaderKJ, VHS_VideoCombine, ZML_ArithmeticComparison, easy cleanGpuUsed, easy int, easy seed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3视频MV版2_2061422103609569282.json, 视频生成/图生视频/LTX2.3视频MV版3_2061422054284554242.json, 视频生成/图生视频/ltx2.3视频MV_2056299096574619650.json, 视频生成/图生视频/急速图生视频mv抽卡必备_2051941097793966081.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_558

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LTX2.3视频MV版2_2061422103609569282.json、视频生成/图生视频/LTX2.3视频MV版3_2061422054284554242.json、视频生成/图生视频/ltx2.3视频MV_2056299096574619650.json、视频生成/图生视频/急速图生视频mv抽卡必备_2051941097793966081.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioCrop`
- `BasicScheduler`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `CR Text`
- `DapaoSmartMemoryOptimizerNode`
- `Display Int (rgthree)`
- `DualCLIPLoader`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `Get resolution [Crystools]`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveString`
- `SamplerCustom`
- `SetLatentNoiseMask`
- `SimpleMath+`
- `SolidMask`
- `SoundFlow_GetLength`
- `Switch any [Crystools]`
- `ToInt`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `ZML_ArithmeticComparison`
- `easy cleanGpuUsed`
- `easy int`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 3/4 个有
- `Display Any (rgthree)` —— 3/4 个有
- `LTXVImgToVideoInplaceKJ` —— 3/4 个有
- `RH_Captioner` —— 3/4 个有
- `CrossFadeImages` —— 2/4 个有
- `FrameSelector` —— 2/4 个有
- `GetImageSizeAndCount` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `ImageBatchMulti` —— 2/4 个有
- `Int` —— 2/4 个有
- `LTXVAddGuideMultiDynamic` —— 2/4 个有
- `LTXVCropGuides` —— 2/4 个有
- `Make Image Batch` —— 2/4 个有
- `MathExpression|pysssss` —— 2/4 个有
- `MelBandRoFormerModelLoader` —— 2/4 个有
- `MelBandRoFormerSampler` —— 2/4 个有
- `NormalizeAudioLoudness` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
