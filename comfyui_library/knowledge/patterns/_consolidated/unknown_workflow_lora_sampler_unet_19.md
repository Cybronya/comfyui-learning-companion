---
name: unknown_workflow_lora_sampler_unet_19
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.675857
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2026-08-31 minimax_h3_i2v_face_refine_2097894239211442178.json, 视频生成/图生视频/2026-08-31 minimax_h3_r2v_face_refine_2097593143318368258.json, 视频生成/图生视频/H3 面部重绘 FACE REFINE 修复崩脸_2090087014422110210.json, 视频生成/图生视频/MiniMax H3 首尾帧_图生视频_2085645887220568065.json, 视频生成/图生视频/Minimax H3  多图参考生视频｜Singularity  武斗专属模型+ 4步 急速 + 放大 + 双重 人脸精修_2107657989724401665.json, 视频生成/图生视频/minimax h3 面部修复_2101135085809520641.json, 视频生成/文生视频/Minimax H3 文生 & 图生视频｜FastH3 8步 急速 + 放大 + 人脸精修_2102582100221325314.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_19

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2026-08-31 minimax_h3_i2v_face_refine_2097894239211442178.json、视频生成/图生视频/2026-08-31 minimax_h3_r2v_face_refine_2097593143318368258.json、视频生成/图生视频/H3 面部重绘 FACE REFINE 修复崩脸_2090087014422110210.json、视频生成/图生视频/MiniMax H3 首尾帧_图生视频_2085645887220568065.json、视频生成/图生视频/Minimax H3  多图参考生视频｜Singularity  武斗专属模型+ 4步 急速 + 放大 + 双重 人脸精修_2107657989724401665.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 6/7 个有
- `H3FaceStitch` —— 6/7 个有
- `H3FaceTrackCrop` —— 6/7 个有
- `H3InjectVideoLatent` —— 6/7 个有
- `H3PerFrameDenoise` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `ResolutionSelector` —— 6/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/7 个有
- `MiniMaxH3NativeAudioLock` —— 5/7 个有
- `MiniMaxH3ReferenceToVideo` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `VHS_VideoCombine` —— 5/7 个有
- `VOSR2ModelLoader` —— 5/7 个有
- `VOSR2Upscale` —— 5/7 个有
- `BlockSparseAttention` —— 3/7 个有
- `GetNode` —— 3/7 个有
- `MiniMaxH3ImageToVideo` —— 3/7 个有
- `MiniMaxH3SigmaShift` —— 3/7 个有
- `ModelAttentionBackend` —— 3/7 个有
- `CreateVideo` —— 2/7 个有
- `GetImageRangeFromBatch` —— 2/7 个有
- `LTXVConcatAVLatent` —— 2/7 个有
- `LTXVSeparateAVLatent` —— 2/7 个有
- `MinimaxH3LatentUpscaler3D` —— 2/7 个有
- `PreviewAny` —— 2/7 个有
- `SaveVideo` —— 2/7 个有
- `SplitSigmas` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `ImageConcanate` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `ManualSigmas` —— 1/7 个有
- `ModelPreviewOverrideKJ` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
