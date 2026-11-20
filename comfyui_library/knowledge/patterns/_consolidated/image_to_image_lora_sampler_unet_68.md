---
name: image_to_image_lora_sampler_unet_68
type: Image To Image
frequency: 10
level: strong
coverage: 0.8069
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit-多图角度生成器_1990322262794530817.json, 图片生成/图生图/Qwen-Image-Edit-InScene-Annotate_1984575376770940930.json, 图片生成/图生图/Qwen-Image-Edit-InScene_1984569830982500353.json, 图片生成/图生图/Qwen-Image-Edit-InStyle_1984563047832436738.json, 图片生成/图生图/Qwen-Image-Edit-InSubject_1984566159439708162.json, 图片生成/图生图/Qwen-Image-Edit-多角度_1984584360991014913.json, 图片生成/图生图/Qwen-Image-Edit千问转角度镜头转换_1990070283493101570.json, 图片生成/图生图/Qwen-Splat_2068695747394105345.json, 图片生成/图生图/Qwen-多角度切换_1994398890684190721.json, 图片生成/图生图/图像多角度转换——一张角色图生成多角度视角_1984598564712103937.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_68

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit-多图角度生成器_1990322262794530817.json、图片生成/图生图/Qwen-Image-Edit-InScene-Annotate_1984575376770940930.json、图片生成/图生图/Qwen-Image-Edit-InScene_1984569830982500353.json、图片生成/图生图/Qwen-Image-Edit-InStyle_1984563047832436738.json、图片生成/图生图/Qwen-Image-Edit-InSubject_1984566159439708162.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
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
- `easy imageSize` —— 9/10 个有
- `Image Comparer (rgthree)` —— 7/10 个有
- `PreviewImage` —— 7/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `ShowText|pysssss` —— 2/10 个有
- `Text Multiline` —— 2/10 个有
- `easy promptLine` —— 2/10 个有
- `Any Switch (rgthree)` —— 1/10 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/10 个有
- `ImageConcatFromBatch` —— 1/10 个有
- `ImageListToImageBatch` —— 1/10 个有
- `VHS_SelectImages` —— 1/10 个有
- `easy imageListToImageBatch` —— 1/10 个有
- `easy promptList` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 10 | 92% |
| Prompt 约束强度(CFG) | 1 | 0.8 - 1 | 10 | 94% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 0.85 - 1 | 10 | 95% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，10 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.8 - 1，10 个样本，取值集中（一致性 94%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.85 - 1，10 个样本，取值集中（一致性 95%）
- 风险：Prompt 约束强度(CFG) 观测到 0.8，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
