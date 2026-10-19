---
name: unknown_workflow_video_lora_sampler_510
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.702
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ComfyMathExpression, ComfySwitchNode, ConditioningZeroOut, CreateVideo, CustomCombo, ImageFromBatch, KSamplerSelect, LatentCutToBatch, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewAny, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, RebatchImages, RegexExtract, ResizeImageMaskNode, SamplerCustom, SamplerCustomAdvanced, SaveVideo, SkipLayerGuidanceDiTSimple, StringConcatenate, StringReplace, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanDancerEncodeAudio, WanDancerPadKeyframesList, WanDancerVideo]
problems: []
missing: []
members: [视频生成/图生视频/2078404185879568386.json, 视频生成/图生视频/2078450867975577602.json, 视频生成/图生视频/2078051444011393026.json, 视频生成/图生视频/2078397900996038658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_510

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2078404185879568386.json、视频生成/图生视频/2078450867975577602.json、视频生成/图生视频/2078051444011393026.json、视频生成/图生视频/2078397900996038658.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `CreateVideo`
- `CustomCombo`
- `ImageFromBatch`
- `KSamplerSelect`
- `LatentCutToBatch`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `RebatchImages`
- `RegexExtract`
- `ResizeImageMaskNode`
- `SamplerCustom`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SkipLayerGuidanceDiTSimple`
- `StringConcatenate`
- `StringReplace`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanDancerEncodeAudio`
- `WanDancerPadKeyframesList`
- `WanDancerVideo`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 3/4 个有
- `1hew_AnySwitchSelect` —— 1/4 个有
- `Int` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
