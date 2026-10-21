---
name: image_to_image_lora_sampler_unet_13
type: Image To Image
frequency: 5
level: strong
coverage: 0.8172
common_nodes: [Anything Everywhere3, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [Text Multiline, CR Prompt List, easy promptLine]
members: [图片生成/图生图/2003652314483335170.json, 图片生成/文生图/1988465961592340482.json, 图片生成/文生图/qwen2509文生图短剧分镜图片_2010143977151930370.json, 图片生成/文生图/视频生成-生成分镜图片_2012090015605596162.json, 图片生成/文生图/视频生成-生成分镜图片多角色_2098296059050160129.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_13

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2003652314483335170.json、图片生成/文生图/1988465961592340482.json、图片生成/文生图/qwen2509文生图短剧分镜图片_2010143977151930370.json、图片生成/文生图/视频生成-生成分镜图片_2012090015605596162.json、图片生成/文生图/视频生成-生成分镜图片多角色_2098296059050160129.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Int` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `CR Prompt List` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `ProcessString` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `Float` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | sa_solver | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、CR Prompt List、easy promptLine
