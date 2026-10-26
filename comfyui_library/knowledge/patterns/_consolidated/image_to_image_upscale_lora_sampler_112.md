---
name: image_to_image_upscale_lora_sampler_112
type: Image To Image
frequency: 2
level: weak
coverage: 0.8355
common_nodes: [CFGNorm, CLIPLoader, CR Text Concatenate, ConstrainImage|pysssss, ImageUpscaleWithModel, KSampler, KSamplerAdvanced, LayerFilter: AddGrain, LayerUtility: ImageScaleByAspectRatio, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, MuyeTextEditOutput, Qwen3_VQA, SaveImage, ShowText|pysssss, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, UnsharpMask, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy globalSeed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/模特不同角度6张图2K高清电商服装_2064599635641065473.json, 图片生成/图生图/电商直出6张2k服装展示【耗时约五分钟】_2057445481487355905.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_112

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/模特不同角度6张图2K高清电商服装_2064599635641065473.json、图片生成/图生图/电商直出6张2k服装展示【耗时约五分钟】_2057445481487355905.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text Concatenate`
- `ConstrainImage|pysssss`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerAdvanced`
- `LayerFilter: AddGrain`
- `LayerUtility: ImageScaleByAspectRatio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `MuyeTextEditOutput`
- `Qwen3_VQA`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `UnsharpMask`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy globalSeed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `TT_img_enc` —— 1/2 个有
- `workflow>文本处理` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 0.3 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
