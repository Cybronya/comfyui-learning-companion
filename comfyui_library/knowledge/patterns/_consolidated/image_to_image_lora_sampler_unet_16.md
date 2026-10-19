---
name: image_to_image_lora_sampler_unet_16
type: Image To Image
frequency: 3
level: strong
coverage: 0.884
common_nodes: [CFGNorm, CLIPLoader, CM_FloatToInt, CM_FloatUnaryOperation, CM_IntToFloat, CR Prompt Text, FL_ImageBatchToGrid, FluxKontextMultiReferenceLatentMethod, GetImageSizeAndCount, ImageListToBatch+, Int, JWIntegerToString, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveStringMultiline, ProcessString, Qwen3_VQA_Plus, RH_LLMAPI_NODE, SaveImage, StringFunction|pysssss, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy saveText, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2107418412778610689.json, 图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2107433169149579266.json, 视频生成/文生视频/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2068856792473493506.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_16

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2107418412778610689.json、图片生成/图生图/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2107433169149579266.json、视频生成/文生视频/图生图+多分镜自动-Qwen-Edit-NextScene-2511-8步_2068856792473493506.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CM_FloatToInt`
- `CM_FloatUnaryOperation`
- `CM_IntToFloat`
- `CR Prompt Text`
- `FL_ImageBatchToGrid`
- `FluxKontextMultiReferenceLatentMethod`
- `GetImageSizeAndCount`
- `ImageListToBatch+`
- `Int`
- `JWIntegerToString`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveStringMultiline`
- `ProcessString`
- `Qwen3_VQA_Plus`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `StringFunction|pysssss`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy saveText`
- `easy seed`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
