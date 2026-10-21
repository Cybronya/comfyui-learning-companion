---
name: unknown_workflow_video_lora_sampler_776
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.909
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, Lora Loader Stack (rgthree), MiniMaxH3HybridLoader, MiniMaxH3MediaLoaderFantastic, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceSplitter, MiniMaxH3ResolutionSelector, MiniMaxH3TurboLoRA, MiniMaxH3TurboSampler, MiniMaxH3UnifiedToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3-参考视频-bf16模型_2104139382696534017.json, 视频生成/文生视频/MinimaxH3-参考视频_1944738387087511554.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_776

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3-参考视频-bf16模型_2104139382696534017.json、视频生成/文生视频/MinimaxH3-参考视频_1944738387087511554.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `Lora Loader Stack (rgthree)`
- `MiniMaxH3HybridLoader`
- `MiniMaxH3MediaLoaderFantastic`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceSplitter`
- `MiniMaxH3ResolutionSelector`
- `MiniMaxH3TurboLoRA`
- `MiniMaxH3TurboSampler`
- `MiniMaxH3UnifiedToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
