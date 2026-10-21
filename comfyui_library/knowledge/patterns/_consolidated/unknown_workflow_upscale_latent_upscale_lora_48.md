---
name: unknown_workflow_upscale_latent_upscale_lora_48
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.852286
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2039165345923080193.json, 视频生成/图生视频/2062522880226848770.json, 视频生成/图生视频/2057789192654123010.json, 视频生成/图生视频/2044766587655294977.json, 视频生成/图生视频/2070029372056231937.json, 视频生成/图生视频/2046184684832428034.json, 视频生成/文生视频/【LTX-2.3唱歌术】输入歌词就能生成MV？SongGeneration2+LTX2.3工作流实测_2033104945955741697.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_48

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2039165345923080193.json、视频生成/图生视频/2062522880226848770.json、视频生成/图生视频/2057789192654123010.json、视频生成/图生视频/2044766587655294977.json、视频生成/图生视频/2070029372056231937.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LTXVImgToVideoInplace`
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
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LTXVAudioVAEEncode` —— 6/7 个有
- `LoadAudio` —— 6/7 个有
- `PrimitiveBoolean` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `SetLatentNoiseMask` —— 6/7 个有
- `SolidMask` —— 6/7 个有
- `TrimAudioDuration` —— 6/7 个有
- `Label (rgthree)` —— 5/7 个有
- `PrimitiveFloat` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `SaveAudio` —— 4/7 个有
- `PreviewAudio` —— 3/7 个有
- `HeartMuLa_Generate` —— 2/7 个有
- `HeartMuLa_Transcribe` —— 2/7 个有
- `LoraLoader` —— 2/7 个有
- `PreviewAny` —— 2/7 个有
- `ShowText|pysssss` —— 2/7 个有
- `SongGeneration_Loader` —— 2/7 个有
- `SongGeneration_Sampler` —— 2/7 个有
- `SongGeneration_Stage1` —— 2/7 个有
- `SongGeneration_Stage2` —— 2/7 个有
- `Text _O` —— 2/7 个有
- `TextGenerateLTX2Prompt` —— 2/7 个有
- `AudioInfo` —— 1/7 个有
- `Bjornulf_ShowInt` —— 1/7 个有
- `ComfySwitchNode` —— 1/7 个有
- `FishS2VoiceCloneTTS` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `LTXVEmptyLatentAudio` —— 1/7 个有
- `RH_LLMAPI_Pro_Node` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `StringReplace` —— 1/7 个有
- `TextInput_` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 97 | - | 1 | 100% |
| 高度 | 25 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
