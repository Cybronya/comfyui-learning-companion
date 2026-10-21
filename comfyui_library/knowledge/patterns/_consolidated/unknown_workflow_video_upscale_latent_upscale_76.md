---
name: unknown_workflow_video_upscale_latent_upscale_76
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.4498
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CM_IntToFloat, CheckpointLoaderSimple, DF_Int_to_Float, EmptyLTXVLatentVideo, Fast Groups Bypasser (rgthree), GetNode, INTConstant, ImageConcatMulti, ImageResizeKJv2, JWIntegerDiv, JoinStrings, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVFirstLastFrameControl_TTP, LTXVLatentUpsampler, LTXVMiddleFrame_TTP, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, Label (rgthree), LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, Qwen3_VQA, RandomNoise, SamplerCustomAdvanced, SetNode, ShellAgentPluginOutputText, TextInput_, VAEDecode, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2016865338914250754.json, 视频生成/图生视频/2017376776682475522.json, 视频生成/图生视频/2017697617920135169.json, 视频生成/图生视频/2037425677011525633.json, 视频生成/图生视频/2031682937711759362.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_76

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2016865338914250754.json、视频生成/图生视频/2017376776682475522.json、视频生成/图生视频/2017697617920135169.json、视频生成/图生视频/2037425677011525633.json、视频生成/图生视频/2031682937711759362.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：45%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CM_IntToFloat`
- `CheckpointLoaderSimple`
- `DF_Int_to_Float`
- `EmptyLTXVLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `ImageConcatMulti`
- `ImageResizeKJv2`
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
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `Qwen3_VQA`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `ShellAgentPluginOutputText`
- `TextInput_`
- `VAEDecode`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `Compare` —— 4/5 个有
- `EmptyImage` —— 4/5 个有
- `ImpactSwitch` —— 4/5 个有
- `LayerUtility: PurgeVRAM` —— 4/5 个有
- `StringReplace` —— 4/5 个有
- `ToString` —— 4/5 个有
- `VAELoaderKJ` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `easy ifElse` —— 4/5 个有
- `DualCLIPLoader` —— 3/5 个有
- `LTXAVTextEncoderLoader` —— 3/5 个有
- `Audio Duration (mtb)` —— 2/5 个有
- `LTXVAudioVAEEncode` —— 2/5 个有
- `LoadAudio` —— 2/5 个有
- `PreviewAudio` —— 2/5 个有
- `SetLatentNoiseMask` —— 2/5 个有
- `SimpleCalculatorKJ` —— 2/5 个有
- `SolidMask` —— 2/5 个有
- `TrimAudioDuration` —— 2/5 个有
- `LTXVAudioVAELoader` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
