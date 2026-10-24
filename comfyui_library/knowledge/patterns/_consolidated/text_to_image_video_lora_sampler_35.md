---
name: text_to_image_video_lora_sampler_35
type: Text To Image
frequency: 17
level: strong
coverage: 0.865471
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, PreviewImage, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, YUAN_TXTJsonExtractor, YuanMultiImage, YuanTool, Yuan_H3MotionContext, Yuan_H3MotionContextTrim, Yuan_MiniMaxH3Video, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 全栈式短剧生成 V4.3.0（8 路参考图 + 首尾帧）_2110346834551074818.json, 视频生成/图生视频/MiniMax H3 全栈式短剧生成 V4.3.0（8 路参考图 + 首尾帧）_2110375174309765121.json, 视频生成/图生视频/MiniMax H3全栈式短剧生成V4.3.0，8路参考图加首尾帧_2111260984777203714.json, 视频生成/图生视频/MiniMax H3全栈式短剧生成V4.3.0｜8路参考图+首尾帧_2110694339532902402.json, 视频生成/图生视频/MiniMax H3全栈式短剧生成原始版，图生视频完整短剧生产管线_2102905558423658497.json, 视频生成/图生视频/MiniMax H3全栈短剧V4.3.0｜8路参考图加首尾帧一站式生成_2111059955322281986.json, 视频生成/图生视频/MiniMax H3全栈短剧生成V4.3.0，8路参考图加首尾帧图生视频_2110796967109554177.json, 视频生成/图生视频/全栈式短剧生成V4.2.2｜MiniMax-H3一分钟直出全节点注释_2091389821397848065.json, 视频生成/图生视频/全栈式短剧生成V4.2.2｜MiniMax-H3一分钟直出全节点注释_2091670085273481217.json, 视频生成/文生视频/MiniMax H3全栈式短剧生成V4.2.2 短剧版本直出1分钟加全节点注释_2105005940985647105.json, 视频生成/文生视频/MiniMax H3全栈式短剧生成V4.2.3 短剧版本直出1分钟加全节点注释_2105004299091795970.json, 视频生成/文生视频/MiniMax-H3全栈式短剧V4.2.2｜1分钟短剧直出｜注释齐全改起来省心_2104818075840368642.json, 视频生成/文生视频/MiniMax-H3全栈式短剧V4.2.3｜直出1分钟成片｜全节点注释好上手_2104811863312789505.json, 视频生成/文生视频/MiniMax-H3全栈式短剧生成V4.2.2｜一分钟视频直出全节点注释_2097849774153228290.json, 视频生成/文生视频/MiniMax-H3全栈式短剧生成V4.2.2｜短剧直出1分钟全节点注释_2097933098980831233.json, 视频生成/文生视频/MiniMax_H3全栈式短剧生成原始版，图生视频完整短剧生产管线_2104386806572732418.json, 视频生成/文生视频/全栈式短剧V4.2.2直出1分钟｜MiniMax-H3全节点注释_2096277568101109762.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_35

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 全栈式短剧生成 V4.3.0（8 路参考图 + 首尾帧）_2110346834551074818.json、视频生成/图生视频/MiniMax H3 全栈式短剧生成 V4.3.0（8 路参考图 + 首尾帧）_2110375174309765121.json、视频生成/图生视频/MiniMax H3全栈式短剧生成V4.3.0，8路参考图加首尾帧_2111260984777203714.json、视频生成/图生视频/MiniMax H3全栈式短剧生成V4.3.0｜8路参考图+首尾帧_2110694339532902402.json、视频生成/图生视频/MiniMax H3全栈式短剧生成原始版，图生视频完整短剧生产管线_2102905558423658497.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `YUAN_TXTJsonExtractor`
- `YuanMultiImage`
- `YuanTool`
- `Yuan_H3MotionContext`
- `Yuan_H3MotionContextTrim`
- `Yuan_MiniMaxH3Video`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 15/17 个有
- `EmptyAudio` —— 15/17 个有
- `If ANY execute A else B` —— 15/17 个有
- `Int` —— 15/17 个有
- `easy batchAnything` —— 15/17 个有
- `easy forLoopEnd` —— 15/17 个有
- `easy forLoopStart` —— 15/17 个有
- `easy isNone` —— 15/17 个有
- `easy mathInt` —— 15/17 个有
- `孤海注释` —— 15/17 个有
- `PrimitiveInt` —— 12/17 个有
- `YUAN_TXTJsonSwitch` —— 12/17 个有
- `YUAN_TXTPreviewContent` —— 12/17 个有
- `YuanAudioList` —— 12/17 个有
- `YuanAudioSplit` —— 12/17 个有
- `Yuan_H3Upscale3D` —— 12/17 个有
- `SaveImage` —— 11/17 个有
- `CR Text` —— 10/17 个有
- `easy convertAnything` —— 6/17 个有
- `ShowText|pysssss` —— 5/17 个有
- `VAEDecodeAudio` —— 5/17 个有
- `YUAN_TXTParagraphSplitter` —— 5/17 个有
- `YUAN_TXTShotReplace` —— 5/17 个有
- `YuanPrimitive` —— 5/17 个有
- `Yuan_H3MotionContextLoadLatent` —— 5/17 个有
- `Yuan_RTXVideoUpscaleH3` —— 5/17 个有
- `MiniMaxH3ResolutionSelector` —— 3/17 个有
- `GetNode` —— 2/17 个有
- `LoraLoaderBypassModelOnly` —— 2/17 个有
- `ManualSigmas` —— 2/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/17 个有
- `SetNode` —— 2/17 个有
- `TextGenerate` —— 2/17 个有
- `EmptyImage` —— 1/17 个有
- `LoadImage` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高发问题（22/17 个样本）：Steps较低可能导致细节不足
