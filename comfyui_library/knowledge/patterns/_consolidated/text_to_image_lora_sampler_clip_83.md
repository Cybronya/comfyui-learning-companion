---
name: text_to_image_lora_sampler_clip_83
type: Text To Image
frequency: 10
level: strong
coverage: 0.8863
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1文生图25步_2102298549261266945.json, 图片生成/文生图/Qwen Image 2.1文生图25步精修版｜提示词直出高质量大片_2103672970286813186.json, 图片生成/文生图/Qwen Image 2.1文生图t2i工作流，7B开源模型2K高清文字渲染方案_2103216666237820930.json, 图片生成/文生图/Qwen Image 2.1文生图上手版｜高质量出图简单易跑_2104575500873191425.json, 图片生成/文生图/Qwen Image 2.1文生图加4步加速，高质量文本到图像生成工作流_2103932568507863042.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，最强开源模型中文提示词直接出图_2102861587425091586.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，高质量文本到图像生成方案_2105772682397700098.json, 视频生成/文生视频/Qwen_Image_2.1文生图工作流，最强开源模型中文提示词直接出图_2105513820637716482.json, 视频生成/文生视频/Qwen_image_2.1文生图美少女特调｜写实风格出图细腻｜二次元真人两相宜_2104048080306917377.json, 视频生成/文生视频/qwen_image_2.1提示词扩写｜一句话自动扩成专业描述｜文生图更省心_2102309278647406593.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_83

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1文生图25步_2102298549261266945.json、图片生成/文生图/Qwen Image 2.1文生图25步精修版｜提示词直出高质量大片_2103672970286813186.json、图片生成/文生图/Qwen Image 2.1文生图t2i工作流，7B开源模型2K高清文字渲染方案_2103216666237820930.json、图片生成/文生图/Qwen Image 2.1文生图上手版｜高质量出图简单易跑_2104575500873191425.json、图片生成/文生图/Qwen Image 2.1文生图加4步加速，高质量文本到图像生成工作流_2103932568507863042.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 9/10 个有
- `TextEncodeQwenImage21` —— 9/10 个有
- `孤海注释` —— 6/10 个有
- `SaveImageAdvanced` —— 5/10 个有
- `easy showAnything` —— 5/10 个有
- `PreviewImage` —— 4/10 个有
- `TextGenerateLTX2Prompt` —— 4/10 个有
- `EmptyImage` —— 3/10 个有
- `ImpactSwitch` —— 2/10 个有
- `PrimitiveStringMultiline` —— 2/10 个有
- `Text` —— 2/10 个有
- `Text Multiline` —— 2/10 个有
- `easy seed` —— 2/10 个有
- `ConditioningZeroOut` —— 1/10 个有
- `ModelAttentionBackend` —— 1/10 个有
- `TextGenerate` —— 1/10 个有

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
| Steps较低可能导致细节不足 | 12/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（12/10 个样本）：Steps较低可能导致细节不足
