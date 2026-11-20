---
name: text_to_image_upscale_lora_sampler_27
type: Text To Image
frequency: 9
level: weak
coverage: 0.823222
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS Image 文生图（8步加速_50步复杂文字）(带模型和lora下载链接)_2112068613405499394.json, 图片生成/文生图/MOSS Image 文生图｜8步加速+50步复杂文字附模型lora_2112403092594585601.json, 图片生成/文生图/Moss image 官方文生图｜人像写真二次元两相宜_2112447881939611649.json, 图片生成/文生图/Moss image角色资产生成 真实美感人像写真提示词增强工具_2113037370600808449.json, 图片生成/文生图/Moss全能生图 多场景文生图高速处理生成工具_2113755415572992001.json, 图片生成/文生图/Qwen image 2.1文生图全套｜模型节点下载链接都备齐_2103098595393228801.json, 图片生成/文生图/Qwen image 2.1文生图带模型节点下载链接 新手友好_2104780019913543682.json, 图片生成/文生图/Qwen image 2.1文生图教程版｜附模型和节点下载链接，开箱即用_2104549164205039618.json, 图片生成/文生图/moss全能生图工作流｜文生图图生图全能覆盖轻松上手_2113504527436574721.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_27

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/MOSS Image 文生图（8步加速_50步复杂文字）(带模型和lora下载链接)_2112068613405499394.json、图片生成/文生图/MOSS Image 文生图｜8步加速+50步复杂文字附模型lora_2112403092594585601.json、图片生成/文生图/Moss image 官方文生图｜人像写真二次元两相宜_2112447881939611649.json、图片生成/文生图/Moss image角色资产生成 真实美感人像写真提示词增强工具_2113037370600808449.json、图片生成/文生图/Moss全能生图 多场景文生图高速处理生成工具_2113755415572992001.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 8/9 个有
- `solarL_SaveImagesToZip` —— 8/9 个有
- `孤海注释` —— 8/9 个有
- `Image Comparer (rgthree)` —— 7/9 个有
- `PreviewAny` —— 7/9 个有
- `PreviewImage` —— 7/9 个有
- `PrimitiveStringMultiline` —— 7/9 个有
- `Any Switch (rgthree)` —— 5/9 个有
- `Seed (rgthree)` —— 5/9 个有
- `TextGenerate` —— 5/9 个有
- `EmptyFlux2LatentImage` —— 4/9 个有
- `RegexExtract` —— 3/9 个有
- `StringConcatenate` —— 3/9 个有
- `TextEncodeQwenImage21` —— 3/9 个有
- `ComfySwitchNode` —— 2/9 个有
- `INTConstant` —— 2/9 个有
- `LoadImage` —— 2/9 个有
- `RH_LLMAPI_Pro_Node` —— 2/9 个有
- `SkipLayerGuidanceDiTSimple` —— 2/9 个有
- `VOSR2ModelLoader` —— 2/9 个有
- `VOSR2Upscale` —— 2/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 9 | 0% |
| 高度 | 80 | 80 - 1024 | 9 | 0% |
| 采样步数 | 4 | 4 - 8 | 9 | 72% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 9 | 73% |
| 采样算法 | er_sde | - | 9 | 89% |
| 调度器 | beta | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，9 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，9 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，9 个样本
- 采样算法 最常用 er_sde，9 个样本，一致性 89%
- 调度器 最常用 beta，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足
