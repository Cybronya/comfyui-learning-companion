---
name: text_to_image_sampler_clip_unet_21
type: Text To Image
frequency: 13
level: weak
coverage: 0.897923
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyImage, EmptyLatentImage, GetImageSizeAndCount, ImpactInt, KSampler, SaveImage, SetNode, StringFunction|pysssss, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy int, easy positive, easy saveText, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2文生图｜角色白底图四视图模板直出_2097905354163187713.json, 图片生成/文生图/Qwen-Image-2.1海报自动生成｜文生图海报制作 排版文案一次到位_2104080017062981634.json, 图片生成/文生图/Z_Image文生图自动出图｜零门槛批量产图_2097887803366526978.json, 图片生成/文生图/Z_Image文生图自动工作流｜提示词自动扩写图像生成_2097753067402911745.json, 图片生成/文生图/Z_Image文生图｜角色白底图四视图一键生成_2097886154271051778.json, 图片生成/文生图/生图-文生图(角色白底图)-Z_Image_1994327080177434626.json, 图片生成/文生图/生图-文生图(角色白底图)-Z_Image_base_2016763551209234434.json, 图片生成/文生图/生图-文生图(角色白底图四视图)-Krea2_2097666811994136578.json, 图片生成/文生图/生图-文生图(角色白底图四视图)-Z_Image_2097687828619685889.json, 图片生成/文生图/生图-文生图自动-Krea2_2097666933897392130.json, 图片生成/文生图/生图-文生图自动-Z_Image_1994066603398676481.json, 图片生成/文生图/生图-文生图自动-Z_Image_2066055904258486272.json, 图片生成/文生图/生图-文生图自动-Z_Image_base_2016763491201327106.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_21

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Krea2文生图｜角色白底图四视图模板直出_2097905354163187713.json、图片生成/文生图/Qwen-Image-2.1海报自动生成｜文生图海报制作 排版文案一次到位_2104080017062981634.json、图片生成/文生图/Z_Image文生图自动出图｜零门槛批量产图_2097887803366526978.json、图片生成/文生图/Z_Image文生图自动工作流｜提示词自动扩写图像生成_2097753067402911745.json、图片生成/文生图/Z_Image文生图｜角色白底图四视图一键生成_2097886154271051778.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyImage`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
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
- `GetNode` —— 12/13 个有
- `ConditioningZeroOut` —— 10/13 个有
- `LoraLoaderModelOnly` —— 8/13 个有
- `llama_cpp_instruct_adv` —— 8/13 个有
- `llama_cpp_model_loader` —— 8/13 个有
- `llama_cpp_parameters` —— 8/13 个有
- `MemoryCleaner` —— 7/13 个有
- `easy imageRemBg` —— 6/13 个有
- `JjkText` —— 5/13 个有
- `solarL_SaveImagesToZip` —— 5/13 个有
- `孤海注释` —— 5/13 个有
- `DapaoImageRatioLimitNode` —— 4/13 个有
- `Qwen3VL_Chat` —— 4/13 个有
- `RH_LLMAPI_NODE` —— 4/13 个有
- `ModelSamplingAuraFlow` —— 2/13 个有
- `PreviewImage` —— 2/13 个有
- `TextEncodeQwenImage21` —— 1/13 个有
- `TextGenerateLTX2Prompt` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 35 | 13 | 7% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4.5 | 13 | 38% |
| 采样算法 | euler | - | 13 | 62% |
| 调度器 | simple | - | 13 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 1920 | 80 - 1920 | 13 | 26% |
| 高度 | 1080 | 80 - 1080 | 13 | 30% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 35，13 个样本，取值分散，一致性仅 7%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4.5，13 个样本，取值分散，一致性仅 38%
- 采样算法 最常用 euler，13 个样本，一致性 62%
- 调度器 最常用 simple，13 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，观测区间 80 - 1920，13 个样本，取值分散，一致性仅 26%
- 高度 中位数 1080，观测区间 80 - 1080，13 个样本，取值分散，一致性仅 30%
- 高发问题（12/13 个样本）：Steps较低可能导致细节不足
