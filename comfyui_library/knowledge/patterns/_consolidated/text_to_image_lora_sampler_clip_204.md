---
name: text_to_image_lora_sampler_clip_204
type: Text To Image
frequency: 6
level: strong
coverage: 0.895167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy showAnything, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1文生图处理生成工具_2102545063422283778.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，最强开源模型中文提示词直接出图_2102861587425091586.json, 图片生成/文生图/Qwen Image 2.1文生图标准版｜官方模型直接调用｜出图质量有保障_2102230734147776513.json, 图片生成/文生图/Qwen image 2.1文生图美少女特调｜写实风格出图细腻｜二次元真人两相宜_2102246172638408706.json, 视频生成/文生视频/Qwen_Image_2.1文生图工作流，最强开源模型中文提示词直接出图_2105513820637716482.json, 视频生成/文生视频/Qwen_image_2.1文生图美少女特调｜写实风格出图细腻｜二次元真人两相宜_2104048080306917377.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_204

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1文生图处理生成工具_2102545063422283778.json、图片生成/文生图/Qwen Image 2.1文生图工作流，最强开源模型中文提示词直接出图_2102861587425091586.json、图片生成/文生图/Qwen Image 2.1文生图标准版｜官方模型直接调用｜出图质量有保障_2102230734147776513.json、图片生成/文生图/Qwen image 2.1文生图美少女特调｜写实风格出图细腻｜二次元真人两相宜_2102246172638408706.json、视频生成/文生视频/Qwen_Image_2.1文生图工作流，最强开源模型中文提示词直接出图_2105513820637716482.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 5/6 个有
- `SaveImageAdvanced` —— 5/6 个有
- `孤海注释` —— 4/6 个有
- `EmptyImage` —— 2/6 个有
- `ImpactSwitch` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `Text` —— 2/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `DF_Text_Box` —— 1/6 个有
- `GoohaiRatioAndResolution` —— 1/6 个有
- `easy ifElse` —— 1/6 个有
- `布尔孤海` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
