---
name: unknown_workflow_video_lora_sampler_555
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.52675
common_nodes: [Any Switch (rgthree), CFGGuider, CLIPTextEncode, CR Float To Integer, ComfyNumberConvert, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, PromptRelayEncode, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3_ref2vid_MSRV2_2087887618532007938.json, 视频生成/图生视频/LTX-2.3_ref2vid_MSRV2_角色表参考-视频生成工作流_2081199769686462466.json, 视频生成/图生视频/MV生成 LTX-2.3_ref2vid_MSRV2_角色表参考+自定义音频视频生成工作流_2081967631405502466.json, 视频生成/文生视频/LTX-2.3_双角色设定集参考 + 自定义音频 视频生成工作流_2064203596383735809.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_555

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3_ref2vid_MSRV2_2087887618532007938.json、视频生成/图生视频/LTX-2.3_ref2vid_MSRV2_角色表参考-视频生成工作流_2081199769686462466.json、视频生成/图生视频/MV生成 LTX-2.3_ref2vid_MSRV2_角色表参考+自定义音频视频生成工作流_2081967631405502466.json、视频生成/文生视频/LTX-2.3_双角色设定集参考 + 自定义音频 视频生成工作流_2064203596383735809.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：53%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGGuider`
- `CLIPTextEncode`
- `CR Float To Integer`
- `ComfyNumberConvert`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `PromptRelayEncode`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `LTX2_NAG` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `ResizeImageMaskNode` —— 3/4 个有
- `PreviewAudio` —— 2/4 个有
- `TrimAudioDuration` —— 2/4 个有
- `AnyBooleanSwitch` —— 1/4 个有
- `LTXVAudioVAELoader` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `VHS_LoadAudio` —— 1/4 个有
- `easy mathFloat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 505 | 505 - 505 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 505，观测区间 505 - 505，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
