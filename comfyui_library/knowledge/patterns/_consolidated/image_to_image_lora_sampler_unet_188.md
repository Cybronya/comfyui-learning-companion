---
name: image_to_image_lora_sampler_unet_188
type: Image To Image
frequency: 4
level: strong
coverage: 0.85475
common_nodes: [CFGNorm, CLIPLoader, Display Any (rgthree), ImageScaleToTotalPixels, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy anythingIndexSwitch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问Edit2509图像编辑三图版_1972125442494885889.json, 图片生成/图生图/千问Edit2509图像编辑单图版_1972125938593034241.json, 图片生成/图生图/千问Edit2509图像编辑双图版_1972837097528860674.json, 图片生成/图生图/千问Edit2509图像编辑姿势迁移版_1972903574260879362.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_188

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/千问Edit2509图像编辑三图版_1972125442494885889.json、图片生成/图生图/千问Edit2509图像编辑单图版_1972125938593034241.json、图片生成/图生图/千问Edit2509图像编辑双图版_1972837097528860674.json、图片生成/图生图/千问Edit2509图像编辑姿势迁移版_1972903574260879362.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Display Any (rgthree)`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy anythingIndexSwitch`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 3/4 个有
- `RH_LLMAPI_NODE` —— 3/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImitationHueNode` —— 1/4 个有
- `LayerUtility: ImageReel` —— 1/4 个有
- `LayerUtility: ImageReelComposit` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `StringFunction|pysssss` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
