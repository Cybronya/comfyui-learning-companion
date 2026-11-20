---
name: unknown_workflow_lora_sampler_unet_288
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.841667
common_nodes: [CLIPLoader, Image Comparer (rgthree), JjkConcat, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: SimpleTextImage, LayerUtility: TextBox, LoadImage, LoraLoaderModelOnly, PainterFluxImageEdit, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/筑视AI建筑透视图渲染_2074320789679202305.json, 平台全量/筑视总图填色_2055192228385050625.json, 平台全量/筑视鸟瞰渲染_2055199924286967809.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_288

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/筑视AI建筑透视图渲染_2074320789679202305.json、平台全量/筑视总图填色_2055192228385050625.json、平台全量/筑视鸟瞰渲染_2055199924286967809.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `JjkConcat`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: SimpleTextImage`
- `LayerUtility: TextBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PainterFluxImageEdit`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 2/3 个有
- `LayerColor: Brightness & Contrast` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `UnetLoaderGGUF` —— 2/3 个有
- `easy seed` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `FluxKontextImageScale` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `LoaderGGUF` —— 1/3 个有
- `llama_cpp_instruct_adv` —— 1/3 个有
- `llama_cpp_model_loader` —— 1/3 个有
- `llama_cpp_parameters` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 5 | 3 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.2 | 3 | 91% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 5，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.2，3 个样本，取值集中（一致性 91%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
