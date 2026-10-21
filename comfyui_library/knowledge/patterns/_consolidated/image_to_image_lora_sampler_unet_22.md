---
name: image_to_image_lora_sampler_unet_22
type: Image To Image
frequency: 5
level: strong
coverage: 0.9136
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/图片多角度工作流_2009868602559696897.json, 图片生成/文生图/多角度拖动控制，水平角度，缩放，仰角控制_2009974189255561218.json, 数字人/数字人/人物-一键换装-文字描述版_2109828236317380609.json, 数字人/数字人/人物-一键换装-服装图版_2109490336476262401.json, 数字人/数字人/人物-人物抠图_2111344374146752514.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_22

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/图片多角度工作流_2009868602559696897.json、图片生成/文生图/多角度拖动控制，水平角度，缩放，仰角控制_2009974189255561218.json、数字人/数字人/人物-一键换装-文字描述版_2109828236317380609.json、数字人/数字人/人物-一键换装-服装图版_2109490336476262401.json、数字人/数字人/人物-人物抠图_2111344374146752514.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 4/5 个有
- `VAEDecode` —— 4/5 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/5 个有
- `ImageStitch` —— 2/5 个有
- `QwenMultiangleCameraNode` —— 2/5 个有
- `StringConcatenate` —— 2/5 个有
- `StringConstantMultiline` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `VAEDecodeTiled` —— 1/5 个有
- `easy seed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 5 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
