---
name: text_to_image_lora_sampler_clip_378
type: Text To Image
frequency: 2
level: weak
coverage: 0.789
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningKrea2Rebalance, ConditioningZeroOut, DepthAnythingV2Preprocessor, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler, Krea2ControlApply, Krea2ControlImageEncode, Krea2ControlLoRALoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewAny, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-深度控制文生图_2077200610818088962.json, 图片生成/文生图/Krea2-深度控制文生图_2078085516737736705.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_378

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Krea2-深度控制文生图_2077200610818088962.json、图片生成/文生图/Krea2-深度控制文生图_2078085516737736705.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningKrea2Rebalance`
- `ConditioningZeroOut`
- `DepthAnythingV2Preprocessor`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler`
- `Krea2ControlApply`
- `Krea2ControlImageEncode`
- `Krea2ControlLoRALoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewAny`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
