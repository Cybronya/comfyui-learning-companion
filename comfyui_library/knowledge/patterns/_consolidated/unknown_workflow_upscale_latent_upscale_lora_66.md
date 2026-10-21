---
name: unknown_workflow_upscale_latent_upscale_lora_66
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.641667
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, Seed (rgthree), SetLatentNoiseMask, SetNode, SolidMask, VAEDecodeTiled]
problems: []
missing: []
members: [图片生成/文生图/LTX2 科比数字人工作流 （附加显存清理）_2013098604533129218.json, 图片生成/文生图/LTX2 科比数字人工作流_2012930792564985857.json, 视频生成/文生视频/ltx-2对口型_2011736436441092097.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_66

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/LTX2 科比数字人工作流 （附加显存清理）_2013098604533129218.json、图片生成/文生图/LTX2 科比数字人工作流_2012930792564985857.json、视频生成/文生视频/ltx-2对口型_2011736436441092097.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetNode`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `CreateVideo` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `SaveVideo` —— 2/3 个有
- `VHS_LoadAudio` —— 2/3 个有
- `Float` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `LTXVImgToVideoInplace` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `TrimAudioDuration` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
