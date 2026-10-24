---
name: image_to_image_controlnet_inpaint_lora_6
type: Image To Image
frequency: 5
level: weak
coverage: 0.8586
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/37.tonnie-Qwen image扩图和重绘（效果不好）_2003855307208073217.json, 图片生成/图生图/72.tonnie-2512局部重绘_2010727383120220161.json, 图片生成/图生图/Qwen Image InstanX超强扩图_2073058803960074242.json, 图片生成/图生图/Qwen-image-2512局部重绘（邪修玩法须要抽卡）_2006558396165660674.json, 图片生成/图生图/Qwen-image-扩图重绘-支持复杂背景_1967619940993961985.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_6

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/37.tonnie-Qwen image扩图和重绘（效果不好）_2003855307208073217.json、图片生成/图生图/72.tonnie-2512局部重绘_2010727383120220161.json、图片生成/图生图/Qwen Image InstanX超强扩图_2073058803960074242.json、图片生成/图生图/Qwen-image-2512局部重绘（邪修玩法须要抽卡）_2006558396165660674.json、图片生成/图生图/Qwen-image-扩图重绘-支持复杂背景_1967619940993961985.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `CFGNorm` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `ImagePadForOutpaint` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `DifferentialDiffusion` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `Mask Fill Holes` —— 2/5 个有
- `MaskBlur+` —— 2/5 个有
- `SetLatentNoiseMask` —— 2/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `MaskFillHoles` —— 1/5 个有
- `Qwen2.5VL` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 25 | 5 | 32% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 5 | 54% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | beta | - | 5 | 40% |
| 重绘幅度 | 1 | 0.1 - 1 | 5 | 56% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 25，5 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 0.1 - 1，5 个样本
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
