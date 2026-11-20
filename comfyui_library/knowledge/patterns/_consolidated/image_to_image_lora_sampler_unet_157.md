---
name: image_to_image_lora_sampler_unet_157
type: Image To Image
frequency: 4
level: strong
coverage: 0.8785
common_nodes: [CFGNorm, CLIPLoader, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen编辑局部重绘_1962045337357762561.json, 图片生成/图生图/Qwen随机改变姿势_1961283635229999105.json, 图片生成/图生图/qwen edit 双图编辑_1960219194140864513.json, 图片生成/图生图/qwen edit双图融合_1957907689856757762.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_157

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen编辑局部重绘_1962045337357762561.json、图片生成/图生图/Qwen随机改变姿势_1961283635229999105.json、图片生成/图生图/qwen edit 双图编辑_1960219194140864513.json、图片生成/图生图/qwen edit双图融合_1957907689856757762.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `ImageStitch` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `BatchCropFromMaskAdvanced` —— 1/4 个有
- `BboxVisualize` —— 1/4 个有
- `CR SDXL Aspect Ratio` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `TextEncodeQwenImageEditPlus` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
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
