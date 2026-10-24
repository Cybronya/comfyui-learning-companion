---
name: text_to_image_upscale_sampler_clip_45
type: Text To Image
frequency: 2
level: weak
coverage: 0.952
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, Image Comparer (rgthree), ImageUpscaleWithModel, JoinStringMulti, KSampler, Label (rgthree), SaveImage, TTResolutionSelector, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/二次元狂喜！动漫美学工作流！_2057015345323536386.json, 图片生成/文生图/动漫美学！全能动漫风格任你选择_2078416233854234625.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/二次元狂喜！动漫美学工作流！_2057015345323536386.json、图片生成/文生图/动漫美学！全能动漫风格任你选择_2078416233854234625.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `JoinStringMulti`
- `KSampler`
- `Label (rgthree)`
- `SaveImage`
- `TTResolutionSelector`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1344 | - | 2 | 100% |
| 高度 | 768 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1344，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
