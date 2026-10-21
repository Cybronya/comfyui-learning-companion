---
name: unknown_workflow_lora_sampler_unet_27
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.649667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, H3FaceStitch, H3FaceTrackCrop, H3InjectVideoLatent, H3PerFrameDenoise, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2026-08-31 minimax_h3_i2v_face_refine_2097894239211442178.json, 视频生成/图生视频/2026-08-31 minimax_h3_r2v_face_refine_2097593143318368258.json, 视频生成/图生视频/H3 面部重绘 FACE REFINE 修复崩脸_2090087014422110210.json, 视频生成/图生视频/Minimax H3  多图参考生视频｜Singularity  武斗专属模型+ 4步 急速 + 放大 + 双重 人脸精修_2107657989724401665.json, 视频生成/图生视频/minimax h3 面部修复_2101135085809520641.json, 视频生成/文生视频/Minimax H3 文生 & 图生视频｜FastH3 8步 急速 + 放大 + 人脸精修_2102582100221325314.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_27

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2026-08-31 minimax_h3_i2v_face_refine_2097894239211442178.json、视频生成/图生视频/2026-08-31 minimax_h3_r2v_face_refine_2097593143318368258.json、视频生成/图生视频/H3 面部重绘 FACE REFINE 修复崩脸_2090087014422110210.json、视频生成/图生视频/Minimax H3  多图参考生视频｜Singularity  武斗专属模型+ 4步 急速 + 放大 + 双重 人脸精修_2107657989724401665.json、视频生成/图生视频/minimax h3 面部修复_2101135085809520641.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `H3FaceStitch`
- `H3FaceTrackCrop`
- `H3InjectVideoLatent`
- `H3PerFrameDenoise`
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
- `ComfyMathExpression` —— 5/6 个有
- `MiniMaxH3NativeAudioLock` —— 5/6 个有
- `MiniMaxH3ReferenceToVideo` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `VHS_VideoCombine` —— 5/6 个有
- `VOSR2ModelLoader` —— 5/6 个有
- `VOSR2Upscale` —— 5/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/6 个有
- `BlockSparseAttention` —— 3/6 个有
- `GetNode` —— 3/6 个有
- `MiniMaxH3SigmaShift` —— 3/6 个有
- `ModelAttentionBackend` —— 3/6 个有
- `GetImageRangeFromBatch` —— 2/6 个有
- `LTXVConcatAVLatent` —— 2/6 个有
- `LTXVSeparateAVLatent` —— 2/6 个有
- `MiniMaxH3ImageToVideo` —— 2/6 个有
- `MinimaxH3LatentUpscaler3D` —— 2/6 个有
- `PreviewAny` —— 2/6 个有
- `SplitSigmas` —— 2/6 个有
- `CreateVideo` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `ManualSigmas` —— 1/6 个有
- `ModelPreviewOverrideKJ` —— 1/6 个有
- `SaveVideo` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
