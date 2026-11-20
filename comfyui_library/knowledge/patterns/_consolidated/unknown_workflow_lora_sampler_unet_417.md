---
name: unknown_workflow_lora_sampler_unet_417
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6125
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ComfySwitchNode, CreateVideo, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Minimax文生视频T2V_2098449873984122882.json, 视频生成/文生视频/minimax_h3_t2v官方文生视频_2114188003567554561.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_417

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Minimax文生视频T2V_2098449873984122882.json、视频生成/文生视频/minimax_h3_t2v官方文生视频_2114188003567554561.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `CreateVideo`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `LTXVSeparateAVLatent` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `SaveLatent` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy minimaxH3AudioLock` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
