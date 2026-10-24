---
name: image_to_image_lora_sampler_unet_128
type: Image To Image
frequency: 5
level: strong
coverage: 0.892
common_nodes: [CFGNorm, CLIPLoader, CR Text, CR Text Replace, ImageScaleToTotalPixels, JDCN_StringToList, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, PreviewAny, PreviewImage, ProcessString, RH_LLMAPI_NODE, SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-旅拍写真：环球旅行照，一键生成，主角颜值始终在线！_1998767784366592002.json, 图片生成/图生图/Qwen旅拍写真_1999296676038836225.json, 图片生成/图生图/旅拍写真：环球旅行照2_1999669660909961217.json, 图片生成/图生图/旅行照相馆 - “旅行”+“照相馆”_2001549140054142977.json, 图片生成/图生图/🎄 Qwen-Edit 2509：圣诞写真，指令级编辑，定格你的节日高光！_1996587057155809282.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_128

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-旅拍写真：环球旅行照，一键生成，主角颜值始终在线！_1998767784366592002.json、图片生成/图生图/Qwen旅拍写真_1999296676038836225.json、图片生成/图生图/旅拍写真：环球旅行照2_1999669660909961217.json、图片生成/图生图/旅行照相馆 - “旅行”+“照相馆”_2001549140054142977.json、图片生成/图生图/🎄 Qwen-Edit 2509：圣诞写真，指令级编辑，定格你的节日高光！_1996587057155809282.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `CR Text Replace`
- `ImageScaleToTotalPixels`
- `JDCN_StringToList`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PreviewImage`
- `ProcessString`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 4/5 个有
- `SeedVR2LoadDiTModel` —— 4/5 个有
- `SeedVR2LoadVAEModel` —— 4/5 个有
- `SeedVR2VideoUpscaler` —— 4/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta57 | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta57，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
