---
name: image_to_image_lora_sampler_unet_116
type: Image To Image
frequency: 6
level: moderate
coverage: 0.9375
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Image-Edit2509&eigen-lora对比_1990410928502050818.json, 图片生成/文生图/Qwen-Image-Edit白模提取Character_Dummy_1985126465392037890.json, 图片生成/文生图/Qwen-Image-Edit转真实3种lora对比_1990373406426226689.json, 图片生成/文生图/Qwen-Image-Edit镜头控制_1990374981525803009.json, 图片生成/文生图/Qwen‑Image‑Edit‑2511的2509lora测试_2004203833310019585.json, 视频生成/文生视频/next-scene-v2-连续分镜生产_1982011247229059073.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_116

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Qwen-Image-Edit2509&eigen-lora对比_1990410928502050818.json、图片生成/文生图/Qwen-Image-Edit白模提取Character_Dummy_1985126465392037890.json、图片生成/文生图/Qwen-Image-Edit转真实3种lora对比_1990373406426226689.json、图片生成/文生图/Qwen-Image-Edit镜头控制_1990374981525803009.json、图片生成/文生图/Qwen‑Image‑Edit‑2511的2509lora测试_2004203833310019585.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ImageConcatMulti` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `easy seed` —— 4/6 个有
- `AddLabel` —— 3/6 个有
- `ImageScaleBy` —— 3/6 个有
- `ImageUpscaleWithModel` —— 3/6 个有
- `UpscaleModelLoader` —— 3/6 个有
- `EmptySD3LatentImage` —— 2/6 个有
- `TextEncodeQwenImageEdit` —— 2/6 个有
- `easy promptLine` —— 2/6 个有
- `String Literal` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 6 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 0.7 | 0.4 - 1 | 6 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.4 - 1，6 个样本
- 高发问题（18/6 个样本）：Steps较低可能导致细节不足
