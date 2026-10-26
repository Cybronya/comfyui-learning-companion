---
name: text_to_image_lora_sampler_clip_178
type: Text To Image
frequency: 10
level: strong
coverage: 0.8419
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/QwenImage2.1 T2I官方提示词助手｜文生图有外挂｜灵感一句话变大片_2102643207380234241.json, 图片生成/文生图/QwenImage2.1文生图加官方提示词助手｜新手也能写好词_2103086483702902786.json, 图片生成/文生图/QwenImage2.1文生图搭配官方提示词助手，T2I自动扩写出图效率提升_2103196536837595138.json, 图片生成/文生图/QwenImage2.1文生图配合官方提示词助手，T2I出图质量与效率兼得_2102841325551972354.json, 图片生成/文生图/qwen image 2.1 turbo大模型基础文生图 高质量画面直出_2109726501351542786.json, 图片生成/文生图/qwen image 2.1官方turbo加速lora文生图基础流 高质量画面直出_2109727981399797762.json, 图片生成/文生图/qwen image 2.1提示词扩写｜一句话自动扩成专业描述｜文生图更省心_2102239968981770242.json, 图片生成/文生图/通用QwenImage2.1文生图图生图二合一｜日常出图万能底座_2111282466421035009.json, 图片生成/文生图/通用QwenImage2.1方案，文生图图生图一站搞定_2111525886070706178.json, 视频生成/文生视频/QwenImage2.1文生图配合官方提示词助手，T2I出图质量与效率兼得_2105861679325208578.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_178

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/QwenImage2.1 T2I官方提示词助手｜文生图有外挂｜灵感一句话变大片_2102643207380234241.json、图片生成/文生图/QwenImage2.1文生图加官方提示词助手｜新手也能写好词_2103086483702902786.json、图片生成/文生图/QwenImage2.1文生图搭配官方提示词助手，T2I自动扩写出图效率提升_2103196536837595138.json、图片生成/文生图/QwenImage2.1文生图配合官方提示词助手，T2I出图质量与效率兼得_2102841325551972354.json、图片生成/文生图/qwen image 2.1 turbo大模型基础文生图 高质量画面直出_2109726501351542786.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：84%

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

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 9/10 个有
- `PrimitiveStringMultiline` —— 8/10 个有
- `ResolutionSelector` —— 8/10 个有
- `TextGenerate` —— 8/10 个有
- `Any Switch (rgthree)` —— 7/10 个有
- `JsonExtractString` —— 7/10 个有
- `TextConcatenator` —— 7/10 个有
- `Fast Groups Bypasser (rgthree)` —— 5/10 个有
- `SaveImageAdvanced` —— 5/10 个有
- `ShowAnything|Mie` —— 5/10 个有
- `easy showAnything` —— 3/10 个有
- `ComfySwitchNode` —— 2/10 个有
- `LoadImage` —— 2/10 个有
- `QwenImage21Cache` —— 2/10 个有
- `easy isNone` —— 2/10 个有
- `EmptyImage` —— 1/10 个有
- `PreviewImage` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（12/10 个样本）：Steps较低可能导致细节不足
