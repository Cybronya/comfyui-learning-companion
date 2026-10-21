---
name: text_to_image_lora_sampler_clip_162
type: Text To Image
frequency: 7
level: strong
coverage: 0.795571
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), JjkText, JsonExtractString, KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, ResolutionSelector, SaveImage, SaveImageAdvanced, TextConcatenator, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2102637170602364929.json, 图片生成/文生图/QwenImage2.1 T2I官方提示词助手｜文生图有外挂｜灵感一句话变大片_2102643207380234241.json, 图片生成/文生图/QwenImage2.1文生图加官方提示词助手｜新手也能写好词_2103086483702902786.json, 图片生成/文生图/QwenImage2.1文生图搭配官方提示词助手，T2I自动扩写出图效率提升_2103196536837595138.json, 图片生成/文生图/QwenImage2.1文生图配合官方提示词助手，T2I出图质量与效率兼得_2102841325551972354.json, 视频生成/图生视频/QwenImage2.1图生图搭配官方提示词助手，I2I编辑效率大幅提升_2105866245517168642.json, 视频生成/文生视频/QwenImage2.1文生图配合官方提示词助手，T2I出图质量与效率兼得_2105861679325208578.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_162

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/2102637170602364929.json、图片生成/文生图/QwenImage2.1 T2I官方提示词助手｜文生图有外挂｜灵感一句话变大片_2102643207380234241.json、图片生成/文生图/QwenImage2.1文生图加官方提示词助手｜新手也能写好词_2103086483702902786.json、图片生成/文生图/QwenImage2.1文生图搭配官方提示词助手，T2I自动扩写出图效率提升_2103196536837595138.json、图片生成/文生图/QwenImage2.1文生图配合官方提示词助手，T2I出图质量与效率兼得_2102841325551972354.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `JjkText`
- `JsonExtractString`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `SaveImageAdvanced`
- `TextConcatenator`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ShowAnything|Mie` —— 5/7 个有
- `孤海注释` —— 5/7 个有
- `ComfySwitchNode` —— 2/7 个有
- `GetNode` —— 2/7 个有
- `ImageBatchMulti` —— 2/7 个有
- `ImageScaleToTotalPixels` —— 2/7 个有
- `LoadImage` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `QwenImage21Cache` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `EmptyImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
