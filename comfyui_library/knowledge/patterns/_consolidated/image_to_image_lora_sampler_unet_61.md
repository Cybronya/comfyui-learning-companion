---
name: image_to_image_lora_sampler_unet_61
type: Image To Image
frequency: 10
level: moderate
coverage: 0.9246
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2511-儿童涂鸦风格转绘-小宣喧-RH_2007047125556797442.json, 图片生成/图生图/Qwen2511-阿凡达风格-小宣喧-RH_2008411628018081793.json, 图片生成/图生图/QwenEdit2511-Q版角色-小宣喧-RH_2006747284024860673.json, 图片生成/图生图/RH-PSAPI插件用-_图生图edit2511_2068683270535081985.json, 图片生成/图生图/image_qwen_image_edit_2511-单图参考+打光_2010914134002503681.json, 图片生成/图生图/image_qwen_image_edit_2511-单图参考+重打光+选视角_2011254283882205186.json, 图片生成/图生图/利用3D相机优势生成多角度图像_2011263097549365250.json, 图片生成/图生图/利用3D相机优势生成多角度图像_2015060059142754306.json, 图片生成/图生图/自由角度和光线调整编辑图片_2036348651290759170.json, 图片生成/文生图/Qwen Image Edit 2511多图融合图像编辑+全节点注释_2058926060804329474.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_61

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen2511-儿童涂鸦风格转绘-小宣喧-RH_2007047125556797442.json、图片生成/图生图/Qwen2511-阿凡达风格-小宣喧-RH_2008411628018081793.json、图片生成/图生图/QwenEdit2511-Q版角色-小宣喧-RH_2006747284024860673.json、图片生成/图生图/RH-PSAPI插件用-_图生图edit2511_2068683270535081985.json、图片生成/图生图/image_qwen_image_edit_2511-单图参考+打光_2010914134002503681.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 7/10 个有
- `QwenMultiangleLightningNode` —— 5/10 个有
- `CR Text Concatenate` —— 4/10 个有
- `ImageResize+` —— 4/10 个有
- `QwenMultiangleCameraNode` —— 4/10 个有
- `CR Text` —— 3/10 个有
- `FluxKontextImageScale` —— 3/10 个有
- `ImageStitch` —— 3/10 个有
- `KOOK_SaveJPGImage` —— 3/10 个有
- `ImpactSwitch` —— 2/10 个有
- `Int` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `easy imageScaleDownToSize` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 25 | 10 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 25，10 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（9/10 个样本）：Steps较低可能导致细节不足
