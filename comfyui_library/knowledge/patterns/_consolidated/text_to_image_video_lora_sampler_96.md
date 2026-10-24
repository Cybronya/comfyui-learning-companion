---
name: text_to_image_video_lora_sampler_96
type: Text To Image
frequency: 8
level: strong
coverage: 0.71225
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3面部修复图生视频处理生成工具_2101749405769625602.json, 视频生成/图生视频/Minimax H3 Singularity中远景脸部精修 反油光质感图生视频_2098647053638393858.json, 视频生成/图生视频/Minimax H3 高动态打斗模型｜更稳更有冲击力_2096914596027260929.json, 视频生成/图生视频/Minimax H3图生视频脸部精修 80 优化版工作流_2098648439998476289.json, 视频生成/图生视频/Minimax H3多图参考生视频Singularity武斗专属模型加4步急速加放大加双重人脸精修工_2108324433835413505.json, 视频生成/图生视频/全能参考二采放大｜MiniMax H3视频图生视频_2092362550968147969.json, 视频生成/图生视频/全能参考二采放大｜MiniMax H3视频生视频图生视频_2092619898299179010.json, 视频生成/文生视频/MiniMax H3文生图生视频FastH3 8步急速加放大加人脸精修，FL2VA模型方案_2103575208023117825.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_96

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3面部修复图生视频处理生成工具_2101749405769625602.json、视频生成/图生视频/Minimax H3 Singularity中远景脸部精修 反油光质感图生视频_2098647053638393858.json、视频生成/图生视频/Minimax H3 高动态打斗模型｜更稳更有冲击力_2096914596027260929.json、视频生成/图生视频/Minimax H3图生视频脸部精修 80 优化版工作流_2098648439998476289.json、视频生成/图生视频/Minimax H3多图参考生视频Singularity武斗专属模型加4步急速加放大加双重人脸精修工_2108324433835413505.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 8 个 workflow 都包含：
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
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 7/8 个有
- `MiniMaxH3ReferenceToVideo` —— 7/8 个有
- `PrimitiveFloat` —— 7/8 个有
- `ResolutionSelector` —— 7/8 个有
- `SetNode` —— 7/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/8 个有
- `MiniMaxH3SigmaShift` —— 6/8 个有
- `ModelAttentionBackend` —— 6/8 个有
- `PrimitiveStringMultiline` —— 6/8 个有
- `GetNode` —— 5/8 个有
- `H3FaceStitch` —— 5/8 个有
- `H3FaceTrackCrop` —— 5/8 个有
- `H3InjectVideoLatent` —— 5/8 个有
- `H3PerFrameDenoise` —— 5/8 个有
- `SaveImage` —— 5/8 个有
- `VOSR2ModelLoader` —— 5/8 个有
- `VOSR2Upscale` —— 5/8 个有
- `LTXVConcatAVLatent` —— 4/8 个有
- `LTXVSeparateAVLatent` —— 4/8 个有
- `MiniMaxH3NativeAudioLock` —— 4/8 个有
- `MinimaxH3LatentUpscaler3D` —— 4/8 个有
- `ModelPreviewOverrideKJ` —— 4/8 个有
- `SplitSigmas` —— 4/8 个有
- `BlockSparseAttention` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `CR Prompt Text` —— 2/8 个有
- `GetImageRangeFromBatch` —— 2/8 个有
- `MiniMaxH3ImageToVideo` —— 2/8 个有
- `PreviewAny` —— 2/8 个有
- `ImageConcanate` —— 1/8 个有
- `ManualSigmas` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
