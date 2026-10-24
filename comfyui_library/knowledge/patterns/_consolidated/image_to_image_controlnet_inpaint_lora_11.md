---
name: image_to_image_controlnet_inpaint_lora_11
type: Image To Image
frequency: 3
level: moderate
coverage: 0.847667
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/万象Qwen 局部重绘＋无限扩图_1967901045248655362.json, 图片生成/图生图/中文文字重绘-QWen-Image-Instantx-Controlnet_1966363579702259713.json, 图片生成/图生图/人物换背景-QWen-Image-Instantx-Controlnet_1966295550452822018.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_11

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/万象Qwen 局部重绘＋无限扩图_1967901045248655362.json、图片生成/图生图/中文文字重绘-QWen-Image-Instantx-Controlnet_1966363579702259713.json、图片生成/图生图/人物换背景-QWen-Image-Instantx-Controlnet_1966295550452822018.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageAndMaskPreview` —— 2/3 个有
- `ImageStitch` —— 2/3 个有
- `CFGNorm` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImagePadForOutpaint` —— 1/3 个有
- `InvertMask` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `Mask Fill Holes` —— 1/3 个有
- `MaskPreview` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 6 - 20 | 3 | 57% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 3 | 65% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 6 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
