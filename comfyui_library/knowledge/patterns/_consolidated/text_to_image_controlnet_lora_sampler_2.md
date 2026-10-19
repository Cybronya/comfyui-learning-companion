---
name: text_to_image_controlnet_lora_sampler_2
type: Text To Image
frequency: 3
level: strong
coverage: 0.835
common_nodes: [CLIPTextEncode, CLIPTextEncodeFlux, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, Joy_caption_two, Joy_caption_two_load, KSampler, LayerMask: SegmentAnythingUltra V2, LayerUtility: ColorPicker, LayerUtility: ImageRemoveAlpha, LoadImage, LoraLoader, PreviewImage, SaveImage, SetShakkerLabsUnionControlNetType, Text Concatenate (JPS), TextInput_, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/Canny _  FLUX_CN 2.0_1900592230405390338.json, 图片生成/文生图/Depth 深度 _  FLUX_CN 2.0_1900600906277363713.json, 图片生成/文生图/F.1-CN-PuLID-joy2_1890278258015973378.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Canny _  FLUX_CN 2.0_1900592230405390338.json、图片生成/文生图/Depth 深度 _  FLUX_CN 2.0_1900600906277363713.json、图片生成/文生图/F.1-CN-PuLID-joy2_1890278258015973378.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `SaveImage`
- `SetShakkerLabsUnionControlNetType`
- `Text Concatenate (JPS)`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Canny` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `ApplyPulidFlux` —— 1/3 个有
- `ConstrainImage|pysssss` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `DepthAnythingV2Preprocessor` —— 1/3 个有
- `Fast Bypasser (rgthree)` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/3 个有
- `PulidFluxEvaClipLoader` —— 1/3 个有
- `PulidFluxInsightFaceLoader` —— 1/3 个有
- `PulidFluxModelLoader` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | 0.7 - 0.8 | 3 | 94% |
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 768 - 1024 | 3 | 87% |
| 高度 | 1536 | 1024 - 1536 | 3 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.7，观测区间 0.7 - 0.8，3 个样本，取值集中（一致性 94%）
- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 1024，3 个样本，取值集中（一致性 87%）
- 高度 中位数 1536，观测区间 1024 - 1536，3 个样本，取值集中（一致性 82%）
