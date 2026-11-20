---
name: unknown_workflow_upscale_latent_upscale_sampler_14
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.8865
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, Int, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, QZ_ResolutionPreset, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleMath+, TrimAudioDuration, UNETLoader, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.3 3阶生成，QWEN TTS+FISH AUDIO+ID LORA工作流合集_2040662756164116482.json, 视频生成/文生视频/Ltx2.3数字人唱歌6.9_2064342443386032129.json, 视频生成/文生视频/Ltx2.3数字人唱歌_2039181216796123137.json, 视频生成/文生视频/ltx2.3 +ID LORA 自定义音频工作流-v2_2040424730452303873.json, 视频生成/文生视频/ltx2.3 +ID LORA 自定义音频工作流_2040214667628384257.json, 视频生成/文生视频/ltx2.3 +fish audio 多人对话 工作流_2039992569207201794.json, 视频生成/文生视频/ltx2.3 多人对话工作流-宠物对话_2039689143625719809.json, 视频生成/文生视频/ltx2.3 多人对话工作流_2039300843228372993.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_14

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/LTX2.3 3阶生成，QWEN TTS+FISH AUDIO+ID LORA工作流合集_2040662756164116482.json、视频生成/文生视频/Ltx2.3数字人唱歌6.9_2064342443386032129.json、视频生成/文生视频/Ltx2.3数字人唱歌_2039181216796123137.json、视频生成/文生视频/ltx2.3 +ID LORA 自定义音频工作流-v2_2040424730452303873.json、视频生成/文生视频/ltx2.3 +ID LORA 自定义音频工作流_2040214667628384257.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `Int`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `QZ_ResolutionPreset`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleMath+`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 7/8 个有
- `PrimitiveInt` —— 7/8 个有
- `SaveVideo` —— 7/8 个有
- `CM_FloatToInt` —— 6/8 个有
- `GetNode` —— 6/8 个有
- `LTXVAudioVAEEncode` —— 6/8 个有
- `LoadAudio` —— 6/8 个有
- `PreviewAudio` —— 6/8 个有
- `RH_LLMAPI_Pro_Node` —— 6/8 个有
- `SetLatentNoiseMask` —— 6/8 个有
- `SolidMask` —— 6/8 个有
- `SoundFlow_GetLength` —— 6/8 个有
- `easy cleanGpuUsed` —— 6/8 个有
- `easy showAnything` —— 6/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `CR Text` —— 4/8 个有
- `ConcatTextOfUtils` —— 4/8 个有
- `LTX2_NAG` —— 4/8 个有
- `FB_Qwen3TTSDialogueInference` —— 3/8 个有
- `FB_Qwen3TTSRoleBank` —— 3/8 个有
- `FB_Qwen3TTSVoiceClonePrompt` —— 3/8 个有
- `FB_Qwen3TTSVoiceDesign` —— 3/8 个有
- `LTXVEmptyLatentAudio` —— 3/8 个有
- `LTXVReferenceAudio` —— 3/8 个有
- `ModelMemoryUsageFactorOverride` —— 3/8 个有
- `ShowAnything|Mie` —— 3/8 个有
- `ResizeImageMaskNode` —— 2/8 个有
- `1hew_SaveVideo` —— 1/8 个有
- `Audio To Text (mtb)` —— 1/8 个有
- `DF_Int_to_Float` —— 1/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `FishS2MultiSpeakerTTS` —— 1/8 个有
- `LTXVPreprocess` —— 1/8 个有
- `Load Whisper (mtb)` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `TrimAudio` —— 1/8 个有
- `ttN text` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
