---
name: unknown_workflow_video_lora_sampler_841
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8585
common_nodes: [BasicGuider, BasicScheduler, BlockSparseAttention, ImageConcanate, JWImageResizeToMegapixels, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, ViggleAnimateConditioning, ViggleTextCondLoader]
problems: []
missing: []
members: [视频生成/图生视频/H3動作遷移_目前支持10秒_2099764920819732482.json, 视频生成/文生视频/Viggle-animate-h3视频角色替换_2097851117714632705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_841

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/H3動作遷移_目前支持10秒_2099764920819732482.json、视频生成/文生视频/Viggle-animate-h3视频角色替换_2097851117714632705.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `ImageConcanate`
- `JWImageResizeToMegapixels`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `ViggleAnimateConditioning`
- `ViggleTextCondLoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 1/2 个有
- `CustomSigmas` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
