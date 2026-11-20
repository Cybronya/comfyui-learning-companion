---
name: text_to_image_video_lora_sampler_71
type: Text To Image
frequency: 12
level: strong
coverage: 0.724083
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Fastvideo H3快速文生视频｜ComfyUI加速生成_2095222013941080065.json, 视频生成/文生视频/H3 氛围感短视频｜文生视频图生视频双双在线_2096866829003218946.json, 视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107191447593246721.json, 视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107333167064637441.json, 视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107444165738057730.json, 视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107958839365689345.json, 视频生成/文生视频/MiniMax H3 新ref V1.0 Lora 阿里8步版｜多参考生视频工作流_2096839668997382146.json, 视频生成/文生视频/MiniMax H3多参考工作流｜全接口开放内部开发版_2095279663810695169.json, 视频生成/文生视频/minimaxH3数字人音色参考｜音色克隆口播视频生成_2094942909484322818.json, 视频生成/文生视频/minimaxH3访谈类数字人｜口播访谈视频生成_2097949263094439937.json, 视频生成/文生视频/refV1.2Lora多参考工作流｜MiniMax H3全接口开放开发版_2096716514572460034.json, 视频生成/文生视频/全能参考生成视频｜MiniMax-H3文生图生视频_2095818212331048962.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_71

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/Fastvideo H3快速文生视频｜ComfyUI加速生成_2095222013941080065.json、视频生成/文生视频/H3 氛围感短视频｜文生视频图生视频双双在线_2096866829003218946.json、视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107191447593246721.json、视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107333167064637441.json、视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107444165738057730.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 11/12 个有
- `LoadImage` —— 11/12 个有
- `MiniMaxH3ReferenceToVideo` —— 11/12 个有
- `SetNode` —— 11/12 个有
- `LoadAudio` —— 10/12 个有
- `孤海注释` —— 10/12 个有
- `ModelPreviewOverrideKJ` —— 8/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/12 个有
- `ModelAttentionBackend` —— 6/12 个有
- `PathchSageAttentionKJ` —— 6/12 个有
- `Fast Groups Bypasser (rgthree)` —— 5/12 个有
- `ManualSigmas` —— 5/12 个有
- `MiniMaxH3SigmaShift` —— 5/12 个有
- `BlockSparseAttention` —— 4/12 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 4/12 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 4/12 个有
- `SaveImage` —— 4/12 个有
- `VHS_LoadVideo` —— 4/12 个有
- `EmptyImage` —— 3/12 个有
- `PreviewImage` —— 3/12 个有
- `AudioCrop` —— 2/12 个有
- `MiniMaxH3ImageToVideo` —— 2/12 个有
- `Any Switch (rgthree)` —— 1/12 个有
- `ExtendIntermediateSigmas` —— 1/12 个有
- `LTXVConcatAVLatent` —— 1/12 个有
- `LTXVSeparateAVLatent` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `MinimaxH3LatentUpscaler3D` —— 1/12 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/12 个有
- `Seed (rgthree)` —— 1/12 个有
- `SolAttnMiniMax` —— 1/12 个有
- `StringConcatenate` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
