---
name: unknown_workflow_lora_sampler_unet_282
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.903667
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler (Efficient), LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2, SeedVR2BlockSwap, TextEncodeQwenImageEditPlus, UNETLoader, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/一键服装迁移 Clothes Transfer QwenEdit_1981352549523570689.json, 平台全量/人物服装提取+迁移_1986009028218236929.json, 平台全量/动漫转真人QwenEdit2511_2003796223314305025.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_282

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/一键服装迁移 Clothes Transfer QwenEdit_1981352549523570689.json、平台全量/人物服装提取+迁移_1986009028218236929.json、平台全量/动漫转真人QwenEdit2511_2003796223314305025.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler (Efficient)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `TextEncodeQwenImageEdit` —— 2/3 个有
- `easy imageRemBg` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageStitch` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_multistep | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
