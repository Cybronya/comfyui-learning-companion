---
name: text_to_image_lora_sampler_clip_418
type: Text To Image
frequency: 5
level: strong
coverage: 0.903
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/文生图生视频通用工作流｜多模式视频快速生成_2097522046669508609.json, 视频生成/文生视频/文生视频｜720P双时钟高质量加速0.8 图生视频视频生视频全能直出_2089415507794550786.json, 视频生成/文生视频/最新8步增速5分钟出10秒｜Minimax H3文生视频+视频放大_2089036367534845953.json, 视频生成/文生视频/最新最快4步8步增速工作流Minimax H3文生视频图生视频_2088410988835074049.json, 视频生成/文生视频/最新最快4步和8步增速｜Minimax H3文生图生视频工作流_2088388313551040514.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_418

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/文生图生视频通用工作流｜多模式视频快速生成_2097522046669508609.json、视频生成/文生视频/文生视频｜720P双时钟高质量加速0.8 图生视频视频生视频全能直出_2089415507794550786.json、视频生成/文生视频/最新8步增速5分钟出10秒｜Minimax H3文生视频+视频放大_2089036367534845953.json、视频生成/文生视频/最新最快4步8步增速工作流Minimax H3文生视频图生视频_2088410988835074049.json、视频生成/文生视频/最新最快4步和8步增速｜Minimax H3文生图生视频工作流_2088388313551040514.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 4/5 个有
- `LoraLoaderBypassModelOnly` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `VAEDecodeAudio` —— 4/5 个有
- `CreateVideo` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `MiniMaxH3ImageToVideo` —— 3/5 个有
- `SaveVideo` —— 3/5 个有
- `CR Float To Integer` —— 2/5 个有
- `CR Text` —— 2/5 个有
- `GetVideoComponents` —— 2/5 个有
- `LoadAudio` —— 2/5 个有
- `LoadVideo` —— 2/5 个有
- `MiniMaxH3AVDecodeT8` —— 2/5 个有
- `MiniMaxH3ReferenceToVideo` —— 2/5 个有
- `VHS_VideoCombine` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `MiniMaxH3AudioConditioningT8` —— 1/5 个有
- `MiniMaxH3Unified` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `SaveImage` —— 1/5 个有

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
