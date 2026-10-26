---
name: image_to_image_sampler_unet_vae_21
type: Image To Image
frequency: 8
level: strong
coverage: 0.891875
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit局部重绘_1964882500403253249.json, 图片生成/图生图/Qwen-Image-Edit 图生图编辑 _ 12 节点保持人物换装_加配饰_2086660579183386625.json, 图片生成/图生图/Qwen-Image-Edit-2511-Multiple-Angles-LoRA单个镜头_2009066368041226242.json, 图片生成/图生图/Qwen-edit 打光工作流｜人物一致_1959175236979732482.json, 图片生成/图生图/人物打光换背景-Qwen-Image-Edit图像编辑_1958790192075268098.json, 图片生成/图生图/人物编辑-Qwen-Image-Edit图像编辑_1958681004053577729.json, 图片生成/图生图/位置偏移解决方案-Qwen-Image-Edit_1968671815499436033.json, 图片生成/图生图/千问Edit局部重绘_Qwen-Edit_1964284723205951490.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_21

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit局部重绘_1964882500403253249.json、图片生成/图生图/Qwen-Image-Edit 图生图编辑 _ 12 节点保持人物换装_加配饰_2086660579183386625.json、图片生成/图生图/Qwen-Image-Edit-2511-Multiple-Angles-LoRA单个镜头_2009066368041226242.json、图片生成/图生图/Qwen-edit 打光工作流｜人物一致_1959175236979732482.json、图片生成/图生图/人物打光换背景-Qwen-Image-Edit图像编辑_1958790192075268098.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/8 个有
- `ImageScaleDownToSize` —— 6/8 个有
- `ImageStitch` —— 6/8 个有
- `Text Multiline` —— 5/8 个有
- `PreviewImage` —— 3/8 个有
- `TextEncodeQwenImageEditEnhanced` —— 3/8 个有
- `ConditioningZeroOut` —— 2/8 个有
- `ImageAndMaskPreview` —— 2/8 个有
- `Anything Everywhere3` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 8 | 79% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 8 | 79% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
