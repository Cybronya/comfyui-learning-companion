---
name: image_to_image_lora_sampler_unet_49
type: Image To Image
frequency: 11
level: moderate
coverage: 0.950636
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen2509姿势迁移+快速放大_1985049833184645121.json, 图片生成/图生图/qwen_image_edit图像编辑_1958047512122765314.json, 图片生成/图生图/qwen_image编辑工作流_1991715839368065026.json, 图片生成/图生图/【老金驿站】动漫转真实Qwen-edit工作流_1967857565159817217.json, 图片生成/图生图/一致性模特同场景 不同表情 不同动作（多图 qwen2509+F2P）V2_2050910271660675073.json, 图片生成/图生图/模特单图生成多场景（qwen2509+F2P+boreal）_1985373069348847618.json, 图片生成/图生图/模特同场景，不同表情 不同动作（多图 qwen2509+F2P）V2_1987919084174118913.json, 图片生成/图生图/模特同场景，不同表情 不同动作（多图 qwen2509+F2P）V2_2045690568805715969.json, 图片生成/图生图/模特同场景，不同表情动作（多图 qwen2509+F2P）_1985917498681958401.json, 图片生成/图生图/表情2_2070078782542802945.json, 数字人/数字人/多表情生成_2069314224567967746.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_49

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/qwen2509姿势迁移+快速放大_1985049833184645121.json、图片生成/图生图/qwen_image_edit图像编辑_1958047512122765314.json、图片生成/图生图/qwen_image编辑工作流_1991715839368065026.json、图片生成/图生图/【老金驿站】动漫转真实Qwen-edit工作流_1967857565159817217.json、图片生成/图生图/一致性模特同场景 不同表情 不同动作（多图 qwen2509+F2P）V2_2050910271660675073.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：95%

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
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 8/11 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 8/11 个有
- `UpscaleModelLoader` —— 8/11 个有
- `easy imageScaleDownBy` —— 8/11 个有
- `CR Text` —— 7/11 个有
- `easy showAnything` —— 7/11 个有
- `AILab_QwenVL` —— 6/11 个有
- `JDCN_StringToList` —— 6/11 个有
- `Text to String` —— 6/11 个有
- `ImageStitch` —— 3/11 个有
- `CR Text Input Switch` —— 2/11 个有
- `ACE_ImageFaceCrop` —— 1/11 个有
- `CR Text Concatenate` —— 1/11 个有
- `DWPreprocessor` —— 1/11 个有
- `MergeString` —— 1/11 个有
- `PathchSageAttentionKJ` —— 1/11 个有
- `PixelPerfectResolution` —— 1/11 个有
- `PreviewAny` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `QWEN_TextDisplay` —— 1/11 个有
- `Qwen3_VQA` —— 1/11 个有
- `StringReplace` —— 1/11 个有
- `Text` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 11 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | beta | - | 11 | 64% |
| 重绘幅度 | 1 | 0.15 - 1 | 11 | 63% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，11 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 0.15 - 1，11 个样本
- 高发问题（19/11 个样本）：Steps较低可能导致细节不足
