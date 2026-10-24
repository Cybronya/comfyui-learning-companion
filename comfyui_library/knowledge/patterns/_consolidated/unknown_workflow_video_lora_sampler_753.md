---
name: unknown_workflow_video_lora_sampler_753
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4815
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, FL_IntToFloat, GetImageRangeFromBatch, GetNode, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, PreviewImage, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, SoundFlow_GetLength, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy imageSize, easy int]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3_Gemini3补全分镜提示词+自定义音频+首尾帧+多图段子视频生成_2055962684570521602.json, 视频生成/图生视频/LTX-2.3_Prompt Relay+自定义音频+首尾帧+多图段子视频生成_2055942419597799425.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_753

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3_Gemini3补全分镜提示词+自定义音频+首尾帧+多图段子视频生成_2055962684570521602.json、视频生成/图生视频/LTX-2.3_Prompt Relay+自定义音频+首尾帧+多图段子视频生成_2055942419597799425.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：48%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `FL_IntToFloat`
- `GetImageRangeFromBatch`
- `GetNode`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `SoundFlow_GetLength`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy imageSize`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `DapaoGeminiInstructionZhenzhenNode` —— 1/2 个有
- `FlashVSRNode` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `LTXVAddGuideMulti` —— 1/2 个有
- `LTXVImgToVideoInplaceKJ` —— 1/2 个有
- `PromptRelayEncodeTimeline` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 349 | - | 2 | 97% |
| 高度 | 24.5 | - | 2 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 349，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 高度 中位数 24.5，样本不足，未给区间，2 个样本，取值集中（一致性 98%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
