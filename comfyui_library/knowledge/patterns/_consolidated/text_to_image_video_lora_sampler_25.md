---
name: text_to_image_video_lora_sampler_25
type: Text To Image
frequency: 21
level: weak
coverage: 0.693714
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI短剧制作全功能工作流_2115751859993530369.json, 图片生成/图生图/Work-Fisher出品AI短剧制作全流程｜热门IP一键改编_2111070378704596993.json, 图片生成/图生图/【拓拓】AI短剧制作全流程_2114263270419951617.json, 图片生成/文生图/AI短剧制作全流程工作流｜文生图到图生视频一条龙｜短剧创作省心方案_2112118425899323393.json, 图片生成/文生图/AI短剧制作全流程视频_2111655145577734145.json, 平台全量/Luomini._AI短剧制作全流程_2118008875579437058.json, 平台全量/Work-Fisher 短剧流水线｜零基础 AI 短剧从 0 到成片完整工作流_2118172428877783042.json, 平台全量/【Work-Fisher】AI短剧制作全流程_2110714647472074754.json, 视频生成/图生视频/MINIMAX-H3开源最强文戏低配版｜角色一致性图生视频_2094855880356491266.json, 视频生成/图生视频/MINIMAX-H3最强文戏5参考图版，低配单采轻松跑_2110866429514960898.json, 视频生成/图生视频/MiniMAX H3导演台｜图生视频一键直出生成_2092357167356669954.json, 视频生成/图生视频/【Gensor】AI短剧制作工具合集工作流_2111079570249183234.json, 视频生成/图生视频/【Work-Fisher】AI短剧制作全流程_2109735475824123905.json, 视频生成/图生视频/【创客训练营】AI短剧制作全流程_2110597688004792322.json, 视频生成/文生视频/MiniMax-H3全能参考工作流｜文生图生视频多模式生成_2097418439563505665.json, 视频生成/文生视频/MiniMax-H3全能参考长视频生成｜文生视频图生视频双模支持_2099094223952900097.json, 视频生成/文生视频/MiniMax-H3全能参考｜多素材视频高质量生成_2095575150086414338.json, 视频生成/文生视频/MiniMax-H3全能参考｜长视频文生图生视频通吃出片_2101564544643592193.json, 视频生成/文生视频/全能参考工作流｜MiniMax-H3文生图生视频生成_2093477174438354945.json, 视频生成/文生视频/全能参考工作流｜MiniMax-H3文生图生视频直出_2090658700645191681.json, 视频生成/文生视频/全能参考生视频｜MiniMax H3图生文生二合一_2090839391815159809.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_25

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/AI短剧制作全功能工作流_2115751859993530369.json、图片生成/图生图/Work-Fisher出品AI短剧制作全流程｜热门IP一键改编_2111070378704596993.json、图片生成/图生图/【拓拓】AI短剧制作全流程_2114263270419951617.json、图片生成/文生图/AI短剧制作全流程工作流｜文生图到图生视频一条龙｜短剧创作省心方案_2112118425899323393.json、图片生成/文生图/AI短剧制作全流程视频_2111655145577734145.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 21 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 19/21 个有
- `Fast Groups Bypasser (rgthree)` —— 18/21 个有
- `SolAttnMiniMax` —— 18/21 个有
- `INTConstant` —— 17/21 个有
- `SaveImage` —— 14/21 个有
- `CR Prompt Text` —— 13/21 个有
- `PreviewImage` —— 13/21 个有
- `JjkText` —— 12/21 个有
- `solarL_SaveImagesToZip` —— 12/21 个有
- `孤海注释` —— 12/21 个有
- `CR Text` —— 11/21 个有
- `ComfySwitchNode` —— 11/21 个有
- `Image Comparer (rgthree)` —— 11/21 个有
- `ImageScaleToTotalPixels` —— 11/21 个有
- `LoadAudio` —— 11/21 个有
- `LoraLoaderBypassModelOnly` —— 11/21 个有
- `SeedVR2LoadDiTModel` —— 11/21 个有
- `SeedVR2LoadVAEModel` —— 11/21 个有
- `SeedVR2VideoUpscaler` —— 11/21 个有
- `TextEncodeQwenImage21` —— 11/21 个有
- `ExtendIntermediateSigmas` —— 10/21 个有
- `GetNode` —— 10/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/21 个有
- `SetNode` —— 10/21 个有
- `LTXVConcatAVLatent` —— 9/21 个有
- `忽略多组孤海` —— 9/21 个有
- `LTXVSeparateAVLatent` —— 8/21 个有
- `Seed (rgthree)` —— 8/21 个有
- `VHS_LoadVideo` —— 8/21 个有
- `MiniMaxH3ImageToVideo` —— 7/21 个有
- `Mute / Bypass Repeater (rgthree)` —— 7/21 个有
- `Any Switch (rgthree)` —— 6/21 个有
- `H3SigmaRefiner` —— 6/21 个有
- `MinimaxH3LatentUpscaler3D` —— 6/21 个有
- `MiniMaxH3SigmaShift` —— 5/21 个有
- `ModelPreviewOverrideKJ` —— 5/21 个有
- `ImageResizeKJv2` —— 3/21 个有
- `SplitSigmas` —— 3/21 个有
- `VAEEncode` —— 3/21 个有
- `VAEEncodeAudio` —— 3/21 个有
- `easy cleanGpuUsed` —— 3/21 个有
- `ConditioningZeroOut` —— 2/21 个有
- `GetImageRangeFromBatch` —— 2/21 个有
- `ImageAddNoise` —— 2/21 个有
- `MiniMaxH3AddGuide` —— 2/21 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/21 个有
- `PT_H3ConcatAVLatent` —— 2/21 个有
- `TrimAudioDuration` —— 2/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1080 | 21 | 3% |
| 高度 | 80 | 80 - 1920 | 21 | 0% |
| 采样步数 | 4 | 4 - 25 | 21 | 30% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 21 | 42% |
| 采样算法 | er_sde | - | 21 | 57% |
| 调度器 | beta | - | 21 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 36/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1080，21 个样本，取值分散，一致性仅 3%
- 高度 中位数 80，观测区间 80 - 1920，21 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 25，21 个样本，取值分散，一致性仅 30%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，21 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 er_sde，21 个样本，一致性 57%
- 调度器 最常用 beta，21 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 高发问题（36/21 个样本）：Steps较低可能导致细节不足
