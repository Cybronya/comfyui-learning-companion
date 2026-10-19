---
name: unknown_workflow_sampler_unet_vae_203
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.907
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Prompt Text, ComfyMathExpression, CreateVideo, EasyCache, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, SaveVideo, ShowAnything|Mie, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/加速版-MiniMax H3 图生视频 首尾帧视频_2091065912949567490.json, 视频生成/文生视频/加速版-MiniMax H3｜图文一键生视频_2084935567606894593.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_203

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/加速版-MiniMax H3 图生视频 首尾帧视频_2091065912949567490.json、视频生成/文生视频/加速版-MiniMax H3｜图文一键生视频_2084935567606894593.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `CreateVideo`
- `EasyCache`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `ShowAnything|Mie`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CM_IntToFloat` —— 1/2 个有
- `DF_Int_to_Float` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `Int` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `ResolutionSelector` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
