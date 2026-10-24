---
name: text_to_image_lora_sampler_clip_226
type: Text To Image
frequency: 8
level: strong
coverage: 0.74925
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyImage, EmptyLatentImage, GetImageSizeAndCount, ImpactInt, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, SetNode, StringFunction|pysssss, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy int, easy positive, easy saveText, easy seed, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1任意数量编辑融合 5图以内多图合一自动出图_2104651655982706689.json, 图片生成/图生图/Qwen-Image-2.1任意数量编辑融合｜5图以内自动合成，分镜出图_2104573949622448130.json, 图片生成/图生图/Qwen-Image-2.1多宫格自动编辑｜5图以内任意数量，分镜生成出图_2104565032179818497.json, 图片生成/文生图/Krea2文生图｜角色白底图四视图模板直出_2097905354163187713.json, 图片生成/文生图/Qwen-Image-2.1海报自动生成｜文生图海报制作 排版文案一次到位_2104080017062981634.json, 图片生成/文生图/Z_Image文生图自动出图｜零门槛批量产图_2097887803366526978.json, 图片生成/文生图/Z_Image文生图自动工作流｜提示词自动扩写图像生成_2097753067402911745.json, 图片生成/文生图/Z_Image文生图｜角色白底图四视图一键生成_2097886154271051778.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_226

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1任意数量编辑融合 5图以内多图合一自动出图_2104651655982706689.json、图片生成/图生图/Qwen-Image-2.1任意数量编辑融合｜5图以内自动合成，分镜出图_2104573949622448130.json、图片生成/图生图/Qwen-Image-2.1多宫格自动编辑｜5图以内任意数量，分镜生成出图_2104565032179818497.json、图片生成/文生图/Krea2文生图｜角色白底图四视图模板直出_2097905354163187713.json、图片生成/文生图/Qwen-Image-2.1海报自动生成｜文生图海报制作 排版文案一次到位_2104080017062981634.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyImage`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `ImpactInt`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SetNode`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy int`
- `easy positive`
- `easy saveText`
- `easy seed`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 7/8 个有
- `llama_cpp_instruct_adv` —— 7/8 个有
- `llama_cpp_model_loader` —— 7/8 个有
- `llama_cpp_parameters` —— 7/8 个有
- `MemoryCleaner` —— 5/8 个有
- `Text Multiline` —— 5/8 个有
- `ConditioningZeroOut` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `TextEncodeQwenImage21` —— 4/8 个有
- `TextGenerateLTX2Prompt` —— 4/8 个有
- `CM_IntUnaryOperation` —— 3/8 个有
- `ImageBatchMulti` —— 3/8 个有
- `ImageLoader` —— 3/8 个有
- `ImageScaleToTotalPixels` —— 3/8 个有
- `SimpleMath+` —— 3/8 个有
- `easy anythingInversedSwitch` —— 3/8 个有
- `DapaoImageRatioLimitNode` —— 2/8 个有
- `easy imageRemBg` —— 2/8 个有
- `RH_LLMAPI_NODE` —— 1/8 个有
- `ResolutionSelector` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（11/8 个样本）：Steps较低可能导致细节不足
