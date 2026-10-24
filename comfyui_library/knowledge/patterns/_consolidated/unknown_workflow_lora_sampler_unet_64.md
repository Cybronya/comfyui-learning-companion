---
name: unknown_workflow_lora_sampler_unet_64
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.898778
common_nodes: [CFGNorm, CLIPLoader, CR Text, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit-2509 下一个镜头_场景_2030202076516585473.json, 图片生成/图生图/Qwen2511——局部重绘(4K直出)-改字_改图_无痕迹_2003712604600213506.json, 图片生成/图生图/Qwen2511——局部重绘(4K直出)-改字_改图_无痕迹_2061627000284078082.json, 图片生成/图生图/Qwen2511——局部重绘(4K直出)-改字_改图_无痕迹_2094263287616720898.json, 图片生成/图生图/Qwen2511局部重绘(4K直出)——改字_改图_消除_2042052010853273601.json, 图片生成/图生图/Qwen2511局部重绘原图尺寸贴回——适用于SDPPP替代创成式填充_2073349898552041473.json, 图片生成/图生图/qwen2511局部重绘-改字_改图_无痕迹_2057305907763179521.json, 图片生成/图生图/qwen2511局部重绘-改字_改图_无痕迹_2067954497997074434.json, 图片生成/图生图/老孙AI Qwen2511局部重绘 原图贴回_2087044751177633794.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_64

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit-2509 下一个镜头_场景_2030202076516585473.json、图片生成/图生图/Qwen2511——局部重绘(4K直出)-改字_改图_无痕迹_2003712604600213506.json、图片生成/图生图/Qwen2511——局部重绘(4K直出)-改字_改图_无痕迹_2061627000284078082.json、图片生成/图生图/Qwen2511——局部重绘(4K直出)-改字_改图_无痕迹_2094263287616720898.json、图片生成/图生图/Qwen2511局部重绘(4K直出)——改字_改图_消除_2042052010853273601.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/9 个有
- `InpaintCropImproved` —— 8/9 个有
- `InpaintModelConditioning` —— 8/9 个有
- `InpaintStitchImproved` —— 8/9 个有
- `MaskPreview+` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `PrimitiveFloat` —— 2/9 个有
- `CR SDXL Aspect Ratio` —— 1/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `ImageScaleToTotalPixels` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 9 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（7/9 个样本）：Steps较低可能导致细节不足
