---
name: image_to_image_lora_sampler_unet_192
type: Image To Image
frequency: 3
level: strong
coverage: 0.891
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/色块生成光源_2050877939109113858.json, 图片生成/图生图/角色转渲染2D手办_2051226037320724481.json, 视频生成/图生视频/定点溶图_2055994336172625922.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_192

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/色块生成光源_2050877939109113858.json、图片生成/图生图/角色转渲染2D手办_2051226037320724481.json、视频生成/图生视频/定点溶图_2055994336172625922.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 2/3 个有
- `CLIPTextEncode` —— 2/3 个有
- `FastCanvas` —— 2/3 个有
- `FastCanvasTool` —— 2/3 个有
- `FluxKontextImageScale` —— 2/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `EmptyImage` —— 1/3 个有
- `LayerColor: RGB` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RMBG` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
