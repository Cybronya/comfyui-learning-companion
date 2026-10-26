---
name: image_to_image_lora_sampler_clip_28
type: Image To Image
frequency: 8
level: strong
coverage: 0.951625
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext3D场景融图工作流_1946053058235166721.json, 图片生成/图生图/KontextDev转绘扁平化风_1942049063250640898.json, 图片生成/图生图/Kontext人像摄影 _ 一键更换战国袍_1953338187823370241.json, 图片生成/图生图/Kontext光影融合_1995291619001819137.json, 图片生成/图生图/PS调和服务端_1955212269064896514.json, 图片生成/图生图/双融图合并工作流_1983413939042197505.json, 图片生成/图生图/最简单的万物迁移工作流_1993107473835950081.json, 图片生成/图生图/电商设计一键万物迁移工作流 V1.0_1980477000945217538.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Kontext3D场景融图工作流_1946053058235166721.json、图片生成/图生图/KontextDev转绘扁平化风_1942049063250640898.json、图片生成/图生图/Kontext人像摄影 _ 一键更换战国袍_1953338187823370241.json、图片生成/图生图/Kontext光影融合_1995291619001819137.json、图片生成/图生图/PS调和服务端_1955212269064896514.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 5/8 个有
- `FastCanvas` —— 4/8 个有
- `FastCanvasTool` —— 4/8 个有
- `easy imageRemBg` —— 4/8 个有
- `RepeatLatentBatch` —— 3/8 个有
- `TeaCache` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `ImageResizeKJ` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `Seed_` —— 1/8 个有
- `Text Multiline` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 8 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，8 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
