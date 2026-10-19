---
name: unknown_workflow_upscale_latent_upscale_lora_27
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8656
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2062522880226848770.json, 视频生成/图生视频/2062486746893471745.json, 视频生成/图生视频/2062515403225649154.json, 视频生成/图生视频/2053653678917206018.json, 视频生成/图生视频/2053653864032813058.json, 视频生成/图生视频/2057789192654123010.json, 视频生成/图生视频/2044766587655294977.json, 视频生成/图生视频/2070029372056231937.json, 视频生成/图生视频/2046184684832428034.json, 视频生成/文生视频/【LTX-2.3唱歌术】输入歌词就能生成MV？SongGeneration2+LTX2.3工作流实测_2033104945955741697.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_27

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2062522880226848770.json、视频生成/图生视频/2062486746893471745.json、视频生成/图生视频/2062515403225649154.json、视频生成/图生视频/2053653678917206018.json、视频生成/图生视频/2053653864032813058.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoInplace` —— 8/10 个有
- `ResizeImagesByLongerEdge` —— 8/10 个有
- `PrimitiveBoolean` —— 7/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `LTXVAudioVAEEncode` —— 5/10 个有
- `LTXVEmptyLatentAudio` —— 5/10 个有
- `LoadAudio` —— 5/10 个有
- `PrimitiveFloat` —— 5/10 个有
- `SetLatentNoiseMask` —— 5/10 个有
- `SolidMask` —— 5/10 个有
- `TrimAudioDuration` —— 5/10 个有
- `Fast Groups Bypasser (rgthree)` —— 4/10 个有
- `Label (rgthree)` —— 4/10 个有
- `SaveAudio` —— 4/10 个有
- `RH_LLMAPI_Pro_Node` —— 3/10 个有
- `HeartMuLa_Generate` —— 2/10 个有
- `HeartMuLa_Transcribe` —— 2/10 个有
- `LTXVAddGuide` —— 2/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/10 个有
- `PreviewAudio` —— 2/10 个有
- `SamplerEulerAncestral` —— 2/10 个有
- `ShowText|pysssss` —— 2/10 个有
- `SongGeneration_Loader` —— 2/10 个有
- `SongGeneration_Sampler` —— 2/10 个有
- `SongGeneration_Stage1` —— 2/10 个有
- `SongGeneration_Stage2` —— 2/10 个有
- `Text _O` —— 2/10 个有
- `ComfySwitchNode` —— 1/10 个有
- `GetNode` —— 1/10 个有
- `LoraLoader` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `SetNode` —— 1/10 个有
- `TextGenerateLTX2Prompt` —— 1/10 个有
- `TextInput_` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
