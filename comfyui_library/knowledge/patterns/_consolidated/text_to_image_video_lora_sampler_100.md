---
name: text_to_image_video_lora_sampler_100
type: Text To Image
frequency: 8
level: strong
coverage: 0.67175
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MinimaxH3全能参考电影质感V2｜高质量视频生成_2094884318077345793.json, 视频生成/文生视频/minimaxH3数字人音色参考｜音色克隆口播视频生成_2094942909484322818.json, 视频生成/文生视频/minimaxH3访谈类数字人｜口播访谈视频生成_2097949263094439937.json, 视频生成/文生视频/refV1.2Lora多参考工作流｜MiniMax H3全接口开放开发版_2096716514572460034.json, 视频生成/文生视频/六宫格生视频｜minimax h3文生图生视频生成_2093790080652627970.json, 视频生成/文生视频/六宫格生视频｜minimax h3文生图生视频直出_2093456500986568705.json, 视频生成/文生视频/多参考生成视频｜MiniMax H3官方工作流一键直出_2090147863308357634.json, 视频生成/文生视频/电影质感V2｜MinimaxH3全能参考三模视频生成_2095082549973438466.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_100

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/MinimaxH3全能参考电影质感V2｜高质量视频生成_2094884318077345793.json、视频生成/文生视频/minimaxH3数字人音色参考｜音色克隆口播视频生成_2094942909484322818.json、视频生成/文生视频/minimaxH3访谈类数字人｜口播访谈视频生成_2097949263094439937.json、视频生成/文生视频/refV1.2Lora多参考工作流｜MiniMax H3全接口开放开发版_2096716514572460034.json、视频生成/文生视频/六宫格生视频｜minimax h3文生图生视频生成_2093790080652627970.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/8 个有
- `LoadAudio` —— 6/8 个有
- `VAEDecodeAudio` —— 5/8 个有
- `ModelPreviewOverrideKJ` —— 4/8 个有
- `VHS_LoadVideo` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `MiniMaxH3AVDecodeT8` —— 3/8 个有
- `MiniMaxH3SigmaShift` —— 3/8 个有
- `PathchSageAttentionKJ` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `AudioCrop` —— 2/8 个有
- `CR Prompt Text` —— 2/8 个有
- `Float` —— 2/8 个有
- `MiniMaxH3ConcatAVLatent` —— 2/8 个有
- `MinimaxH3LatentUpscaler3D` —— 2/8 个有
- `ModelAttentionBackend` —— 2/8 个有
- `easy clearCacheAll` —— 2/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `Text` —— 1/8 个有
- `忽略多组孤海` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
