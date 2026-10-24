---
name: unknown_workflow_video_lora_sampler_241
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.4565
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LiconMSR, LoadImage, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleMath+, TTResolutionSelector, Text, VAEDecode, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/3图 （人物1 人物2 三视图 场景图）LTX2.3-MSR多参考图V2（质量高）_2111328454267461633.json, 视频生成/图生视频/AI代码侠土豆-LTX2.3-MSR多参考图V2+音频参考_2080190771210313729.json, 视频生成/图生视频/AI代码侠土豆-LTX2.3-MSR多参考图V2_2076177138851602434.json, 视频生成/图生视频/AI代码侠土豆-LTX2.3-MSR多参考图生成_2072900234711228417.json, 视频生成/图生视频/LTX-2.3-Licon-MSR-V2 一致性更好 逻辑性更强_2076669054097649666.json, 视频生成/图生视频/LTX2.3-MSR2.0多参考图生成_2076157351371034626.json, 视频生成/图生视频/LTX2.3-MSR多参考图V2_2078645813319921665.json, 视频生成/图生视频/MumsAIGC-LTX-MSR多参V2_2083224386701709313.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_241

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/3图 （人物1 人物2 三视图 场景图）LTX2.3-MSR多参考图V2（质量高）_2111328454267461633.json、视频生成/图生视频/AI代码侠土豆-LTX2.3-MSR多参考图V2+音频参考_2080190771210313729.json、视频生成/图生视频/AI代码侠土豆-LTX2.3-MSR多参考图V2_2076177138851602434.json、视频生成/图生视频/AI代码侠土豆-LTX2.3-MSR多参考图生成_2072900234711228417.json、视频生成/图生视频/LTX-2.3-Licon-MSR-V2 一致性更好 逻辑性更强_2076669054097649666.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleMath+`
- `TTResolutionSelector`
- `Text`
- `VAEDecode`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CM_FloatToInt` —— 7/8 个有
- `INTConstant` —— 7/8 个有
- `ImageResizeKJv2` —— 7/8 个有
- `LTXVAudioVAELoader` —— 7/8 个有
- `LTXVEmptyLatentAudio` —— 7/8 个有
- `PrimitiveFloat` —— 7/8 个有
- `Label (rgthree)` —— 6/8 个有
- `PromptRelayEncode` —— 5/8 个有
- `LTX2_NAG` —— 4/8 个有
- `LowVRAMCheckpointLoader` —— 4/8 个有
- `CheckpointLoaderSimple` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `LTXVAudioVAEEncode` —— 2/8 个有
- `LoadAudio` —— 2/8 个有
- `SetLatentNoiseMask` —— 2/8 个有
- `SolidMask` —— 2/8 个有
- `Any Switch (rgthree)` —— 1/8 个有
- `Audio Duration` —— 1/8 个有
- `AudioMerge` —— 1/8 个有
- `CM_IntToFloat` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `Float` —— 1/8 个有
- `Int` —— 1/8 个有
- `LTXVAudioVideoMask` —— 1/8 个有
- `MelBandRoFormerModelLoader` —— 1/8 个有
- `MelBandRoFormerSampler` —— 1/8 个有
- `PreviewAudio` —— 1/8 个有
- `SeedVCRun` —— 1/8 个有
- `UNETLoader` —— 1/8 个有
- `VAELoaderKJ` —— 1/8 个有
- `easy imageRemBg` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 7 | 100% |
| 高度 | 24 | 24 - 24 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，7 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，7 个样本，取值集中（一致性 100%）
