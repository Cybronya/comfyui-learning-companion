---
name: text_to_image_controlnet_sampler_clip_18
type: Text To Image
frequency: 3
level: strong
coverage: 0.897
common_nodes: [AIO_Preprocessor, CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/写实唯美风参考动作生成图片洗图_1929105091276521473.json, 图片生成/图生图/毛坯房一键出图（可换风格）_1920152104714047490.json, 图片生成/文生图/01_参考生图_2074230063763116033.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/写实唯美风参考动作生成图片洗图_1929105091276521473.json、图片生成/图生图/毛坯房一键出图（可换风格）_1920152104714047490.json、图片生成/文生图/01_参考生图_2074230063763116033.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `SetUnionControlNetType` —— 2/3 个有
- `UltimateSDUpscale` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `DF_Image_scale_to_side` —— 1/3 个有
- `DifferentialDiffusion` —— 1/3 个有
- `FaceDetailer` —— 1/3 个有
- `ImageGenResolutionFromImage` —— 1/3 个有
- `LayerMask: LoadFlorence2Model` —— 1/3 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/3 个有
- `UltralyticsDetectorProvider` —— 1/3 个有
- `easy imageScaleDownToSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 800 | 768 - 1024 | 3 | 87% |
| 高度 | 1024 | 512 - 1368 | 3 | 64% |
| 采样步数 | 25 | 20 - 30 | 3 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 3 | 65% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.8 | 0.7 - 0.8 | 3 | 94% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 800，观测区间 768 - 1024，3 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 512 - 1368，3 个样本
- 采样步数 中位数 25，观测区间 20 - 30，3 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.8，观测区间 0.7 - 0.8，3 个样本，取值集中（一致性 94%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
