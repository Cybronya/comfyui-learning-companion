---
name: unknown_workflow_video_upscale_latent_upscale_84
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.5872
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoaderGGUF, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, ImageScaleBy, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, TrimAudioDuration, UNETLoader, UnetLoaderGGUF, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/AA--LTX-2.0文生视频MV(歌曲MP3对口型)_2015272887397130242.json, 视频生成/文生视频/AA--LTX2.0自动提示词--文生视频-文生MV(对口型)-黄蝉lora_2017202468442087426.json, 视频生成/文生视频/LTX-2文生视频快速低显存推荐生成数字人说话数字人唱歌音频加文本生成数字人视频高清_2014360629548687361.json, 视频生成/文生视频/LTX-2文生视频：上传歌曲MP3，一键生成MV音乐视频！_2013887424543330305.json, 视频生成/文生视频/👾怪獸-LTX-2文生视频+数字人👾_2014693130410397697.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_84

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/AA--LTX-2.0文生视频MV(歌曲MP3对口型)_2015272887397130242.json、视频生成/文生视频/AA--LTX2.0自动提示词--文生视频-文生MV(对口型)-黄蝉lora_2017202468442087426.json、视频生成/文生视频/LTX-2文生视频快速低显存推荐生成数字人说话数字人唱歌音频加文本生成数字人视频高清_2014360629548687361.json、视频生成/文生视频/LTX-2文生视频：上传歌曲MP3，一键生成MV音乐视频！_2013887424543330305.json、视频生成/文生视频/👾怪獸-LTX-2文生视频+数字人👾_2014693130410397697.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoaderGGUF`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `TrimAudioDuration`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVEmptyLatentAudio` —— 4/5 个有
- `ComfySwitchNode` —— 3/5 个有
- `SimpleCalculatorKJ` —— 3/5 个有
- `CM_FloatBinaryOperation` —— 2/5 个有
- `CM_FloatToInt` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `easy float` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `CheckpointLoaderSimple` —— 1/5 个有
- `CreateVideo` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `Int` —— 1/5 个有
- `JoinStrings` —— 1/5 个有
- `LTXAVTextEncoderLoader` —— 1/5 个有
- `LTXVAudioVAELoader` —— 1/5 个有
- `LTXVCropGuides` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `Qwen3_VQA` —— 1/5 个有
- `SaveVideo` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `TextInput_` —— 1/5 个有
- `VAEDecode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 97 - 121 | 4 | 91% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 97 - 121，4 个样本，取值集中（一致性 91%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
