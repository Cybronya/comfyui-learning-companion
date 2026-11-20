---
name: unknown_workflow_video_lora_sampler_332
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.510714
common_nodes: [BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/minimax_h3_singularity_V2_r2va_2113800800932818945.json, 数字人/数字人/MiNimax超写实颜值赛道起号神器_2112333375519420418.json, 数字人/数字人/极速生视频 Fast_h3_omini_latent_upscale精品_2114537045958942722.json, 视频生成/图生视频/Minimax H3 Singularity V2 + 8步加速 + 人脸修复 Face Refin_2113835488653168641.json, 视频生成/图生视频/fast_h3_omini_latent_upscale_2114522676265050114.json, 视频生成/图生视频/minimax_h3_singularity_V2_face_refine_2113475613863538689.json, 视频生成/图生视频/minimax_h3_singularity_V2_r2va_2113488913896660994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_332

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/minimax_h3_singularity_V2_r2va_2113800800932818945.json、数字人/数字人/MiNimax超写实颜值赛道起号神器_2112333375519420418.json、数字人/数字人/极速生视频 Fast_h3_omini_latent_upscale精品_2114537045958942722.json、视频生成/图生视频/Minimax H3 Singularity V2 + 8步加速 + 人脸修复 Face Refin_2113835488653168641.json、视频生成/图生视频/fast_h3_omini_latent_upscale_2114522676265050114.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 6/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/7 个有
- `GetNode` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `MiniMaxH3SigmaShift` —— 3/7 个有
- `H3FaceStitch` —— 2/7 个有
- `H3FaceTrackCrop` —— 2/7 个有
- `PreviewAny` —— 2/7 个有
- `VOSR2ModelLoader` —— 2/7 个有
- `VOSR2Upscale` —— 2/7 个有
- `EmptyImage` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `MiniMaxChunkFeedForward` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `QwenH3PromptLocal` —— 1/7 个有
- `StringFormat` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
