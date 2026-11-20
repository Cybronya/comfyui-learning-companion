---
name: text_to_image_sampler_clip_vae_38
type: Text To Image
frequency: 2
level: weak
coverage: 0.923
common_nodes: [CLIPTextEncode, CLIPVisionLoader, Canny, DualCLIPLoader, EmptyLatentImage, Fast Bypasser (rgthree), FluxGuidance, GetImageSize, ImageScaleBy, InstructPixToPixConditioning, KSampler, LoadImage, NunchakuFluxDiTLoader, PreviewImage, RH_Translator, RMBG, ReduxAdvanced, SaveImage, StyleModelApply, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/Flux毛坯房虚拟装修(风格转换)_1940340995407876097.json, 平台全量/Kontext风格转换_1946146024585129985.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_38

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Flux毛坯房虚拟装修(风格转换)_1940340995407876097.json、平台全量/Kontext风格转换_1946146024585129985.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `Canny`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Bypasser (rgthree)`
- `FluxGuidance`
- `GetImageSize`
- `ImageScaleBy`
- `InstructPixToPixConditioning`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `PreviewImage`
- `RH_Translator`
- `RMBG`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DepthAnything_V2` —— 1/2 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
