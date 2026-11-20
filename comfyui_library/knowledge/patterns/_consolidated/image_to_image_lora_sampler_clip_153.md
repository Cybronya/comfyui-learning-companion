---
name: image_to_image_lora_sampler_clip_153
type: Image To Image
frequency: 3
level: moderate
coverage: 0.826
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【提升真实感】Flux.1-Dev SRPO 摄影通用_1988882688666898434.json, 平台全量/kontext万物迁移_1964644212178341890.json, 平台全量/kontext专业工作流_2009461679523897345.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_153

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/【提升真实感】Flux.1-Dev SRPO 摄影通用_1988882688666898434.json、平台全量/kontext万物迁移_1964644212178341890.json、平台全量/kontext专业工作流_2009461679523897345.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 2/3 个有
- `GoogleTranslateTextNode` —— 2/3 个有
- `ImageUpscaleWithModel` —— 2/3 个有
- `ReferenceLatent` —— 2/3 个有
- `RepeatLatentBatch` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `ChinesePrompt_Mix` —— 1/3 个有
- `DyPE_FLUX` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy imageScaleDownToSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 25 | 3 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 33% |
| 重绘幅度 | 1 | 0.3 - 1 | 3 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 25，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，3 个样本
