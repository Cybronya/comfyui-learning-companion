---
name: text_to_image_lora_sampler_clip_57
type: Text To Image
frequency: 14
level: strong
coverage: 0.875929
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1文生图25步_2102298549261266945.json, 图片生成/文生图/Qwen Image 2.1文生图25步官流处理生成工具_2102098942266798082.json, 图片生成/文生图/Qwen Image 2.1文生图25步精修版｜提示词直出高质量大片_2103672970286813186.json, 图片生成/文生图/Qwen Image 2.1文生图6步加速无PE工作流，文生图高效文本到图像方案_2107548461108387841.json, 图片生成/文生图/Qwen Image 2.1文生图t2i工作流，7B开源模型2K高清文字渲染方案_2103216666237820930.json, 图片生成/文生图/Qwen Image 2.1文生图上手版｜高质量出图简单易跑_2104575500873191425.json, 图片生成/文生图/Qwen Image 2.1文生图人像写真处理生成工具_2102490947526418434.json, 图片生成/文生图/Qwen Image 2.1文生图处理生成工具_2102470456296169473.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，高质量文本到图像生成方案_2105772682397700098.json, 图片生成/文生图/Qwen-Image-2.1 T2I文生图｜人像写真级出图质感｜写实人像一步生成_2102229026680164354.json, 图片生成/文生图/qwen image 2.1提示词扩写｜一句话自动扩成专业描述｜文生图更省心_2102239968981770242.json, 视频生成/文生视频/Qwen Image 2.1 T2I文生图人像写真级质感 写实人像一步生成_2104696107367489538.json, 视频生成/文生视频/Qwen-Image-2.1_T2I文生图｜人像写真级出图质感｜写实人像一步生成_2104043820429176833.json, 视频生成/文生视频/qwen_image_2.1提示词扩写｜一句话自动扩成专业描述｜文生图更省心_2102309278647406593.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_57

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1文生图25步_2102298549261266945.json、图片生成/文生图/Qwen Image 2.1文生图25步官流处理生成工具_2102098942266798082.json、图片生成/文生图/Qwen Image 2.1文生图25步精修版｜提示词直出高质量大片_2103672970286813186.json、图片生成/文生图/Qwen Image 2.1文生图6步加速无PE工作流，文生图高效文本到图像方案_2107548461108387841.json、图片生成/文生图/Qwen Image 2.1文生图t2i工作流，7B开源模型2K高清文字渲染方案_2103216666237820930.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 11/14 个有
- `PrimitiveStringMultiline` —— 8/14 个有
- `easy showAnything` —— 8/14 个有
- `TextGenerate` —— 6/14 个有
- `Fast Groups Bypasser (rgthree)` —— 4/14 个有
- `Seed (rgthree)` —— 4/14 个有
- `Text Multiline` —— 4/14 个有
- `easy promptList` —— 4/14 个有
- `EmptyImage` —— 3/14 个有
- `PreviewImage` —— 3/14 个有
- `easy seed` —— 3/14 个有
- `TextGenerateLTX2Prompt` —— 2/14 个有
- `ComfySwitchNode` —— 1/14 个有
- `RH_LLMAPI_Pro_Node` —— 1/14 个有
- `SaveImageAdvanced` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高发问题（17/14 个样本）：Steps较低可能导致细节不足
