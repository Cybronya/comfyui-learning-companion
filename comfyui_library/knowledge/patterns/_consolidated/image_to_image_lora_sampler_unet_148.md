---
name: image_to_image_lora_sampler_unet_148
type: Image To Image
frequency: 4
level: strong
coverage: 0.935
common_nodes: [CFGNorm, CLIPLoader, FluxKontextImageScale, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN-EDIT2511-利用3D相机生成多角度图像26年2月更新版_2028682011325505538.json, 图片生成/图生图/Qwen Image Edit 2511 - 材质替换_2036450743074426881.json, 图片生成/图生图/Qwen-2511-多视角出图_2012015227755307010.json, 图片生成/图生图/Qwen-Edit-2511 场景自定义角度工作流_2091520586739699713.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_148

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/QWEN-EDIT2511-利用3D相机生成多角度图像26年2月更新版_2028682011325505538.json、图片生成/图生图/Qwen Image Edit 2511 - 材质替换_2036450743074426881.json、图片生成/图生图/Qwen-2511-多视角出图_2012015227755307010.json、图片生成/图生图/Qwen-Edit-2511 场景自定义角度工作流_2091520586739699713.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextImageScale`
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
- `PreviewImage` —— 3/4 个有
- `QwenMultiangleCameraNode` —— 3/4 个有
- `AddLabel` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `JWImageResize` —— 1/4 个有
- `QwenMultiangleLightningNode` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `StringConcat|Mie` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `easy imageSize` —— 1/4 个有
- `easy promptList` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
