---
name: text_to_image_lora_sampler_clip_66
type: Text To Image
frequency: 13
level: strong
coverage: 0.854
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3图生视频fastH3加速 trim多帧动态优化_2110252157650956290.json, 视频生成/图生视频/MiniMax H3图生视频fastH3加速 trim多帧动态优化_2110367355523133442.json, 视频生成/图生视频/MiniMax H3图生视频fastH3基础版 trim加速快速直出_2110253662495928321.json, 视频生成/图生视频/MiniMax H3图生视频fastH3基础版 trim加速快速直出_2110368880341377026.json, 视频生成/图生视频/MiniMax H3图生视频首尾帧控制｜原生音频自带，两张图变一段电影感短片_2100451183075880961.json, 视频生成/图生视频/MiniMax H3图生视频首尾帧视频二采加速版 高质量动态生成_2105373937122242561.json, 视频生成/图生视频/MiniMax H3数字人带货视频｜多图直生成模特产品展示_2103033669408608258.json, 视频生成/图生视频/MiniMax H3首尾帧3步快速生成图生视频处理工具_2101395032807923714.json, 视频生成/图生视频/MiniMax H3首尾帧二采加速版｜图生视频稳定出片_2105267559749734401.json, 视频生成/图生视频/MiniMax-H3开源多图生视频｜数字人视频带货电商口播好帮手_2104534112320180225.json, 视频生成/图生视频/MiniMax-H3开源数字人视频带货｜多图生视频电商口播神器_2104495131775815681.json, 视频生成/图生视频/MiniMax_H3单模双采放大工作流8G显存版，低显存笔记本也能跑方案_2109819079400968194.json, 视频生成/文生视频/MiniMax H3单模双采放大工作流8G显存版，低显存笔记本也能跑方案_2106866016801345537.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_66

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3图生视频fastH3加速 trim多帧动态优化_2110252157650956290.json、视频生成/图生视频/MiniMax H3图生视频fastH3加速 trim多帧动态优化_2110367355523133442.json、视频生成/图生视频/MiniMax H3图生视频fastH3基础版 trim加速快速直出_2110253662495928321.json、视频生成/图生视频/MiniMax H3图生视频fastH3基础版 trim加速快速直出_2110368880341377026.json、视频生成/图生视频/MiniMax H3图生视频首尾帧控制｜原生音频自带，两张图变一段电影感短片_2100451183075880961.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 13 个 workflow 都包含：
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
- `孤海注释` —— 12/13 个有
- `PrimitiveStringMultiline` —— 9/13 个有
- `LTXVConcatAVLatent` —— 8/13 个有
- `LTXVSeparateAVLatent` —— 8/13 个有
- `MiniMaxH3ImageToVideo` —— 8/13 个有
- `MinimaxH3LatentUpscaler3D` —— 8/13 个有
- `SaveImage` —— 8/13 个有
- `VHS_VideoCombine` —— 8/13 个有
- `MiniMaxH3SigmaShift` —— 7/13 个有
- `ModelAttentionBackend` —— 7/13 个有
- `SetNode` —— 7/13 个有
- `CreateVideo` —— 6/13 个有
- `SaveVideo` —— 6/13 个有
- `GetNode` —— 5/13 个有
- `MiniMaxH3ReferenceToVideo` —— 5/13 个有
- `SplitSigmas` —— 5/13 个有
- `BlockSparseAttention` —— 4/13 个有
- `ManualSigmas` —— 4/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/13 个有
- `ModelPreviewOverrideKJ` —— 3/13 个有
- `EmptyImage` —— 2/13 个有
- `ExtendIntermediateSigmas` —— 2/13 个有
- `Fast Groups Bypasser (rgthree)` —— 2/13 个有
- `MiniMaxH3AddGuide` —— 2/13 个有
- `PathchSageAttentionKJ` —— 2/13 个有
- `PreviewAny` —— 2/13 个有
- `PreviewImage` —— 2/13 个有
- `easy getNode` —— 2/13 个有
- `easy int` —— 2/13 个有
- `easy loraStack` —— 2/13 个有
- `easy loraStackApply` —— 2/13 个有
- `easy setNode` —— 2/13 个有
- `easy showAnything` —— 2/13 个有
- `Fast Groups Muter (rgthree)` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
