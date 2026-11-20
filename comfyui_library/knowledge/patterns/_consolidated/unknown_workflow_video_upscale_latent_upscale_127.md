---
name: unknown_workflow_video_upscale_latent_upscale_127
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.654333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3  多图参考生视频｜Singularity  武斗专属模型+ 4步 急速 + 放大 + 双重 人脸精修_2107657989724401665.json, 视频生成/图生视频/MinimaxH3_高动态_Singularity-(新)分段采样进阶工作流_2104944269617352706.json, 视频生成/文生视频/Minimax H3 文生 & 图生视频｜FastH3 8步 急速 + 放大 + 人脸精修_2102582100221325314.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_127

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Minimax H3  多图参考生视频｜Singularity  武斗专属模型+ 4步 急速 + 放大 + 双重 人脸精修_2107657989724401665.json、视频生成/图生视频/MinimaxH3_高动态_Singularity-(新)分段采样进阶工作流_2104944269617352706.json、视频生成/文生视频/Minimax H3 文生 & 图生视频｜FastH3 8步 急速 + 放大 + 人脸精修_2102582100221325314.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 2/3 个有
- `H3FaceStitch` —— 2/3 个有
- `H3FaceTrackCrop` —— 2/3 个有
- `H3InjectVideoLatent` —— 2/3 个有
- `H3PerFrameDenoise` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `MiniMaxH3ReferenceToVideo` —— 2/3 个有
- `ModelAttentionBackend` —— 2/3 个有
- `VOSR2ModelLoader` —— 2/3 个有
- `VOSR2Upscale` —— 2/3 个有
- `BlockSparseAttention` —— 1/3 个有
- `DisableNoise` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ManualSigmas` —— 1/3 个有
- `MiniMaxH3ImageToVideo` —— 1/3 个有
- `MiniMaxH3NativeAudioLock` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `StringConcatenate` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
