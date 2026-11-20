---
name: unknown_workflow_upscale_clip_unet_8
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.550333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, Image Comparer (rgthree), PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Klein-12步超真实生图9B-True-V2-Ded-CKS_2039691867251544066.json, 图片生成/文生图/超真实生图Klein-9B-True-V2-bf16-25步_2039686701332832258.json, 平台全量/CG脸模（CG Face Model）_2038873216386600962.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_unet_8

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Klein-12步超真实生图9B-True-V2-Ded-CKS_2039691867251544066.json、图片生成/文生图/超真实生图Klein-9B-True-V2-bf16-25步_2039686701332832258.json、平台全量/CG脸模（CG Face Model）_2038873216386600962.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 2/3 个有
- `CR Simple Text Watermark` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `Int` —— 2/3 个有
- `KSamplerSelect` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `RandomNoise` —— 2/3 个有
- `SamplerCustomAdvanced` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `ClownsharKSampler_Beta` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | sgm_uniform | - | 1 | 100% |
| Prompt 约束强度(CFG) | 30 | - | 1 | 100% |
| 采样算法 | -1 | - | 1 | 100% |
| 调度器 | 1 | - | 1 | 100% |
| 重绘幅度 | 0.85 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
