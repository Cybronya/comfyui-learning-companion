---
name: unknown_workflow_sampler_clip_unet_28
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.919625
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [Text Multiline]
members: [图片生成/文生图/1932450301490425858.json, 图片生成/文生图/1932966165364834305.json, 图片生成/文生图/1933850253839749122.json, 图片生成/文生图/1937538449320906754.json, 图片生成/文生图/1942505597264924674.json, 图片生成/文生图/1962372606101950465.json, 图片生成/文生图/1963922300439547906.json, 图片生成/文生图/1984515249296523265.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_28

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1932450301490425858.json、图片生成/文生图/1932966165364834305.json、图片生成/文生图/1933850253839749122.json、图片生成/文生图/1937538449320906754.json、图片生成/文生图/1942505597264924674.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UpscaleModelLoader` —— 7/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `ImageUpscaleWithModel` —— 4/8 个有
- `UltimateSDUpscale` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `ImageScaleBy` —— 2/8 个有
- `LoraLoader` —— 2/8 个有
- `CheckpointLoaderSimple` —— 1/8 个有
- `JoinStrings` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `Text Multiline` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1176 | 1024 - 1344 | 8 | 91% |
| 高度 | 1536 | 720 - 1600 | 8 | 68% |
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1176，观测区间 1024 - 1344，8 个样本，取值集中（一致性 91%）
- 高度 中位数 1536，观测区间 720 - 1600，8 个样本
- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline
