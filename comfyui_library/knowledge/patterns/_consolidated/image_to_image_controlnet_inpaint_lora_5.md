---
name: image_to_image_controlnet_inpaint_lora_5
type: Image To Image
frequency: 6
level: strong
coverage: 0.903167
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【阡陌】Qwen image无痕局部重绘工作流_1970488186512285698.json, 图片生成/图生图/【阡陌】Qwen image无痕扩图工作流_1970498194360705025.json, 图片生成/图生图/图片定位去水印_2038258013731033090.json, 图片生成/图生图/🥨千问-QwenImage-InstantX-ControlNet外扩图片🥨_1966380144518705154.json, 图片生成/图生图/🥨千问-QwenImage-InstantX-ControlNet局部重绘🥨_1966372435891302401.json, 平台全量/【阡陌】Qwen image无痕去水印工作流_1970761428598726658.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_5

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/【阡陌】Qwen image无痕局部重绘工作流_1970488186512285698.json、图片生成/图生图/【阡陌】Qwen image无痕扩图工作流_1970498194360705025.json、图片生成/图生图/图片定位去水印_2038258013731033090.json、图片生成/图生图/🥨千问-QwenImage-InstantX-ControlNet外扩图片🥨_1966380144518705154.json、图片生成/图生图/🥨千问-QwenImage-InstantX-ControlNet局部重绘🥨_1966372435891302401.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerMask: MaskGrow` —— 5/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `ImageConcanate` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `ImageCompositeMasked` —— 2/6 个有
- `Note Plus (mtb)` —— 2/6 个有
- `GrowMaskWithBlur` —— 1/6 个有
- `ImagePadForOutpaint` —— 1/6 个有
- `ImagePadForOutpaintMasked` —— 1/6 个有
- `InpaintPreprocessor` —— 1/6 个有
- `PurgeVRAM_UTK` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 4 - 10 | 6 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 4 - 10，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
