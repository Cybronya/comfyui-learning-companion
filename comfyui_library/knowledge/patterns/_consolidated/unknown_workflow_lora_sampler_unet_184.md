---
name: unknown_workflow_lora_sampler_unet_184
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.46525
common_nodes: [CFGNorm, CLIPLoader, CR Seed, Fast Groups Bypasser (rgthree), GetImageSize+, GetNode, Image Comparer (rgthree), KSampler (Efficient), LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoraLoaderModelOnly, ModelSamplingAuraFlow, PainterFluxImageEdit, PreviewImage, SetNode, UNETLoader, VAELoader, easy getNode, easy setNode]
problems: []
missing: []
members: [图片生成/图生图/flux-2-klein-9b-KV-fp8    单图编辑_2032695788039577601.json, 图片生成/图生图/一键运行：flux-2-klein-9b-fp8 EDIT 单独修图优化版 文生图_2063462407997059073.json, 图片生成/图生图/一键运行：klein 人物衣服提取，3D质感展示工作流_2035568544326361090.json, 图片生成/文生图/一键运行：flux-2-klein-9b-fp8    GGUF  文生图 图像控制 升级版本_2017375676734640130.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_184

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/flux-2-klein-9b-KV-fp8    单图编辑_2032695788039577601.json、图片生成/图生图/一键运行：flux-2-klein-9b-fp8 EDIT 单独修图优化版 文生图_2063462407997059073.json、图片生成/图生图/一键运行：klein 人物衣服提取，3D质感展示工作流_2035568544326361090.json、图片生成/文生图/一键运行：flux-2-klein-9b-fp8    GGUF  文生图 图像控制 升级版本_2017375676734640130.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：47%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Seed`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSampler (Efficient)`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PainterFluxImageEdit`
- `PreviewImage`
- `SetNode`
- `UNETLoader`
- `VAELoader`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `PromptExpand` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `FluxKVCache` —— 2/4 个有
- `easy textSwitch` —— 2/4 个有
- `ClipLoaderGGUF` —— 1/4 个有
- `KOOK_ImageCompression` —— 1/4 个有
- `KOOK_SaveJPGImage` —— 1/4 个有
- `LoaderGGUF` —— 1/4 个有
- `MultiImageLoader` —— 1/4 个有
- `StringFunction|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 4 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
