---
name: unknown_workflow_sampler_clip_unet_248
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6374
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DisableNoise, DualCLIPLoader, FlipSigmas, FluxForwardODESampler, FluxReverseODESampler, InFluxModelSamplingPred, LoadImage, OutFluxModelSamplingPred, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/10_产品精修_2074323611346882561.json, 图片生成/图生图/23.tonnie-flux万物精修、重塑_1997964839077208065.json, 图片生成/图生图/Flux逆采样修图_1926603675945570306.json, 图片生成/图生图/一键精修，图片精修_1961613590690205697.json, 图片生成/图生图/反差修图_2071109475523719169.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_248

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/10_产品精修_2074323611346882561.json、图片生成/图生图/23.tonnie-flux万物精修、重塑_1997964839077208065.json、图片生成/图生图/Flux逆采样修图_1926603675945570306.json、图片生成/图生图/一键精修，图片精修_1961613590690205697.json、图片生成/图生图/反差修图_2071109475523719169.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DisableNoise`
- `DualCLIPLoader`
- `FlipSigmas`
- `FluxForwardODESampler`
- `FluxReverseODESampler`
- `InFluxModelSamplingPred`
- `LoadImage`
- `OutFluxModelSamplingPred`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxDeGuidance` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `Joy_caption_two` —— 4/5 个有
- `Joy_caption_two_load` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `ImageBlend` —— 3/5 个有
- `LayerColor: Brightness & Contrast` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `easy hiresFix` —— 3/5 个有
- `easy imageSize` —— 3/5 个有
- `LayerMask: BiRefNetUltraV2` —— 2/5 个有
- `LayerMask: LoadBiRefNetModel` —— 2/5 个有
- `LoraLoader` —— 2/5 个有
- `PreviewBridge` —— 2/5 个有
- `ColorMatch` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `FluxGuidance` —— 1/5 个有
- `Get Image Size` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有
- `LayerMask: MaskPreview` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.95 | - | 2 | 95% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.95，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
