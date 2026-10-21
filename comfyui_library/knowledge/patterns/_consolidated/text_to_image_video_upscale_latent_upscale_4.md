---
name: text_to_image_video_upscale_latent_upscale_4
type: Text To Image
frequency: 16
level: strong
coverage: 0.483375
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfySwitchNode, EmptyLatentImage, ExtendIntermediateSigmas, Fast Groups Bypasser (rgthree), GetImageRangeFromBatch, GetNode, GetVideoComponents, ImageAddNoise, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewImage, PrimitiveBoolean, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, Seed (rgthree), SetNode, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy anythingInversedSwitch, easy batchAnything, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy mergeVideosFromPaths, easy minimaxH3ToVideo, easy multiTrackEditor, easy multiTrackInfoOutput, easy multiTrackTaskOutput, easy saveVideo, easy showAnything, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, easy anythingInversedSwitch, easy batchAnything, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy mergeVideosFromPaths, easy minimaxH3ToVideo, easy multiTrackEditor, Seed (rgthree), easy multiTrackInfoOutput, easy multiTrackTaskOutput, easy saveVideo]
members: [视频生成/图生视频/H3导演台长视频 视频生视频图生视频创作_2100270526487949313.json, 视频生成/图生视频/MiniMax H3导演台模式生成长视频，支持视频生视频与图生视频双模式_2102809851134042114.json, 视频生成/图生视频/MiniMax H3导演台长视频 多段编排视频生成方案_2105353411913932801.json, 视频生成/图生视频/MiniMax H3导演台长视频 长视频多段编排视频生成_2109384708021907458.json, 视频生成/图生视频/MiniMax H3导演台长视频 长视频多段编排视频生成_2109690032536772609.json, 视频生成/图生视频/MiniMax H3导演台长视频工作流，视频生视频图生视频高效创作方案_2106436294774706178.json, 视频生成/图生视频/MiniMax H3导演台长视频视频生成处理工具_2101725133303013378.json, 视频生成/图生视频/MiniMax-H3导演台模式｜视频生视频一键产出电影级长视频_2101482381654978561.json, 视频生成/图生视频/MiniMax-H3导演台模式｜长视频一站式生成神器_2105107847519490050.json, 视频生成/图生视频/MiniMax-H3导演台长视频方案，视频生视频连贯出片_2110484693325012993.json, 视频生成/图生视频/MiniMax-H3导演台长视频｜视频生视频图生视频 电影级长镜头创作_2104025435729383426.json, 视频生成/图生视频/MiniMax_H3导演台模式生成长视频，支持视频生视频与图生视频双模式_2106912694749188098.json, 视频生成/图生视频/导演台式长视频创作 MiniMax H3图生视频多段运镜编排_2104263147673706498.json, 视频生成/视频生视频/MiniMax H3导演台长视频工作流_视频生视频图生视频高效创作方案_2106436294774706178.json, 视频生成/视频生视频/MiniMax H3导演台长视频工作流_角色表演图生视频高效创作工具_2106089759742447618.json, 视频生成/视频生视频/MiniMax H3导演台长视频来了_图生视频视频生视频双支持一键出大片_2106193167304445953.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_4

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/H3导演台长视频 视频生视频图生视频创作_2100270526487949313.json、视频生成/图生视频/MiniMax H3导演台模式生成长视频，支持视频生视频与图生视频双模式_2102809851134042114.json、视频生成/图生视频/MiniMax H3导演台长视频 多段编排视频生成方案_2105353411913932801.json、视频生成/图生视频/MiniMax H3导演台长视频 长视频多段编排视频生成_2109384708021907458.json、视频生成/图生视频/MiniMax H3导演台长视频 长视频多段编排视频生成_2109690032536772609.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：48%

## 共有节点

全部 16 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `ExtendIntermediateSigmas`
- `Fast Groups Bypasser (rgthree)`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetVideoComponents`
- `ImageAddNoise`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `MiniMaxH3AddGuide`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `SetNode`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy anythingInversedSwitch`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy mergeVideosFromPaths`
- `easy minimaxH3ToVideo`
- `easy multiTrackEditor`
- `easy multiTrackInfoOutput`
- `easy multiTrackTaskOutput`
- `easy saveVideo`
- `easy showAnything`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 15/16 个有
- `SaveImage` —— 12/16 个有
- `INTConstant` —— 11/16 个有
- `VHS_VideoInfoLoaded` —— 11/16 个有
- `BlockSparseAttention` —— 8/16 个有
- `SplitSigmas` —— 8/16 个有
- `BatchImagesNode` —— 3/16 个有
- `EmptyImage` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高发问题（17/16 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、easy anythingInversedSwitch、easy batchAnything、easy cleanGpuUsed、easy forLoopEnd
