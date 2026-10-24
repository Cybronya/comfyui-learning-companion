---
name: unknown_workflow_upscale_latent_upscale_lora_80
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.927
common_nodes: [CFGGuider, CLIPTextEncode, CM_IntToFloat, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, GetLatentSizeAndCount, ImageFromBatch, Image_Resize_longsize, Int, JjkText, KSamplerSelect, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, PathchSageAttentionKJ, PrimitiveBoolean, PromptRelayEncode, RandomNoise, SamplerCustomAdvanced, SaveVideo, Seed Everywhere, SetLatentNoiseMask, SolidMask, TrimAudioDuration, VAEDecodeTiled, VRAMReserver, easy cleanGpuUsed, image_scale_pixel_v2]
problems: []
missing: []
members: [视频生成/图生视频/V4_2053030948815548417.json, 视频生成/图生视频/电商生成双人对话视频 Ltx2.3bcx_2049061989212758018.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_80

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/V4_2053030948815548417.json、视频生成/图生视频/电商生成双人对话视频 Ltx2.3bcx_2049061989212758018.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `GetLatentSizeAndCount`
- `ImageFromBatch`
- `Image_Resize_longsize`
- `Int`
- `JjkText`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoConditionOnly`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PromptRelayEncode`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `Seed Everywhere`
- `SetLatentNoiseMask`
- `SolidMask`
- `TrimAudioDuration`
- `VAEDecodeTiled`
- `VRAMReserver`
- `easy cleanGpuUsed`
- `image_scale_pixel_v2`

**可变部分**（部分 workflow 才有）：
- `FB_Qwen3TTSVoiceClone` —— 1/2 个有
- `ImageCompositeMasked` —— 1/2 个有
- `Text` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
