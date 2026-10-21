---
name: unknown_workflow_video_lora_sampler_575
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.633
common_nodes: [AudioCrop, AudioInfo, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, Float, Int, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PrimitiveInt, SamplerCustom, SetLatentNoiseMask, SimpleMath+, SolidMask, Text, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/ltx2.3文本驱动-声音设计_2100950016872505346.json, 视频生成/图生视频/2034445280996761602.json, 视频生成/文生视频/LTX2.3极速版 图生视频 图片音频双驱动 自动生提示词 优化版_2034787261849538562.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_575

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/ltx2.3文本驱动-声音设计_2100950016872505346.json、视频生成/图生视频/2034445280996761602.json、视频生成/文生视频/LTX2.3极速版 图生视频 图片音频双驱动 自动生提示词 优化版_2034787261849538562.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioCrop`
- `AudioInfo`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `Float`
- `Int`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `SamplerCustom`
- `SetLatentNoiseMask`
- `SimpleMath+`
- `SolidMask`
- `Text`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Apply Whisper` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `InversionDemoLazySwitch` —— 2/3 个有
- `LTXVLatentUpsampler` —— 2/3 个有
- `LatentUpscaleModelLoader` —— 2/3 个有
- `PreviewAudio` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `Qwen3TTSModelLoader` —— 2/3 个有
- `Qwen3TTSVoiceClone` —— 2/3 个有
- `Qwen3TTSVoiceDesign` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `ShowText` —— 2/3 个有
- `StringSubstring` —— 2/3 个有
- `llama_cpp_instruct_adv` —— 2/3 个有
- `llama_cpp_model_loader` —— 2/3 个有
- `llama_cpp_parameters` —— 2/3 个有
- `MelBandRoFormerModelLoader` —— 1/3 个有
- `MelBandRoFormerSampler` —— 1/3 个有
- `Qwen3_VQA_Plus` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
