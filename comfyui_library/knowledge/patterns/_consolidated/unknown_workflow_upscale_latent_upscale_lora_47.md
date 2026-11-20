---
name: unknown_workflow_upscale_latent_upscale_lora_47
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.878
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, SetLatentNoiseMask, SolidMask, TrimAudioDuration, VAEDecodeTiled]
problems: []
missing: []
members: [数字人/数字人/DaNotebook LTX2.3 Digital_2093191068970999809.json, 数字人/数字人/LTX2.3 s2v双人数字人_2031917616582889474.json, 数字人/数字人/LTX2.3 s2v数字人-Prompt Relay 版- 高动作遵从_2047120056772993026.json, 数字人/数字人/LTX2.3 s2v数字人_2030584684144500738.json, 数字人/数字人/LTX2.3数字人25秒长视频工作流 V2.3_2034646872190623745.json, 视频生成/图生视频/LTX-2.3图生视频，声画同步_2035291558307700737.json, 视频生成/图生视频/LTX2.3数字人V2—支持双人，自动计算帧数_2073315948735586306.json, 视频生成/图生视频/OpenClaw + Fish Audio：一键复现“不要怕”名场面！_2039165345923080193.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_47

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/DaNotebook LTX2.3 Digital_2093191068970999809.json、数字人/数字人/LTX2.3 s2v双人数字人_2031917616582889474.json、数字人/数字人/LTX2.3 s2v数字人-Prompt Relay 版- 高动作遵从_2047120056772993026.json、数字人/数字人/LTX2.3 s2v数字人_2030584684144500738.json、数字人/数字人/LTX2.3数字人25秒长视频工作流 V2.3_2034646872190623745.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
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
- `LoadAudio` —— 7/8 个有
- `PrimitiveStringMultiline` —— 6/8 个有
- `LoadImage` —— 4/8 个有
- `PreviewAny` —— 4/8 个有
- `PreviewAudio` —— 4/8 个有
- `PrimitiveBoolean` —— 4/8 个有
- `AudioInfo` —— 3/8 个有
- `FloatConstant` —— 3/8 个有
- `ImageLoader` —— 3/8 个有
- `LTX2_NAG` —— 3/8 个有
- `MelBandRoFormerModelLoader` —— 3/8 个有
- `MelBandRoFormerSampler` —— 3/8 个有
- `SimpleMath+` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `PrimitiveFloat` —— 2/8 个有
- `AudioConcat` —— 1/8 个有
- `Bjornulf_ShowInt` —— 1/8 个有
- `DA_LoadMedia` —— 1/8 个有
- `DA_Nag` —— 1/8 个有
- `FishS2VoiceCloneTTS` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `LoraLoader` —— 1/8 个有
- `PromptRelayEncode` —— 1/8 个有
- `ResolutionSelector` —— 1/8 个有
- `StringReplace` —— 1/8 个有
- `TextGenerateLTX2Prompt` —— 1/8 个有
- `llama_cpp_instruct_adv` —— 1/8 个有
- `llama_cpp_model_loader` —— 1/8 个有
- `llama_cpp_parameters` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
