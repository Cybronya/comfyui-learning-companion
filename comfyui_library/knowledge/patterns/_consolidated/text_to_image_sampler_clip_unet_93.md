---
name: text_to_image_sampler_clip_unet_93
type: Text To Image
frequency: 8
level: moderate
coverage: 0.90075
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyImage, EmptyLatentImage, GetImageSizeAndCount, GetNode, ImpactInt, KSampler, SaveImage, SetNode, StringFunction|pysssss, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy int, easy positive, easy saveText, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/生图-文生图(角色白底图)-Z_Image_1994327080177434626.json, 图片生成/文生图/生图-文生图(角色白底图)-Z_Image_base_2016763551209234434.json, 图片生成/文生图/生图-文生图(角色白底图四视图)-Krea2_2097666811994136578.json, 图片生成/文生图/生图-文生图(角色白底图四视图)-Z_Image_2097687828619685889.json, 图片生成/文生图/生图-文生图自动-Krea2_2097666933897392130.json, 图片生成/文生图/生图-文生图自动-Z_Image_1994066603398676481.json, 图片生成/文生图/生图-文生图自动-Z_Image_2066055904258486272.json, 图片生成/文生图/生图-文生图自动-Z_Image_base_2016763491201327106.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_93

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/生图-文生图(角色白底图)-Z_Image_1994327080177434626.json、图片生成/文生图/生图-文生图(角色白底图)-Z_Image_base_2016763551209234434.json、图片生成/文生图/生图-文生图(角色白底图四视图)-Krea2_2097666811994136578.json、图片生成/文生图/生图-文生图(角色白底图四视图)-Z_Image_2097687828619685889.json、图片生成/文生图/生图-文生图自动-Krea2_2097666933897392130.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyImage`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImpactInt`
- `KSampler`
- `SaveImage`
- `SetNode`
- `StringFunction|pysssss`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy int`
- `easy positive`
- `easy saveText`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/8 个有
- `MemoryCleaner` —— 5/8 个有
- `Qwen3VL_Chat` —— 4/8 个有
- `easy imageRemBg` —— 4/8 个有
- `llama_cpp_instruct_adv` —— 4/8 个有
- `llama_cpp_model_loader` —— 4/8 个有
- `llama_cpp_parameters` —— 4/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `RH_LLMAPI_NODE` —— 3/8 个有
- `DapaoImageRatioLimitNode` —— 2/8 个有
- `ModelSamplingAuraFlow` —— 2/8 个有
- `PreviewImage` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | 1920 - 1920 | 8 | 100% |
| 高度 | 1080 | 1080 - 1080 | 8 | 100% |
| 采样步数 | 9.5 | 9 - 35 | 8 | 29% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 8 | 53% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1920，观测区间 1920 - 1920，8 个样本，取值集中（一致性 100%）
- 高度 中位数 1080，观测区间 1080 - 1080，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 9.5，观测区间 9 - 35，8 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（4/8 个样本）：Steps较低可能导致细节不足
