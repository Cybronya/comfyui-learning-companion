---
name: unknown_workflow_lora_sampler_unet_132
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.904167
common_nodes: [BasicGuider, CLIPLoader, GH_CropRestore, GH_MaskCropV2, Get Image Size, GulfSeaImageMergeMask, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ColorImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImage21GH, UNETLoader, VAEDecode, VAELoader, 图像缩放V2_孤海, 图像缩放范围孤海]
problems: []
missing: []
members: [图片生成/图生图/Qwen-image 2.1 零偏移物体移除和局部重绘_2114593938492448769.json, 图片生成/图生图/Qwen-image 2.1 零偏移物体移除和局部重绘_2114615796927393794.json, 图片生成/图生图/Qwen-image_2.1_零偏移物体移除和局部重绘_2115616524726784002.json, 图片生成/图生图/Qwen-image_2.1_零偏移物体移除和局部重绘_2115664539189600257.json, 平台全量/移除_1890359830995968002.json, 平台全量/表情替换_2119984629083107330.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_132

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen-image 2.1 零偏移物体移除和局部重绘_2114593938492448769.json、图片生成/图生图/Qwen-image 2.1 零偏移物体移除和局部重绘_2114615796927393794.json、图片生成/图生图/Qwen-image_2.1_零偏移物体移除和局部重绘_2115616524726784002.json、图片生成/图生图/Qwen-image_2.1_零偏移物体移除和局部重绘_2115664539189600257.json、平台全量/移除_1890359830995968002.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `GH_CropRestore`
- `GH_MaskCropV2`
- `Get Image Size`
- `GulfSeaImageMergeMask`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerUtility: ColorImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImage21GH`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `图像缩放V2_孤海`
- `图像缩放范围孤海`

**可变部分**（部分 workflow 才有）：
- `DF_Text_Box` —— 5/6 个有
- `QwenImage21SageAttentionT8` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `LoadImage` —— 4/6 个有
- `WujiCleaner` —— 4/6 个有
- `WujiUpscaler2` —— 4/6 个有
- `LoadImageGoohai` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `GoohaiRatioAndResolution` —— 1/6 个有
- `GoohaiRouteBlocker` —— 1/6 个有
- `Image Overlay` —— 1/6 个有
- `KSampler` —— 1/6 个有
- `QwenImage21BlockCacheT8` —— 1/6 个有
- `QwenImage21SpectrumT8` —— 1/6 个有
- `RestoreQwenImage21GH` —— 1/6 个有
- `SplitImageWithAlpha` —— 1/6 个有
- `孤海注释` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
