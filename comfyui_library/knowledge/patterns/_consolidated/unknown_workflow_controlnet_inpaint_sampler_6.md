---
name: unknown_workflow_controlnet_inpaint_sampler_6
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.826833
common_nodes: [CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, EmptyLatentImage, GetImageSize, ImageConcanate, KSampler (Efficient), LayerFilter: HDREffects, LoadImage, ModelSamplingAuraFlow, PreviewImage, Prompts Everywhere, SaveImage, UNETLoader, VAELoader]
problems: []
missing: []
members: [平台全量/一键运行：Flux-dev-fp8-ControlNet-Inpainting 一键换背景_1971395067741192193.json, 平台全量/一键运行：Flux-dev-fp8-ControlNet-Inpainting 局部重绘，图像修复_1970306684570791937.json, 平台全量/一键运行：Flux-dev-fp8-ControlNet-Inpainting 扩图工作流图像修复_1970313299302772737.json, 平台全量/一键运行：Qwen-Image-ControlNet-Inpainting  扩图 ，修复_1967768450057854978.json, 平台全量/一键运行：QwenImage-InstantX-ControlNet 一键换背，抠图洗图_1967428728403922946.json, 平台全量/一键运行：QwenImage-InstantX-ControlNet局部重绘，图像修复，洗图_1967421346013700097.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler_6

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/一键运行：Flux-dev-fp8-ControlNet-Inpainting 一键换背景_1971395067741192193.json、平台全量/一键运行：Flux-dev-fp8-ControlNet-Inpainting 局部重绘，图像修复_1970306684570791937.json、平台全量/一键运行：Flux-dev-fp8-ControlNet-Inpainting 扩图工作流图像修复_1970313299302772737.json、平台全量/一键运行：Qwen-Image-ControlNet-Inpainting  扩图 ，修复_1967768450057854978.json、平台全量/一键运行：QwenImage-InstantX-ControlNet 一键换背，抠图洗图_1967428728403922946.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `EmptyLatentImage`
- `GetImageSize`
- `ImageConcanate`
- `KSampler (Efficient)`
- `LayerFilter: HDREffects`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `Prompts Everywhere`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `ApplyFBCacheOnModel` —— 3/6 个有
- `CLIPLoader` —— 3/6 个有
- `DualCLIPLoader` —— 3/6 个有
- `BiRefNet_Hugo` —— 2/6 个有
- `ImagePadForOutpaint` —— 2/6 个有
- `InvertMask` —— 2/6 个有
- `GrowMaskWithBlur` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 8 - 20 | 6 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 6 | 55% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 512 | 512 - 512 | 6 | 100% |
| 高度 | 512 | 512 - 512 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 15，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，6 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，6 个样本，取值集中（一致性 100%）
