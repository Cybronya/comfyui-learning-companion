---
name: image_to_image_controlnet_inpaint_sampler_6
type: Image To Image
frequency: 7
level: strong
coverage: 0.797143
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ControlNetInpaintingAliMamaApply, ImagePadForOutpaint, KSampler, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/PS高阶-扩图（个人原创）_1900387378224164866.json, 图片生成/图生图/QWN扩图稳定版本_1969758555643518978.json, 图片生成/图生图/Qwen-image-扩图重绘-支持复杂背景_1967619940993961985.json, 平台全量/Qwen-image最强扩图1.0_1967573540822216705.json, 平台全量/Qwen-image最强扩图1.0_2030660374214742017.json, 平台全量/Qwen-image最强扩图_2033510118997889025.json, 平台全量/通义千问Qwen-image-扩图工作流【2025-9-13】_2009277064993574913.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_sampler_6

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/PS高阶-扩图（个人原创）_1900387378224164866.json、图片生成/图生图/QWN扩图稳定版本_1969758555643518978.json、图片生成/图生图/Qwen-image-扩图重绘-支持复杂背景_1967619940993961985.json、平台全量/Qwen-image最强扩图1.0_1967573540822216705.json、平台全量/Qwen-image最强扩图1.0_2030660374214742017.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetInpaintingAliMamaApply`
- `ImagePadForOutpaint`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 6/7 个有
- `ShowText|pysssss` —— 6/7 个有
- `Anything Everywhere3` —— 5/7 个有
- `RH_Captioner` —— 5/7 个有
- `ControlNetLoader` —— 4/7 个有
- `ImageScaleToTotalPixels` —— 4/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `RHHiddenNodes` —— 3/7 个有
- `GetImageSize+` —— 2/7 个有
- `GrowMaskWithBlur` —— 2/7 个有
- `ImpactInt` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `SetLatentNoiseMask` —— 2/7 个有
- `SolidMask` —— 2/7 个有
- `ByteDanceSeedreamNode` —— 1/7 个有
- `DownloadAndLoadFlorence2Model` —— 1/7 个有
- `Florence2Run` —— 1/7 个有
- `Qwen2.5VL` —— 1/7 个有
- `RH_LLMAPI_NODE` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | normal | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 normal，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
