---
name: unknown_workflow_video_upscale_latent_upscale_73
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.893
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PreviewAudio, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, TrimAudioDuration, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/Moss语音设计-LTX-2.3 双人 or 单人对口型优化版（时长由说话时长决定）无字幕版_2050361109261107202.json, 视频生成/图生视频/LTX-2.3 双人对口型横屏优化版（时长由说话时长决定）1920p_2045788656627097601.json, 视频生成/图生视频/LTX2.3 自用版 I2V Customer Audio_2063969467373281282.json, 视频生成/图生视频/🦞LTX-2.3 单人对口型数字人（带配音）极速无字幕版_2046500148146085890.json, 音频生成/音频生成/Moss语音设计-LTX-2.3 双人 or 单人对口型优化版（时长由说话时长决定）1920p_2046997844069982210.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_73

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/Moss语音设计-LTX-2.3 双人 or 单人对口型优化版（时长由说话时长决定）无字幕版_2050361109261107202.json、视频生成/图生视频/LTX-2.3 双人对口型横屏优化版（时长由说话时长决定）1920p_2045788656627097601.json、视频生成/图生视频/LTX2.3 自用版 I2V Customer Audio_2063969467373281282.json、视频生成/图生视频/🦞LTX-2.3 单人对口型数字人（带配音）极速无字幕版_2046500148146085890.json、音频生成/音频生成/Moss语音设计-LTX-2.3 双人 or 单人对口型优化版（时长由说话时长决定）1920p_2046997844069982210.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PreviewAudio`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SolidMask`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 4/5 个有
- `CreateVideo` —— 4/5 个有
- `GetAudioDurationFromAudio` —— 4/5 个有
- `LayerUtility: PurgeVRAM V2` —— 4/5 个有
- `PrimitiveBoolean` —— 4/5 个有
- `ResizeImageMaskNode` —— 4/5 个有
- `SimpleCalculatorKJ` —— 4/5 个有
- `Text` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `math_calculate` —— 4/5 个有
- `DiffusionModelLoaderKJ` —— 3/5 个有
- `RunningHub_VoxCPM_Generate` —— 3/5 个有
- `RunningHub_VoxCPM_LoadModel` —— 3/5 个有
- `Fast Groups Muter (rgthree)` —— 2/5 个有
- `MossTTSModelLoader` —— 2/5 个有
- `MossTTSVoiceDesign` —— 2/5 个有
- `LTX2_NAG` —— 1/5 个有
- `LTXTiledSampler` —— 1/5 个有
- `LTXVChunkFeedForward` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `ModelPatchTorchSettings` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `PromptRelayEncode` —— 1/5 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/5 个有
- `easy indexTTSGenerateSimple` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
