---
name: unknown_workflow_upscale_lora_sampler_34
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.819857
common_nodes: [CLIPLoader, CR Prompt Text, CR Text Concatenate, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, 孤海注释]
problems: []
missing: []
members: [图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1-手动版_2108103051025403905.json, 图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1-手动版_2112437243515334657.json, 图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1-手动版_2114999103636725761.json, 图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1_2108018565587750914.json, 图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1_2108450514630430721.json, 图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1_2110565599368794114.json, 图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1_2111009497987768321.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_34

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1-手动版_2108103051025403905.json、图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1-手动版_2112437243515334657.json、图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1-手动版_2114999103636725761.json、图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1_2108018565587750914.json、图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1_2108450514630430721.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `CR Text Concatenate`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `FastCanvas` —— 4/7 个有
- `FastCanvasTool` —— 4/7 个有
- `InspyrenetRembg` —— 4/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 100% |
| Prompt 约束强度(CFG) | 40 | 40 - 40 | 7 | 100% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 40，观测区间 40 - 40，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
