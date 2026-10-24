---
name: unknown_workflow_sampler_clip_unet_358
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.804333
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, PreviewImage, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/手动去角标水印+高清放大_2000650421381328898.json, 图片生成/图生图/构图参考（厨房风格模型）_2000773431815700482.json, 图片生成/文生图/Flux1-Dev-SRPO FP8版本工作流_1968745066112143361.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_358

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/手动去角标水印+高清放大_2000650421381328898.json、图片生成/图生图/构图参考（厨房风格模型）_2000773431815700482.json、图片生成/文生图/Flux1-Dev-SRPO FP8版本工作流_1968745066112143361.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `InpaintModelConditioning` —— 1/3 个有
- `InstructPixToPixConditioning` —— 1/3 个有
- `ModelSamplingFlux` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 40 | 3 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 40，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
