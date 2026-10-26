---
name: text_to_image_video_lora_sampler_162
type: Text To Image
frequency: 4
level: strong
coverage: 0.90575
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Reference to Video全能参考｜MiniMax H3高质量加速版_2092022792094048258.json, 视频生成/图生视频/Reference to Video高质量加速｜MiniMax H3全能参考生成_2092211916549738497.json, 视频生成/图生视频/高质量加速版图生视频｜MiniMax H3图片转视频工作流_2088135941901864962.json, 视频生成/文生视频/高质量文生图生视频｜MiNiMax H3视频生视频全能工作流_2093088546247757825.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_162

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Reference to Video全能参考｜MiniMax H3高质量加速版_2092022792094048258.json、视频生成/图生视频/Reference to Video高质量加速｜MiniMax H3全能参考生成_2092211916549738497.json、视频生成/图生视频/高质量加速版图生视频｜MiniMax H3图片转视频工作流_2088135941901864962.json、视频生成/文生视频/高质量文生图生视频｜MiNiMax H3视频生视频全能工作流_2093088546247757825.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
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
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `EasyCache` —— 3/4 个有
- `MiniMaxH3AVDecodeT8` —— 3/4 个有
- `MiniMaxH3AudioConditioningT8` —— 3/4 个有
- `MiniMaxH3DualClockSamplerT8` —— 3/4 个有
- `MiniMaxH3ReferenceToVideo` —— 3/4 个有
- `ModelAttentionBackend` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `SolAttnMiniMax` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `Label (rgthree)` —— 2/4 个有
- `MiniMaxH3PromptEnhancerT8` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `RHLLMChatNode` —— 2/4 个有
- `StringConcatenate` —— 2/4 个有
- `easy convertAnything` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `easy string` —— 2/4 个有
- `string_util_StrConcat` —— 2/4 个有
- `LayerUtility: TextBox` —— 1/4 个有
- `LoraLoaderBypassModelOnly` —— 1/4 个有
- `MiniMaxH3ImageToVideo` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
