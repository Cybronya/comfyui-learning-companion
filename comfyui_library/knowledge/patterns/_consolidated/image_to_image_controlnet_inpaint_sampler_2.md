---
name: image_to_image_controlnet_inpaint_sampler_2
type: Image To Image
frequency: 12
level: moderate
coverage: 0.795333
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, ImageAndMaskPreview, ImageConcanate, ImagePadForOutpaint, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen按比例无损扩图-指定长宽_1997281629649453057.json, 图片生成/图生图/ai扩图应用版_1985252354868002817.json, 图片生成/图生图/一键无缝扩图_1985686454313594882.json, 图片生成/图生图/扩图Qwen Image InstanX_加速版_双节棍版本_1971387798001532929.json, 图片生成/图生图/扩图Qwen Image InstanX_加速版_双节棍版本_2090289911185362945.json, 图片生成/图生图/扩图Qwen_Image_InstanX_加速版_双节棍版本_2091708724745424897.json, 图片生成/图生图/扩图Qwen_Image_InstanX_加速版_双节棍版本_2091841005497700353.json, 图片生成/图生图/扩图Qwen_Image_InstanX_加速版_双节棍版本_2108764571812061186.json, 图片生成/图生图/扩图Qwen_Image_InstanX_加速版_双节棍版本_2110556288672428033.json, 图片生成/图生图/扩图加速版_双节棍版本Qwen Image InstanX__1996444349015670785.json, 图片生成/图生图/无限画布-扩图Qwen Image_2065988771551731713.json, 图片生成/图生图/🦖Qwen超强扩图 （可选比例）_1968202243537272833.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_sampler_2

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen按比例无损扩图-指定长宽_1997281629649453057.json、图片生成/图生图/ai扩图应用版_1985252354868002817.json、图片生成/图生图/一键无缝扩图_1985686454313594882.json、图片生成/图生图/扩图Qwen Image InstanX_加速版_双节棍版本_1971387798001532929.json、图片生成/图生图/扩图Qwen Image InstanX_加速版_双节棍版本_2090289911185362945.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `ImageAndMaskPreview`
- `ImageConcanate`
- `ImagePadForOutpaint`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 11/12 个有
- `LoraLoaderModelOnly` —— 11/12 个有
- `NunchakuQwenImageDiTLoader` —— 10/12 个有
- `Bjornulf_ShowInt` —— 2/12 个有
- `ImageResize+` —— 2/12 个有
- `MathExpression|pysssss` —— 2/12 个有
- `PDIMAGE_LongerSize` —— 2/12 个有
- `Convert Masks to Images` —— 1/12 个有
- `FluxResolutionNode` —— 1/12 个有
- `GetImageSizeAndCount` —— 1/12 个有
- `Int` —— 1/12 个有
- `PreviewAny` —— 1/12 个有
- `SimpleMath+` —— 1/12 个有
- `YCMaskComposite` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 12 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 12 | 55% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，12 个样本
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（10/12 个样本）：Steps较低可能导致细节不足
