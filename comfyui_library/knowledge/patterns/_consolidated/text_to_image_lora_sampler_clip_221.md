---
name: text_to_image_lora_sampler_clip_221
type: Text To Image
frequency: 9
level: strong
coverage: 0.875889
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1文生图处理生成工具_2102545063422283778.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，高质量文本到图像生成方案_2105772682397700098.json, 图片生成/文生图/Qwen Image 2.1文生图标准版｜一句话生成好图｜写实插画都能驾驭_2102638633646907393.json, 图片生成/文生图/Qwen Image 2.1文生图标准版｜官方模型直接调用｜出图质量有保障_2102230734147776513.json, 图片生成/文生图/Qwen image 2.1 turbo文生图 高质量画面稳定直出_2110355293870837762.json, 图片生成/文生图/Qwen image 2.1 turbo文生图｜画质优化LoRA加持_2112451573052952578.json, 图片生成/文生图/qwen image 2.1 rurbo文生图，高清创意直出_2111281294968709122.json, 图片生成/文生图/qwen image 2.1 rurbo文生图，高清创意直出_2111954037758316546.json, 图片生成/文生图/（文生图）qwen image 2.1 rurbo，高清创意直出_2111591580015620098.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_221

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1文生图处理生成工具_2102545063422283778.json、图片生成/文生图/Qwen Image 2.1文生图工作流，高质量文本到图像生成方案_2105772682397700098.json、图片生成/文生图/Qwen Image 2.1文生图标准版｜一句话生成好图｜写实插画都能驾驭_2102638633646907393.json、图片生成/文生图/Qwen Image 2.1文生图标准版｜官方模型直接调用｜出图质量有保障_2102230734147776513.json、图片生成/文生图/Qwen image 2.1 turbo文生图 高质量画面稳定直出_2110355293870837762.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
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
- `ResolutionSelector` —— 8/9 个有
- `TextGenerateLTX2Prompt` —— 8/9 个有
- `easy showAnything` —— 8/9 个有
- `PrimitiveStringMultiline` —— 6/9 个有
- `KSamplerSelect` —— 5/9 个有
- `ManualSigmas` —— 5/9 个有
- `SamplerCustom` —— 5/9 个有
- `SaveImageAdvanced` —— 3/9 个有
- `CR Text Concatenate` —— 1/9 个有
- `DF_Text_Box` —— 1/9 个有
- `GoohaiRatioAndResolution` —— 1/9 个有
- `easy ifElse` —— 1/9 个有
- `布尔孤海` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足
