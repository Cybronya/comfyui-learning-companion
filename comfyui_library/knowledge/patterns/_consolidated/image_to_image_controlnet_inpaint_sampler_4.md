---
name: image_to_image_controlnet_inpaint_sampler_4
type: Image To Image
frequency: 10
level: strong
coverage: 0.8708
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Nunchaku_局部重绘Qwen Image InstanX_加速版_双节棍版本_1971494923574951938.json, 平台全量/Qwen 局部重绘工作流2.0_1966781068697382913.json, 平台全量/Qwen 无限扩图工作流_1967035456913281025.json, 平台全量/Qwen-inpaint扩图_1966392412677582850.json, 平台全量/千问-扩图_Qwen-Image-Instantx-ControlNet-Inpainting_1944953395129278466.json, 平台全量/增强版Qwen-image最强扩图 扩图Qwen+Image+InstanX_加速版_双节棍版本_1999309377121157122.json, 平台全量/扩图+效果无敌+速度超快_1996918021040062466.json, 平台全量/扩图Qwen Image InstanX_加速版_双节棍版本_1966328182372806658.json, 平台全量/竖版极速扩图(向下)Qwen Image InstanX_1990090695505530882.json, 平台全量/超强扩图 加速版 +局部重绘功能 Qwen Image InstanX双节棍版_2039149487368708098.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_sampler_4

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Nunchaku_局部重绘Qwen Image InstanX_加速版_双节棍版本_1971494923574951938.json、平台全量/Qwen 局部重绘工作流2.0_1966781068697382913.json、平台全量/Qwen 无限扩图工作流_1967035456913281025.json、平台全量/Qwen-inpaint扩图_1966392412677582850.json、平台全量/千问-扩图_Qwen-Image-Instantx-ControlNet-Inpainting_1944953395129278466.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/10 个有
- `ImagePadForOutpaint` —— 8/10 个有
- `LoraLoaderModelOnly` —— 8/10 个有
- `PreviewImage` —— 7/10 个有
- `NunchakuQwenImageDiTLoader` —— 6/10 个有
- `ImageAndMaskPreview` —— 5/10 个有
- `LayerUtility: PurgeVRAM` —— 5/10 个有
- `ImageConcanate` —— 4/10 个有
- `CFGNorm` —— 2/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有
- `ImageScaleToTotalPixels` —— 1/10 个有
- `Mask Fill Holes` —— 1/10 个有
- `MaskToImage` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 10 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，10 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
