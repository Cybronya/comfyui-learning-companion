---
name: text_to_image_lora_sampler_clip_194
type: Text To Image
frequency: 9
level: strong
coverage: 0.896
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1单图编辑任意比例自动化出图_2104683492004159489.json, 图片生成/图生图/Qwen Image 2.1单图编辑自动化 指令式改图直出_2104645434831626242.json, 图片生成/图生图/Qwen image2.1人像多角度生成 同一角色多姿态批量出图_2104686784390197250.json, 图片生成/图生图/Qwen image2.1人像多角度生成 同一角色多姿态批量出图_2105067914251554817.json, 图片生成/图生图/Qwen image2.1人像多角度生成 同一角色多姿态批量出图_2105446415681024002.json, 图片生成/图生图/Qwen-Image-2.1单图编辑自动出图｜任意比例换背景轻松搞定_2104537166071296002.json, 图片生成/图生图/Qwen-Image-2.1单图编辑自动｜角色一致性图生图保持不走样_2104558840414031873.json, 图片生成/图生图/Qwen-Image-2.1双海报自动生成｜中英文海报制作 图生图一键出图_2104070766462595074.json, 图片生成/图生图/生图一键四视图白底图Qwen Image 2.1 角色设定批量产出_2109767225895907329.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_194

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1单图编辑任意比例自动化出图_2104683492004159489.json、图片生成/图生图/Qwen Image 2.1单图编辑自动化 指令式改图直出_2104645434831626242.json、图片生成/图生图/Qwen image2.1人像多角度生成 同一角色多姿态批量出图_2104686784390197250.json、图片生成/图生图/Qwen image2.1人像多角度生成 同一角色多姿态批量出图_2105067914251554817.json、图片生成/图生图/Qwen image2.1人像多角度生成 同一角色多姿态批量出图_2105446415681024002.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/9 个有
- `GetImageSizeAndCount` —— 6/9 个有
- `StringFunction|pysssss` —— 6/9 个有
- `TextGenerateLTX2Prompt` —— 6/9 个有
- `easy anythingIndexSwitch` —— 6/9 个有
- `easy imageConcat` —— 6/9 个有
- `easy int` —— 6/9 个有
- `easy positive` —— 6/9 个有
- `easy seed` —— 6/9 个有
- `easy saveText` —— 4/9 个有
- `QwenMultiangleCameraNode` —— 3/9 个有
- `easy promptList` —— 3/9 个有
- `AppendStringsToList` —— 1/9 个有
- `ComfySwitchNode` —— 1/9 个有
- `ImageLoader` —— 1/9 个有
- `MemoryCleaner` —— 1/9 个有
- `MultiplePathsInput` —— 1/9 个有
- `PrimitiveBoolean` —— 1/9 个有
- `Qwen3_VQA` —— 1/9 个有
- `RH_LLMAPI_NODE` —— 1/9 个有
- `RH_Translator` —— 1/9 个有
- `easy outputToList` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（12/9 个样本）：Steps较低可能导致细节不足
