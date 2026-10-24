---
name: text_to_image_lora_sampler_clip_125
type: Text To Image
frequency: 11
level: strong
coverage: 0.873364
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107241699616575490.json, 图片生成/反推提示词/H3单采工作流｜反推提示词图生图快速上手版_2106964960260739074.json, 图片生成/图生图/H3最强打斗工作流，战斗特效人物出招快如闪电_2112293222151188482.json, 图片生成/图生图/H3最强打斗工作流｜天下武功唯快不破｜30秒长视频合并高燃战斗_2112116841031225345.json, 图片生成/图生图/MiniMaxH3参考生视频量化加速版｜文本图像音频视频多模态_2101210370760335362.json, 图片生成/图生图/Minimax h3高一致性工作流｜多镜头音频参考视频生成_2097838671696318466.json, 图片生成/文生图/H3fast-v2全参加速方案，文生图图生图双模快跑_2111585524942204929.json, 图片生成/文生图/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107334378736144385.json, 图片生成/文生图/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107445023326429185.json, 视频生成/图生视频/minimax最强动作武打视频生视频，战斗特效一步到位_2111187364122030082.json, 视频生成/图生视频/最强单采V2加特林版，10步极速战斗特效出片_2111231473561989122.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_125

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/反推提示词/H3单采工作流兼顾效果和速度，文生图反推提示词图生图处理方案_2107241699616575490.json、图片生成/反推提示词/H3单采工作流｜反推提示词图生图快速上手版_2106964960260739074.json、图片生成/图生图/H3最强打斗工作流，战斗特效人物出招快如闪电_2112293222151188482.json、图片生成/图生图/H3最强打斗工作流｜天下武功唯快不破｜30秒长视频合并高燃战斗_2112116841031225345.json、图片生成/图生图/MiniMaxH3参考生视频量化加速版｜文本图像音频视频多模态_2101210370760335362.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：87%

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
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 10/11 个有
- `BlockSparseAttention` —— 9/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `VHS_LoadVideo` —— 9/11 个有
- `孤海注释` —— 9/11 个有
- `ManualSigmas` —— 8/11 个有
- `ModelPreviewOverrideKJ` —— 8/11 个有
- `SaveImage` —— 8/11 个有
- `VHS_VideoCombine` —— 8/11 个有
- `MiniMaxH3AddGuide` —— 4/11 个有
- `AudioConcat` —— 3/11 个有
- `EasyCache` —— 3/11 个有
- `GetImageRangeFromBatch` —— 3/11 个有
- `ImageBatchMulti` —— 3/11 个有
- `SaveAudioAdvanced` —— 3/11 个有
- `SaveVideo` —— 3/11 个有
- `CreateVideo` —— 2/11 个有
- `EmptyImage` —— 2/11 个有
- `GetNode` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `SetNode` —— 2/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `MiniMaxH3SigmaShift` —— 1/11 个有
- `PainterVRAM` —— 1/11 个有
- `VideoCombineV2` —— 1/11 个有
- `easy positive` —— 1/11 个有

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
