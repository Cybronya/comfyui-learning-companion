---
name: image_to_image_upscale_lora_sampler_55
type: Image To Image
frequency: 3
level: moderate
coverage: 0.936333
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwenedit2511多视角套图编辑_2003670076165398530.json, 图片生成/图生图/三视图_1993511170038497282.json, 图片生成/图生图/千问Edit2509人物一致性【双采样高清大图】_1971405689400836097.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_55

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/qwenedit2511多视角套图编辑_2003670076165398530.json、图片生成/图生图/三视图_1993511170038497282.json、图片生成/图生图/千问Edit2509人物一致性【双采样高清大图】_1971405689400836097.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `ImageUpscaleWithModel` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `CR Prompt Text` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageScaleToMegapixels` —— 1/3 个有
- `NunchakuQwenImageDiTLoader` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `easy promptLine` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.4 | 0.35 - 1 | 3 | 49% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.35 - 1，3 个样本，取值分散，一致性仅 49%
- 高发问题（14/3 个样本）：Steps较低可能导致细节不足
