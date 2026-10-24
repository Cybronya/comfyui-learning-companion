---
name: unknown_workflow_video_upscale_latent_upscale_70
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8902
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoraLoaderModelOnly, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PreviewAudio, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, TrimAudioDuration, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3 双人对口型横屏优化版（时长由说话时长决定）1920p_2045788656627097601.json, 视频生成/图生视频/LTX2.3 自用版 I2V Customer Audio_2063969467373281282.json, 视频生成/图生视频/🦞LTX-2.3 单人对口型数字人（带配音）极速无字幕版_2046500148146085890.json, 视频生成/文生视频/LTX2.3 自用优化版 T2V customer Audio_2063969507642798081.json, 音频生成/音频生成/Moss语音设计-LTX-2.3 双人 or 单人对口型优化版（时长由说话时长决定）1920p_2046997844069982210.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_70

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3 双人对口型横屏优化版（时长由说话时长决定）1920p_2045788656627097601.json、视频生成/图生视频/LTX2.3 自用版 I2V Customer Audio_2063969467373281282.json、视频生成/图生视频/🦞LTX-2.3 单人对口型数字人（带配音）极速无字幕版_2046500148146085890.json、视频生成/文生视频/LTX2.3 自用优化版 T2V customer Audio_2063969507642798081.json、音频生成/音频生成/Moss语音设计-LTX-2.3 双人 or 单人对口型优化版（时长由说话时长决定）1920p_2046997844069982210.json）

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
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PreviewAudio`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
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
- `LTXVAudioVAEDecode` —— 4/5 个有
- `LTXVImgToVideoInplace` —— 4/5 个有
- `LTXVPreprocess` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `PrimitiveBoolean` —— 4/5 个有
- `ResizeImagesByLongerEdge` —— 4/5 个有
- `CreateVideo` —— 3/5 个有
- `GetAudioDurationFromAudio` —— 3/5 个有
- `LayerUtility: PurgeVRAM V2` —— 3/5 个有
- `ResizeImageMaskNode` —— 3/5 个有
- `SimpleCalculatorKJ` —— 3/5 个有
- `Text` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `math_calculate` —— 3/5 个有
- `DiffusionModelLoaderKJ` —— 2/5 个有
- `LTX2_NAG` —— 2/5 个有
- `LTXTiledSampler` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `PromptRelayEncode` —— 2/5 个有
- `RunningHub_VoxCPM_Generate` —— 2/5 个有
- `RunningHub_VoxCPM_LoadModel` —— 2/5 个有
- `BasicScheduler` —— 1/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `LTXVChunkFeedForward` —— 1/5 个有
- `ModelPatchTorchSettings` —— 1/5 个有
- `MossTTSModelLoader` —— 1/5 个有
- `MossTTSVoiceDesign` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/5 个有
- `easy indexTTSGenerateSimple` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
