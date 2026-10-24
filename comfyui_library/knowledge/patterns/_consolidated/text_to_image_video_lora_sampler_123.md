---
name: text_to_image_video_lora_sampler_123
type: Text To Image
frequency: 6
level: strong
coverage: 0.5525
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PreviewImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAEEncodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy cleanGpuUsed, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/短剧直出多合一｜MiniMax H3图生视频超级工作流_2093064037759279105.json, 视频生成/图生视频/短剧直出超级多合一｜MiniMax H3图生视频生成_2093219274356772866.json, 视频生成/图生视频/超级多合一官方版｜YZ金鱼 MiniMax H3图生图生视频_2094723951757971458.json, 视频生成/文生视频/傲雪AIGC短剧双采｜MiniMax H3文生图生视频工作流_2093212268778582018.json, 视频生成/文生视频/多参2采8步加速｜MiniMax H3文生图生视频生成_2091601751957925889.json, 视频生成/文生视频/多参二采8步加速｜MiniMax H3视频生成提速_2091773543188090881.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_123

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/短剧直出多合一｜MiniMax H3图生视频超级工作流_2093064037759279105.json、视频生成/图生视频/短剧直出超级多合一｜MiniMax H3图生视频生成_2093219274356772866.json、视频生成/图生视频/超级多合一官方版｜YZ金鱼 MiniMax H3图生图生视频_2094723951757971458.json、视频生成/文生视频/傲雪AIGC短剧双采｜MiniMax H3文生图生视频工作流_2093212268778582018.json、视频生成/文生视频/多参2采8步加速｜MiniMax H3文生图生视频生成_2091601751957925889.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：55%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PreviewImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 2/6 个有
- `ComfySwitchNode` —— 2/6 个有
- `PrimitiveBoolean` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `RegexExtract` —— 2/6 个有
- `ShowText|pysssss` —— 2/6 个有
- `YUAN_TXTConvertAny` —— 2/6 个有
- `YUAN_TXTJsonExtractor` —— 2/6 个有
- `YUAN_TXTParagraphSplitter` —— 2/6 个有
- `easy positive` —— 2/6 个有
- `MiniMaxH3ImageToVideo` —— 1/6 个有
- `PlaySound|pysssss` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
