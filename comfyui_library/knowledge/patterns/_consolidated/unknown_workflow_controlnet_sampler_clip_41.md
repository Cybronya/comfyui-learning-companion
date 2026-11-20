---
name: unknown_workflow_controlnet_sampler_clip_41
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.882
common_nodes: [AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncodeFlux, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux-平面IP生成毛绒玩具效果图_1913101896712712194.json, 平台全量/FLUX 3D_ Your Superstar by 金运_1834116804837863426.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_41

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/flux-平面IP生成毛绒玩具效果图_1913101896712712194.json、平台全量/FLUX 3D_ Your Superstar by 金运_1834116804837863426.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageCrop` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `ImpactLatentInfo` —— 1/2 个有
- `Joy_caption` —— 1/2 个有
- `Joy_caption_load` —— 1/2 个有
- `Lora Loader Stack (rgthree)` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `ttN concat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.65 | - | 2 | 77% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.65，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
