---
name: text_to_image_video_lora_sampler_123
type: Text To Image
frequency: 6
level: strong
coverage: 0.723333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3面部修复图生视频处理生成工具_2101749405769625602.json, 视频生成/图生视频/Minimax H3 Singularity中远景脸部精修 反油光质感图生视频_2098647053638393858.json, 视频生成/图生视频/Minimax H3图生视频脸部精修 80 优化版工作流_2098648439998476289.json, 视频生成/图生视频/Minimax H3多图参考生视频Singularity武斗专属模型加4步急速加放大加双重人脸精修工_2108324433835413505.json, 视频生成/图生视频/极速图生视频 MinimaxH3 人物场景特效快速生成_2094196531091034114.json, 视频生成/文生视频/MiniMax H3文生图生视频FastH3 8步急速加放大加人脸精修，FL2VA模型方案_2103575208023117825.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_123

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3面部修复图生视频处理生成工具_2101749405769625602.json、视频生成/图生视频/Minimax H3 Singularity中远景脸部精修 反油光质感图生视频_2098647053638393858.json、视频生成/图生视频/Minimax H3图生视频脸部精修 80 优化版工作流_2098648439998476289.json、视频生成/图生视频/Minimax H3多图参考生视频Singularity武斗专属模型加4步急速加放大加双重人脸精修工_2108324433835413505.json、视频生成/图生视频/极速图生视频 MinimaxH3 人物场景特效快速生成_2094196531091034114.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 5/6 个有
- `H3FaceStitch` —— 5/6 个有
- `H3FaceTrackCrop` —— 5/6 个有
- `H3InjectVideoLatent` —— 5/6 个有
- `H3PerFrameDenoise` —— 5/6 个有
- `MiniMaxH3ReferenceToVideo` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `VOSR2ModelLoader` —— 5/6 个有
- `VOSR2Upscale` —— 5/6 个有
- `GetNode` —— 4/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/6 个有
- `MiniMaxH3NativeAudioLock` —— 4/6 个有
- `MiniMaxH3SigmaShift` —— 4/6 个有
- `ModelAttentionBackend` —— 4/6 个有
- `BlockSparseAttention` —— 3/6 个有
- `LTXVConcatAVLatent` —— 3/6 个有
- `LTXVSeparateAVLatent` —— 3/6 个有
- `MinimaxH3LatentUpscaler3D` —— 3/6 个有
- `SplitSigmas` —— 3/6 个有
- `GetImageRangeFromBatch` —— 2/6 个有
- `MiniMaxH3ImageToVideo` —— 2/6 个有
- `PreviewAny` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `GetVideoComponents` —— 1/6 个有
- `H3SigmaRefiner` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `ManualSigmas` —— 1/6 个有
- `MiniMaxH3HybridArtifactBuilderT8Advanced` —— 1/6 个有
- `MiniMaxH3HybridModelLoaderT8Advanced` —— 1/6 个有
- `MiniMaxH3HybridPairInspectorT8Advanced` —— 1/6 个有
- `ModelPreviewOverrideKJ` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
