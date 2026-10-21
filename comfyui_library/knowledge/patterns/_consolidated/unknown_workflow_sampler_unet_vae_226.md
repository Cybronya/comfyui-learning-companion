---
name: unknown_workflow_sampler_unet_vae_226
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9585
common_nodes: [BasicScheduler, CLIPLoader, ConditioningZeroOut, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, ResolutionSelector, SaveVideo, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/H3完整版-无LoRA-480P_2099176270763479041.json, 视频生成/文生视频/【遇见AI】Minimax H3 selflift低分辨率采样器加速_2100472514764951554.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_226

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/H3完整版-无LoRA-480P_2099176270763479041.json、视频生成/文生视频/【遇见AI】Minimax H3 selflift低分辨率采样器加速_2100472514764951554.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ConditioningZeroOut`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `ResolutionSelector`
- `SaveVideo`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 1/2 个有
- `ExtendIntermediateSigmas` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `MiniMaxH3SigmaShift` —— 1/2 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/2 个有
- `ModelAttentionBackend` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
