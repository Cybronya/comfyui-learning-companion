---
name: text_to_image_controlnet_lora_sampler_12
type: Text To Image
frequency: 3
level: strong
coverage: 0.906333
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, DepthAnythingPreprocessor, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Controlnet-全家桶-线稿_深度_姿态_软边缘_局部重绘_1963779615453171713.json, 图片生成/图生图/Qwen-Controlnet线稿_深度_姿态_软边缘_局部重绘-全家桶_1963538621120876546.json, 图片生成/图生图/Qwen-Controlnet线稿_深度_姿态_软边缘_局部重绘-全家桶_1967585593507094530.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_12

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-Controlnet-全家桶-线稿_深度_姿态_软边缘_局部重绘_1963779615453171713.json、图片生成/图生图/Qwen-Controlnet线稿_深度_姿态_软边缘_局部重绘-全家桶_1963538621120876546.json、图片生成/图生图/Qwen-Controlnet线稿_深度_姿态_软边缘_局部重绘-全家桶_1967585593507094530.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DepthAnythingPreprocessor`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 2/3 个有
- `JanusImageUnderstanding` —— 2/3 个有
- `JanusModelLoader` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1208 | 1208 - 1208 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| ControlNet 权重 | 1 | 1 - 1 | 3 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1.5 | 1.5 - 1.5 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1208，观测区间 1208 - 1208，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1.5 - 1.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（15/3 个样本）：Steps较低可能导致细节不足
