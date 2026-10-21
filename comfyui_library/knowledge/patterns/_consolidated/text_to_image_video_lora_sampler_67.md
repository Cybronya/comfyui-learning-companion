---
name: text_to_image_video_lora_sampler_67
type: Text To Image
frequency: 11
level: strong
coverage: 0.893545
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Minimax_H3开源版8步极速文生视频｜600步新加速LORA加持｜短剧漫剧场景特效角色设计全能_2104444733849423874.json, 视频生成/文生视频/Minimax双时钟加速版图生视频文生视频生成_2088175309471444994.json, 视频生成/文生视频/h3开源版H3数字人加速四倍MiniMax图生视频口播数字宫格图片_2086259776987684865.json, 视频生成/文生视频/h3开源版H3数字人单人数字人图生视频口播数字人T8加速版MiniMax_2086264262372188162.json, 视频生成/文生视频/minimaxH3文生视频light2v8步lora双时钟生成工作流_2088272475523211266.json, 视频生成/文生视频/minimax三图工作流｜文生图生视频一键生成_2091309114570919938.json, 视频生成/文生视频/sage无损加速双bf16满血版MinimaxH3文生视频图生视频极致清晰_2088396155074990082.json, 视频生成/文生视频/sage无损加速｜MinimaxH3双bf16满血版文生图生视频全能_2089463275493875714.json, 视频生成/文生视频/二采高清放大minimaxH3工作流ENG_2087133080908816386.json, 视频生成/文生视频/开源版8步极速｜MiniMax H3文生视频跳舞创意_2093813895210299394.json, 视频生成/文生视频/开源版文生视频8步极速｜Minimax H3跳舞短剧漫剧创意生成_2095558045421101058.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_67

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/Minimax_H3开源版8步极速文生视频｜600步新加速LORA加持｜短剧漫剧场景特效角色设计全能_2104444733849423874.json、视频生成/文生视频/Minimax双时钟加速版图生视频文生视频生成_2088175309471444994.json、视频生成/文生视频/h3开源版H3数字人加速四倍MiniMax图生视频口播数字宫格图片_2086259776987684865.json、视频生成/文生视频/h3开源版H3数字人单人数字人图生视频口播数字人T8加速版MiniMax_2086264262372188162.json、视频生成/文生视频/minimaxH3文生视频light2v8步lora双时钟生成工作流_2088272475523211266.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 10/11 个有
- `CR Prompt Text` —— 8/11 个有
- `LoraLoaderBypassModelOnly` —— 8/11 个有
- `MiniMaxH3DualClockSamplerT8` —— 8/11 个有
- `孤海注释` —— 8/11 个有
- `LoadImage` —— 7/11 个有
- `ModelAttentionBackend` —— 5/11 个有
- `BasicScheduler` —— 3/11 个有
- `KSamplerSelect` —— 3/11 个有
- `CR Text` —— 1/11 个有
- `EmptyImage` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `Int` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `LoadAudio` —— 1/11 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/11 个有
- `PT_H3ConcatAVLatent` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `PrimitiveStringMultiline` —— 1/11 个有
- `Text Multiline` —— 1/11 个有
- `VAEEncode` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
