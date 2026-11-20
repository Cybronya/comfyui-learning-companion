---
name: image_to_image_upscale_lora_sampler_40
type: Image To Image
frequency: 4
level: strong
coverage: 0.8875
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, Float, FluxGuidance, Image Comparer (rgthree), JDCN_StringToList, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, PreviewAny, PreviewImage, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VAEEncodeBatched, easy int]
problems: []
missing: []
members: [图片生成/图生图/FLUX+WAN2.2高清放大修复细节_2064895041612632065.json, 图片生成/图生图/FLUX+WAN2.2高清放大修复细节_2064919590370631682.json, 图片生成/图生图/图片超高清放大·无损分辨率_2014207050292666370.json, 图片生成/图生图/图片超高清放大·无损分辨率_2015409756227248129.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_40

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX+WAN2.2高清放大修复细节_2064895041612632065.json、图片生成/图生图/FLUX+WAN2.2高清放大修复细节_2064919590370631682.json、图片生成/图生图/图片超高清放大·无损分辨率_2014207050292666370.json、图片生成/图生图/图片超高清放大·无损分辨率_2015409756227248129.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Float`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `JDCN_StringToList`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `PreviewAny`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VAEEncodeBatched`
- `easy int`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
