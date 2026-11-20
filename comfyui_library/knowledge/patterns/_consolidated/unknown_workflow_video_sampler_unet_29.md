---
name: unknown_workflow_video_sampler_unet_29
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.497615
common_nodes: [BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/Regenerate 2K IC-Lora _H3 ref2va 生成视频 & 放大_2121090118177091586.json, 视频生成/图生视频/Minimax H3｜Fast H3 Omini + 高清放大 latent upscale_2114843477690376193.json, 视频生成/图生视频/fast_h3_omini_latent_upscale_2114522676265050114.json, 视频生成/图生视频/fast_h3_omni_base_2114521289464569857.json, 视频生成/图生视频/fast_h3_omni_base_2114839284506259458.json, 视频生成/图生视频/fast_h3_omni_base_2115235796805578753.json, 视频生成/图生视频/fast_h3_omni_base_2115243980542791681.json, 视频生成/图生视频/fast_h3_omni_base_2115607838142844930.json, 视频生成/图生视频/minimax_h3_rawmodel_veta_attention_ref2va_2110547591858581506.json, 视频生成/图生视频/minimax_h3_rawmodel_veta_attention_ref2va快速参考生视频精品_2110562127370084354.json, 视频生成/图生视频/minimax_h3_singularity_V2_r2va_2113488913896660994.json, 视频生成/图生视频/minimax_h3多图快速参考生视频_2110577324570796034.json, 视频生成/图生视频/极速生视频_Fast_h3_omini_latent_upscale精品_2114878357006536705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_29

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（平台全量/Regenerate 2K IC-Lora _H3 ref2va 生成视频 & 放大_2121090118177091586.json、视频生成/图生视频/Minimax H3｜Fast H3 Omini + 高清放大 latent upscale_2114843477690376193.json、视频生成/图生视频/fast_h3_omini_latent_upscale_2114522676265050114.json、视频生成/图生视频/fast_h3_omni_base_2114521289464569857.json、视频生成/图生视频/fast_h3_omni_base_2114839284506259458.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 12/13 个有
- `PrimitiveStringMultiline` —— 12/13 个有
- `GetNode` —— 11/13 个有
- `SetNode` —— 11/13 个有
- `BasicGuider` —— 10/13 个有
- `ModelAttentionBackend` —— 10/13 个有
- `RandomNoise` —— 10/13 个有
- `SamplerCustomAdvanced` —— 10/13 个有
- `ImageScaleToTotalPixels` —— 9/13 个有
- `LoraLoaderModelOnly` —— 8/13 个有
- `ConditioningZeroOut` —— 5/13 个有
- `SelfLiftH3Sampler` —— 5/13 个有
- `QwenH3PromptLocal` —— 3/13 个有
- `VedaSparseAttention` —— 3/13 个有
- `Label (rgthree)` —— 1/13 个有
- `LatentUpscaleModelLoader` —— 1/13 个有
- `MiniMaxH3LatentUpscaleWithModel` —— 1/13 个有
- `OpenH3ICComposeLatent` —— 1/13 个有
- `OpenH3ICDraft` —— 1/13 个有
- `OpenH3ICPrompt` —— 1/13 个有
- `OpenH3ICSigmas` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
