---
name: image_to_image_lora_sampler_unet_73
type: Image To Image
frequency: 8
level: strong
coverage: 0.93025
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/76.tonnie-2511图像多角度_2011789730735722497.json, 图片生成/图生图/96个角度多视角一致性【最新】_2009528199734104066.json, 图片生成/图生图/Qwen Image Edit 2511图像编辑_2003705913477349378.json, 图片生成/图生图/Qwen Image Edit 2511图像编辑_2014264674426032130.json, 图片生成/图生图/Qwen Image Edit 2511图像编辑_2014293822842347522.json, 图片生成/图生图/Qwen Image Edit 2511图像编辑_2030907456901095425.json, 图片生成/图生图/Qwen-Image-Edit 2509-模特一致性不同姿势生成_2005271889100636161.json, 图片生成/图生图/完美一致性 qwen2511一键多镜头，多角度分镜，_2004882198304096257.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_73

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/76.tonnie-2511图像多角度_2011789730735722497.json、图片生成/图生图/96个角度多视角一致性【最新】_2009528199734104066.json、图片生成/图生图/Qwen Image Edit 2511图像编辑_2003705913477349378.json、图片生成/图生图/Qwen Image Edit 2511图像编辑_2014264674426032130.json、图片生成/图生图/Qwen Image Edit 2511图像编辑_2014293822842347522.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
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
- `FluxKontextMultiReferenceLatentMethod` —— 7/8 个有
- `Int` —— 6/8 个有
- `ImageResize+` —— 5/8 个有
- `ImpactSwitch` —— 5/8 个有
- `ConditioningZeroOut` —— 4/8 个有
- `ReferenceLatent` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `Qwen3_VQA` —— 2/8 个有
- `QwenMultiangleCameraNode` —— 2/8 个有
- `TextInput_` —— 2/8 个有
- `easy promptLine` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `Anything Everywhere3` —— 1/8 个有
- `Display Any (rgthree)` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `easy promptList` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 8 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，8 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
