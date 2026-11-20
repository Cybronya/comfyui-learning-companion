---
name: text_to_image_controlnet_sampler_clip_12
type: Text To Image
frequency: 4
level: strong
coverage: 0.77525
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetImageSizeAndCount, ImageConcatMulti, ImpactSwitch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy imageConcat, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Z-Image Fun-ControlNet-Union 2.0 深度、姿态、条线，精准控制_1996476841798025217.json, 图片生成/图生图/Z-Image+三种ControlNet洗图新姿势（单采样器）Fun版_1996838851123585025.json, 图片生成/图生图/z image三种ControlNet洗图新姿势-fun版_1996944254406705154.json, 图片生成/文生图/Z-Image 三种控制生图+提示词反推_1997284184953667585.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Z-Image Fun-ControlNet-Union 2.0 深度、姿态、条线，精准控制_1996476841798025217.json、图片生成/图生图/Z-Image+三种ControlNet洗图新姿势（单采样器）Fun版_1996838851123585025.json、图片生成/图生图/z image三种ControlNet洗图新姿势-fun版_1996944254406705154.json、图片生成/文生图/Z-Image 三种控制生图+提示词反推_1997284184953667585.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImpactSwitch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy ifElse`
- `easy imageConcat`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 3/4 个有
- `CR Text Concatenate` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `MaraScottIsEmpty_v1` —— 3/4 个有
- `MuyeTextEditOutput` —— 3/4 个有
- `Qwen3_VQA` —— 3/4 个有
- `QwenLoader` —— 3/4 个有
- `WanVideoPromptExtender` —— 3/4 个有
- `easy convertAnything` —— 3/4 个有
- `easy int` —— 3/4 个有
- `RH_Captioner` —— 2/4 个有
- `MaraScottIsEmptyOrNone_v1` —— 1/4 个有
- `ttN concat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1536 | 1536 - 1536 | 4 | 100% |
| 采样步数 | 10 | 10 - 10 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 10，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
