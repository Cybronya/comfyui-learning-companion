---
name: unknown_workflow_video_sampler_unet_37
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.505818
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/10eros_singularity_latent_upscale_2115636763057278978.json, 图片生成/图生图/fastH3_ref2va_2112720537771397122.json, 图片生成/图生图/fast_h3_omni_base_2114878531695112194.json, 图片生成/图生图/minimax_h3_singularity_V2_r2va_2113800800932818945.json, 图片生成/图生图/人像VLOG丨MiniMax-H3丨三图参考·音画生成_2099794040656060418.json, 平台全量/2026-08-31+minimax_h3_i2v_face_refine_2119599322248597505.json, 平台全量/自用fast_h3_omini_latent_upscale_2118516597345316865.json, 视频生成/图生视频/2026-08-31 minimax_h3_i2v_face_refine_2097894239211442178.json, 视频生成/图生视频/2026-08-31 minimax_h3_r2v_face_refine_2097593143318368258.json, 视频生成/图生视频/Minimax H3 Singularity V2 + 8步加速 + 人脸修复 Face Refin_2113835488653168641.json, 视频生成/图生视频/minimax_h3_singularity_V2_face_refine_2113475613863538689.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_37

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/10eros_singularity_latent_upscale_2115636763057278978.json、图片生成/图生图/fastH3_ref2va_2112720537771397122.json、图片生成/图生图/fast_h3_omni_base_2114878531695112194.json、图片生成/图生图/minimax_h3_singularity_V2_r2va_2113800800932818945.json、图片生成/图生图/人像VLOG丨MiniMax-H3丨三图参考·音画生成_2099794040656060418.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
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
- `BlockSparseAttention` —— 10/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/11 个有
- `PrimitiveStringMultiline` —— 10/11 个有
- `GetNode` —— 9/11 个有
- `SetNode` —— 9/11 个有
- `ImageScaleToTotalPixels` —— 7/11 个有
- `LoraLoaderModelOnly` —— 7/11 个有
- `ModelAttentionBackend` —— 7/11 个有
- `BasicGuider` —— 6/11 个有
- `ConditioningZeroOut` —— 6/11 个有
- `RandomNoise` —— 6/11 个有
- `SamplerCustomAdvanced` —— 6/11 个有
- `SelfLiftH3Sampler` —— 6/11 个有
- `H3FaceStitch` —— 5/11 个有
- `H3FaceTrackCrop` —— 5/11 个有
- `VOSR2ModelLoader` —— 5/11 个有
- `VOSR2Upscale` —— 5/11 个有
- `PreviewAny` —— 4/11 个有
- `H3InjectVideoLatent` —— 3/11 个有
- `H3PerFrameDenoise` —— 3/11 个有
- `MiniMaxH3NativeAudioLock` —— 3/11 个有
- `MiniMaxH3SigmaShift` —— 2/11 个有
- `CM_FloatToInt` —— 1/11 个有
- `EmptyImage` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `LoadAudio` —— 1/11 个有
- `MiniMaxH3ImageToVideo` —— 1/11 个有
- `PreviewImage` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
