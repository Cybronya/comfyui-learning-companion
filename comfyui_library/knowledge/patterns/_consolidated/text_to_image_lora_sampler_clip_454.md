---
name: text_to_image_lora_sampler_clip_454
type: Text To Image
frequency: 4
level: weak
coverage: 0.975
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/中文直出一件多图中文直出一件多图_1919003517552361474.json, 图片生成/文生图/Anima 示例工作流_2055183971406884866.json, 图片生成/文生图/Lisa生成器1.0【含8step+基础】_1985898941021659137.json, 图片生成/文生图/xingtong_base_2037099688356220930.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_454

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/中文直出一件多图中文直出一件多图_1919003517552361474.json、图片生成/文生图/Anima 示例工作流_2055183971406884866.json、图片生成/文生图/Lisa生成器1.0【含8step+基础】_1985898941021659137.json、图片生成/文生图/xingtong_base_2037099688356220930.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `ClipLoaderGGUF` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `Int` —— 1/4 个有
- `Power Lora Loader (rgthree)` —— 1/4 个有
- `TextEncodeQwenImageEdit` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 13 | 8 - 50 | 4 | 20% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 4 | 26% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 25% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 832 | 512 - 1080 | 4 | 75% |
| 高度 | 1088 | 512 - 1920 | 4 | 56% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 13，观测区间 8 - 50，4 个样本，取值分散，一致性仅 20%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，4 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 25%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 832，观测区间 512 - 1080，4 个样本
- 高度 中位数 1088，观测区间 512 - 1920，4 个样本
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
