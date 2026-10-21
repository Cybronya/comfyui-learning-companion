---
name: unknown_workflow_sampler_unet_vae_229
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.83
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, ImageResizeKJv2, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax_H3_Ref2VA全功能_官方提示词版_2084288422902059010.json, 视频生成/文生视频/【遇见AI】Minimax H3，多参考生图，9视频9图3音频_2084533778860568577.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_229

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MiniMax_H3_Ref2VA全功能_官方提示词版_2084288422902059010.json、视频生成/文生视频/【遇见AI】Minimax H3，多参考生图，9视频9图3音频_2084533778860568577.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ImageScaleDownToSize` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `JoinStrings` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有
- `easy positive` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
