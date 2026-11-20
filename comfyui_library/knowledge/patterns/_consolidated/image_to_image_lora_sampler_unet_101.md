---
name: image_to_image_lora_sampler_unet_101
type: Image To Image
frequency: 6
level: strong
coverage: 0.5945
common_nodes: [Any Switch (rgthree), CFGNorm, CLIPLoader, Fast Groups Bypasser (rgthree), GetNode, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed 1.1 海报文字渲染 参考图生艺术字_2029383175213948929.json, 图片生成/图生图/FireRed 1.1 自动化妆美颜-超强一致性_2029381063323160577.json, 图片生成/图生图/FireRed Image-Eidt  4步加速Lora 小红书图像编辑模型_2025955278805540865.json, 图片生成/图生图/FireRed Image-Eidt 1.1 8步加速Lora 小红书图像编辑模型_2029213158472159233.json, 图片生成/图生图/Qwen-Image多视角图像生成，强一致性！！_1975747642506522626.json, 图片生成/文生图/2029840730553847809.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_101

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/FireRed 1.1 海报文字渲染 参考图生艺术字_2029383175213948929.json、图片生成/图生图/FireRed 1.1 自动化妆美颜-超强一致性_2029381063323160577.json、图片生成/图生图/FireRed Image-Eidt  4步加速Lora 小红书图像编辑模型_2025955278805540865.json、图片生成/图生图/FireRed Image-Eidt 1.1 8步加速Lora 小红书图像编辑模型_2029213158472159233.json、图片生成/图生图/Qwen-Image多视角图像生成，强一致性！！_1975747642506522626.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 6 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AspectRatio` —— 5/6 个有
- `EmptySD3LatentImage` —— 5/6 个有
- `Image Comparer (rgthree)` —— 5/6 个有
- `JjkText` —— 5/6 个有
- `ImageResize+` —— 4/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `AlphaChanelRemove` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/6 个有
- `NunchakuQwenImageDiTLoader` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `ZML_AddSolidColorBackground` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 6 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，6 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
