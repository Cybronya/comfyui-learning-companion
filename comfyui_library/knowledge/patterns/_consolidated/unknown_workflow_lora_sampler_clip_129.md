---
name: unknown_workflow_lora_sampler_clip_129
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.851333
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, TrimAudioDuration, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/LTX 2.3-IA2V-国风 MV_2038201954467323905.json, 视频生成/图生视频/danotebook-ltx2.3-digital_2062522880226848770.json, 视频生成/图生视频/【LTX-2.3MV唱歌】输入歌词生成AI音乐？MV制作HeartMula+LTX2.3工作流实测_2044766587655294977.json, 视频生成/图生视频/【LTX-2.3xinyao】_2070029372056231937.json, 视频生成/图生视频/【LTX-2.3唱歌术】SongGeneration2+LTX2.3工作流_2046184684832428034.json, 视频生成/文生视频/【LTX-2.3唱歌术】输入歌词就能生成MV？SongGeneration2+LTX2.3工作流实测_2033104945955741697.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_129

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3-IA2V-国风 MV_2038201954467323905.json、视频生成/图生视频/danotebook-ltx2.3-digital_2062522880226848770.json、视频生成/图生视频/【LTX-2.3MV唱歌】输入歌词生成AI音乐？MV制作HeartMula+LTX2.3工作流实测_2044766587655294977.json、视频生成/图生视频/【LTX-2.3xinyao】_2070029372056231937.json、视频生成/图生视频/【LTX-2.3唱歌术】SongGeneration2+LTX2.3工作流_2046184684832428034.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SolidMask`
- `TrimAudioDuration`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 5/6 个有
- `CreateVideo` —— 5/6 个有
- `LTXAVTextEncoderLoader` —— 5/6 个有
- `LTXVLatentUpsampler` —— 5/6 个有
- `LatentUpscaleModelLoader` —— 5/6 个有
- `SaveVideo` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `Label (rgthree)` —— 4/6 个有
- `PrimitiveBoolean` —— 4/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `SaveAudio` —— 4/6 个有
- `HeartMuLa_Generate` —— 2/6 个有
- `HeartMuLa_Transcribe` —— 2/6 个有
- `PreviewAudio` —— 2/6 个有
- `ShowText|pysssss` —— 2/6 个有
- `SongGeneration_Loader` —— 2/6 个有
- `SongGeneration_Sampler` —— 2/6 个有
- `SongGeneration_Stage1` —— 2/6 个有
- `SongGeneration_Stage2` —— 2/6 个有
- `Text _O` —— 2/6 个有
- `Anything Everywhere` —— 1/6 个有
- `DiffusionModelLoaderKJ` —— 1/6 个有
- `DualCLIPLoaderGGUF` —— 1/6 个有
- `RH_LLMAPI_Pro_Node` —— 1/6 个有
- `RecordAudio` —— 1/6 个有
- `TextInput_` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有
- `VAELoaderKJ` —— 1/6 个有
- `VHS_VideoCombine` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
