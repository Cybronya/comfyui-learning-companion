---
name: image_to_image_lora_sampler_unet_81
type: Image To Image
frequency: 7
level: strong
coverage: 0.925857
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/002.Qwen编辑之王003.单图编辑_2034486910499954689.json, 图片生成/图生图/002.Qwen编辑之王019.单图多视角_2034824618657193985.json, 图片生成/图生图/0像素偏移基准版和非基准版_2042496356362752001.json, 图片生成/图生图/2511人物变瘦工作流_2004064077204889602.json, 图片生成/图生图/2511饰品多角度摆放+机位（5个）_2094745463726624770.json, 图片生成/图生图/5.其他类型-6.NSF+-08.Qwen_2511生图001.QW2511单图编辑.json_2021976908983963649.json, 图片生成/图生图/5.其他类型-6.NSF+-08.Qwen_2511生图003.QW2511单图多视角.json_2021976973089710082.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_81

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/002.Qwen编辑之王003.单图编辑_2034486910499954689.json、图片生成/图生图/002.Qwen编辑之王019.单图多视角_2034824618657193985.json、图片生成/图生图/0像素偏移基准版和非基准版_2042496356362752001.json、图片生成/图生图/2511人物变瘦工作流_2004064077204889602.json、图片生成/图生图/2511饰品多角度摆放+机位（5个）_2094745463726624770.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `easy cleanGpuUsed` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `Image Comparer (rgthree)` —— 4/7 个有
- `CR Prompt List` —— 2/7 个有
- `ModelSamplingAuraFlow` —— 2/7 个有
- `PathchSageAttentionKJ` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `String Literal` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `ImageBatch` —— 1/7 个有
- `孤海图像缩放按像素` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler_ancestral | - | 7 | 71% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（12/7 个样本）：Steps较低可能导致细节不足
