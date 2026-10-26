---
name: image_to_image_lora_sampler_unet_78
type: Image To Image
frequency: 8
level: moderate
coverage: 0.87775
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/image_qwen_image_edit_2509 art_1998353918872682498.json, 图片生成/文生图/image_qwen_image_edit_2511-三图参考-换沙发+人物_2004738010233139201.json, 图片生成/文生图/image_qwen_image_edit_2511-单图参考-上色_2004744836605505538.json, 图片生成/文生图/image_qwen_image_edit_2511-单图参考-转写实_2005067891861061634.json, 图片生成/文生图/image_qwen_image_edit_2511-双图参考-沙发换材质_2004736076759662593.json, 图片生成/文生图/image_qwen_image_edit_2511-文生图_2005074898978570241.json, 图片生成/文生图/三图参考生成组合_1993498915181969409.json, 图片生成/文生图/千问 手办盲盒超火模型_1993973079732846594.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_78

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/image_qwen_image_edit_2509 art_1998353918872682498.json、图片生成/文生图/image_qwen_image_edit_2511-三图参考-换沙发+人物_2004738010233139201.json、图片生成/文生图/image_qwen_image_edit_2511-单图参考-上色_2004744836605505538.json、图片生成/文生图/image_qwen_image_edit_2511-单图参考-转写实_2005067891861061634.json、图片生成/文生图/image_qwen_image_edit_2511-双图参考-沙发换材质_2004736076759662593.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
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
- `FluxKontextMultiReferenceLatentMethod` —— 5/8 个有
- `EmptySD3LatentImage` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `CR Simple Image Compare` —— 1/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `EmptyLatentImage` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有
- `c46c74c1-cfc4-41eb-81a8-9c6701737ef6` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 20 | 8 | 45% |
| Prompt 约束强度(CFG) | 3.25 | 1 - 4 | 8 | 48% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1080 | - | 1 | 100% |
| 高度 | 1536 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 20，8 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 3.25，观测区间 1 - 4，8 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（4/8 个样本）：Steps较低可能导致细节不足
