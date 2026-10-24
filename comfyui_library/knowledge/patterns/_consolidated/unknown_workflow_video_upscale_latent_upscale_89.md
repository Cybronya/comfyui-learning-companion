---
name: unknown_workflow_video_upscale_latent_upscale_89
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.4435
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CM_IntToFloat, CR Text, CheckpointLoaderSimple, Compare, DF_Int_to_Float, EmptyImage, EmptyLTXVLatentVideo, Fast Groups Bypasser (rgthree), GetNode, INTConstant, ImageConcatMulti, ImageResizeKJv2, ImpactSwitch, JWIntegerDiv, JoinStrings, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVFirstLastFrameControl_TTP, LTXVLatentUpsampler, LTXVMiddleFrame_TTP, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, Label (rgthree), LatentUpscaleModelLoader, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ManualSigmas, Qwen3_VQA, RandomNoise, SamplerCustomAdvanced, SetNode, ShellAgentPluginOutputText, StringReplace, TextInput_, ToString, VAEDecode, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed, easy ifElse, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.0首尾帧生视频V3_极速优化版_三次采样（支持自动提示词）_2017376776682475522.json, 视频生成/图生视频/LTX2.0首尾帧生视频V3音频驱动版_三次采样(自行上传音频)_2017697617920135169.json, 视频生成/图生视频/LTX2.3首尾帧生视频 音频驱动版_三次采样(自行上传音频)_2037425677011525633.json, 视频生成/图生视频/LTX2.3首尾帧生视频（支持自动提示词）_2031682937711759362.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_89

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LTX2.0首尾帧生视频V3_极速优化版_三次采样（支持自动提示词）_2017376776682475522.json、视频生成/图生视频/LTX2.0首尾帧生视频V3音频驱动版_三次采样(自行上传音频)_2017697617920135169.json、视频生成/图生视频/LTX2.3首尾帧生视频 音频驱动版_三次采样(自行上传音频)_2037425677011525633.json、视频生成/图生视频/LTX2.3首尾帧生视频（支持自动提示词）_2031682937711759362.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：44%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CM_IntToFloat`
- `CR Text`
- `CheckpointLoaderSimple`
- `Compare`
- `DF_Int_to_Float`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `JWIntegerDiv`
- `JoinStrings`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVFirstLastFrameControl_TTP`
- `LTXVLatentUpsampler`
- `LTXVMiddleFrame_TTP`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `Label (rgthree)`
- `LatentUpscaleModelLoader`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `Qwen3_VQA`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `ShellAgentPluginOutputText`
- `StringReplace`
- `TextInput_`
- `ToString`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 3/4 个有
- `Audio Duration (mtb)` —— 2/4 个有
- `LTXAVTextEncoderLoader` —— 2/4 个有
- `LTXVAudioVAEEncode` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `PreviewAudio` —— 2/4 个有
- `SetLatentNoiseMask` —— 2/4 个有
- `SimpleCalculatorKJ` —— 2/4 个有
- `SolidMask` —— 2/4 个有
- `TrimAudioDuration` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
