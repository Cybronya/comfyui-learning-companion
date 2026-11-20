---
name: image_to_image_controlnet_inpaint_lora_13
type: Image To Image
frequency: 3
level: moderate
coverage: 0.827333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ControlNetInpaintingAliMamaApply, ControlNetLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2030843688124948482.json, 图片生成/文生图/重绘_1978010668211261442.json, 数字人/数字人/重绘_1978017926974504962.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/2030843688124948482.json、图片生成/文生图/重绘_1978010668211261442.json、数字人/数字人/重绘_1978017926974504962.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GrowMaskWithBlur` —— 2/3 个有
- `InpaintPreprocessor` —— 2/3 个有
- `SetLatentNoiseMask` —— 2/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImagePadForOutpaint` —— 1/3 个有
- `NunchakuQwenImageDiTLoader` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 3 | 65% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 3 | 65% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
