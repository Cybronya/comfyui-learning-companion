---
name: unknown_workflow_video_lora_sampler_887
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.883
common_nodes: [AILab_QwenVL_Advanced, CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageRangeFromBatch, HunyuanVideoFoley, ImageBatch, ImageResizeKJv2, JjkText, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAddGuideMulti, LTXVChunkFeedForward, LTXVConditioning, LTXVPreprocess, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, ShowText|pysssss, StringFunction|pysssss, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, VRAMReserver, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2081421017964171266.json, 视频生成/文生视频/三关键帧图生视频_自动提示词_2059173762448314370.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_887

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2081421017964171266.json、视频生成/文生视频/三关键帧图生视频_自动提示词_2059173762448314370.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL_Advanced`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageRangeFromBatch`
- `HunyuanVideoFoley`
- `ImageBatch`
- `ImageResizeKJv2`
- `JjkText`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAddGuideMulti`
- `LTXVChunkFeedForward`
- `LTXVConditioning`
- `LTXVPreprocess`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VRAMReserver`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LTXVAddGuide` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
