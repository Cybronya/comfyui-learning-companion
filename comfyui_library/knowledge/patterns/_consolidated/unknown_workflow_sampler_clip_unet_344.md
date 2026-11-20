---
name: unknown_workflow_sampler_clip_unet_344
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8265
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LoadImage, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: ["图片生成/图生图/老版三件套Flux,Redux,Clipvision双图融合加速可调权重工作流_1912460148080635906.json", 图片生成/文生图/Redux角色一致性_1901277660763275265.json, 平台全量/Flux 1 Dev Redux Merge Images_1889872068291309570.json, 平台全量/Flux_Style_Adjust+Redux+flux_1866029087566548993.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_344

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/老版三件套Flux,Redux,Clipvision双图融合加速可调权重工作流_1912460148080635906.json、图片生成/文生图/Redux角色一致性_1901277660763275265.json、平台全量/Flux 1 Dev Redux Merge Images_1889872068291309570.json、平台全量/Flux_Style_Adjust+Redux+flux_1866029087566548993.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 2/4 个有
- `StyleModelAdvancedApply` —— 2/4 个有
- `ApplyFBCacheOnModel` —— 1/4 个有
- `ConditioningAverage` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `Note Plus (mtb)` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `Switch any [Crystools]` —— 1/4 个有
- `Text Multiline` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
