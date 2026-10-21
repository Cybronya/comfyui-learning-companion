---
name: image_to_image_lora_sampler_unet_26
type: Image To Image
frequency: 4
level: moderate
coverage: 0.98675
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Image-Edit2509&eigen-lora对比_1990410928502050818.json, 图片生成/文生图/Qwen-Image-Edit转真实3种lora对比_1990373406426226689.json, 图片生成/文生图/Qwen-Image-Edit镜头控制_1990374981525803009.json, 图片生成/文生图/Qwen‑Image‑Edit‑2511的2509lora测试_2004203833310019585.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_26

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen-Image-Edit2509&eigen-lora对比_1990410928502050818.json、图片生成/文生图/Qwen-Image-Edit转真实3种lora对比_1990373406426226689.json、图片生成/文生图/Qwen-Image-Edit镜头控制_1990374981525803009.json、图片生成/文生图/Qwen‑Image‑Edit‑2511的2509lora测试_2004203833310019585.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 4 个 workflow 都包含：
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
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 3/4 个有
- `ImageConcatMulti` —— 3/4 个有
- `ImageScaleBy` —— 3/4 个有
- `ImageUpscaleWithModel` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `TextEncodeQwenImageEdit` —— 2/4 个有
- `String Literal` —— 1/4 个有
- `easy promptLine` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 1 | 4 | 53% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 1，4 个样本
- 高发问题（16/4 个样本）：Steps较低可能导致细节不足
