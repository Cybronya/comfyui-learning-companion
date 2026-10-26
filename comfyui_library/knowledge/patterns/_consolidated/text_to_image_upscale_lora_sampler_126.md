---
name: text_to_image_upscale_lora_sampler_126
type: Text To Image
frequency: 2
level: weak
coverage: 0.836
common_nodes: [Anything Everywhere3, CLIPTextEncode, CLIPTextEncodeFlux, ConditioningZeroOut, EmptyLatentImage, Florence2ModelLoader, Florence2Run, Image Batch, Image Lucy Sharpen, ImageCrop, ImageUpscaleWithModel, ImpactImageBatchToImageList, Int, KSampler, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, PreviewImage, Prompts Everywhere, RH_Captioner, RH_Translator, SaveImage, ShowText|pysssss, SimpleMath+, Text Concatenate, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader, easy imageSize, easy positive, easy showAnything, easy textSwitch]
problems: []
missing: []
members: [图片生成/图生图/文生图一致性角色多角度分镜【可反推图自动生成角色分镜】_1951178863873302529.json, 图片生成/文生图/文生图一致性角色多角度分镜【可反推图自动生成角色分镜】_1944008265967734786.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_126

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/文生图一致性角色多角度分镜【可反推图自动生成角色分镜】_1951178863873302529.json、图片生成/文生图/文生图一致性角色多角度分镜【可反推图自动生成角色分镜】_1944008265967734786.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `Image Batch`
- `Image Lucy Sharpen`
- `ImageCrop`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `Int`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `PreviewImage`
- `Prompts Everywhere`
- `RH_Captioner`
- `RH_Translator`
- `SaveImage`
- `ShowText|pysssss`
- `SimpleMath+`
- `Text Concatenate`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`
- `easy positive`
- `easy showAnything`
- `easy textSwitch`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1440 | - | 2 | 100% |
| 高度 | 2000 | - | 2 | 100% |
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1440，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 2000，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
