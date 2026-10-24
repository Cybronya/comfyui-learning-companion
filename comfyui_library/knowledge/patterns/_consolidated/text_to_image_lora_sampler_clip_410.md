---
name: text_to_image_lora_sampler_clip_410
type: Text To Image
frequency: 4
level: strong
coverage: 0.81325
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1多合一极简版文生图图生图处理工具_2102513018897788929.json, 图片生成/图生图/Qwen Image 2.1文生图处理生成工具_2102563638816104449.json, 图片生成/图生图/Qwen Image2.1角色四视图生成短剧通用 角色设定批量产出_2109794002504601602.json, 图片生成/图生图/qwen-image-2.1多合一极简版｜文生图图生图一页搞定｜界面清爽好用_2102274702399070209.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_410

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1多合一极简版文生图图生图处理工具_2102513018897788929.json、图片生成/图生图/Qwen Image 2.1文生图处理生成工具_2102563638816104449.json、图片生成/图生图/Qwen Image2.1角色四视图生成短剧通用 角色设定批量产出_2109794002504601602.json、图片生成/图生图/qwen-image-2.1多合一极简版｜文生图图生图一页搞定｜界面清爽好用_2102274702399070209.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `QwenImage21Cache` —— 3/4 个有
- `Seed (rgthree)` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `MiniMaxH3EasyMediaLoader` —— 2/4 个有
- `MiniMaxH3EasyMediaSplitter` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `ImageBatchMultiV2` —— 1/4 个有
- `Int` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `QwenPERewriteT8` —— 1/4 个有
- `SaveImageAdvanced` —— 1/4 个有
- `TextGenerateLTX2Prompt` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
