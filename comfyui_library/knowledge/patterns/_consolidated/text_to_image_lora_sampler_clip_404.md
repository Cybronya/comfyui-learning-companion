---
name: text_to_image_lora_sampler_clip_404
type: Text To Image
frequency: 5
level: strong
coverage: 0.9234
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/自动多视图设计表（人物_场景_道具_任意主体）_2089630532681428993.json, 图片生成/图生图/角色四视图-FireRed_2084116890556919810.json, 平台全量/Qwen Image Edit 2511 图像编辑 三图_2004159709529677826.json, 平台全量/Qwen Image Edit 2511 图像编辑 单图_2004161679506186241.json, 平台全量/Qwen Image Edit 2511 图像编辑 双图_2004152823786946562.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_404

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/自动多视图设计表（人物_场景_道具_任意主体）_2089630532681428993.json、图片生成/图生图/角色四视图-FireRed_2084116890556919810.json、平台全量/Qwen Image Edit 2511 图像编辑 三图_2004159709529677826.json、平台全量/Qwen Image Edit 2511 图像编辑 单图_2004161679506186241.json、平台全量/Qwen Image Edit 2511 图像编辑 双图_2004152823786946562.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `JWInteger` —— 4/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `RHLLMChatNode` —— 1/5 个有
- `ResolutionSelector` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 1024 - 1664 | 5 | 78% |
| 高度 | 768 | 768 - 928 | 5 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1664，5 个样本
- 高度 中位数 768，观测区间 768 - 928，5 个样本，取值集中（一致性 92%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
