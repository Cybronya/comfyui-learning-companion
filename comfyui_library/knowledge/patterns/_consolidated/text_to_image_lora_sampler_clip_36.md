---
name: text_to_image_lora_sampler_clip_36
type: Text To Image
frequency: 21
level: strong
coverage: 0.88219
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1写实文生图 高质量画面一键直出_2104277798167859202.json, 图片生成/文生图/Qwen Image 2.1写实文生图｜图生图双模式 文生图质感稳定在线_2104101053124931586.json, 图片生成/文生图/Qwen Image 2.1文生图 官方模板，原生2K高清文本到图像方案_2103550536535601154.json, 图片生成/文生图/Qwen Image 2.1文生图25步_2102298549261266945.json, 图片生成/文生图/Qwen Image 2.1文生图25步官流处理生成工具_2102098942266798082.json, 图片生成/文生图/Qwen Image 2.1文生图25步精修版｜提示词直出高质量大片_2103672970286813186.json, 图片生成/文生图/Qwen Image 2.1文生图6步加速无PE工作流，文生图高效文本到图像方案_2107548461108387841.json, 图片生成/文生图/Qwen Image 2.1文生图t2i工作流，7B开源模型2K高清文字渲染方案_2103216666237820930.json, 图片生成/文生图/Qwen Image 2.1文生图上手版｜高质量出图简单易跑_2104575500873191425.json, 图片生成/文生图/Qwen Image 2.1文生图人像写真处理生成工具_2102490947526418434.json, 图片生成/文生图/Qwen Image 2.1文生图处理生成工作流_2102103619591036930.json, 图片生成/文生图/Qwen Image 2.1文生图官方工作流BF16版处理生成工具_2102484931288068098.json, 图片生成/文生图/Qwen Image 2.1文生图提示词增强，原生2K直出高质量文本到图像方案_2105766561448550401.json, 图片生成/文生图/Qwen-Image-2.1 T2I文生图｜人像写真级出图质感｜写实人像一步生成_2102229026680164354.json, 图片生成/文生图/QwenImage2.1 T2I官方提示词助手｜文生图有外挂｜灵感一句话变大片_2102643207380234241.json, 图片生成/文生图/QwenImage2.1文生图加官方提示词助手｜新手也能写好词_2103086483702902786.json, 图片生成/文生图/QwenImage2.1文生图搭配官方提示词助手，T2I自动扩写出图效率提升_2103196536837595138.json, 图片生成/文生图/QwenImage2.1文生图配合官方提示词助手，T2I出图质量与效率兼得_2102841325551972354.json, 视频生成/文生视频/Qwen Image 2.1 T2I文生图人像写真级质感 写实人像一步生成_2104696107367489538.json, 视频生成/文生视频/Qwen-Image-2.1_T2I文生图｜人像写真级出图质感｜写实人像一步生成_2104043820429176833.json, 视频生成/文生视频/QwenImage2.1文生图配合官方提示词助手，T2I出图质量与效率兼得_2105861679325208578.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_36

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1写实文生图 高质量画面一键直出_2104277798167859202.json、图片生成/文生图/Qwen Image 2.1写实文生图｜图生图双模式 文生图质感稳定在线_2104101053124931586.json、图片生成/文生图/Qwen Image 2.1文生图 官方模板，原生2K高清文本到图像方案_2103550536535601154.json、图片生成/文生图/Qwen Image 2.1文生图25步_2102298549261266945.json、图片生成/文生图/Qwen Image 2.1文生图25步官流处理生成工具_2102098942266798082.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 21 个 workflow 都包含：
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
- `孤海注释` —— 18/21 个有
- `PrimitiveStringMultiline` —— 14/21 个有
- `SaveImageAdvanced` —— 12/21 个有
- `TextGenerate` —— 10/21 个有
- `Fast Groups Bypasser (rgthree)` —— 9/21 个有
- `Any Switch (rgthree)` —— 5/21 个有
- `JsonExtractString` —— 5/21 个有
- `ShowAnything|Mie` —— 5/21 个有
- `TextConcatenator` —— 5/21 个有
- `Seed (rgthree)` —— 4/21 个有
- `easy promptList` —— 4/21 个有
- `easy showAnything` —— 4/21 个有
- `EmptyImage` —— 3/21 个有
- `PreviewImage` —— 3/21 个有
- `Text Multiline` —— 3/21 个有
- `easy seed` —— 3/21 个有
- `ModelAttentionBackend` —— 2/21 个有
- `PreviewAny` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 21 | 100% |
| 高度 | 80 | 80 - 80 | 21 | 100% |
| 采样步数 | 4 | 4 - 4 | 21 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 21 | 100% |
| 采样算法 | er_sde | - | 21 | 100% |
| 调度器 | beta | - | 21 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，21 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，21 个样本，一致性 100%
- 调度器 最常用 beta，21 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 高发问题（24/21 个样本）：Steps较低可能导致细节不足
