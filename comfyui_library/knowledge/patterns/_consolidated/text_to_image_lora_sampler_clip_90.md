---
name: text_to_image_lora_sampler_clip_90
type: Text To Image
frequency: 10
level: strong
coverage: 0.7983
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MinimaxH3全能参考电影质感V2｜高质量视频生成_2094884318077345793.json, 视频生成/文生视频/Minimax开源版H3多宫格图生视频开源版加速版_2086200437891485697.json, 视频生成/文生视频/minimaxH3数字人音色参考｜音色克隆口播视频生成_2094942909484322818.json, 视频生成/文生视频/minimaxH3访谈类数字人｜口播访谈视频生成_2097949263094439937.json, 视频生成/文生视频/refV1.2Lora多参考工作流｜MiniMax H3全接口开放开发版_2096716514572460034.json, 视频生成/文生视频/开源加速版MiniMax h3海螺多参文生视频图生视频音频参考_2085178835024306178.json, 视频生成/文生视频/新4步LoRa参考图｜MiniMax H3角色一致图生视频_2092736016280023041.json, 视频生成/文生视频/新ref V1.0 Lora阿里8步版｜MiniMax H3多参考加速生成_2096684025057468417.json, 视频生成/文生视频/电影质感V2｜MinimaxH3全能参考三模视频生成_2095082549973438466.json, 视频生成/文生视频/超级加速版多参考视频｜minimaxH3文生图生视频生视频_2092577712144732161.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_90

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/MinimaxH3全能参考电影质感V2｜高质量视频生成_2094884318077345793.json、视频生成/文生视频/Minimax开源版H3多宫格图生视频开源版加速版_2086200437891485697.json、视频生成/文生视频/minimaxH3数字人音色参考｜音色克隆口播视频生成_2094942909484322818.json、视频生成/文生视频/minimaxH3访谈类数字人｜口播访谈视频生成_2097949263094439937.json、视频生成/文生视频/refV1.2Lora多参考工作流｜MiniMax H3全接口开放开发版_2096716514572460034.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 10 个 workflow 都包含：
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
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 9/10 个有
- `PathchSageAttentionKJ` —— 8/10 个有
- `PrimitiveStringMultiline` —— 8/10 个有
- `VAEDecodeAudio` —— 8/10 个有
- `VHS_LoadVideo` —— 8/10 个有
- `GetNode` —— 7/10 个有
- `SetNode` —— 7/10 个有
- `VHS_VideoCombine` —— 7/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/10 个有
- `CreateVideo` —— 3/10 个有
- `ModelPreviewOverrideKJ` —— 3/10 个有
- `SaveVideo` —— 3/10 个有
- `AudioCrop` —— 2/10 个有
- `Float` —— 2/10 个有
- `MiniMaxH3AVDecodeT8` —— 2/10 个有
- `MiniMaxH3ConcatAVLatent` —— 2/10 个有
- `MiniMaxH3SigmaShift` —— 2/10 个有
- `MinimaxH3LatentUpscaler3D` —— 2/10 个有
- `easy clearCacheAll` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `PainterVRAM` —— 1/10 个有
- `忽略多组孤海` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
