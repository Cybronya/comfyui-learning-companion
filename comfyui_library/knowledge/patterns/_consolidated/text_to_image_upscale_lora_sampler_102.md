---
name: text_to_image_upscale_lora_sampler_102
type: Text To Image
frequency: 3
level: strong
coverage: 0.836
common_nodes: [Anything Everywhere3, CLIPTextEncode, CLIPTextEncodeFlux, ConditioningZeroOut, EmptyLatentImage, Florence2ModelLoader, Florence2Run, Image Batch, Image Lucy Sharpen, ImageCrop, ImageUpscaleWithModel, ImpactImageBatchToImageList, KSampler, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, PreviewImage, Prompts Everywhere, SaveImage, SimpleMath+, Text Concatenate, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader, easy imageSize, easy positive, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/文生图一致性角色多角度分镜【可反推图自动生成角色分镜】_1951178863873302529.json, 图片生成/文生图/文生图一致性角色多角度分镜【可反推图自动生成角色分镜】_1944008265967734786.json, 平台全量/文生图一致性人物多角度角色生成_1938046725879959553.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_102

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/文生图一致性角色多角度分镜【可反推图自动生成角色分镜】_1951178863873302529.json、图片生成/文生图/文生图一致性角色多角度分镜【可反推图自动生成角色分镜】_1944008265967734786.json、平台全量/文生图一致性人物多角度角色生成_1938046725879959553.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
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
- `KSampler`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `PreviewImage`
- `Prompts Everywhere`
- `SaveImage`
- `SimpleMath+`
- `Text Concatenate`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`
- `easy positive`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Int` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `easy textSwitch` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1440 | 1440 - 1440 | 3 | 100% |
| 高度 | 2000 | 2000 - 2000 | 3 | 100% |
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1440，观测区间 1440 - 1440，3 个样本，取值集中（一致性 100%）
- 高度 中位数 2000，观测区间 2000 - 2000，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
