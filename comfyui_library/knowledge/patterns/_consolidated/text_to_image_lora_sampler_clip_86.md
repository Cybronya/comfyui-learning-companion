---
name: text_to_image_lora_sampler_clip_86
type: Text To Image
frequency: 14
level: strong
coverage: 0.800357
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1多合一极简版文生图图生图处理工具_2102513018897788929.json, 图片生成/图生图/Qwen Image 2.1多图编辑图生图处理生成工具_2102483334352953345.json, 图片生成/图生图/Qwen Image 2.1官方原版图生图工作流，通义千问7B DiT轻量高效方案_2103198014163742721.json, 图片生成/图生图/Qwen Image 2.1换头换脸Face Swap模特换头加换脸，图生图面部替换_2105790956023926785.json, 图片生成/图生图/Qwen Image 2.1换头换脸Face Swap模特换头加换脸，图生图面部替换工具_2105730994383974402.json, 图片生成/图生图/Qwen Image 2.1换头换脸Face Swap模特换头加换脸，图生图面部替换工具_2106109794053607425.json, 图片生成/图生图/Qwen Image 2.1｜万能输入文生图图生图一体工作流，千问2.1一站式创作_2107281533928300545.json, 图片生成/图生图/Qwen Image2.1角色四视图生成 短剧通用图生图工具_2113679532476682242.json, 图片生成/图生图/Qwen Image2.1角色四视图生成短剧通用 角色设定批量产出_2109794002504601602.json, 图片生成/图生图/qwen-image-2.1多合一极简版｜文生图图生图一页搞定｜界面清爽好用_2102274702399070209.json, 图片生成/图生图/最多10张参考图 Qwen-Image-2.1图像编辑2K输出换装局部重绘_2104274563130548225.json, 图片生成/图生图/最强换装工作流，电商服装展示一键换衣图生图处理工具_2106510801598246914.json, 图片生成/文生图/Qwen Image 2.1万能输入工作流，文生图图生图全场景覆盖处理方案_2107588581916233729.json, 视频生成/图生视频/Qwen_Image_2.1图像生成二十步大合集，全方位图生图能力覆盖_2106178017696505857.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_86

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1多合一极简版文生图图生图处理工具_2102513018897788929.json、图片生成/图生图/Qwen Image 2.1多图编辑图生图处理生成工具_2102483334352953345.json、图片生成/图生图/Qwen Image 2.1官方原版图生图工作流，通义千问7B DiT轻量高效方案_2103198014163742721.json、图片生成/图生图/Qwen Image 2.1换头换脸Face Swap模特换头加换脸，图生图面部替换_2105790956023926785.json、图片生成/图生图/Qwen Image 2.1换头换脸Face Swap模特换头加换脸，图生图面部替换工具_2105730994383974402.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 13/14 个有
- `LoadImage` —— 12/14 个有
- `ComfySwitchNode` —— 10/14 个有
- `CR Prompt Text` —— 9/14 个有
- `TextGenerateLTX2Prompt` —— 9/14 个有
- `GetNode` —— 8/14 个有
- `SetNode` —— 8/14 个有
- `BatchImagesNode` —— 6/14 个有
- `Fast Groups Bypasser (rgthree)` —— 6/14 个有
- `PreviewAny` —— 6/14 个有
- `Seed (rgthree)` —— 5/14 个有
- `Anything Everywhere3` —— 4/14 个有
- `Int` —— 2/14 个有
- `MiniMaxH3EasyMediaLoader` —— 2/14 个有
- `MiniMaxH3EasyMediaSplitter` —— 2/14 个有
- `EmptyImage` —— 1/14 个有
- `Image Comparer (rgthree)` —— 1/14 个有
- `ImageBatchMultiV2` —— 1/14 个有
- `LayerUtility: ImageReel` —— 1/14 个有
- `LayerUtility: ImageReelComposit` —— 1/14 个有
- `PreviewImage` —— 1/14 个有
- `PrimitiveStringMultiline` —— 1/14 个有
- `QwenPERewriteT8` —— 1/14 个有
- `RHLLMChatNode` —— 1/14 个有
- `ShowText|pysssss` —— 1/14 个有
- `easy setNode` —— 1/14 个有
- `easy showAnything` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（15/14 个样本）：Steps较低可能导致细节不足
