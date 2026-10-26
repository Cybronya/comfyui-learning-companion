---
name: text_to_image_video_lora_sampler_93
type: Text To Image
frequency: 9
level: strong
coverage: 0.940889
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text, ComfyMathExpression, EmptyLatentImage, Fast Groups Bypasser (rgthree), H3DistanceAttentionPatcher, H3ExactRecover, H3InjectSchedule, H3JerkHeatmap, H3JerkOracle, H3SigmaRefiner, H3TimeSmear, H3V2VInit, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ImageToVideo, MiniMaxH3MotionContextSaveLatent, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PlaySound|pysssss, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAELoader, VHS_LoadAudioUpload, VHS_LoadVideo, VHS_VideoCombine, VRAM_Debug, easy int, easy seed, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3双采全功能工作流细节残影修复与双重去油及远景优化，图生视频_2106876832036515842.json, 视频生成/图生视频/MiniMax_H3双采全功能工作流细节残影修复与双重去油及远景优化，图生视频_2109444477218807809.json, 视频生成/文生视频/MiniMax H3单采全功能，视频延长与残影修复及双重去油远景优化合一_2102830394193301506.json, 视频生成/文生视频/MiniMax H3单采全功能｜细节残影修复视频延长｜双重去油远景优化_2102617056968531970.json, 视频生成/文生视频/MiniMax H3双采全功能再上线｜残影细节修复双重去油｜远景优化一步到位_2102602330863661057.json, 视频生成/文生视频/MiniMax H3双采全功能工作流，细节残影修复与双重去油及远景优化_2102825546802618370.json, 视频生成/文生视频/MiniMax H3双采全功能｜细节残影修复加双重去油｜远景画质再进化_2102576207878512642.json, 视频生成/视频生视频/MiniMax_H3单采全功能，视频延长与残影修复及双重去油远景优化合一_2106175322394816514.json, 视频生成/视频生视频/MiniMax_H3双采全功能工作流，细节残影修复与双重去油及远景优化_2106182433518481409.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_93

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3双采全功能工作流细节残影修复与双重去油及远景优化，图生视频_2106876832036515842.json、视频生成/图生视频/MiniMax_H3双采全功能工作流细节残影修复与双重去油及远景优化，图生视频_2109444477218807809.json、视频生成/文生视频/MiniMax H3单采全功能，视频延长与残影修复及双重去油远景优化合一_2102830394193301506.json、视频生成/文生视频/MiniMax H3单采全功能｜细节残影修复视频延长｜双重去油远景优化_2102617056968531970.json、视频生成/文生视频/MiniMax H3双采全功能再上线｜残影细节修复双重去油｜远景优化一步到位_2102602330863661057.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `H3DistanceAttentionPatcher`
- `H3ExactRecover`
- `H3InjectSchedule`
- `H3JerkHeatmap`
- `H3JerkOracle`
- `H3SigmaRefiner`
- `H3TimeSmear`
- `H3V2VInit`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MotionContextSaveLatent`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PlaySound|pysssss`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadAudioUpload`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VRAM_Debug`
- `easy int`
- `easy seed`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 6/9 个有
- `LTXVSeparateAVLatent` —— 6/9 个有
- `ManualSigmas` —— 6/9 个有
- `MinimaxH3LatentUpscaler3D` —— 6/9 个有
- `SaveImage` —— 6/9 个有
- `SplitSigmas` —— 6/9 个有
- `easy float` —— 6/9 个有
- `孤海注释` —— 6/9 个有
- `EmptyImage` —— 4/9 个有
- `PreviewImage` —— 4/9 个有
- `AudioConcat` —— 3/9 个有
- `MiniMaxH3MotionContext` —— 3/9 个有
- `MiniMaxH3MotionContextLoadLatent` —— 3/9 个有
- `MiniMaxH3MotionContextTrim` —— 3/9 个有
- `VHS_MergeImages` —— 3/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（11/9 个样本）：Steps较低可能导致细节不足
