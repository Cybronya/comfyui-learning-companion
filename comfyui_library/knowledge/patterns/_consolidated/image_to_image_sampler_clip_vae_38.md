---
name: image_to_image_sampler_clip_vae_38
type: Image To Image
frequency: 3
level: strong
coverage: 0.867667
common_nodes: [CLIPTextEncode, Compositor3, CompositorConfig3, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, InspyrenetRembg, KSampler, KepStringLiteral, LoadImage, PreviewImage, RH_Translator, ReferenceLatent, SDXLEmptyLatentSizePicker+, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/nunchaku-Kontext-3倍加速_1940681407448641538.json, 图片生成/图生图/图像拼接与融合（Kontext&enricos-nodes）_1939667632876654594.json, 图片生成/图生图/图像融合-Kontext&ACE++_1940386465027174401.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_38

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/nunchaku-Kontext-3倍加速_1940681407448641538.json、图片生成/图生图/图像拼接与融合（Kontext&enricos-nodes）_1939667632876654594.json、图片生成/图生图/图像融合-Kontext&ACE++_1940386465027174401.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `Compositor3`
- `CompositorConfig3`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `InspyrenetRembg`
- `KSampler`
- `KepStringLiteral`
- `LoadImage`
- `PreviewImage`
- `RH_Translator`
- `ReferenceLatent`
- `SDXLEmptyLatentSizePicker+`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 2/3 个有
- `ACE_ImageFaceCrop` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `LayerMask: LoadSAM2Model` —— 1/3 个有
- `LayerMask: ObjectDetectorFL2` —— 1/3 个有
- `LayerMask: SAM2UltraV2` —— 1/3 个有
- `LoadFlorence2Model` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `NunchakuFluxDiTLoader` —— 1/3 个有
- `NunchakuFluxLoraLoader` —— 1/3 个有
- `RH_ComfyFluxKontext` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768x1280 (0.6) | - | 3 | 67% |
| 高度 | 1 | 1 - 1 | 3 | 100% |
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 最常用 768x1280 (0.6)，3 个样本，一致性 67%
- 高度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
