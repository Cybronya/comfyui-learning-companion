---
name: text_to_image_lora_sampler_clip_329
type: Text To Image
frequency: 6
level: strong
coverage: 0.826833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1多合一极简版文生图图生图处理工具_2102513018897788929.json, 图片生成/图生图/Qwen Image 2.1文生图处理生成工具_2102563638816104449.json, 图片生成/图生图/qwen-image-2.1多合一极简版｜文生图图生图一页搞定｜界面清爽好用_2102274702399070209.json, 图片生成/图生图/千问2.1多图像编辑工作流｜提示词自动优化省心出图_2103724810600804354.json, 数字人/数字人/Qwen 2.1透明背景抠图，一键生成PNG透明图生图工具_2102899365059846146.json, 视频生成/图生视频/Qwen_2.1透明背景抠图，一键生成PNG透明图生图工具_2104737318635659265.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_329

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1多合一极简版文生图图生图处理工具_2102513018897788929.json、图片生成/图生图/Qwen Image 2.1文生图处理生成工具_2102563638816104449.json、图片生成/图生图/qwen-image-2.1多合一极简版｜文生图图生图一页搞定｜界面清爽好用_2102274702399070209.json、图片生成/图生图/千问2.1多图像编辑工作流｜提示词自动优化省心出图_2103724810600804354.json、数字人/数字人/Qwen 2.1透明背景抠图，一键生成PNG透明图生图工具_2102899365059846146.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
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
- `QwenImage21Cache` —— 5/6 个有
- `孤海注释` —— 5/6 个有
- `GetNode` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `FastGroupsBypassSwitch` —— 3/6 个有
- `LoadImage` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `MiniMaxH3EasyMediaLoader` —— 2/6 个有
- `MiniMaxH3EasyMediaSplitter` —— 2/6 个有
- `PreviewAny` —— 2/6 个有
- `QwenPERewriteT8` —— 2/6 个有
- `Seed (rgthree)` —— 2/6 个有
- `TextCombinerTwo` —— 2/6 个有
- `EmptyImage` —— 1/6 个有
- `ImageBatchMultiV2` —— 1/6 个有
- `SaveImageAdvanced` —— 1/6 个有
- `TextGenerateLTX2Prompt` —— 1/6 个有

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
