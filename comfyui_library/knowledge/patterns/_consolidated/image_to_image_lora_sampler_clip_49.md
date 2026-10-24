---
name: image_to_image_lora_sampler_clip_49
type: Image To Image
frequency: 6
level: strong
coverage: 0.800167
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, GetNode, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/klein多图编辑+高清修复_2035621289964081153.json, 图片生成/图生图/klien-多图编辑_2077583346317746178.json, 图片生成/图生图/图像仿色-光影色调迁移_flux2 klein_2050495157325320194.json, 图片生成/图生图/工作流基础系列01-Klein的单图编辑工作流-基础向讲解此工作流_2012461408067260418.json, 图片生成/图生图/模特换装 替换人物与服装  精准版_2085542352353062914.json, 图片生成/图生图/模特换装 替换人物与服装  精准版_2089594684371988481.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_49

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/klein多图编辑+高清修复_2035621289964081153.json、图片生成/图生图/klien-多图编辑_2077583346317746178.json、图片生成/图生图/图像仿色-光影色调迁移_flux2 klein_2050495157325320194.json、图片生成/图生图/工作流基础系列01-Klein的单图编辑工作流-基础向讲解此工作流_2012461408067260418.json、图片生成/图生图/模特换装 替换人物与服装  精准版_2085542352353062914.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `GetNode`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 5/6 个有
- `Image Comparer (rgthree)` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `GetImageSize` —— 4/6 个有
- `LoaderGGUF` —— 4/6 个有
- `easy imageColorMatch` —— 4/6 个有
- `AIO_Preprocessor` —— 3/6 个有
- `Image Padding` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `AILab_QwenVL` —— 1/6 个有
- `ImitationHueNode` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `Seed (rgthree)` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `Text` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 6 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，6 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
