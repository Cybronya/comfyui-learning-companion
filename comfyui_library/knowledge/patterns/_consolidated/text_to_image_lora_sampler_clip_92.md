---
name: text_to_image_lora_sampler_clip_92
type: Text To Image
frequency: 11
level: strong
coverage: 0.742273
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1080全能参考生视频｜海螺v2图生视频直出_2093816760570044417.json, 视频生成/图生视频/H3 People Dancing人物跳舞多种舞蹈风格加跳舞自动机Minimax工作流_2107960466378149889.json, 视频生成/图生视频/H3 sigma强化超清放大｜1080P打斗不糊脸不崩视频_2094933026361921538.json, 视频生成/图生视频/H3_People_Dancing人物跳舞｜多种舞蹈风格自动机_2107669075152433153.json, 视频生成/图生视频/H3潜空间放大工作流｜图生视频画质提升_2090444142102011905.json, 视频生成/图生视频/H3视频衔接工作流｜多段视频无缝拼接生成_2095211983237894146.json, 视频生成/图生视频/MiniMax H3双采潜空间放大图生视频处理工作流_2101380889010855937.json, 视频生成/图生视频/带视频1080全能参考｜海螺v2视频生视频生成_2094014088853680129.json, 视频生成/图生视频/带视频1080全能参考｜海螺生视频v2视频生视频_2093786874312749058.json, 视频生成/图生视频/带视频720全能参考｜海螺v2生视频生成工作流_2094038101344739330.json, 视频生成/图生视频/带音频1080全能参考｜海螺生视频v2图生视频_2093785361196605441.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_92

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/1080全能参考生视频｜海螺v2图生视频直出_2093816760570044417.json、视频生成/图生视频/H3 People Dancing人物跳舞多种舞蹈风格加跳舞自动机Minimax工作流_2107960466378149889.json、视频生成/图生视频/H3 sigma强化超清放大｜1080P打斗不糊脸不崩视频_2094933026361921538.json、视频生成/图生视频/H3_People_Dancing人物跳舞｜多种舞蹈风格自动机_2107669075152433153.json、视频生成/图生视频/H3潜空间放大工作流｜图生视频画质提升_2090444142102011905.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MinimaxH3LatentUpscaler3D` —— 10/11 个有
- `GetNode` —— 9/11 个有
- `H3SigmaRefiner` —— 9/11 个有
- `SetNode` —— 9/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/11 个有
- `SolAttnMiniMax` —— 8/11 个有
- `CR Prompt Text` —— 7/11 个有
- `VHS_VideoCombine` —— 7/11 个有
- `easy showAnything` —— 7/11 个有
- `LoadAudio` —— 6/11 个有
- `ModelPreviewOverrideKJ` —— 6/11 个有
- `PrimitiveFloat` —— 6/11 个有
- `VHS_LoadVideo` —— 6/11 个有
- `CM_IntToFloat` —— 5/11 个有
- `FloatConstant` —— 5/11 个有
- `INTConstant` —— 5/11 个有
- `LoraLoaderBypassModelOnly` —— 5/11 个有
- `ManualSigmas` —— 5/11 个有
- `ResizeShortestToNode` —— 5/11 个有
- `CreateVideo` —— 4/11 个有
- `PrimitiveStringMultiline` —— 4/11 个有
- `SaveVideo` —— 4/11 个有
- `EmptyImage` —— 2/11 个有
- `MiniMaxChunkFeedForward` —— 2/11 个有
- `MiniMaxLowVRAMAttention` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `RHHiddenNodes` —— 2/11 个有
- `SaveImage` —— 2/11 个有
- `FL_UnloadAllModels` —— 1/11 个有
- `Float` —— 1/11 个有
- `GetImageRangeFromBatch` —— 1/11 个有
- `MiniMaxH3AddGuide` —— 1/11 个有
- `MiniMaxH3BlockCacheT8` —— 1/11 个有
- `MinimaxH3LatentUpscalerNode2D` —— 1/11 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
