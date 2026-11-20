---
name: image_to_image_controlnet_inpaint_lora
type: Image To Image
frequency: 13
level: moderate
coverage: 0.849
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, ImageAndMaskPreview, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/中文文字重绘-QWen-Image-Instantx-Controlnet_1966363579702259713.json, 图片生成/图生图/人物换背景-QWen-Image-Instantx-Controlnet_1966295550452822018.json, 图片生成/图生图/千问局部重绘工作流_2005603751757053954.json, 图片生成/图生图/千问局部重绘工作流_2010317606443552769.json, 图片生成/图生图/局部重绘-QWen-Image-Instantx-Controlnet_1966292208708128769.json, 图片生成/图生图/局部重绘-QWen-Image-Instantx-Controlnet_1971006146779717633.json, 图片生成/图生图/局部重绘-QWen-Image-Instantx-Controlnet_2028275236034060289.json, 图片生成/图生图/局部重绘-QWen-Image【Instantx-Controlnet】_1966421780745400322.json, 图片生成/图生图/扩图重绘-QWen-Image-Instantx-Controlnet_1966296641936461825.json, 图片生成/图生图/扩图重绘-千问-Image-【Instantx-Controlnet】_1966428766404816897.json, 图片生成/图生图/调色局部重绘-QWen-Image-Instantx-Controlnet_2026552365544902657.json, 图片生成/文生图/局部重绘_1968599107654832130.json, 平台全量/Qwen-Image扩图（可以要求扩图后的效果）_1966393040736825345.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/中文文字重绘-QWen-Image-Instantx-Controlnet_1966363579702259713.json、图片生成/图生图/人物换背景-QWen-Image-Instantx-Controlnet_1966295550452822018.json、图片生成/图生图/千问局部重绘工作流_2005603751757053954.json、图片生成/图生图/千问局部重绘工作流_2010317606443552769.json、图片生成/图生图/局部重绘-QWen-Image-Instantx-Controlnet_1966292208708128769.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `ImageAndMaskPreview`
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
- `ImageStitch` —— 10/13 个有
- `ImagePadForOutpaint` —— 3/13 个有
- `ConditioningZeroOut` —— 2/13 个有
- `PDImageResizeV2` —— 2/13 个有
- `DF_Float` —— 1/13 个有
- `ImageScaleToTotalPixels` —— 1/13 个有
- `InvertMask` —— 1/13 个有
- `MaskPreview` —— 1/13 个有
- `easy imageRemBg` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 13 | 71% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 13 | 71% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，13 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，13 个样本
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
