---
name: unknown_workflow_video_upscale_latent_upscale_57
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.662667
common_nodes: [AudioCrop, Bjornulf_ShowInt, CFGGuider, CLIPTextEncode, CM_IntToFloat, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, PainterAudioLength, PreviewAudio, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, VAEDecodeTiled, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3 _不变脸超自然数字人MV完美版_2037499415048495105.json, 数字人/数字人/虚拟歌手MV工作流进化版_ltx2.3 2ia2v_2042205278552199169.json, 视频生成/图生视频/MV间奏画面生成，ltx2.3 2i2v_2034984738728972289.json, 视频生成/图生视频/老胡超自然完美音乐数字人_2037219153244856322.json, 视频生成/图生视频/超自然人物唱歌：不变脸！：LTX2.3 _超自然数字人MV完美（发布版）_2035706238415151105.json, 音频生成/音频生成/超自然人物唱歌：不变脸！：_2046937022413152258.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_57

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/LTX2.3 _不变脸超自然数字人MV完美版_2037499415048495105.json、数字人/数字人/虚拟歌手MV工作流进化版_ltx2.3 2ia2v_2042205278552199169.json、视频生成/图生视频/MV间奏画面生成，ltx2.3 2i2v_2034984738728972289.json、视频生成/图生视频/老胡超自然完美音乐数字人_2037219153244856322.json、视频生成/图生视频/超自然人物唱歌：不变脸！：LTX2.3 _超自然数字人MV完美（发布版）_2035706238415151105.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioCrop`
- `Bjornulf_ShowInt`
- `CFGGuider`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplaceKJ`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PainterAudioLength`
- `PreviewAudio`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `FloatConstant` —— 5/6 个有
- `ImageResizeKJv2` —— 5/6 个有
- `Int` —— 5/6 个有
- `LTXAVTextEncoderLoader` —— 5/6 个有
- `LTXVChunkFeedForward` —— 5/6 个有
- `LTXVImgToVideoInplace` —— 5/6 个有
- `MathExpression_UTK` —— 5/6 个有
- `ModelPatchTorchSettings` —— 5/6 个有
- `PathchSageAttentionKJ` —— 5/6 个有
- `Text Multiline` —— 5/6 个有
- `CR Text Replace` —— 4/6 个有
- `HeartMuLa_Transcribe` —— 4/6 个有
- `ImageAndMaskResizeNode` —— 4/6 个有
- `ShowText|pysssss` —— 4/6 个有
- `Bjornulf_ShowFloat` —— 2/6 个有
- `GetImageRangeFromBatch` —— 2/6 个有
- `LTX2_NAG` —— 2/6 个有
- `MelBandRoFormerModelLoader` —— 2/6 个有
- `MelBandRoFormerSampler` —— 2/6 个有
- `TTResolutionSelector` —— 2/6 个有
- `Text` —— 2/6 个有
- `workflow>1` —— 2/6 个有
- `Audio To Text (mtb)` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `DualCLIPLoader` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `Float` —— 1/6 个有
- `ImpactSwitch` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `Load Whisper (mtb)` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `PrimitiveString` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `RH_LLMAPI_Pro_Node` —— 1/6 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `Resize` —— 1/6 个有
- `ResizeImagesByLongerEdge` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `TTP_text_mix` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
