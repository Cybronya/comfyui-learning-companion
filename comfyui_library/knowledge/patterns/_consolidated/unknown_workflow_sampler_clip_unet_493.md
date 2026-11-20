---
name: unknown_workflow_sampler_clip_unet_493
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.896
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RHBatchImages:, RHUploadZip, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy forLoopEnd, easy forLoopStart, easy imageCount, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/在线批量人物换脸（全自动），开源顶级一致性flux.2 klein_2016775105338155009.json, 平台全量/Flux.2 Klein 4B 瞬间擦除水印+批量处理_2032703743040425985.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_493

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/在线批量人物换脸（全自动），开源顶级一致性flux.2 klein_2016775105338155009.json、平台全量/Flux.2 Klein 4B 瞬间擦除水印+批量处理_2032703743040425985.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RHBatchImages:`
- `RHUploadZip`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowInt` —— 1/2 个有
- `ColorToMask_UTK` —— 1/2 个有
- `DifferentialDiffusion` —— 1/2 个有
- `Get Image Size` —— 1/2 个有
- `ImageCropByMask` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RHExtractImage` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `RH_ExtractImage` —— 1/2 个有
- `easy batchAnything` —— 1/2 个有
- `kkGetImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
