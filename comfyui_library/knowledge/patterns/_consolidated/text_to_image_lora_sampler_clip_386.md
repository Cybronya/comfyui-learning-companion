---
name: text_to_image_lora_sampler_clip_386
type: Text To Image
frequency: 5
level: strong
coverage: 0.8568
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/minimax_h3_i2vw4a8-0810超低显存ENGENG_2087115217783316482.json, 视频生成/文生视频/minimax开源版中文锁定语音H3稳定4步lora加速版优化版图生视频_2086411021345972225.json, 视频生成/文生视频/六段式自动生成自动校验MiniMax H3 Ref2VA剧本直出9图参考成片原生音画同步_2088355373936893954.json, 视频生成/文生视频/双重加速）LoRA图生视频（SageAttentionMiniMax_2086535926196555778.json, 视频生成/文生视频/图文生视频直出｜MiniMax H3多模态视频生成_2093141446219091969.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_386

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/minimax_h3_i2vw4a8-0810超低显存ENGENG_2087115217783316482.json、视频生成/文生视频/minimax开源版中文锁定语音H3稳定4步lora加速版优化版图生视频_2086411021345972225.json、视频生成/文生视频/六段式自动生成自动校验MiniMax H3 Ref2VA剧本直出9图参考成片原生音画同步_2088355373936893954.json、视频生成/文生视频/双重加速）LoRA图生视频（SageAttentionMiniMax_2086535926196555778.json、视频生成/文生视频/图文生视频直出｜MiniMax H3多模态视频生成_2093141446219091969.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
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
- `CreateVideo` —— 4/5 个有
- `SaveVideo` —— 4/5 个有
- `孤海注释` —— 4/5 个有
- `LoraLoaderBypassModelOnly` —— 3/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/5 个有
- `MiniMaxH3BlockCacheT8` —— 2/5 个有
- `MiniMaxH3ImageToVideo` —— 2/5 个有
- `MiniMaxH3ReferenceToVideo` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `VHS_VideoCombine` —— 2/5 个有
- `Display Any (rgthree)` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `MiniMaxH3AudioConditioningT8` —— 1/5 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/5 个有
- `PlaySound|pysssss` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RHLLMChatNode` —— 1/5 个有
- `SolAttnPatch` —— 1/5 个有
- `Text` —— 1/5 个有

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
