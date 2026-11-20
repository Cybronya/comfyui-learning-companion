---
name: image_to_image_lora_sampler_unet_47
type: Image To Image
frequency: 11
level: strong
coverage: 0.958182
common_nodes: [CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-edit2511三图融合--标准版--（必收藏）_2049911848614543361.json, 图片生成/图生图/Qwen-image-edit2511双图编辑--标准版--（必收藏）_2049875414901903362.json, 图片生成/图生图/Qwen-image-edit2511多角度一致性-标准版-(必收藏)_2050953090811080705.json, 图片生成/图生图/Qwen20角度训练集_正式版lora训练集_2086043197633028097.json, 图片生成/图生图/Qwen2511-多角度工作流 260708_2074859797379371010.json, 图片生成/图生图/Qwen2511多角度可视化控制流_2009977063985385474.json, 图片生成/图生图/Qwen2511多角度控制_2009846604588654594.json, 图片生成/图生图/QwenImage-Edit-2511-多角度编辑APP_2009969851430866946.json, 图片生成/图生图/QwenMultiangle2511图片多角度自由控制_2058843387687690241.json, 图片生成/图生图/Qwen可视化角度编辑_2035698477958696962.json, 图片生成/文生图/智能会展空间设计 任意角度 3D交互方案工作流 V2.0_2011120346996412418.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_47

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen-image-edit2511三图融合--标准版--（必收藏）_2049911848614543361.json、图片生成/图生图/Qwen-image-edit2511双图编辑--标准版--（必收藏）_2049875414901903362.json、图片生成/图生图/Qwen-image-edit2511多角度一致性-标准版-(必收藏)_2050953090811080705.json、图片生成/图生图/Qwen20角度训练集_正式版lora训练集_2086043197633028097.json、图片生成/图生图/Qwen2511-多角度工作流 260708_2074859797379371010.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
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
- `CFGNorm` —— 10/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/11 个有
- `QwenMultiangleCameraNode` —— 9/11 个有
- `PreviewImage` —— 5/11 个有
- `easy showAnything` —— 5/11 个有
- `JDCN_StringToList` —— 3/11 个有
- `MemoryCleaner` —— 3/11 个有
- `Text Concatenate` —— 3/11 个有
- `CR Text` —— 2/11 个有
- `CR Text Concatenate` —— 2/11 个有
- `Int` —— 2/11 个有
- `KepStringList` —— 2/11 个有
- `RHHiddenNodes` —— 2/11 个有
- `easy promptList` —— 2/11 个有
- `AddLabel` —— 1/11 个有
- `GetNode` —— 1/11 个有
- `ImageConcanate` —— 1/11 个有
- `ImageScaleToTotalPixels` —— 1/11 个有
- `RH_Nano_Banana2_Image2Image` —— 1/11 个有
- `Text Multiline` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 11 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（30/11 个样本）：Steps较低可能导致细节不足
