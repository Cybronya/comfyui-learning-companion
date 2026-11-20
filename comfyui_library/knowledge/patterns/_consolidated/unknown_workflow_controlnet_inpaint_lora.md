---
name: unknown_workflow_controlnet_inpaint_lora
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.880056
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageCrop, InpaintModelConditioning, KSampler, LayerUtility: CropByMask V2, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleRestore V2, LayerUtility: RestoreCropBox, LoadImage, ReduxAdvanced, SaveImage, SetUnionControlNetType, StyleModelLoader, VAELoader, easy cleanGpuUsed, easy makeImageForICLora]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/F1-双截棍-指定模特_1952233243020046337.json, 图片生成/图生图/F1-双截棍-模特生成-涂抹模特版_2011625900286156802.json, 图片生成/图生图/FLux 万物蒙层迁移 海报模特首饰展示_1935212163520987137.json, 图片生成/图生图/Flux Redux 首饰迁移｜模特展示_1933867823372656642.json, 图片生成/图生图/segment anything 局部重绘_2009913990259941378.json, 图片生成/图生图/万物迁移-涂抹版_2103667367531343874.json, 图片生成/图生图/万物迁移-涂抹版_2104848385386831874.json, 图片生成/图生图/万物迁移-涂抹版_2115282052957429761.json, 图片生成/图生图/产品场景人物迁移_1946528169655431169.json, 图片生成/图生图/人物迁移，模特换脸_2095325629901266946.json, 图片生成/图生图/人物迁移，模特换脸_2095428503754858498.json, 图片生成/图生图/图片-人物迁移_1960169430372265986.json, 图片生成/图生图/首饰饰品万物迁移｜Mask 蒙层_1947254447506345985.json, 平台全量/F1--高级版-模特生成-指定模特-指定动作-姿态_1920232709871046657.json, 平台全量/F1-双截棍-指定模特版_1920227628249452545.json, 平台全量/F1-高级版-模特生成-指定动作-深度_1920278900012945410.json, 平台全量/万物迁移-涂抹版_1931206756767039490.json, 平台全量/人物迁移_1920301033904607234.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_lora

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/F1-双截棍-指定模特_1952233243020046337.json、图片生成/图生图/F1-双截棍-模特生成-涂抹模特版_2011625900286156802.json、图片生成/图生图/FLux 万物蒙层迁移 海报模特首饰展示_1935212163520987137.json、图片生成/图生图/Flux Redux 首饰迁移｜模特展示_1933867823372656642.json、图片生成/图生图/segment anything 局部重绘_2009913990259941378.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 18 个 workflow 都包含：
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
- `ReduxAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `StyleModelLoader`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 17/18 个有
- `ImageConcanate` —— 17/18 个有
- `LayerUtility: ColorImage V2` —— 17/18 个有
- `PreviewImage` —— 17/18 个有
- `VAEDecode` —— 16/18 个有
- `ImageAndMaskPreview` —— 14/18 个有
- `LayerMask: LoadSegmentAnythingModels` —— 14/18 个有
- `LayerMask: SegmentAnythingUltra V3` —— 14/18 个有
- `NunchakuFluxDiTLoader` —— 14/18 个有
- `GrowMask` —— 11/18 个有
- `Mask Fill Holes` —— 11/18 个有
- `Anything Everywhere` —— 9/18 个有
- `DWPreprocessor` —— 9/18 个有
- `UNETLoader` —— 9/18 个有
- `AIO_Preprocessor` —— 8/18 个有
- `ImpactDilateMask` —— 7/18 个有
- `ImpactInt` —— 7/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/18 个有
- `VAEDecodeTiled` —— 7/18 个有
- `DifferentialDiffusion` —— 5/18 个有
- `GrowMaskWithBlur` —— 5/18 个有
- `LayerMask: MaskPreview` —— 5/18 个有
- `MaskComposite` —— 5/18 个有
- `ImageResizeKJ` —— 4/18 个有
- `LayerMask: SegmentAnythingUltra V2` —— 4/18 个有
- `LoraLoader` —— 4/18 个有
- `ImageComposite+` —— 3/18 个有
- `LayerUtility: ColorPicker` —— 3/18 个有
- `InvertMask (segment anything)` —— 2/18 个有
- `InvertMask` —— 1/18 个有
- `NunchakuFluxLoraLoader` —— 1/18 个有
- `RHHiddenNodes` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 0.7 - 1 | 18 | 83% |
| 采样步数 | 20 | 20 - 30 | 18 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/18 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 0.7 - 1，18 个样本，取值集中（一致性 83%）
- 采样步数 中位数 20，观测区间 20 - 30，18 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
