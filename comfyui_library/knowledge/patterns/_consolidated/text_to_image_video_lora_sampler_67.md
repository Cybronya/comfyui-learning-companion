---
name: text_to_image_video_lora_sampler_67
type: Text To Image
frequency: 10
level: strong
coverage: 0.8317
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, ResolutionSelector, SelfLiftAvatarH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax H3 舞蹈短片｜首帧驱动音画同生律动成片_2112438123752939521.json, 视频生成/图生视频/MMH3 Selflift常规万能流，直出1080p最高质量版_2110447282897383425.json, 视频生成/图生视频/MMH3 Selflift短剧直出1080p 高质量视频制作_2110255149494132737.json, 视频生成/图生视频/MMH3 Selflift短剧直出1080p 高质量视频制作_2110369401181655042.json, 视频生成/图生视频/MiniMax H3 360度环绕视频加Selflift专用高分辨率生成工作流，图生视频_2106477153318686722.json, 视频生成/图生视频/MiniMax H3 360度环绕视频｜Selflift专用高分辨率转场运镜出片_2106207397177024513.json, 视频生成/图生视频/短剧制作直出1080P最高质量版MMH3 Selflift工作流，图生视频方案_2106889115852689410.json, 视频生成/图生视频/短剧制作直出1080P最高质量版MMH3_Selflift工作流，图生视频方案_2109094089965789186.json, 视频生成/图生视频/短剧制作直出1080p最高质量版 MMH3 Selflift 视频生成优化_2109336160928616450.json, 视频生成/图生视频/短剧制作直出1080p最高质量版MMH3 Selflift 视频生成优化_2109762427930890242.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_67

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/MiniMax H3 舞蹈短片｜首帧驱动音画同生律动成片_2112438123752939521.json、视频生成/图生视频/MMH3 Selflift常规万能流，直出1080p最高质量版_2110447282897383425.json、视频生成/图生视频/MMH3 Selflift短剧直出1080p 高质量视频制作_2110255149494132737.json、视频生成/图生视频/MMH3 Selflift短剧直出1080p 高质量视频制作_2110369401181655042.json、视频生成/图生视频/MiniMax H3 360度环绕视频加Selflift专用高分辨率生成工作流，图生视频_2106477153318686722.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 9/10 个有
- `LTXVSeparateAVLatent` —— 8/10 个有
- `SaveImage` —— 8/10 个有
- `LoadAudio` —— 7/10 个有
- `MiniMaxH3ReferenceToVideo` —— 7/10 个有
- `PreviewAny` —— 7/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `Int` —— 4/10 个有
- `JWStringToFloat` —— 3/10 个有
- `MiniMaxH3ImageToVideo` —— 3/10 个有
- `CR Prompt Text` —— 2/10 个有
- `ExtendIntermediateSigmas` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/10 个有
- `PlaySound|pysssss` —— 2/10 个有
- `PrimitiveFloat` —— 2/10 个有
- `EmptyImage` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `RTXVideoFrameGeneration` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（15/10 个样本）：Steps较低可能导致细节不足
