---
name: image_to_image_controlnet_inpaint_lora_3
type: Image To Image
frequency: 9
level: moderate
coverage: 0.853556
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image InstanX超强重绘_2073058687467479042.json, 图片生成/图生图/Qwen Image InstantX Controlnet Inpainting 局部重绘_1968332939400499202.json, 图片生成/图生图/Qwen Image InstantX Controlnet inpaint 完美扩图_1966697557932060674.json, 图片生成/图生图/Qwen InstanX_扩图（双节棍加速）_1993594369395671041.json, 图片生成/图生图/Qwen+Image扩图_2003316383398100994.json, 图片生成/图生图/Qwen-Image-ControlNet-Inpainting支持_1966168675248148482.json, 图片生成/图生图/Qwen-Image-inpaint完美扩图_1966404970901876738.json, 图片生成/图生图/Qwen-Image-inpain完美扩图：无限视野！任意图像任意扩展_1967044379166826498.json, 图片生成/图生图/Qwen-Image-inpain完美扩图：无限视野，一键拓展你的视界！图生图_InstantX_1967024055033401346.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_3

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen Image InstanX超强重绘_2073058687467479042.json、图片生成/图生图/Qwen Image InstantX Controlnet Inpainting 局部重绘_1968332939400499202.json、图片生成/图生图/Qwen Image InstantX Controlnet inpaint 完美扩图_1966697557932060674.json、图片生成/图生图/Qwen InstanX_扩图（双节棍加速）_1993594369395671041.json、图片生成/图生图/Qwen+Image扩图_2003316383398100994.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
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
- `ImageAndMaskPreview` —— 7/9 个有
- `ImageConcanate` —— 7/9 个有
- `PreviewImage` —— 7/9 个有
- `ImagePadForOutpaint` —— 6/9 个有
- `ImageScaleToTotalPixels` —— 6/9 个有
- `Image Comparer (rgthree)` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/9 个有
- `LayerUtility: JoyCaptionBeta1` —— 3/9 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 3/9 个有
- `LayerUtility: PurgeVRAM` —— 3/9 个有
- `easy cleanGpuUsed` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `GrowMaskWithBlur` —— 2/9 个有
- `InpaintPreprocessor` —— 2/9 个有
- `LayerUtility: ImageBlend V2` —— 2/9 个有
- `NunchakuQwenImageDiTLoader` —— 2/9 个有
- `SetLatentNoiseMask` —— 2/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `LayerMask: MaskGrow` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `ShowText|pysssss` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 9 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 9 | 60% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（7/9 个样本）：Steps较低可能导致细节不足
