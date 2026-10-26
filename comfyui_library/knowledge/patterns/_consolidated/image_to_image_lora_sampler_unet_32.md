---
name: image_to_image_lora_sampler_unet_32
type: Image To Image
frequency: 14
level: strong
coverage: 0.866143
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit 2511 极简工作流_2003712655913304065.json, 图片生成/图生图/Qwen-edit-2511-图像不偏移版_2004541985673412609.json, 图片生成/图生图/Qwen-edit-2511-无限扩图（简化版）_2005999334229495810.json, 图片生成/图生图/Qwen-eidt-2511-人物表情精准编辑(不偏移版)_2039330373867409410.json, 图片生成/图生图/Qwen-eidt-2511-人物表情精准编辑(不偏移版)_2076485352134631425.json, 图片生成/图生图/Qwen-eidt-2511-人物表情精准编辑(不偏移版)_2094969204024897537.json, 图片生成/图生图/Qwen-eidt-2511-人物表情精细编辑_2039326002383429633.json, 图片生成/图生图/QwenEdit2511多图编辑工作流_2062019518045708289.json, 图片生成/图生图/Qwen_Edit_2511 多图编辑工作流_2049747436729536513.json, 图片生成/图生图/Qwen_Edit_2511 零偏移多图编辑工作流_2019645832496160769.json, 图片生成/图生图/Qwen_Edit_2511_真正的零偏移工作流_2009132588815880194.json, 图片生成/图生图/Qwen_Edit_2511多图改图_2055553864379715585.json, 图片生成/图生图/qwen2511改图工作流_2038270042151849986.json, 图片生成/图生图/🐳老许Gary：Qwen-eidt-2511-人物表情精准编辑_2046823303439982593.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_32

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit 2511 极简工作流_2003712655913304065.json、图片生成/图生图/Qwen-edit-2511-图像不偏移版_2004541985673412609.json、图片生成/图生图/Qwen-edit-2511-无限扩图（简化版）_2005999334229495810.json、图片生成/图生图/Qwen-eidt-2511-人物表情精准编辑(不偏移版)_2039330373867409410.json、图片生成/图生图/Qwen-eidt-2511-人物表情精准编辑(不偏移版)_2076485352134631425.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 13/14 个有
- `ModelSamplingAuraFlow` —— 13/14 个有
- `CFGNorm` —— 12/14 个有
- `ConditioningZeroOut` —— 8/14 个有
- `PreviewImage` —— 8/14 个有
- `FluxKontextImageScale` —— 7/14 个有
- `FluxKontextMultiReferenceLatentMethod` —— 7/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/14 个有
- `PixelSmileConditioning` —— 5/14 个有
- `PrimitiveFloat` —— 3/14 个有
- `ReferenceLatent` —— 2/14 个有
- `Anything Everywhere3` —— 1/14 个有
- `CR Simple Image Compare` —— 1/14 个有
- `DapaoImagePadDirectionNode` —— 1/14 个有
- `ImageConcanate` —— 1/14 个有
- `Label (rgthree)` —— 1/14 个有
- `String` —— 1/14 个有
- `StringFunction|pysssss` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 14 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，14 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
