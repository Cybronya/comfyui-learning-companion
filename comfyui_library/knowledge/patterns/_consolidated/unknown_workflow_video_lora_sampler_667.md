---
name: unknown_workflow_video_lora_sampler_667
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.859
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, DualCLIPLoader, GetImageRangeFromBatch, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVideoMask, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveInt, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEEncode, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy showAnything]
problems: []
missing: []
members: [平台全量/LTX2.3-视频增加音效，提高帧率_2073044359297196033.json, 平台全量/LTX2.3-音效配音_2045054104585637890.json, 音频生成/音频生成/LTX2.3-无声视频音效设计优化版V2_2030312017944383489.json, 音频生成/音频生成/LTX2.3-无声视频音效设计优化版V2_2076279979465330690.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_667

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/LTX2.3-视频增加音效，提高帧率_2073044359297196033.json、平台全量/LTX2.3-音效配音_2045054104585637890.json、音频生成/音频生成/LTX2.3-无声视频音效设计优化版V2_2030312017944383489.json、音频生成/音频生成/LTX2.3-无声视频音效设计优化版V2_2076279979465330690.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 1/4 个有
- `VAEDecodeTiled` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
