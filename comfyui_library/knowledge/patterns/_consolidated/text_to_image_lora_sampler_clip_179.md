---
name: text_to_image_lora_sampler_clip_179
type: Text To Image
frequency: 10
level: strong
coverage: 0.8647
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen image 2.1文生图，高清创意形象快速生成_2110841563134914562.json, 图片生成/文生图/Qwen image 2.1文生图｜简洁高效直出高质量画面_2110710655673266177.json, 图片生成/文生图/Qwen-Image-2.1-Turbo汉服美学写真｜一键国风服装展示文生图_2111051887217827841.json, 图片生成/文生图/qwen image 2.1 turbo大模型基础文生图 高质量画面直出_2109726501351542786.json, 图片生成/文生图/qwen image 2.1官方turbo加速lora文生图基础流 高质量画面直出_2109727981399797762.json, 图片生成/文生图/qwen image 2.1提示词扩写｜一句话自动扩成专业描述｜文生图更省心_2102239968981770242.json, 图片生成/文生图/qwen2.1文生图基础工作流 新手友好稳定出图_2104664392800489473.json, 图片生成/文生图/qwen2.1文生图基础工作流 新手友好稳定出图_2105070911778021377.json, 图片生成/文生图/通用QwenImage2.1文生图图生图二合一｜日常出图万能底座_2111282466421035009.json, 图片生成/文生图/通用QwenImage2.1方案，文生图图生图一站搞定_2111525886070706178.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_179

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Qwen image 2.1文生图，高清创意形象快速生成_2110841563134914562.json、图片生成/文生图/Qwen image 2.1文生图｜简洁高效直出高质量画面_2110710655673266177.json、图片生成/文生图/Qwen-Image-2.1-Turbo汉服美学写真｜一键国风服装展示文生图_2111051887217827841.json、图片生成/文生图/qwen image 2.1 turbo大模型基础文生图 高质量画面直出_2109726501351542786.json、图片生成/文生图/qwen image 2.1官方turbo加速lora文生图基础流 高质量画面直出_2109727981399797762.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 7/10 个有
- `ResolutionSelector` —— 6/10 个有
- `ComfySwitchNode` —— 5/10 个有
- `easy showAnything` —— 5/10 个有
- `PrimitiveStringMultiline` —— 3/10 个有
- `TextGenerate` —— 3/10 个有
- `Any Switch (rgthree)` —— 2/10 个有
- `CR Text` —— 2/10 个有
- `EmptySD3LatentImage` —— 2/10 个有
- `JsonExtractString` —— 2/10 个有
- `LoadImage` —— 2/10 个有
- `TextConcatenator` —— 2/10 个有
- `TextGenerateLTX2Prompt` —— 2/10 个有
- `easy isNone` —— 2/10 个有
- `CR Prompt Text` —— 1/10 个有
- `Color Grading JK` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（14/10 个样本）：Steps较低可能导致细节不足
