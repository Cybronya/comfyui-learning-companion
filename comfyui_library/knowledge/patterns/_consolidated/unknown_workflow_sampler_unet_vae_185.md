---
name: unknown_workflow_sampler_unet_vae_185
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.909667
common_nodes: [CLIPLoader, GetImageSizeAndCount, KSampler, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SaveImage, StringFunction|pysssss, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy imageConcat, easy int, easy positive, easy saveText, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/生图-一键四视图白底图-Qwen-Image-2.1_2109243233774690306.json, 图片生成/图生图/生图-单图编辑自动(任意比例)-Qwen-Image-2.1_2104140313920102401.json, 图片生成/图生图/生图-单图编辑自动-Qwen-Image-2.1_2104100007581409282.json, 图片生成/图生图/生图-单图编辑自动-Qwen-Image-2.1_2108745864796790785.json, 图片生成/图生图/生图-单图编辑自动-Qwen-Image-2.1_2110190830991532033.json, 图片生成/图生图/生图-图片双海报自动(中英文)-Qwen-Image-2.1_2103796343163678721.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_185

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/生图-一键四视图白底图-Qwen-Image-2.1_2109243233774690306.json、图片生成/图生图/生图-单图编辑自动(任意比例)-Qwen-Image-2.1_2104140313920102401.json、图片生成/图生图/生图-单图编辑自动-Qwen-Image-2.1_2104100007581409282.json、图片生成/图生图/生图-单图编辑自动-Qwen-Image-2.1_2108745864796790785.json、图片生成/图生图/生图-单图编辑自动-Qwen-Image-2.1_2110190830991532033.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `GetImageSizeAndCount`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `easy saveText`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `EmptyLatentImage` —— 2/6 个有
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
| 采样步数 | 40 | 40 - 50 | 6 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 40 - 50，6 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
