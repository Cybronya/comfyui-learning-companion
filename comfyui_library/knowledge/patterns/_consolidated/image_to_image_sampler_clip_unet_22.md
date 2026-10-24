---
name: image_to_image_sampler_clip_unet_22
type: Image To Image
frequency: 11
level: strong
coverage: 0.944909
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext [dev]极简基础工作流_1938804683022782466.json, 图片生成/图生图/Kontext dev  -remove watermark_1942780220313112578.json, 图片生成/图生图/Kontext dev  neon style_1942229764629278721.json, 图片生成/图生图/Kontext dev jojo anime style_1942206268469620738.json, 图片生成/图生图/Kontext dev 像素风格_1942206684389642242.json, 图片生成/图生图/Kontext 角色一致性多角度_1950003872502865922.json, 图片生成/图生图/flux_dev-fp8_1938610130756030465.json, 图片生成/图生图/kontext手办_1946110044947836930.json, 图片生成/图生图/手办盲盒超火模型——图片转3D手办模型_2046143930944720898.json, 图片生成/图生图/星蝶Q版画风一键转换工作流_1945724032648093697.json, 图片生成/图生图/转手办_1950076112036651010.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_22

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Kontext [dev]极简基础工作流_1938804683022782466.json、图片生成/图生图/Kontext dev  -remove watermark_1942780220313112578.json、图片生成/图生图/Kontext dev  neon style_1942229764629278721.json、图片生成/图生图/Kontext dev jojo anime style_1942206268469620738.json、图片生成/图生图/Kontext dev 像素风格_1942206684389642242.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 10/11 个有
- `ImageConcatMulti` —— 8/11 个有
- `RH_Translator` —— 7/11 个有
- `Text Multiline` —— 7/11 个有
- `ImageResize` —— 5/11 个有
- `LoraLoader` —— 3/11 个有
- `PreviewImage` —— 3/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/11 个有
- `RHHiddenNodes` —— 2/11 个有
- `ImagePadForOutpaint` —— 1/11 个有
- `ImageResize+` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `PreviewTextNode` —— 1/11 个有
- `easy seed` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 11 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| LoRA 模型强度 | 0.9 | 0.85 - 1 | 3 | 93% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，11 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.9，观测区间 0.85 - 1，3 个样本，取值集中（一致性 93%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
