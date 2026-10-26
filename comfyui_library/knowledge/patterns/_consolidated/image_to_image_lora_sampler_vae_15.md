---
name: image_to_image_lora_sampler_vae_15
type: Image To Image
frequency: 5
level: strong
coverage: 0.8274
common_nodes: [KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit2511自动分镜_一图多角度_2003774367333007362.json, 图片生成/图生图/QwenRapidAIO自动分镜_2002427270620934145.json, 图片生成/图生图/qwen image edit 2509 智能多分镜_2003308971400298497.json, 图片生成/图生图/（2）WH-手动输入分镜词-人物一致自动分镜控制_2005276694682497026.json, 视频生成/图生视频/Qwen-Edit Next Scene微电影分镜制作（自动分镜）_1983046436193468417.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_15

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/QwenEdit2511自动分镜_一图多角度_2003774367333007362.json、图片生成/图生图/QwenRapidAIO自动分镜_2002427270620934145.json、图片生成/图生图/qwen image edit 2509 智能多分镜_2003308971400298497.json、图片生成/图生图/（2）WH-手动输入分镜词-人物一致自动分镜控制_2005276694682497026.json、视频生成/图生视频/Qwen-Edit Next Scene微电影分镜制作（自动分镜）_1983046436193468417.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 4/5 个有
- `Qwen3_VQA` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `VAELoader` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `easy clearCacheAll` —— 3/5 个有
- `CheckpointLoaderSimple` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `ProcessString` —— 2/5 个有
- `Anything Everywhere` —— 1/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `CR Prompt Text` —— 1/5 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/5 个有
- `JWStringConcat` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 5 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 40% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 40%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（7/5 个样本）：Steps较低可能导致细节不足
