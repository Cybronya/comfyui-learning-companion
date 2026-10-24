---
name: text_to_image_lora_sampler_clip_402
type: Text To Image
frequency: 4
level: moderate
coverage: 0.85475
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt List, CR Text, ConditioningZeroOut, Dapao_LlamaCaption, Dapao_LlamaCaptionOptions, EmptyLatentImage, Fast Groups Bypasser (rgthree), ImpactInt, KSampler, LoadImage, LoraLoaderModelOnly, RegexReplace, SaveImage, String Literal, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea+2+电商模特图  写真摄影 真实拍摄 高清放大_2083011900706746369.json, 图片生成/图生图/极致美图 电商模特图  写真摄影 Krea+2+ 真实拍摄 高清放大_2083022262218878978.json, 图片生成/文生图/Gemma4+Zimage-turbo反推生成保暖内衣_2054902666865717249.json, 图片生成/文生图/Krea 2 电商模特图-2.0_2076532743651020802.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_402

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Krea+2+电商模特图  写真摄影 真实拍摄 高清放大_2083011900706746369.json、图片生成/图生图/极致美图 电商模特图  写真摄影 Krea+2+ 真实拍摄 高清放大_2083022262218878978.json、图片生成/文生图/Gemma4+Zimage-turbo反推生成保暖内衣_2054902666865717249.json、图片生成/文生图/Krea 2 电商模特图-2.0_2076532743651020802.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt List`
- `CR Text`
- `ConditioningZeroOut`
- `Dapao_LlamaCaption`
- `Dapao_LlamaCaptionOptions`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImpactInt`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RegexReplace`
- `SaveImage`
- `String Literal`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `ResizeImageMaskNode` —— 3/4 个有
- `SeedVR2Conditioning` —— 3/4 个有
- `SeedVR2PostProcessing` —— 3/4 个有
- `SeedVR2Preprocess` —— 3/4 个有
- `VAEDecodeTiled` —— 3/4 个有
- `VAEEncodeTiled` —— 3/4 个有
- `CR Batch Images From List` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImageFromBatch` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有
- `llama_cpp_parameters` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 720 - 1280 | 4 | 79% |
| 高度 | 720 | 720 - 1280 | 4 | 72% |
| 采样步数 | 8 | 8 - 15 | 4 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.1 | 4 | 96% |
| 采样算法 | euler_ancestral | - | 4 | 75% |
| 调度器 | bong_tangent | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，观测区间 720 - 1280，4 个样本
- 高度 中位数 720，观测区间 720 - 1280，4 个样本
- 采样步数 中位数 8，观测区间 8 - 15，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.1，4 个样本，取值集中（一致性 96%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 75%
- 调度器 最常用 bong_tangent，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
