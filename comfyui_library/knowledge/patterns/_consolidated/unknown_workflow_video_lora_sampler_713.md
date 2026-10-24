---
name: unknown_workflow_video_lora_sampler_713
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.549
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTX2_NAG, LTXVAddGuide, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, Label (rgthree), LayerUtility: TextBox, LoadAudioUI, LoadImage, LoraLoaderModelOnly, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PrimitiveInt, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, UNETLoader, VAEDecodeTiled, VAELoader, VHS_SelectImages, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/【easy-use】71-2 Set_Get节点_2076488594667171841.json, 视频生成/图生视频/工作流基础系列27-LTX 2.3首尾帧工作流+音频上传_2062758696102481922.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_713

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/【easy-use】71-2 Set_Get节点_2076488594667171841.json、视频生成/图生视频/工作流基础系列27-LTX 2.3首尾帧工作流+音频上传_2062758696102481922.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：55%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAddGuide`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `Label (rgthree)`
- `LayerUtility: TextBox`
- `LoadAudioUI`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_SelectImages`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowInt` —— 1/2 个有
- `LoadVideo` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `easy getNode` —— 1/2 个有
- `easy setNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
