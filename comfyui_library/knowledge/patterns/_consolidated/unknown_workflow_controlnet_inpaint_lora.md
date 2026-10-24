---
name: unknown_workflow_controlnet_inpaint_lora
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.88275
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageCrop, InpaintModelConditioning, KSampler, LayerUtility: CropByMask V2, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleRestore V2, LayerUtility: RestoreCropBox, LoadImage, PreviewImage, ReduxAdvanced, SaveImage, SetUnionControlNetType, StyleModelLoader, VAELoader, easy cleanGpuUsed, easy makeImageForICLora]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/F1-双截棍-指定模特_1952233243020046337.json, 图片生成/图生图/F1-双截棍-模特生成-涂抹模特版_2011625900286156802.json, 图片生成/图生图/FLux 万物蒙层迁移 海报模特首饰展示_1935212163520987137.json, 图片生成/图生图/Flux Redux 首饰迁移｜模特展示_1933867823372656642.json, 图片生成/图生图/segment anything 局部重绘_2009913990259941378.json, 图片生成/图生图/万物迁移-涂抹版_2103667367531343874.json, 图片生成/图生图/万物迁移-涂抹版_2104848385386831874.json, 图片生成/图生图/产品场景人物迁移_1946528169655431169.json, 图片生成/图生图/人物迁移，模特换脸_2095325629901266946.json, 图片生成/图生图/人物迁移，模特换脸_2095428503754858498.json, 图片生成/图生图/图片-人物迁移_1960169430372265986.json, 图片生成/图生图/首饰饰品万物迁移｜Mask 蒙层_1947254447506345985.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_lora

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/F1-双截棍-指定模特_1952233243020046337.json、图片生成/图生图/F1-双截棍-模特生成-涂抹模特版_2011625900286156802.json、图片生成/图生图/FLux 万物蒙层迁移 海报模特首饰展示_1935212163520987137.json、图片生成/图生图/Flux Redux 首饰迁移｜模特展示_1933867823372656642.json、图片生成/图生图/segment anything 局部重绘_2009913990259941378.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageCrop`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleRestore V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `StyleModelLoader`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 11/12 个有
- `ImageConcanate` —— 11/12 个有
- `LayerUtility: ColorImage V2` —— 11/12 个有
- `NunchakuFluxDiTLoader` —— 10/12 个有
- `VAEDecode` —— 10/12 个有
- `ImageAndMaskPreview` —— 9/12 个有
- `LayerMask: LoadSegmentAnythingModels` —— 9/12 个有
- `LayerMask: SegmentAnythingUltra V3` —— 9/12 个有
- `Mask Fill Holes` —— 8/12 个有
- `GrowMask` —— 7/12 个有
- `DWPreprocessor` —— 6/12 个有
- `AIO_Preprocessor` —— 5/12 个有
- `Anything Everywhere` —— 5/12 个有
- `ImpactDilateMask` —— 5/12 个有
- `VAEDecodeTiled` —— 5/12 个有
- `ImpactInt` —— 4/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/12 个有
- `UNETLoader` —— 4/12 个有
- `DifferentialDiffusion` —— 3/12 个有
- `GrowMaskWithBlur` —— 3/12 个有
- `LayerMask: MaskPreview` —— 3/12 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/12 个有
- `LayerUtility: ColorPicker` —— 3/12 个有
- `MaskComposite` —— 3/12 个有
- `ImageResizeKJ` —— 2/12 个有
- `LoraLoader` —— 2/12 个有
- `ImageComposite+` —— 1/12 个有
- `InvertMask` —— 1/12 个有
- `NunchakuFluxLoraLoader` —— 1/12 个有
- `RHHiddenNodes` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 0.7 - 1 | 12 | 83% |
| 采样步数 | 20 | 20 - 30 | 12 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/12 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 0.7 - 1，12 个样本，取值集中（一致性 83%）
- 采样步数 中位数 20，观测区间 20 - 30，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
