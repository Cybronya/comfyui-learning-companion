---
name: image_to_image_upscale_lora_sampler_113
type: Image To Image
frequency: 2
level: weak
coverage: 0.981
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ConstrainImage|pysssss, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, NunchakuFluxDiTLoader, RH_Captioner, SaveImage, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/模糊图像高清放大【4K】_1965272626576936962.json, 图片生成/图生图/轻微模糊图像高清放大【4K】_1965275384780607490.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_113

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/模糊图像高清放大【4K】_1965272626576936962.json、图片生成/图生图/轻微模糊图像高清放大【4K】_1965275384780607490.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `NunchakuFluxDiTLoader`
- `RH_Captioner`
- `SaveImage`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `HYPIRImageRestoration` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `Upscale Model Loader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | kl_optimal | - | 2 | 100% |
| 重绘幅度 | 0.35 | - | 2 | 71% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 kl_optimal，2 个样本，一致性 100%
- 重绘幅度 中位数 0.35，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
