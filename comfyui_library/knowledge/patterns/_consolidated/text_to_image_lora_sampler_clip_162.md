---
name: text_to_image_lora_sampler_clip_162
type: Text To Image
frequency: 6
level: strong
coverage: 0.913833
common_nodes: [BasicGuider, BasicScheduler, BlockSparseAttention, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/自行车图生视频测试工作流，图生视频处理方案_2106875364315324417.json, 视频生成/图生视频/自行车图生视频测试工作流，图生视频处理方案_2109447261494272002.json, 视频生成/文生视频/FastH3 V2首尾帧视频 文生视频图生视频处理_2100685040215740418.json, 视频生成/文生视频/FastH3图生视频 高效视频生成处理工具_2100661665351168002.json, 视频生成/文生视频/FastVideo FastH3文生视频工作流，文生视频高效文本到视频生成方案_2107907010388914178.json, 视频生成/文生视频/FastVideo FastH3文生视频｜提示词直出视频不绕路_2107692375844941826.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_162

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/自行车图生视频测试工作流，图生视频处理方案_2106875364315324417.json、视频生成/图生视频/自行车图生视频测试工作流，图生视频处理方案_2109447261494272002.json、视频生成/文生视频/FastH3 V2首尾帧视频 文生视频图生视频处理_2100685040215740418.json、视频生成/文生视频/FastH3图生视频 高效视频生成处理工具_2100661665351168002.json、视频生成/文生视频/FastVideo FastH3文生视频工作流，文生视频高效文本到视频生成方案_2107907010388914178.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 5/6 个有
- `孤海注释` —— 5/6 个有
- `LoadImage` —— 4/6 个有
- `MiniMaxH3ImageToVideo` —— 4/6 个有
- `MiniMaxH3SigmaShift` —— 4/6 个有
- `GetVideoComponents` —— 2/6 个有
- `LoadAudio` —— 2/6 个有
- `LoadVideo` —— 2/6 个有
- `MiniMaxH3MotionContext` —— 2/6 个有
- `MiniMaxH3MotionContextChain` —— 2/6 个有
- `MiniMaxH3MotionContextLoadLatent` —— 2/6 个有
- `MiniMaxH3MotionContextSaveLatent` —— 2/6 个有
- `MiniMaxH3MotionContextTrim` —— 2/6 个有
- `MiniMaxH3ReferenceToVideo` —— 2/6 个有
- `Text Multiline` —— 2/6 个有
- `ViggleAnimateConditioningWindowed` —— 2/6 个有
- `EmptyImage` —— 1/6 个有
- `GetImageSize` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
