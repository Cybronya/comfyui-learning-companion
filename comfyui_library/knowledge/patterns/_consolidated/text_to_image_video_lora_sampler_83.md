---
name: text_to_image_video_lora_sampler_83
type: Text To Image
frequency: 9
level: strong
coverage: 0.917889
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107241699616575490.json, 图片生成/反推提示词/H3单采工作流｜反推提示词图生图快速上手版_2106964960260739074.json, 图片生成/图生图/H3人物替换专用流v1.5整理版 动作迁移视频处理工具_2113763372444504066.json, 图片生成/图生图/H3人物替换专用流v1.5整理版｜换人专用稳定好上手_2113531228686213122.json, 图片生成/图生图/H3官流单采极速文戏 快速出片美女文戏处理工具_2113415713628180481.json, 图片生成/图生图/H3最强打斗工作流，战斗特效人物出招快如闪电_2112293222151188482.json, 图片生成/图生图/H3最强打斗工作流｜天下武功唯快不破｜30秒长视频合并高燃战斗_2112116841031225345.json, 视频生成/图生视频/H3人物替换专用流，一键完成视频人物替换角色一致性_2110445753108881409.json, 视频生成/图生视频/H3人物替换专用流，一键完成视频人物替换角色一致性_2113815036748718081.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_83

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107241699616575490.json、图片生成/反推提示词/H3单采工作流｜反推提示词图生图快速上手版_2106964960260739074.json、图片生成/图生图/H3人物替换专用流v1.5整理版 动作迁移视频处理工具_2113763372444504066.json、图片生成/图生图/H3人物替换专用流v1.5整理版｜换人专用稳定好上手_2113531228686213122.json、图片生成/图生图/H3官流单采极速文戏 快速出片美女文戏处理工具_2113415713628180481.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelPreviewOverrideKJ`
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
- `ManualSigmas` —— 8/9 个有
- `孤海注释` —— 8/9 个有
- `ModelAttentionBackend` —— 7/9 个有
- `ImageBatchMulti` —— 6/9 个有
- `MiniMaxH3AddGuide` —— 6/9 个有
- `SaveImage` —— 6/9 个有
- `BlockSparseAttention` —— 5/9 个有
- `LoadAudio` —— 5/9 个有
- `VHS_LoadVideo` —— 5/9 个有
- `AudioConcat` —— 4/9 个有
- `H3SigmaRefiner` —— 4/9 个有
- `ImageFromBatch` —— 4/9 个有
- `ImageScaleToTotalPixels` —— 4/9 个有
- `LTXVConcatAVLatent` —— 4/9 个有
- `LTXVSeparateAVLatent` —— 4/9 个有
- `MiniMaxChunkFeedForward` —— 4/9 个有
- `MiniMaxLowVRAMAttention` —— 4/9 个有
- `MinimaxH3LatentUpscaler3D` —— 4/9 个有
- `PrimitiveInt` —— 4/9 个有
- `RepeatImageBatch` —— 4/9 个有
- `ResizeImagesByShorterEdge` —— 4/9 个有
- `VHS_LoadVideoFFmpeg` —— 4/9 个有
- `VHS_VideoInfo` —— 4/9 个有
- `EasyCache` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `GetImageRangeFromBatch` —— 2/9 个有
- `GetImageSize` —— 2/9 个有
- `ImageBatch` —— 2/9 个有
- `ImageExpandBatch+` —— 2/9 个有
- `PathchSageAttentionKJ` —— 2/9 个有
- `SaveAudioAdvanced` —— 2/9 个有
- `TrimAudioDuration` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `easy forLoopEnd` —— 2/9 个有
- `easy forLoopStart` —— 2/9 个有
- `EmptyImage` —— 1/9 个有
- `ExtendIntermediateSigmas` —— 1/9 个有
- `MiniMaxH3SigmaShift` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `PreviewImage` —— 1/9 个有

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
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
