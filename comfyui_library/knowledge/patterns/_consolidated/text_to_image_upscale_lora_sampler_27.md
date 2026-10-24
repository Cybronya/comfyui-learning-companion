---
name: text_to_image_upscale_lora_sampler_27
type: Text To Image
frequency: 7
level: strong
coverage: 0.947
common_nodes: [CLIPTextEncode, CR Latent Batch Size, CR Latent Input Switch, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, ImageUpscaleWithModel, ImpactInt, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX.1 Kontext商业级印花_纹理提取工作_2055163655582429186.json, 图片生成/图生图/印花提取_kontext_1955092292547874818.json, 图片生成/图生图/服装产品提取_kontext_1972140716925382657.json, 图片生成/图生图/服装提取_kontext_1955086376859570177.json, 图片生成/图生图/线稿提取_kontext_1955083266447609857.json, 图片生成/文生图/服装提取_1989951791611736065.json, 图片生成/文生图/服装提取_内部用_1967455597295702017.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_27

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/FLUX.1 Kontext商业级印花_纹理提取工作_2055163655582429186.json、图片生成/图生图/印花提取_kontext_1955092292547874818.json、图片生成/图生图/服装产品提取_kontext_1972140716925382657.json、图片生成/图生图/服装提取_kontext_1955086376859570177.json、图片生成/图生图/线稿提取_kontext_1955083266447609857.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Latent Batch Size`
- `CR Latent Input Switch`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageUpscaleWithModel`
- `ImpactInt`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerMask: SegformerB2ClothesUltra` —— 6/7 个有
- `LayerUtility: CropByMask V2` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `ResizeLongestToNode` —— 4/7 个有
- `LayerUtility: PurgeVRAM` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `1hew_AnySwitchSelect` —— 1/7 个有
- `Int` —— 1/7 个有
- `LayerUtility: ImageAutoCrop V2` —— 1/7 个有
- `Text` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 768 | 768 - 1440 | 7 | 74% |
| 高度 | 1024 | 1024 - 1440 | 7 | 87% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 1440，7 个样本
- 高度 中位数 1024，观测区间 1024 - 1440，7 个样本，取值集中（一致性 87%）
