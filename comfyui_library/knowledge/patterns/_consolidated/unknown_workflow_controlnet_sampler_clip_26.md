---
name: unknown_workflow_controlnet_sampler_clip_26
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.939333
common_nodes: [AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/转换风格，不改变构图 Controlnet union 2 串联工作流（深度图+线稿图）_1936410663122030594.json, 图片生成/文生图/FLUX ControlNet-Union-Pro-2.0 生图可控性增强流_1912691278339895298.json, 图片生成/文生图/最强Flux控制工作流_FLUX ControlNet-Union-Pro-2.0_1921750937419857922.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/转换风格，不改变构图 Controlnet union 2 串联工作流（深度图+线稿图）_1936410663122030594.json、图片生成/文生图/FLUX ControlNet-Union-Pro-2.0 生图可控性增强流_1912691278339895298.json、图片生成/文生图/最强Flux控制工作流_FLUX ControlNet-Union-Pro-2.0_1921750937419857922.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
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
- `EmptyLatentImage` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `ApplyFBCacheOnModel` —— 1/3 个有
- `ApplyIPAdapterFlux` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `GridLoras` —— 1/3 个有
- `IPAdapterFluxLoader` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `Text Concatenate (JPS)` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | 0.8 - 1 | 3 | 89% |
| 宽度 | 896 | - | 2 | 86% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.8，观测区间 0.8 - 1，3 个样本，取值集中（一致性 89%）
- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
