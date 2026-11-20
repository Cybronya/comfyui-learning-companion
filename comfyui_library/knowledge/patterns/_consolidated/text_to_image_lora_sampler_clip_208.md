---
name: text_to_image_lora_sampler_clip_208
type: Text To Image
frequency: 9
level: strong
coverage: 0.614333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, GetNode, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SetNode, SplitSigmas, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MINImax-H3全自动视频编辑流 人物替换迁移一步到位_2094818687348989954.json, 视频生成/图生视频/H3 sigma强化超清放大｜1080P打斗不糊脸不崩视频_2094933026361921538.json, 视频生成/图生视频/H3潜空间放大工作流｜图生视频画质提升_2090444142102011905.json, 视频生成/图生视频/H3视频衔接工作流｜多段视频无缝拼接生成_2095211983237894146.json, 视频生成/图生视频/视频衔接无缝续接生成｜H3图生视频工作流_2095490694986166273.json, 视频生成/文生视频/MINImax-H3单人音乐MV制作｜文生视频音乐生成_2094927265846091778.json, 视频生成/文生视频/minimaxH3混合模型sigma强化｜潜空间放大高清直出_2094545098968227842.json, 视频生成/文生视频/sigma强化不油腻混合模型｜minimaxH3潜空间放大高清直出_2094790731905986562.json, 视频生成/文生视频/单人音乐MV制作｜MINImax-H3三模视频生成工作流_2095106732040220673.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_208

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/MINImax-H3全自动视频编辑流 人物替换迁移一步到位_2094818687348989954.json、视频生成/图生视频/H3 sigma强化超清放大｜1080P打斗不糊脸不崩视频_2094933026361921538.json、视频生成/图生视频/H3潜空间放大工作流｜图生视频画质提升_2090444142102011905.json、视频生成/图生视频/H3视频衔接工作流｜多段视频无缝拼接生成_2095211983237894146.json、视频生成/图生视频/视频衔接无缝续接生成｜H3图生视频工作流_2095490694986166273.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `GetNode`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MinimaxH3LatentUpscaler3D` —— 8/9 个有
- `SolAttnMiniMax` —— 7/9 个有
- `VAEDecodeAudio` —— 7/9 个有
- `Fast Groups Bypasser (rgthree)` —— 5/9 个有
- `INTConstant` —— 5/9 个有
- `ResizeShortestToNode` —— 5/9 个有
- `easy float` —— 5/9 个有
- `MiniMaxH3SigmaShift` —— 4/9 个有
- `MuyeTextEditOutput` —— 3/9 个有
- `RHLLMChatNode` —— 3/9 个有
- `VHS_LoadVideo` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `FL_UnloadAllModels` —— 2/9 个有
- `GetImageRangeFromBatch` —— 2/9 个有
- `LoadAudio` —— 2/9 个有
- `MiniMaxChunkFeedForward` —— 2/9 个有
- `MiniMaxH3AddGuide` —— 2/9 个有
- `MiniMaxLowVRAMAttention` —— 2/9 个有
- `PreviewAudio` —— 2/9 个有
- `SoundFlow_GetLength` —— 2/9 个有
- `TrimAudioDuration` —— 2/9 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/9 个有
- `CR String To Number` —— 1/9 个有
- `Float` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `MinimaxH3LatentUpscalerNode2D` —— 1/9 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/9 个有
- `VHS_VideoInfo` —— 1/9 个有
- `easy clearCacheAll` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
