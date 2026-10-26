---
name: unknown_workflow_video_lora_sampler_1035
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.857
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, DualCLIPLoader, GetImageRangeFromBatch, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVideoMask, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveInt, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEEncode, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy showAnything]
problems: []
missing: []
members: [音频生成/音频生成/LTX2.3-无声视频音效设计优化版V2_2030312017944383489.json, 音频生成/音频生成/LTX2.3-无声视频音效设计优化版V2_2076279979465330690.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1035

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/LTX2.3-无声视频音效设计优化版V2_2030312017944383489.json、音频生成/音频生成/LTX2.3-无声视频音效设计优化版V2_2076279979465330690.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `DualCLIPLoader`
- `GetImageRangeFromBatch`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVideoMask`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEEncode`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy showAnything`

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
