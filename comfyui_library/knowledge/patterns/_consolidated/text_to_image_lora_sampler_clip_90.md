---
name: text_to_image_lora_sampler_clip_90
type: Text To Image
frequency: 14
level: strong
coverage: 0.831714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Moss image 官方文生图｜人像写真二次元两相宜_2112447881939611649.json, 图片生成/文生图/Moss image角色资产生成 真实美感人像写真提示词增强工具_2113037370600808449.json, 图片生成/文生图/Moss-image Base 基础文生图｜轻量快速出图首选_2112407813287931906.json, 图片生成/文生图/Moss-image Base 文生图入门款｜极简参数秒上手_2112420853316153345.json, 图片生成/文生图/Moss-image+Base 文生图带反推｜提示词一键获取_2112453139499667458.json, 图片生成/文生图/Moss-image+Sft 文生图反推版｜反推提示词更准_2112461263623254018.json, 图片生成/文生图/Moss全能生图 多场景文生图高速处理生成工具_2113755415572992001.json, 图片生成/文生图/Qwen Image 2.1全能文生图官方提示词强化处理工具_2102565199348850689.json, 图片生成/文生图/Qwen Image2.1全能文生图 官方提示词强化场景人物生成工具_2113032764122558466.json, 图片生成/文生图/Qwen image 2.1文生图全套｜模型节点下载链接都备齐_2103098595393228801.json, 图片生成/文生图/Qwen image 2.1文生图带模型节点下载链接 新手友好_2104780019913543682.json, 图片生成/文生图/Qwen image 2.1文生图教程版｜附模型和节点下载链接，开箱即用_2104549164205039618.json, 图片生成/文生图/Qwen-Image2.1全能文生图｜官方提示词强化场景人物通吃_2112904831517159425.json, 图片生成/文生图/moss全能生图工作流｜文生图图生图全能覆盖轻松上手_2113504527436574721.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_90

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Moss image 官方文生图｜人像写真二次元两相宜_2112447881939611649.json、图片生成/文生图/Moss image角色资产生成 真实美感人像写真提示词增强工具_2113037370600808449.json、图片生成/文生图/Moss-image Base 基础文生图｜轻量快速出图首选_2112407813287931906.json、图片生成/文生图/Moss-image Base 文生图入门款｜极简参数秒上手_2112420853316153345.json、图片生成/文生图/Moss-image+Base 文生图带反推｜提示词一键获取_2112453139499667458.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `TextGenerate` —— 12/14 个有
- `PreviewAny` —— 11/14 个有
- `Fast Groups Bypasser (rgthree)` —— 10/14 个有
- `Image Comparer (rgthree)` —— 10/14 个有
- `ImageScaleToTotalPixels` —— 10/14 个有
- `SeedVR2LoadDiTModel` —— 10/14 个有
- `SeedVR2LoadVAEModel` —— 10/14 个有
- `SeedVR2VideoUpscaler` —— 10/14 个有
- `ComfySwitchNode` —— 9/14 个有
- `EmptyFlux2LatentImage` —— 8/14 个有
- `RegexExtract` —— 6/14 个有
- `TextEncodeQwenImage21` —— 6/14 个有
- `PreviewImage` —— 5/14 个有
- `PrimitiveBoolean` —— 4/14 个有
- `Any Switch (rgthree)` —— 3/14 个有
- `Seed (rgthree)` —— 3/14 个有
- `ShowAnything|Mie` —— 3/14 个有
- `StringConcatenate` —— 3/14 个有
- `StringFormat` —— 3/14 个有
- `INTConstant` —— 2/14 个有
- `LoadImage` —— 2/14 个有
- `RH_LLMAPI_Pro_Node` —— 2/14 个有
- `SkipLayerGuidanceDiTSimple` —— 2/14 个有

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
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
