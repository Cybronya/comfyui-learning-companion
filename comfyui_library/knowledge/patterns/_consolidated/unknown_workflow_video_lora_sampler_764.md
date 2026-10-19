---
name: unknown_workflow_video_lora_sampler_764
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.699
common_nodes: [CLIPTextEncode, CR Float To Integer, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSizeAndCount, ImageResizeKJv2, KSamplerSelect, LTX2_NAG, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, LoadImage, ManualSigmas, MathExpression|pysssss, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveInt, ResizeImageMaskNode, SamplerCustom, SimpleMath+, VAEDecode, VHS_LoadVideo, VHS_VideoCombine, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [视频生成/图生视频/2071613148762824706.json, 视频生成/图生视频/2074498263339855873.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_764

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2071613148762824706.json、视频生成/图生视频/2074498263339855873.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Float To Integer`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `SamplerCustom`
- `SimpleMath+`
- `VAEDecode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `LTX2MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `LTXVAudioVAELoader` —— 1/2 个有
- `LTXVChunkFeedForward` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `VHS_LoadVideoPath` —— 1/2 个有

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
