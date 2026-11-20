---
name: unknown_workflow_sampler_clip_unet_39
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.954444
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/QwenImage千问文生图4步加速放大工作流_1955919657263923201.json, 图片生成/文生图/Qwen_Image_2512_商业商品摄影_LoRA｜单品棚拍_2100057678470012930.json, 图片生成/文生图/Qwen_Image_2512_商业商品摄影_LoRA｜单品棚拍_2100137995608346626.json, 图片生成/文生图/Qwen_Image_2512_文生图_2038551608694415361.json, 图片生成/文生图/Qwen_Image_2512_文生图_bf16版本_2008392762101604354.json, 图片生成/文生图/Qwen_Image_2512文生图工作流_2063234247065948161.json, 图片生成/文生图/Qwen_Image_2512版4步加速出图_2006606275999703041.json, 图片生成/文生图/Qwen_Image_2512版4步加速出图_2019651247913046018.json, 图片生成/文生图/Qwen_Image文生图_1955444251107606530.json, 图片生成/文生图/Qwen白丝长腿丝袜美腿_2019647690329559041.json, 图片生成/文生图/Z-IMAGE文生图_2052276305177133058.json, 图片生成/文生图/Z-Image-Turbo 极致写实文生图工作流_2084326650979905538.json, 图片生成/文生图/Z-Image-Turbo文生图_1994260229521162241.json, 图片生成/文生图/Z-image  zimage  文生图  工作流_2042926754704134145.json, 图片生成/文生图/Z-image Base Distilled蒸馏加速版_2019063606171668481.json, 图片生成/文生图/Z-image Tubro文生图工作流，没有AI味的模型！_2061058146243801090.json, 图片生成/文生图/Z-image 文生图_2017213414262710273.json, 图片生成/文生图/Zimage图片加速生成（Zimage Quick Text-to-Image Generatio）_2029019962836258817.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_39

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/QwenImage千问文生图4步加速放大工作流_1955919657263923201.json、图片生成/文生图/Qwen_Image_2512_商业商品摄影_LoRA｜单品棚拍_2100057678470012930.json、图片生成/文生图/Qwen_Image_2512_商业商品摄影_LoRA｜单品棚拍_2100137995608346626.json、图片生成/文生图/Qwen_Image_2512_文生图_2038551608694415361.json、图片生成/文生图/Qwen_Image_2512_文生图_bf16版本_2008392762101604354.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 16/18 个有
- `LoraLoaderModelOnly` —— 13/18 个有
- `PreviewImage` —— 6/18 个有
- `CR Prompt Text` —— 3/18 个有
- `ConditioningZeroOut` —— 2/18 个有
- `LoraLoader` —— 2/18 个有
- `CR Upscale Image` —— 1/18 个有
- `EmptyZImageLatentImage //ZImagePowerNodes` —— 1/18 个有
- `PrimitiveFloat` —— 1/18 个有
- `StringFunction|pysssss` —— 1/18 个有
- `easy promptList` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 50 | 18 | 21% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 18 | 29% |
| 采样算法 | euler | - | 18 | 67% |
| 调度器 | simple | - | 18 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 50，18 个样本，取值分散，一致性仅 21%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，18 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，18 个样本，一致性 67%
- 调度器 最常用 simple，18 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（10/18 个样本）：Steps较低可能导致细节不足
