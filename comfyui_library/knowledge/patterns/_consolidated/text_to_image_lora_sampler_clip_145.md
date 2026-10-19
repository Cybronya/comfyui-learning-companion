---
name: text_to_image_lora_sampler_clip_145
type: Text To Image
frequency: 7
level: strong
coverage: 0.902571
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SplitSigmas, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/文生图一次15图｜MiniMaxH3爆图工作流批量生成_2093721661387395074.json, 视频生成/图生视频/视频同款滔博MV工作流，音频驱动图生视频MV生成工具_2103601280408182786.json, 视频生成/文生视频/FL2VA首尾帧文生全能｜MiniMax H3视频生成工作流_2093069819640901634.json, 视频生成/文生视频/MiniMax H3 FL2VA文生首尾帧全能视频｜文生视频视频生视频图生视频_2090423722896347138.json, 视频生成/文生视频/MiniMax H3 Sigma双采强化｜4K超清通用生视频旗舰版｜文图视频三合一_2099100789926096898.json, 视频生成/文生视频/MiniMax H3 Sigma强化双采通用生视频 4K超高清_2098832550188904449.json, 视频生成/文生视频/MiniMax H3双采Sigma强化版｜2K通用视频一站生成｜文生视频图生视频_2099091523861307393.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_145

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/文生图一次15图｜MiniMaxH3爆图工作流批量生成_2093721661387395074.json、视频生成/图生视频/视频同款滔博MV工作流，音频驱动图生视频MV生成工具_2103601280408182786.json、视频生成/文生视频/FL2VA首尾帧文生全能｜MiniMax H3视频生成工作流_2093069819640901634.json、视频生成/文生视频/MiniMax H3 FL2VA文生首尾帧全能视频｜文生视频视频生视频图生视频_2090423722896347138.json、视频生成/文生视频/MiniMax H3 Sigma双采强化｜4K超清通用生视频旗舰版｜文图视频三合一_2099100789926096898.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/7 个有
- `MinimaxH3LatentUpscaler3D` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `VAEDecodeAudio` —— 6/7 个有
- `H3SigmaRefiner` —— 5/7 个有
- `MiniMaxH3SigmaShift` —— 5/7 个有
- `ModelPreviewOverrideKJ` —— 5/7 个有
- `Int` —— 4/7 个有
- `MiniMaxH3AudioConditioningT8` —— 4/7 个有
- `ImageResizeKJv2` —— 3/7 个有
- `MiniMaxH3ImageToVideo` —— 3/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/7 个有
- `ModelAttentionBackend` —— 3/7 个有
- `RH_DLSS5FrameInterpolation` —— 3/7 个有
- `SaveImage` —— 3/7 个有
- `SeedVR2` —— 3/7 个有
- `SeedVR2BlockSwap` —— 3/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `1hew_AudioDuration` —— 1/7 个有
- `ExtractStoryboards_xuhuan1024` —— 1/7 个有
- `LatentUpscale` —— 1/7 个有
- `LoadAudio` —— 1/7 个有
- `MiniMaxChunkFeedForward` —— 1/7 个有
- `MiniMaxLowVRAMAttention` —— 1/7 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `RH_LLMAPI_Pro_Node` —— 1/7 个有
- `easy clearCacheAll` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
