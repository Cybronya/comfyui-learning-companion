---
name: image_to_image_lora_sampler_unet_160
type: Image To Image
frequency: 4
level: strong
coverage: 0.639
common_nodes: [CLIPLoader, CR Prompt Text, KSampler, LoadImage, LoraLoaderModelOnly, ProcessString, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen-2511多角度批量生图_2031310962111811586.json, 图片生成/图生图/图片无限素材流 — 支持多分镜 _ 多角度 _ 多场景_1993296418674769922.json, 图片生成/图生图/应用级：写真写意+多角度，千问编辑模型，和风整理。_2008029412943466498.json, 图片生成/图生图/最强分镜_2015319873622122498.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_160

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/qwen-2511多角度批量生图_2031310962111811586.json、图片生成/图生图/图片无限素材流 — 支持多分镜 _ 多角度 _ 多场景_1993296418674769922.json、图片生成/图生图/应用级：写真写意+多角度，千问编辑模型，和风整理。_2008029412943466498.json、图片生成/图生图/最强分镜_2015319873622122498.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ProcessString`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `TextEncodeQwenImageEditPlus` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `Int` —— 2/4 个有
- `JWStringConcat` —— 2/4 个有
- `Qwen3_VQA` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `ReferenceLatent` —— 1/4 个有
- `TextEncodeQwenImageEdit` —— 1/4 个有
- `图像缩放V2_孤海` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 4 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
