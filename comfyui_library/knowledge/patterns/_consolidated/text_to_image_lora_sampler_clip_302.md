---
name: text_to_image_lora_sampler_clip_302
type: Text To Image
frequency: 3
level: moderate
coverage: 0.836333
common_nodes: [AddLabel, CFGOverride, CLIPLoader, CLIPTextEncode, CR Prompt Text, ClipLoaderGGUF, ComfyMathExpression, ComfyNumberConvert, ConditioningZeroOut, DualModelGuider, EmptyFlux2LatentImage, EmptyLatentImage, EmptySD3LatentImage, Ideogram4Scheduler, ImageConcatMulti, JsonExtractString, KSampler, KSamplerSelect, LoraLoaderModelOnly, PreviewAny, PrimitiveInt, PrimitiveStringMultiline, RH_LLMAPI_Pro_Node, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy cleanGpuUsed, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-多种模型生图对比_2070056239719084034.json, 图片生成/文生图/Krea2多模型对比_2069651388786896898.json, 图片生成/文生图/boogu 多模型对比_2067840542964281346.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_302

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea2-多种模型生图对比_2070056239719084034.json、图片生成/文生图/Krea2多模型对比_2069651388786896898.json、图片生成/文生图/boogu 多模型对比_2067840542964281346.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `AddLabel`
- `CFGOverride`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ClipLoaderGGUF`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `ConditioningZeroOut`
- `DualModelGuider`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `Ideogram4Scheduler`
- `ImageConcatMulti`
- `JsonExtractString`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `StringConcatenate` —— 2/3 个有
- `TextGenerate` —— 2/3 个有
- `easy promptLine` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 8 - 50 | 3 | 40% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 3.5 | 3 | 56% |
| 采样算法 | res_multistep | - | 3 | 33% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 720 - 1280 | 3 | 77% |
| 高度 | 1024 | 720 - 1280 | 3 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 28，观测区间 8 - 50，3 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 3.5，3 个样本
- 采样算法 最常用 res_multistep，3 个样本，一致性 33%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 720 - 1280，3 个样本
- 高度 中位数 1024，观测区间 720 - 1280，3 个样本
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
