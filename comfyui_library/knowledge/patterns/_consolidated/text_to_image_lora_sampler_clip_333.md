---
name: text_to_image_lora_sampler_clip_333
type: Text To Image
frequency: 6
level: strong
coverage: 0.8955
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSizeAndCount, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, PreviewImage, SaveImage, StringFunction|pysssss, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy imageConcat, easy int, easy positive, easy seed, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1单图编辑任意比例自动化出图_2104683492004159489.json, 图片生成/图生图/Qwen Image 2.1单图编辑自动化 指令式改图直出_2104645434831626242.json, 图片生成/图生图/Qwen-Image-2.1单图编辑自动出图｜任意比例换背景轻松搞定_2104537166071296002.json, 图片生成/图生图/Qwen-Image-2.1单图编辑自动｜角色一致性图生图保持不走样_2104558840414031873.json, 图片生成/图生图/Qwen-Image-2.1双海报自动生成｜中英文海报制作 图生图一键出图_2104070766462595074.json, 图片生成/图生图/生图一键四视图白底图Qwen Image 2.1 角色设定批量产出_2109767225895907329.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_333

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1单图编辑任意比例自动化出图_2104683492004159489.json、图片生成/图生图/Qwen Image 2.1单图编辑自动化 指令式改图直出_2104645434831626242.json、图片生成/图生图/Qwen-Image-2.1单图编辑自动出图｜任意比例换背景轻松搞定_2104537166071296002.json、图片生成/图生图/Qwen-Image-2.1单图编辑自动｜角色一致性图生图保持不走样_2104558840414031873.json、图片生成/图生图/Qwen-Image-2.1双海报自动生成｜中英文海报制作 图生图一键出图_2104070766462595074.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `StringFunction|pysssss`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy imageConcat`
- `easy int`
- `easy positive`
- `easy seed`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `easy saveText` —— 4/6 个有
- `AppendStringsToList` —— 1/6 个有
- `ComfySwitchNode` —— 1/6 个有
- `ImageLoader` —— 1/6 个有
- `MemoryCleaner` —— 1/6 个有
- `MultiplePathsInput` —— 1/6 个有
- `PrimitiveBoolean` —— 1/6 个有
- `Qwen3_VQA` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `easy outputToList` —— 1/6 个有

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
