---
name: image_to_image_upscale_lora_sampler_78
type: Image To Image
frequency: 2
level: weak
coverage: 0.8105
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Fast Groups Bypasser (rgthree), KSampler, Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PrimitiveInt, PrimitiveStringMultiline, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [图片生成/图生图/Krea 2 自动提示词反推洗图工作流(黑兽ContrilNet版)_2075048520431792129.json, 图片生成/图生图/Krea+2+自动提示词反推洗图工作流(黑兽latent版)_2074071317728555009.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_78

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Krea 2 自动提示词反推洗图工作流(黑兽ContrilNet版)_2075048520431792129.json、图片生成/图生图/Krea+2+自动提示词反推洗图工作流(黑兽latent版)_2074071317728555009.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `Label (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `DepthAnythingV2Preprocessor` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `Krea2ControlApply` —— 1/2 个有
- `Krea2ControlImageEncode` —— 1/2 个有
- `Krea2ControlLoRALoader` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.85 | - | 2 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
