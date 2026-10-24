---
name: image_to_image_lora_sampler_unet_92
type: Image To Image
frequency: 7
level: strong
coverage: 0.953286
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-next-scene 一图十五生视角_1992262489524031489.json, 图片生成/图生图/Qwen2509-艺术写真_1992774724711411713.json, 图片生成/图生图/一图生成15视角qwen（姿势控制出图）_1983309779022049281.json, 图片生成/图生图/宝宝写真1119_1991051348286349313.json, 图片生成/图生图/宝宝艺术照写真_1999842319564238850.json, 图片生成/图生图/👉千问2509-一键生成艺术写真 🧁_1992532497875660802.json, 图片生成/图生图/👉千问2509-宝宝艺术写真 🧁_1990324254409453570.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_92

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen-next-scene 一图十五生视角_1992262489524031489.json、图片生成/图生图/Qwen2509-艺术写真_1992774724711411713.json、图片生成/图生图/一图生成15视角qwen（姿势控制出图）_1983309779022049281.json、图片生成/图生图/宝宝写真1119_1991051348286349313.json、图片生成/图生图/宝宝艺术照写真_1999842319564238850.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 5/7 个有
- `ImpactInt` —— 5/7 个有
- `RepeatLatentBatch` —— 5/7 个有
- `SDXLEmptyLatentSizePicker+` —— 5/7 个有
- `CR Text` —— 4/7 个有
- `RH_LLMAPI_NODE` —— 4/7 个有
- `easy showAnything` —— 3/7 个有
- `Note Plus (mtb)` —— 2/7 个有
- `easy anythingIndexSwitch` —— 2/7 个有
- `easy forLoopEnd` —— 2/7 个有
- `easy forLoopStart` —— 2/7 个有
- `PreviewImage` —— 1/7 个有
- `Qwen3VL_Chat` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 832x1216 (0.68) | - | 5 | 80% |
| 高度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 最常用 832x1216 (0.68)，5 个样本，一致性 80%
- 高度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
