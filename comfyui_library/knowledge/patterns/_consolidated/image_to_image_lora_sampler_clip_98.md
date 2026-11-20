---
name: image_to_image_lora_sampler_clip_98
type: Image To Image
frequency: 4
level: strong
coverage: 0.7215
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text Concatenate, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, GetNode, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2老照片修复_2095332872243736577.json, 图片生成/图生图/flux-2-klein全家桶系列-4（ 多角度转换流）_2044609507912851458.json, 图片生成/图生图/图像高清重绘放大   一次性可以多个照片处理（淘宝二十多一张修复照片同款）_2065425282701549570.json, 平台全量/▶3_Flux2Klein-图像高清重绘放大_2063517366482464769.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_98

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux2老照片修复_2095332872243736577.json、图片生成/图生图/flux-2-klein全家桶系列-4（ 多角度转换流）_2044609507912851458.json、图片生成/图生图/图像高清重绘放大   一次性可以多个照片处理（淘宝二十多一张修复照片同款）_2065425282701549570.json、平台全量/▶3_Flux2Klein-图像高清重绘放大_2063517366482464769.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text Concatenate`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `WD14Tagger|pysssss` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `QwenMultiangleCameraNode` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `图像缩放V2_孤海` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 6 | 4 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 6，4 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
