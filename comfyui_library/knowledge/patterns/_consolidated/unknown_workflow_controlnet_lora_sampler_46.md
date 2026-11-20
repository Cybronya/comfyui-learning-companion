---
name: unknown_workflow_controlnet_lora_sampler_46
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.844
common_nodes: [CLIPLoader, CannyEdgePreprocessor, DepthAnythingPreprocessor, Image Comparer (rgthree), ImagePadForOutpaint, ImageScaleToTotalPixels, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskPreview+, ModelPatchLoader, OpenposePreprocessor, PreviewImage, QwenImageDiffsynthControlnet, QwenImageIntegratedKSampler, SaveImage, UNETLoader, VAELoader, easy imageSize]
problems: []
missing: []
members: [平台全量/Qwen-Edit-2509-多功能合集_1983425100517187586.json, 平台全量/Qwen-Edit-2509-多功能合集_2012524375374827522.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_46

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Qwen-Edit-2509-多功能合集_1983425100517187586.json、平台全量/Qwen-Edit-2509-多功能合集_2012524375374827522.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CannyEdgePreprocessor`
- `DepthAnythingPreprocessor`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskPreview+`
- `ModelPatchLoader`
- `OpenposePreprocessor`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `QwenImageIntegratedKSampler`
- `SaveImage`
- `UNETLoader`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 1/2 个有
- `CLIPTextEncode` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `EmptyFlux2LatentImage` —— 1/2 个有
- `Flux2Scheduler` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `KSamplerSelect` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 图生图 image-to-image | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | 1472 | - | 2 | 100% |
| 调度器 | 1104 | - | 2 | 100% |
| 重绘幅度 | 7.95343e+14 | - | 2 | 68% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 图生图 image-to-image，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1472，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 1104，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 7.95343e+14，样本不足，未给区间，2 个样本
- 风险：重绘幅度 观测到 1.05324e+15，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
