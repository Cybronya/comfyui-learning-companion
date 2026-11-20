---
name: unknown_workflow_upscale_latent_upscale_lora_68
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.6195
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CR Text, CheckpointLoaderSimple, CreateVideo, DualCLIPLoader, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveFloat, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, SetNode, ShowText|pysssss, SimpleCalculatorKJ, UNETLoader, UnetLoaderGGUF, VAEDecodeTiled, VAELoaderKJ, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 音图驱数字人工作流（自动提示词全配置可调适配12G ）_2027025326320128001.json, 视频生成/图生视频/LTX2.3 首尾帧视频工作流（自动提示词全配置可调适配12G ）_2027279750514872322.json, 视频生成/图生视频/aidir-LTX2.3 首尾帧视频工作流（自动提示词全配置可调适配12G ）_2069614485752598529.json, 视频生成/文生视频/LTX2.3 图文生视频工作流（自动提示词全配置可调适配12G ）_2030943530058784769.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_68

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 音图驱数字人工作流（自动提示词全配置可调适配12G ）_2027025326320128001.json、视频生成/图生视频/LTX2.3 首尾帧视频工作流（自动提示词全配置可调适配12G ）_2027279750514872322.json、视频生成/图生视频/aidir-LTX2.3 首尾帧视频工作流（自动提示词全配置可调适配12G ）_2069614485752598529.json、视频生成/文生视频/LTX2.3 图文生视频工作流（自动提示词全配置可调适配12G ）_2030943530058784769.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CR Text`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `DualCLIPLoader`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `ShowText|pysssss`
- `SimpleCalculatorKJ`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `LTXVAudioVAEDecode` —— 3/4 个有
- `LTXVEmptyLatentAudio` —— 3/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `LTXVImgToVideoInplace` —— 2/4 个有
- `LTXVImgToVideoInplaceKJ` —— 2/4 个有
- `DF_Int_to_Float` —— 1/4 个有
- `LTXVAudioVAEEncode` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `MelBandRoFormerModelLoader` —— 1/4 个有
- `MelBandRoFormerSampler` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `SetLatentNoiseMask` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `SolidMask` —— 1/4 个有
- `SoundFlow_GetLength` —— 1/4 个有
- `TrimAudioDuration` —— 1/4 个有

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
