---
name: unknown_workflow_video_lora_sampler_113
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.44025
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, GetNode, INTConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SetNode, VAEDecode, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3-MSR多参考图V2_2116698209576906753.json, 平台全量/MSR_Sample_workflow_2064002647774031874.json, 视频生成/图生视频/3图 （人物1 人物2 三视图 场景图）LTX2.3-MSR多参考图V2（质量高）_2111328454267461633.json, 视频生成/图生视频/AI代码侠土豆-LTX2.3-MSR多参考图V2_2076177138851602434.json, 视频生成/图生视频/AI代码侠土豆-LTX2.3-MSR多参考图生成_2072900234711228417.json, 视频生成/图生视频/LTX-2.3-Licon-MSR-V2 一致性更好 逻辑性更强_2076669054097649666.json, 视频生成/图生视频/LTX-2.3-MSR_V2_Sample_workflow_2077298487875694594.json, 视频生成/图生视频/LTX2.3 MSR V2 (多主体参考) 图生视频_2083493730379722754.json, 视频生成/图生视频/LTX2.3-MSR-workflow_2066907383061901313.json, 视频生成/图生视频/LTX2.3-MSR2.0多参考图生成_2076157351371034626.json, 视频生成/图生视频/LTX2.3-MSR多参考图V2_2078645813319921665.json, 视频生成/图生视频/Ltx2.3-Licon-MSR-多图参考-全能参考生视频_2065971442394689538.json, 视频生成/图生视频/Ltx2.3-Licon-MSR-多图参考-全能参考生视频_2067900124038254593.json, 视频生成/图生视频/MSR - 多图参考视频生成 - LTX2.3_2068177667341508609.json, 视频生成/图生视频/MSR_角色道具参考-ltx2.3_2067174173994213378.json, 视频生成/图生视频/MumsAIGC-LTX-MSR多参V2_2083224386701709313.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_113

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/LTX2.3-MSR多参考图V2_2116698209576906753.json、平台全量/MSR_Sample_workflow_2064002647774031874.json、视频生成/图生视频/3图 （人物1 人物2 三视图 场景图）LTX2.3-MSR多参考图V2（质量高）_2111328454267461633.json、视频生成/图生视频/AI代码侠土豆-LTX2.3-MSR多参考图V2_2076177138851602434.json、视频生成/图生视频/AI代码侠土豆-LTX2.3-MSR多参考图生成_2072900234711228417.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：44%

## 共有节点

全部 16 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LowVRAMCheckpointLoader` —— 13/16 个有
- `SimpleMath+` —— 9/16 个有
- `CM_FloatToInt` —— 8/16 个有
- `ComfyMathExpression` —— 8/16 个有
- `ImageResizeKJv2` —— 8/16 个有
- `PrimitiveFloat` —— 8/16 个有
- `TTResolutionSelector` —— 8/16 个有
- `Text` —— 8/16 个有
- `easy cleanGpuUsed` —— 8/16 个有
- `LTX2_NAG` —— 7/16 个有
- `PromptRelayEncode` —— 7/16 个有
- `LTXVAddGuideMulti` —— 6/16 个有
- `Label (rgthree)` —— 6/16 个有
- `CheckpointLoaderSimple` —— 3/16 个有
- `PreviewImage` —— 3/16 个有
- `孤海注释` —— 2/16 个有
- `Any Switch (rgthree)` —— 1/16 个有
- `Audio Duration` —— 1/16 个有
- `AudioMerge` —— 1/16 个有
- `CM_IntToFloat` —— 1/16 个有
- `Fast Groups Bypasser (rgthree)` —— 1/16 个有
- `LTXVAudioVAEEncode` —— 1/16 个有
- `LTXVAudioVideoMask` —— 1/16 个有
- `LoadAudio` —— 1/16 个有
- `LoraLoaderModelOnly` —— 1/16 个有
- `MelBandRoFormerModelLoader` —— 1/16 个有
- `MelBandRoFormerSampler` —— 1/16 个有
- `SeedVCRun` —— 1/16 个有
- `SetLatentNoiseMask` —— 1/16 个有
- `SolidMask` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 133 | 121 - 145 | 16 | 91% |
| 高度 | 24 | 24 - 24 | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 133，观测区间 121 - 145，16 个样本，取值集中（一致性 91%）
- 高度 中位数 24，观测区间 24 - 24，16 个样本，取值集中（一致性 100%）
