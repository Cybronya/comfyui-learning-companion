---
name: image_to_image_lora_sampler_vae_15
type: Image To Image
frequency: 8
level: strong
coverage: 0.911875
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image Edit Plus双截棍加速&像素偏移优化_1972625362733711361.json, 图片生成/文生图/Qwen2509&Next Scene一致性增强的下一分镜预测_1977629873571287042.json, 图片生成/文生图/Qwen（千问）图像处理（文生图，图生图，水印去除）_1990338995290820610.json, 图片生成/文生图/comfyui图像转钢笔插画_2045310027589750785.json, 平台全量/2511小高清_2030987200996839426.json, 平台全量/Qwen-2509-三图场景融合_1984095333204590593.json, 平台全量/Qwen-edit-2509 改画风-换背景-合影_2006261670783488001.json, 平台全量/动作迁移人物一致性_qweneditpllus_1970468580192100354.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_15

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Qwen Image Edit Plus双截棍加速&像素偏移优化_1972625362733711361.json、图片生成/文生图/Qwen2509&Next Scene一致性增强的下一分镜预测_1977629873571287042.json、图片生成/文生图/Qwen（千问）图像处理（文生图，图生图，水印去除）_1990338995290820610.json、图片生成/文生图/comfyui图像转钢笔插画_2045310027589750785.json、平台全量/2511小高清_2030987200996839426.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `ImageScaleToTotalPixels` —— 6/8 个有
- `PreviewImage` —— 4/8 个有
- `DWPreprocessor` —— 3/8 个有
- `easy imageConcat` —— 3/8 个有
- `ConditioningZeroOut` —— 2/8 个有
- `EmptySD3LatentImage` —— 2/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `LynxInsightFaceCrop` —— 1/8 个有
- `NunchakuQwenImageDiTLoader` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有
- `easy seed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 10 | 8 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 10，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
