---
name: unknown_workflow_sampler_clip_checkpoint
type: Unknown Workflow
frequency: 23
level: strong
coverage: 0.781391
common_nodes: [Anything Everywhere, CLIPLoader, CLIPTextEncode, CR Text Concatenate, CheckpointLoaderSimple, ConditioningZeroOut, Constant Number, EmptyLatentImage, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingAuraFlow, MuyeTextEditOutput, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [图片生成/文生图/Krea2+Z-image AIO 双采样文生图_2076917503313399809.json, 图片生成/文生图/Krea2+Z-image AIO 双采样美图生成_2074694861239971842.json, 图片生成/文生图/Krea2+Z-image AIO 双采样美图生成_2075135586591137794.json, 图片生成/文生图/Krea2+Z-image+AIO 极致美学 双采样优化_2088276981094899713.json, 图片生成/文生图/Krea2+Z-image+AIO 极致美学 双采样优化工作流_2088256228513370114.json, 图片生成/文生图/Krea2+双采样-文生图_2072589473052975106.json, 图片生成/文生图/【极致美学】Krea2 Z-image AIO 双采样整合_2089344978542743553.json, 图片生成/文生图/极致美学 Krea2+Z-image AIO 双采样_2071569515518971905.json, 图片生成/文生图/极致美学 Krea2+Z-image AIO 双采样_2072206080729501698.json, 图片生成/文生图/极致美学 Krea2+Z-image AIO 双采样_2073954956847173633.json, 图片生成/文生图/极致美学 Krea2+Z-image AIO 双采样_2073957942851891201.json, 图片生成/文生图/极致美学 Krea2+Z-image AIO 双采样_2086299352485683202.json, 图片生成/文生图/极致美学+Krea2+Z-image+AIO+双采样_2073722804272451586.json, 图片生成/文生图/极致美学+Krea2+Z-image+AIO+双采样_2074029468489969666.json, 图片生成/文生图/极致美学+Krea2+Z-image+AIO+双采样_2074111527757635585.json, 图片生成/文生图/极致美学+Krea2+Z-image+AIO+双采样_2074116789126123521.json, 图片生成/文生图/极致美学+Krea2+Z-image+AIO+双采样_2074729540471058433.json, 图片生成/文生图/极致美学+Krea2+Z-image+AIO+双采样_2074729571148189698.json, 图片生成/文生图/极致美学+Krea2+Z-image+AIO+双采样_2074748703159709697.json, 图片生成/文生图/极致美学+Krea2+Z-image+AIO+双采样_2076616289145155586.json, 图片生成/文生图/极致美学+Krea2+Z-image+AIO+双采样_2076621028700282881.json, 图片生成/文生图/极致美学+Krea2+Z-image+AIO+双采样_2079603648522448898.json, 图片生成/文生图/极致美学渲染，Krea2、Z‑image、AIO 双采样组合_2086815893220319234.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/文生图/Krea2+Z-image AIO 双采样文生图_2076917503313399809.json、图片生成/文生图/Krea2+Z-image AIO 双采样美图生成_2074694861239971842.json、图片生成/文生图/Krea2+Z-image AIO 双采样美图生成_2075135586591137794.json、图片生成/文生图/Krea2+Z-image+AIO 极致美学 双采样优化_2088276981094899713.json、图片生成/文生图/Krea2+Z-image+AIO 极致美学 双采样优化工作流_2088256228513370114.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 23 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `Constant Number`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingAuraFlow`
- `MuyeTextEditOutput`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 22/23 个有
- `ImageScaleToTotalPixels` —— 22/23 个有
- `LoadImage` —— 22/23 个有
- `workflow>llama-cpp` —— 22/23 个有
- `workflow>提示词反推` —— 22/23 个有
- `CR Text` —— 1/23 个有
- `llama_cpp_instruct_adv` —— 1/23 个有
- `llama_cpp_model_loader` —— 1/23 个有
- `llama_cpp_parameters` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 23 | 100% |
| Prompt 约束强度(CFG) | 10 | 10 - 10 | 23 | 100% |
| 采样算法 | 1 | 1 - 1 | 23 | 100% |
| 调度器 | euler | - | 23 | 100% |
| 重绘幅度 | simple | - | 23 | 100% |
| 宽度 | 512 | 512 - 512 | 23 | 100% |
| 高度 | 768 | 768 - 768 | 23 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，23 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 10，23 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，23 个样本，一致性 100%
- 重绘幅度 最常用 simple，23 个样本，一致性 100%
- 宽度 中位数 512，观测区间 512 - 512，23 个样本，取值集中（一致性 100%）
- 高度 中位数 768，观测区间 768 - 768，23 个样本，取值集中（一致性 100%）
