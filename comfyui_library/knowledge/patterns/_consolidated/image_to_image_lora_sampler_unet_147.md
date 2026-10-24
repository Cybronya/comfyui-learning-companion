---
name: image_to_image_lora_sampler_unet_147
type: Image To Image
frequency: 4
level: strong
coverage: 0.63475
common_nodes: [Any Switch (rgthree), CLIPLoader, CR SDXL Aspect Ratio, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit 图像风格转换_1957998910599999490.json, 图片生成/图生图/[🛫书墨]Qwen-Edit千问编辑（支持单图、双图、自定义尺寸切换）_1957836065800552450.json, 图片生成/图生图/小红书全能编辑模型FireRed-Image-edit1.0_2026605916237336577.json, 图片生成/图生图/皮克斯风格4格漫画_分镜工作流_1961249449370697729.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_147

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit 图像风格转换_1957998910599999490.json、图片生成/图生图/[🛫书墨]Qwen-Edit千问编辑（支持单图、双图、自定义尺寸切换）_1957836065800552450.json、图片生成/图生图/小红书全能编辑模型FireRed-Image-edit1.0_2026605916237336577.json、图片生成/图生图/皮克斯风格4格漫画_分镜工作流_1961249449370697729.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CR SDXL Aspect Ratio`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 3/4 个有
- `FluxKontextImageScale` —— 3/4 个有
- `ImageConcatMulti` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `TextEncodeQwenImageEdit` —— 3/4 个有
- `GetNode` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `TextEncodeQwenImageEditPlus` —— 1/4 个有
- `easy int` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 0.9 | 0.9 - 1 | 4 | 95% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 0.9，观测区间 0.9 - 1，4 个样本，取值集中（一致性 95%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.9，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（7/4 个样本）：Steps较低可能导致细节不足
