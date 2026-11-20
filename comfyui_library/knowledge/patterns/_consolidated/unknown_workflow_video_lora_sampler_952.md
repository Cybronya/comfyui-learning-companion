---
name: unknown_workflow_video_lora_sampler_952
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7405
common_nodes: [BasicScheduler, CLIPLoader, CR Text, ComfyMathExpression, ConditioningZeroOut, GetNode, KSamplerSelect, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, ResolutionSelector, SelfLiftAvatarH3Sampler, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/【阿良绘】H3数字人（自生台词+自动提词+自动时长）_2100779861139873793.json, 视频生成/文生视频/【变态加速高清版2.0】MinMaxH3 全能参考-推荐_2106435863944196098.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_952

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/【阿良绘】H3数字人（自生台词+自动提词+自动时长）_2100779861139873793.json、视频生成/文生视频/【变态加速高清版2.0】MinMaxH3 全能参考-推荐_2106435863944196098.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `GetNode`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `Float` —— 1/2 个有
- `H3SigmaRefiner` —— 1/2 个有
- `Int` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MiniMaxH3AudioConditioningT8` —— 1/2 个有
- `MiniMaxH3Unified` —— 1/2 个有
- `MiniMaxH3VAEDecodeFast` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `RunningHub Deepcleaner` —— 1/2 个有
- `StringFunction|pysssss` —— 1/2 个有
- `StringToNumber` —— 1/2 个有
- `YUAN_TXTConvertAny` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
