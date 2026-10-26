---
name: image_to_image_controlnet_inpaint_sampler
type: Image To Image
frequency: 12
level: moderate
coverage: 0.877667
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Nunchaku-Qwen-Image-ControlNet-Inpainting 局部重绘_2073059743991681026.json, 图片生成/图生图/QWen-Image 局部重绘_1966848954535174146.json, 图片生成/图生图/Qwen Image InstanX超强扩图_2073058803960074242.json, 图片生成/图生图/Qwen Image InstanX超强重绘_2073058687467479042.json, 图片生成/图生图/Qwen Image InstantX Controlnet Inpainting 局部重绘_1968332939400499202.json, 图片生成/图生图/Qwen Image InstantX Controlnet inpaint 完美扩图_1966697557932060674.json, 图片生成/图生图/Qwen InstanX_扩图（双节棍加速）_1993594369395671041.json, 图片生成/图生图/Qwen+Image扩图_2003316383398100994.json, 图片生成/图生图/Qwen-Image-ControlNet-Inpainting支持_1966168675248148482.json, 图片生成/图生图/Qwen-Image-inpaint完美扩图_1966404970901876738.json, 图片生成/图生图/Qwen-Image-inpain完美扩图：无限视野！任意图像任意扩展_1967044379166826498.json, 图片生成/图生图/Qwen-Image-inpain完美扩图：无限视野，一键拓展你的视界！图生图_InstantX_1967024055033401346.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_sampler

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Nunchaku-Qwen-Image-ControlNet-Inpainting 局部重绘_2073059743991681026.json、图片生成/图生图/QWen-Image 局部重绘_1966848954535174146.json、图片生成/图生图/Qwen Image InstanX超强扩图_2073058803960074242.json、图片生成/图生图/Qwen Image InstanX超强重绘_2073058687467479042.json、图片生成/图生图/Qwen Image InstantX Controlnet Inpainting 局部重绘_1968332939400499202.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 11/12 个有
- `UNETLoader` —— 11/12 个有
- `PreviewImage` —— 8/12 个有
- `ImageAndMaskPreview` —— 7/12 个有
- `ImageConcanate` —— 7/12 个有
- `ImagePadForOutpaint` —— 7/12 个有
- `ImageScaleToTotalPixels` —— 7/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/12 个有
- `Image Comparer (rgthree)` —— 5/12 个有
- `LayerUtility: PurgeVRAM` —— 4/12 个有
- `LayerUtility: JoyCaptionBeta1` —— 3/12 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 3/12 个有
- `NunchakuQwenImageDiTLoader` —— 3/12 个有
- `easy cleanGpuUsed` —— 3/12 个有
- `CR Text` —— 2/12 个有
- `GrowMaskWithBlur` —— 2/12 个有
- `InpaintPreprocessor` —— 2/12 个有
- `LayerUtility: ImageBlend V2` —— 2/12 个有
- `SetLatentNoiseMask` —— 2/12 个有
- `Anything Everywhere3` —— 1/12 个有
- `LayerMask: MaskGrow` —— 1/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有
- `ShowText|pysssss` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 25 | 12 | 49% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 12 | 53% |
| 采样算法 | euler | - | 12 | 83% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 25，12 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，12 个样本
- 采样算法 最常用 euler，12 个样本，一致性 83%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（8/12 个样本）：Steps较低可能导致细节不足
