---
name: unknown_workflow_video_lora_sampler_758
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.796
common_nodes: [> Text Replace, Any To Any, CFGGuider, CLIPTextEncode, CR Prompt Text, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetNode, ImageConcatMulti, ImageResizeKJv2, Int, JWInteger, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, MultiplePathsInput, PathchSageAttentionKJ, PreviewImage, Qwen3_VQA, RandomNoise, SamplerCustomAdvanced, SetNode, VAEDecodeTiled, VHS_SelectFilename, VHS_VideoCombine, VRAMReserver, VisualizeSigmasKJ, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Ltx2多帧首尾帧运动强化版V1_2010552640517705729.json, 视频生成/图生视频/多图首尾帧视频-Ltx2-V20260112(48g)_2010704583722536962.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_758

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Ltx2多帧首尾帧运动强化版V1_2010552640517705729.json、视频生成/图生视频/多图首尾帧视频-Ltx2-V20260112(48g)_2010704583722536962.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `> Text Replace`
- `Any To Any`
- `CFGGuider`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `Int`
- `JWInteger`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MultiplePathsInput`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `Qwen3_VQA`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `VAEDecodeTiled`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `VRAMReserver`
- `VisualizeSigmasKJ`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
