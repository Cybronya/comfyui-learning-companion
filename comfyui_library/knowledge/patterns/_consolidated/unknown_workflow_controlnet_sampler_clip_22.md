---
name: unknown_workflow_controlnet_sampler_clip_22
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.90975
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/转换风格，不改变构图 Controlnet union 2 串联工作流（深度图+线稿图）_1936410663122030594.json, 图片生成/文生图/FLUX ControlNet-Union-Pro-2.0 生图可控性增强流_1912691278339895298.json, 图片生成/文生图/最强Flux控制工作流_FLUX ControlNet-Union-Pro-2.0_1921750937419857922.json, 平台全量/图生图基础款_1910841538946002946.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/转换风格，不改变构图 Controlnet union 2 串联工作流（深度图+线稿图）_1936410663122030594.json、图片生成/文生图/FLUX ControlNet-Union-Pro-2.0 生图可控性增强流_1912691278339895298.json、图片生成/文生图/最强Flux控制工作流_FLUX ControlNet-Union-Pro-2.0_1921750937419857922.json、平台全量/图生图基础款_1910841538946002946.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 3/4 个有
- `EmptyLatentImage` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `ApplyFBCacheOnModel` —— 1/4 个有
- `ApplyIPAdapterFlux` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `DepthAnythingV2Preprocessor` —— 1/4 个有
- `GridLoras` —— 1/4 个有
- `IPAdapterFluxLoader` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `ModelSamplingFlux` —— 1/4 个有
- `Text Concatenate (JPS)` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | 0.6 - 1 | 4 | 82% |
| 宽度 | 768 | 512 - 1024 | 3 | 73% |
| 高度 | 1024 | 512 - 1024 | 3 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.8，观测区间 0.6 - 1，4 个样本，取值集中（一致性 82%）
- 宽度 中位数 768，观测区间 512 - 1024，3 个样本
- 高度 中位数 1024，观测区间 512 - 1024，3 个样本
