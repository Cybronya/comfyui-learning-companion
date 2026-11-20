---
name: image_to_image_lora_sampler_unet_52
type: Image To Image
frequency: 10
level: strong
coverage: 0.9277
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/96个角度多视角一致性【最新】_2009528199734104066.json, 图片生成/图生图/QWEN角度随心换升级版本_2010187591118757890.json, 图片生成/图生图/QWEN角度随心换升级版本_2027345865211387906.json, 图片生成/图生图/Qwen Image Edit 2511图像编辑_2003705913477349378.json, 图片生成/图生图/Qwen Image Edit 2511图像编辑_2014264674426032130.json, 图片生成/图生图/Qwen Image Edit 2511图像编辑_2014293822842347522.json, 图片生成/图生图/Qwen Image Edit 2511图像编辑_2030907456901095425.json, 图片生成/图生图/Qwen Multiangle Camera 多角度切换_2009905557972459522.json, 图片生成/图生图/Qwen-Image-Edit 2509-模特一致性不同姿势生成_2005271889100636161.json, 图片生成/图生图/完美一致性 qwen2511一键多镜头，多角度分镜，_2004882198304096257.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_52

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/96个角度多视角一致性【最新】_2009528199734104066.json、图片生成/图生图/QWEN角度随心换升级版本_2010187591118757890.json、图片生成/图生图/QWEN角度随心换升级版本_2027345865211387906.json、图片生成/图生图/Qwen Image Edit 2511图像编辑_2003705913477349378.json、图片生成/图生图/Qwen Image Edit 2511图像编辑_2014264674426032130.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
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
- `Int` —— 7/10 个有
- `ImageResize+` —— 5/10 个有
- `ImpactSwitch` —— 5/10 个有
- `ConditioningZeroOut` —— 4/10 个有
- `QwenMultiangleCameraNode` —— 4/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/10 个有
- `PreviewAny` —— 3/10 个有
- `ReferenceLatent` —— 3/10 个有
- `Qwen3_VQA` —— 2/10 个有
- `TextInput_` —— 2/10 个有
- `easy promptLine` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `Anything Everywhere3` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 10 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 90% |
| 调度器 | simple | - | 10 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，10 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 90%
- 调度器 最常用 simple，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
