---
name: text_to_image_lora_sampler_clip_37
type: Text To Image
frequency: 17
level: strong
coverage: 0.875706
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/反推提示词/Qwen Image 2.1全能图像二合一加提示增强，文生图多图编辑自由切换_2103219635977015297.json, 图片生成/反推提示词/Qwen Image 2.1参考生图标准版 参考图输入高质量出图_2105030116769353730.json, 图片生成/图生图/2102088091476512769.json, 图片生成/图生图/2102095974146596866.json, 图片生成/图生图/2102100461598892034.json, 图片生成/图生图/2102101983669866498.json, 图片生成/图生图/2102105087035400194.json, 图片生成/图生图/2102192876569583617.json, 图片生成/图生图/2102210466104832001.json, 图片生成/图生图/2102211983704678402.json, 图片生成/图生图/2102224257387425794.json, 图片生成/图生图/2102232264989036546.json, 图片生成/图生图/2102252322154962946.json, 图片生成/图生图/2102257321794695170.json, 图片生成/图生图/2102480198032781314.json, 图片生成/图生图/2102505314745667586.json, 图片生成/文生图/Qwen Image 2.1全能图像二合一加提示增强，文生图多图编辑自由切换_2103219635977015297.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_37

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1全能图像二合一加提示增强，文生图多图编辑自由切换_2103219635977015297.json、图片生成/反推提示词/Qwen Image 2.1参考生图标准版 参考图输入高质量出图_2105030116769353730.json、图片生成/图生图/2102088091476512769.json、图片生成/图生图/2102095974146596866.json、图片生成/图生图/2102100461598892034.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 15/17 个有
- `ComfySwitchNode` —— 14/17 个有
- `ResolutionSelector` —— 14/17 个有
- `PrimitiveStringMultiline` —— 9/17 个有
- `SaveImageAdvanced` —— 9/17 个有
- `BatchImagesNode` —— 8/17 个有
- `TextGenerateLTX2Prompt` —— 8/17 个有
- `CR Text` —— 5/17 个有
- `easy showAnything` —— 5/17 个有
- `PrimitiveBoolean` —— 4/17 个有
- `PreviewAny` —— 3/17 个有
- `TextGenerate` —— 3/17 个有
- `JDCN_StringToList` —— 2/17 个有
- `SeedNode` —— 2/17 个有
- `StringConcatenate` —— 2/17 个有
- `Textbox` —— 2/17 个有
- `Fast Groups Bypasser (rgthree)` —— 1/17 个有
- `ImageConcatMulti` —— 1/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerUtility: ImageScaleByAspectRatio V2
