---
name: image_to_image_lora_sampler_clip_95
type: Image To Image
frequency: 3
level: strong
coverage: 0.920667
common_nodes: [CFGNorm, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, ImageScaleByAspectRatio_UTK, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, TextBoxNode_UTK, TextConcatenate_UTK, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext_美妆精修_1955498299379912705.json, 图片生成/图生图/Kontext_超级卸妆_1955185915981434882.json, 图片生成/图生图/Kontext_面部放大_1965713970420187138.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_95

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Kontext_美妆精修_1955498299379912705.json、图片生成/图生图/Kontext_超级卸妆_1955185915981434882.json、图片生成/图生图/Kontext_面部放大_1965713970420187138.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageScaleByAspectRatio_UTK`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `TextBoxNode_UTK`
- `TextConcatenate_UTK`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatenate_UTK` —— 2/3 个有
- `ImageUpscaleWithModel` —— 2/3 个有
- `LayerUtility: SaveImagePlus` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `NunchakuFluxDiTLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_multistep | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
