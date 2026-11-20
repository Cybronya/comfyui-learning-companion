---
name: image_to_image_lora_sampler_unet_37
type: Image To Image
frequency: 15
level: weak
coverage: 0.861933
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit-2511姿态迁移_2012123669828472833.json, 图片生成/图生图/Qwen-Edit-2511真实转动漫风V2.0_2015682167266873345.json, 图片生成/图生图/QwenEdit2511多图编辑工作流_2062019518045708289.json, 图片生成/图生图/Qwen_Edit_2511 多图编辑工作流_2049747436729536513.json, 图片生成/图生图/Qwen_Edit_2511 零偏移多图编辑工作流_2019645832496160769.json, 图片生成/图生图/Qwen_Edit_2511_真正的零偏移工作流_2009132588815880194.json, 图片生成/图生图/Qwen_Edit_2511多图改图_2055553864379715585.json, 图片生成/图生图/Qwen_Edit_2511改图_2055536614876688385.json, 图片生成/图生图/Qwen_image_Edit_2511_单图编辑_2004473601208315905.json, 图片生成/图生图/Qwen_image_Edit_2511_多图编辑_2004495314616811522.json, 图片生成/图生图/Qwenedit 2511 一键换衣_2004388430463332354.json, 图片生成/图生图/【🛫书墨】姿态构图迁移v3-anypose_2010972516814168065.json, 图片生成/图生图/多图编辑-小红书FireRed-Image-edit1.1-40步原版 电商模特换装等_2030532517639495682.json, 图片生成/图生图/多图编辑-小红书FireRed-Image-edit1.1-加速版 电商模特换装等_2030120115282386945.json, 平台全量/多图编辑-电商模特换装-FireRed-Image-edit1.1-加速版_2030612656188563458.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_37

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit-2511姿态迁移_2012123669828472833.json、图片生成/图生图/Qwen-Edit-2511真实转动漫风V2.0_2015682167266873345.json、图片生成/图生图/QwenEdit2511多图编辑工作流_2062019518045708289.json、图片生成/图生图/Qwen_Edit_2511 多图编辑工作流_2049747436729536513.json、图片生成/图生图/Qwen_Edit_2511 零偏移多图编辑工作流_2019645832496160769.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
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
- `CFGNorm` —— 13/15 个有
- `FluxKontextImageScale` —— 12/15 个有
- `Image Comparer (rgthree)` —— 12/15 个有
- `FluxKontextMultiReferenceLatentMethod` —— 11/15 个有
- `PreviewImage` —— 10/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/15 个有
- `ImageConcatMulti` —— 6/15 个有
- `AddLabel` —— 4/15 个有
- `CR Prompt Text` —— 4/15 个有
- `KOOK_SaveJPGImage` —— 4/15 个有
- `easy int` —— 3/15 个有
- `ColorCorrect` —— 2/15 个有
- `ImageBlend` —— 2/15 个有
- `SDPoseOODLoader` —— 2/15 个有
- `SDPoseOODProcessor` —— 2/15 个有
- `CLIPTextEncode` —— 1/15 个有
- `CR Text` —— 1/15 个有
- `CR Text Concatenate` —— 1/15 个有
- `EmptySD3LatentImage` —— 1/15 个有
- `Int` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 40 | 15 | 4% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 15 | 27% |
| 采样算法 | euler | - | 15 | 80% |
| 调度器 | simple | - | 15 | 87% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 40，15 个样本，取值分散，一致性仅 4%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，15 个样本，取值分散，一致性仅 27%
- 采样算法 最常用 euler，15 个样本，一致性 80%
- 调度器 最常用 simple，15 个样本，一致性 87%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（14/15 个样本）：Steps较低可能导致细节不足
