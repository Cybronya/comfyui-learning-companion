---
name: unknown_workflow_video_lora_sampler_889
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6795
common_nodes: [BasicScheduler, CFGGuider, CS-LTXDirectorGuide, CS-LTXGridDirector, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, TTResolutionSelector, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2068160315895934977.json, 视频生成/文生视频/全自动多宫格LTX2.3导演台+光锥多参生视频(0623修复）_2066670452965199873.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_889

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2068160315895934977.json、视频生成/文生视频/全自动多宫格LTX2.3导演台+光锥多参生视频(0623修复）_2066670452965199873.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CS-LTXDirectorGuide`
- `CS-LTXGridDirector`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
