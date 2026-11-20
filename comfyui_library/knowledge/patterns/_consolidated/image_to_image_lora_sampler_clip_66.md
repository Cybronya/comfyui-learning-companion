---
name: image_to_image_lora_sampler_clip_66
type: Image To Image
frequency: 4
level: strong
coverage: 0.77875
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2老照片修复_2095332872243736577.json, 图片生成/图生图/klein放大+一致性编辑流_2035255613680259073.json, 图片生成/图生图/图像高清重绘放大   一次性可以多个照片处理（淘宝二十多一张修复照片同款）_2065425282701549570.json, 图片生成/图生图/工作流基础系列01-Klein的单图编辑工作流-基础向讲解此工作流_2012461408067260418.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_66

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux2老照片修复_2095332872243736577.json、图片生成/图生图/klein放大+一致性编辑流_2035255613680259073.json、图片生成/图生图/图像高清重绘放大   一次性可以多个照片处理（淘宝二十多一张修复照片同款）_2065425282701549570.json、图片生成/图生图/工作流基础系列01-Klein的单图编辑工作流-基础向讲解此工作流_2012461408067260418.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `CR Text Concatenate` —— 3/4 个有
- `ColorMatch` —— 3/4 个有
- `GetImageSize` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `WD14Tagger|pysssss` —— 3/4 个有
- `CFGGuider` —— 2/4 个有
- `Flux2Scheduler` —— 2/4 个有
- `KSamplerSelect` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `RandomNoise` —— 2/4 个有
- `SamplerCustomAdvanced` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `孤海注释` —— 2/4 个有
- `DrawMaskOnImage` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `Text` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5.5 | 5 - 6 | 4 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5.5，观测区间 5 - 6，4 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
