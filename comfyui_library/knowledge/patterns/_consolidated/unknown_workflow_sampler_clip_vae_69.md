---
name: unknown_workflow_sampler_clip_vae_69
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.953
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/ControlnetUpscaleJoycaption_模型放大修复_1957004198078504961.json, 平台全量/Kontext 一键去水印_1943555461784498178.json, 平台全量/Kontext一键极速去水印_1952572470245175298.json, 平台全量/一键去除水印工作流_1942212918056521729.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_69

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/ControlnetUpscaleJoycaption_模型放大修复_1957004198078504961.json、平台全量/Kontext 一键去水印_1943555461784498178.json、平台全量/Kontext一键极速去水印_1952572470245175298.json、平台全量/一键去除水印工作流_1942212918056521729.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 3/4 个有
- `FluxKontextImageScale` —— 3/4 个有
- `GetImageSize+` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ReferenceLatent` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `ControlNetApplyAdvanced` —— 1/4 个有
- `ControlNetLoader` —— 1/4 个有
- `Get resolution [Crystools]` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `JoyCaption2` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `NunchakuFluxDiTLoader` —— 1/4 个有
- `NunchakuFluxLoraLoader` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
