---
name: unknown_workflow_video_lora_sampler_1012
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.732
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, GetNode, JjkText, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3AudioConditioningT8, MiniMaxH3VDNExecutionPlanT8Advanced, MiniMaxH3VDNModelComposerT8Advanced, PrimitiveFloat, RandomSeedNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SolAttnMiniMax, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/文生视频/MinimaxH3全能参考：VDN一采_2096894819447697410.json, 视频生成/文生视频/MinimaxH3全能参考：VDN一采_2096916840424497154.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1012

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MinimaxH3全能参考：VDN一采_2096894819447697410.json、视频生成/文生视频/MinimaxH3全能参考：VDN一采_2096916840424497154.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `JjkText`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3VDNExecutionPlanT8Advanced`
- `MiniMaxH3VDNModelComposerT8Advanced`
- `PrimitiveFloat`
- `RandomSeedNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `忽略多组孤海`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
