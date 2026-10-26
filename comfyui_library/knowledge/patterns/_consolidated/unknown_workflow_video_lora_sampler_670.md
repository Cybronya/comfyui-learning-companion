---
name: unknown_workflow_video_lora_sampler_670
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.614667
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, MemoryCleaner, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleMath+, TTResolutionSelector, Text, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/(极致加速)影视级音画同步直出LTX2-T2V_2009258891162427394.json, 视频生成/图生视频/(高配)影视级音画同步直出LTX2-T2V_2009163247743668226.json, 视频生成/文生视频/LTX2-T2V文生视频-影视级音画同步直出_2008481297760526338.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_670

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/(极致加速)影视级音画同步直出LTX2-T2V_2009258891162427394.json、视频生成/图生视频/(高配)影视级音画同步直出LTX2-T2V_2009163247743668226.json、视频生成/文生视频/LTX2-T2V文生视频-影视级音画同步直出_2008481297760526338.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MemoryCleaner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleMath+`
- `TTResolutionSelector`
- `Text`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Any To String (mtb)` —— 2/3 个有
- `CheckpointLoaderSimple` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `JoinStrings` —— 2/3 个有
- `LTXVAudioVAELoader` —— 2/3 个有
- `LatentUpscaleModelLoader` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `LowVRAMLatentUpscaleModelLoader` —— 2/3 个有
- `Qwen3_VQA` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `Int` —— 1/3 个有
- `LowVRAMAudioVAELoader` —— 1/3 个有
- `LowVRAMCheckpointLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
