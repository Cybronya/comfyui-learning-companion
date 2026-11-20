---
name: image_to_image_lora_sampler_unet_169
type: Image To Image
frequency: 4
level: strong
coverage: 0.8665
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI口播人物-编辑_2026997964123676674.json, 图片生成/图生图/Edit2511产品多角度转换（配批量提示词）_2009552317019856898.json, 图片生成/图生图/Qianwen Edit 2511  单图新年贺卡编辑稳定版_2011353251496599553.json, 平台全量/镜头可视化自由视角_2059391523283890177.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_169

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/AI口播人物-编辑_2026997964123676674.json、图片生成/图生图/Edit2511产品多角度转换（配批量提示词）_2009552317019856898.json、图片生成/图生图/Qianwen Edit 2511  单图新年贺卡编辑稳定版_2011353251496599553.json、平台全量/镜头可视化自由视角_2059391523283890177.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
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
- `CR Text` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `PromptBatchQueue` —— 2/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `Qwen3_VQA_Plus` —— 1/4 个有
- `QwenMultiangleCameraNode` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `RH_Nano_Banana2_Image2Image` —— 1/4 个有
- `TextEncodeQwenImageEdit` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 5 - 8 | 4 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 5 - 8，4 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
