---
name: unknown_workflow_upscale_latent_upscale_lora_49
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.896429
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, SetLatentNoiseMask, SolidMask, TrimAudioDuration, VAEDecodeTiled]
problems: []
missing: []
members: [数字人/数字人/DaNotebook LTX2.3 Digital_2093191068970999809.json, 数字人/数字人/LTX2.3 s2v双人数字人_2031917616582889474.json, 数字人/数字人/LTX2.3 s2v数字人-Prompt Relay 版- 高动作遵从_2047120056772993026.json, 数字人/数字人/LTX2.3 s2v数字人_2030584684144500738.json, 数字人/数字人/Ltx2.3指定音色+图片输入文案自动化配音生成数字人视频_2053381791427375106.json, 视频生成/图生视频/Ltx2.3+龙猫克隆+图片输入文案自动化配音生成数字人视频_2049792632808853506.json, 视频生成/图生视频/Ltx2.3指定音色+图片输入文案自动化配音生成数字人视频_2040420049630007297.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_49

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/DaNotebook LTX2.3 Digital_2093191068970999809.json、数字人/数字人/LTX2.3 s2v双人数字人_2031917616582889474.json、数字人/数字人/LTX2.3 s2v数字人-Prompt Relay 版- 高动作遵从_2047120056772993026.json、数字人/数字人/LTX2.3 s2v数字人_2030584684144500738.json、数字人/数字人/Ltx2.3指定音色+图片输入文案自动化配音生成数字人视频_2053381791427375106.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：90%

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
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetLatentNoiseMask`
- `SolidMask`
- `TrimAudioDuration`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 6/7 个有
- `MelBandRoFormerModelLoader` —— 6/7 个有
- `MelBandRoFormerSampler` —— 6/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `PrimitiveFloat` —— 4/7 个有
- `Apply Whisper` —— 3/7 个有
- `FloatConstant` —— 3/7 个有
- `ImageLoader` —— 3/7 个有
- `LTX2_NAG` —— 3/7 个有
- `LoadImage` —— 3/7 个有
- `LongCatVoiceCloneTTS` —— 3/7 个有
- `PreviewAny` —— 3/7 个有
- `PreviewAudio` —— 3/7 个有
- `PrimitiveBoolean` —— 3/7 个有
- `SimpleMath+` —— 3/7 个有
- `SoundFlow_GetLength` —— 3/7 个有
- `Text` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `AudioConcat` —— 1/7 个有
- `DA_LoadMedia` —— 1/7 个有
- `DA_Nag` —— 1/7 个有
- `IAMCCS_VRAMCleanup` —— 1/7 个有
- `NormalizeAudioLoudness` —— 1/7 个有
- `PromptRelayEncode` —— 1/7 个有
- `ResolutionSelector` —— 1/7 个有
- `llama_cpp_instruct_adv` —— 1/7 个有
- `llama_cpp_model_loader` —— 1/7 个有
- `llama_cpp_parameters` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
