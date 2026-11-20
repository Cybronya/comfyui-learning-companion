---
name: unknown_workflow_upscale_latent_upscale_sampler_19
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.5725
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, ImageScaleBy, KSamplerSelect, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleCalculatorKJ, UNETLoader, UnetLoaderGGUF, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2文生视频数字人说话唱歌音频加文本生成_2015583679321477122.json, 视频生成/图生视频/LTX-2高效数字人生成：一键创建实时口型同步视频，支持对嘴型音频图片视频数字人视频_2017463016526192641.json, 视频生成/图生视频/LTX2.3 音图驱数字人工作流（自动提示词全配置可调适配12G ）_2027025326320128001.json, 视频生成/图生视频/LTX2.3 首尾帧视频工作流（自动提示词全配置可调适配12G ）_2027279750514872322.json, 视频生成/图生视频/aidir-LTX2.3 首尾帧视频工作流（自动提示词全配置可调适配12G ）_2069614485752598529.json, 视频生成/文生视频/LTX2.3 图文生视频工作流（自动提示词全配置可调适配12G ）_2030943530058784769.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_19

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/LTX-2文生视频数字人说话唱歌音频加文本生成_2015583679321477122.json、视频生成/图生视频/LTX-2高效数字人生成：一键创建实时口型同步视频，支持对嘴型音频图片视频数字人视频_2017463016526192641.json、视频生成/图生视频/LTX2.3 音图驱数字人工作流（自动提示词全配置可调适配12G ）_2027025326320128001.json、视频生成/图生视频/LTX2.3 首尾帧视频工作流（自动提示词全配置可调适配12G ）_2027279750514872322.json、视频生成/图生视频/aidir-LTX2.3 首尾帧视频工作流（自动提示词全配置可调适配12G ）_2069614485752598529.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：57%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleCalculatorKJ`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 5/6 个有
- `LTXVAudioVAEDecode` —— 5/6 个有
- `LTXVEmptyLatentAudio` —— 5/6 个有
- `LTXVPreprocess` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `ResizeImagesByLongerEdge` —— 5/6 个有
- `CM_FloatToInt` —— 4/6 个有
- `CR Text` —— 4/6 个有
- `CheckpointLoaderSimple` —— 4/6 个有
- `CreateVideo` —— 4/6 个有
- `DualCLIPLoader` —— 4/6 个有
- `LTXAVTextEncoderLoader` —— 4/6 个有
- `LTXVAudioVAELoader` —— 4/6 个有
- `ModelPatchTorchSettings` —— 4/6 个有
- `PrimitiveBoolean` —— 4/6 个有
- `SaveVideo` —— 4/6 个有
- `ShowText|pysssss` —— 4/6 个有
- `llama_cpp_instruct_adv` —— 4/6 个有
- `llama_cpp_model_loader` —— 4/6 个有
- `LTXVAudioVAEEncode` —— 3/6 个有
- `LTXVImgToVideoInplace` —— 3/6 个有
- `LoadAudio` —— 3/6 个有
- `MelBandRoFormerModelLoader` —— 3/6 个有
- `MelBandRoFormerSampler` —— 3/6 个有
- `SetLatentNoiseMask` —— 3/6 个有
- `SolidMask` —— 3/6 个有
- `TrimAudioDuration` —— 3/6 个有
- `ComfySwitchNode` —— 2/6 个有
- `DualCLIPLoaderGGUF` —— 2/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `LTXVImgToVideoInplaceKJ` —— 2/6 个有
- `LTXVScheduler` —— 2/6 个有
- `SimpleMath+` —— 2/6 个有
- `VAELoader` —— 2/6 个有
- `VHS_VideoCombine` —— 2/6 个有
- `DF_Int_to_Float` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `SoundFlow_GetLength` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 5 | 89% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，5 个样本，取值集中（一致性 89%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
