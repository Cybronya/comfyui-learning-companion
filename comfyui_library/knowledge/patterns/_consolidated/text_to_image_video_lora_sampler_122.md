---
name: text_to_image_video_lora_sampler_122
type: Text To Image
frequency: 5
level: strong
coverage: 0.8668
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, H3SigmaRefiner, JjkText, KSampler, LoadAudio, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PreviewAny, PrimitiveFloat, RH_Screenwriter, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, SoundFlow_GetLength, SoundFlow_TrimAudio, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WujiCleaner, WujiH3PromptEnhancer, ZML_IntegerFloatConverter, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MV创作音频驱动对口型｜MiniMax-H3开源数字人生成_2094794949479981057.json, 视频生成/图生视频/MiniMax-H3音频驱动对口型数字人｜MV创作专用开源版_2094550723869626370.json, 视频生成/图生视频/MiniMax-H3音频驱动数字人｜MV创作专用生成_2095582163516350466.json, 视频生成/图生视频/音频驱动对口型数字人｜MiniMax-H3 MV创作专用_2092395157151895554.json, 视频生成/文生视频/多参首尾帧多合一分镜｜MiniMax-H3文生图生视频制作_2092895660407353345.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_122

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MV创作音频驱动对口型｜MiniMax-H3开源数字人生成_2094794949479981057.json、视频生成/图生视频/MiniMax-H3音频驱动对口型数字人｜MV创作专用开源版_2094550723869626370.json、视频生成/图生视频/MiniMax-H3音频驱动数字人｜MV创作专用生成_2095582163516350466.json、视频生成/图生视频/音频驱动对口型数字人｜MiniMax-H3 MV创作专用_2092395157151895554.json、视频生成/文生视频/多参首尾帧多合一分镜｜MiniMax-H3文生图生视频制作_2092895660407353345.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `PreviewAny`
- `PrimitiveFloat`
- `RH_Screenwriter`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `SoundFlow_GetLength`
- `SoundFlow_TrimAudio`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WujiCleaner`
- `WujiH3PromptEnhancer`
- `ZML_IntegerFloatConverter`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `VAEDecodeAudio` —— 4/5 个有
- `PrimitiveStringMultiline` —— 3/5 个有
- `RHHiddenNodes` —— 3/5 个有
- `WujiAudioLoader` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `AudioSeparation` —— 1/5 个有
- `Int` —— 1/5 个有
- `PreviewAudio` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
