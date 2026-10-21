---
name: image_to_image_lora_sampler_unet_2
type: Image To Image
frequency: 11
level: weak
coverage: 0.865545
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/image_qwen_image_edit_2509 art_1998353918872682498.json, 图片生成/文生图/image_qwen_image_edit_2511-三图参考-换沙发+人物_2004738010233139201.json, 图片生成/文生图/image_qwen_image_edit_2511-单图参考-上色_2004744836605505538.json, 图片生成/文生图/image_qwen_image_edit_2511-单图参考-转写实_2005067891861061634.json, 图片生成/文生图/image_qwen_image_edit_2511-双图参考-沙发换材质_2004736076759662593.json, 图片生成/文生图/image_qwen_image_edit_2511-文生图_2005074898978570241.json, 图片生成/文生图/qwen_image_edit_2511连续分镜生产_2007869415899013122.json, 图片生成/文生图/增加光影‑2511单图编辑（发散）_2005600964696571906.json, 图片生成/文生图/增加光影‑2511单图编辑（防偏移）_2005600933931352066.json, 图片生成/文生图/增加光影‑2511多图编辑_2005600974947450882.json, 视频生成/文生视频/next-scene-v2-连续分镜生产_1982011247229059073.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_2

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/image_qwen_image_edit_2509 art_1998353918872682498.json、图片生成/文生图/image_qwen_image_edit_2511-三图参考-换沙发+人物_2004738010233139201.json、图片生成/文生图/image_qwen_image_edit_2511-单图参考-上色_2004744836605505538.json、图片生成/文生图/image_qwen_image_edit_2511-单图参考-转写实_2005067891861061634.json、图片生成/文生图/image_qwen_image_edit_2511-双图参考-沙发换材质_2004736076759662593.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
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
- `FluxKontextMultiReferenceLatentMethod` —— 8/11 个有
- `EmptySD3LatentImage` —— 6/11 个有
- `Image Comparer (rgthree)` —— 4/11 个有
- `VAEDecodeTiled` —— 4/11 个有
- `GetImageSize+` —— 3/11 个有
- `PreviewImage` —— 3/11 个有
- `easy promptLine` —— 2/11 个有
- `EmptyLatentImage` —— 1/11 个有
- `ReferenceLatent` —— 1/11 个有
- `UnetLoaderGGUF` —— 1/11 个有
- `c46c74c1-cfc4-41eb-81a8-9c6701737ef6` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 11 | 34% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 11 | 37% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 1080 | - | 1 | 100% |
| 高度 | 1536 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，11 个样本，取值分散，一致性仅 34%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，11 个样本，取值分散，一致性仅 37%
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（7/11 个样本）：Steps较低可能导致细节不足
