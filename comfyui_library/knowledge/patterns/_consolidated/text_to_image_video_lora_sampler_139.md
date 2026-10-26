---
name: text_to_image_video_lora_sampler_139
type: Text To Image
frequency: 5
level: strong
coverage: 0.8658
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, GetNode, INTConstant, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MultiTextConcatenate, MuyeTextEditOutput, RHLLMChatNode, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/全行业广告制作加音频驱动加提示词生成器辅助扩写，数字人电商产品方案_2107226505611923457.json, 数字人/数字人/全行业广告制作助手｜音频驱动加提示词生成器辅助扩写_2106927316462039041.json, 视频生成/图生视频/全行业广告制作助手｜音频驱动加提示词生成器辅助扩写_2107981763464220673.json, 视频生成/图生视频/全行业广告制作｜提示词生成器辅助扩写图生视频_2092373596747419650.json, 视频生成/图生视频/提示词生成器辅助扩写｜全行业电商视频广告制作_2090833556611362817.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_139

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/全行业广告制作加音频驱动加提示词生成器辅助扩写，数字人电商产品方案_2107226505611923457.json、数字人/数字人/全行业广告制作助手｜音频驱动加提示词生成器辅助扩写_2106927316462039041.json、视频生成/图生视频/全行业广告制作助手｜音频驱动加提示词生成器辅助扩写_2107981763464220673.json、视频生成/图生视频/全行业广告制作｜提示词生成器辅助扩写图生视频_2092373596747419650.json、视频生成/图生视频/提示词生成器辅助扩写｜全行业电商视频广告制作_2090833556611362817.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `GetNode`
- `INTConstant`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MultiTextConcatenate`
- `MuyeTextEditOutput`
- `RHLLMChatNode`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 4/5 个有
- `ComfyMathExpression` —— 3/5 个有
- `LTXVAudioVAEEncode` —— 3/5 个有
- `LTXVConcatAVLatent` —— 3/5 个有
- `LTXVSeparateAVLatent` —— 3/5 个有
- `SetLatentNoiseMask` —— 3/5 个有
- `SolidMask` —— 3/5 个有
- `SoundFlow_GetLength` —— 3/5 个有
- `MathExpression|pysssss` —— 2/5 个有
- `VAEDecodeAudio` —— 2/5 个有
- `easy int` —— 2/5 个有
- `EasyCache` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `LoraLoaderBypassModelOnly` —— 1/5 个有
- `ModelAttentionBackend` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `忽略多组孤海` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
