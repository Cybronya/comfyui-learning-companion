---
name: unknown_workflow_inpaint_sampler_clip_8
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.826444
common_nodes: [Anything Everywhere, CLIPTextEncode, DualCLIPLoader, FaceParse(FaceParsing), FaceParsingModelLoader(FaceParsing), FaceParsingProcessorLoader(FaceParsing), FaceParsingResultsParser(FaceParsing), FluxGuidance, Image Comparer (rgthree), ImageToMask, ImpactGaussianBlurMask, InpaintModelConditioning, KSampler, LayerUtility: ColorImage, LayerUtility: ImageBlendAdvance, LoadImage, MaskPreview+, MaskToImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, easy imageSize, 取色器_孤海]
problems: []
missing: []
members: [图片生成/图生图/flux2-Klein9b-人像磨皮-真实皮肤_2069335361314181121.json, 图片生成/图生图/flux2Klein9B人像精修皮肤添加真实感细节_2064499608063135746.json, 图片生成/图生图/flux2Klein9B磨皮人像精修皮肤添加真实感细节_2062719097502265345.json, 图片生成/图生图/flux2Klein9B磨皮人像精修皮肤添加真实感细节_2063812992285888514.json, 图片生成/图生图/flux2Klein9B磨皮人像精修皮肤添加真实感细节_2093237112207396866.json, 图片生成/图生图/flux2Klein9B磨皮人像精修皮肤添加真实感细节_2093508562092912642.json, 图片生成/图生图/人像磨皮精修  Flux2人像精修皮肤添加真实感细节_2064916544941019138.json, 图片生成/图生图/人像精修磨皮 皮肤增加真实感细节 去除AI塑料感 Klein9B  图片去除Ai感_2067437441396596737.json, 图片生成/图生图/人像精修磨皮 皮肤增加真实感细节 去除AI塑料感（ Klein9B）_2067154115523858434.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_8

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/flux2-Klein9b-人像磨皮-真实皮肤_2069335361314181121.json、图片生成/图生图/flux2Klein9B人像精修皮肤添加真实感细节_2064499608063135746.json、图片生成/图生图/flux2Klein9B磨皮人像精修皮肤添加真实感细节_2062719097502265345.json、图片生成/图生图/flux2Klein9B磨皮人像精修皮肤添加真实感细节_2063812992285888514.json、图片生成/图生图/flux2Klein9B磨皮人像精修皮肤添加真实感细节_2093237112207396866.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 9 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FaceParse(FaceParsing)`
- `FaceParsingModelLoader(FaceParsing)`
- `FaceParsingProcessorLoader(FaceParsing)`
- `FaceParsingResultsParser(FaceParsing)`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageToMask`
- `ImpactGaussianBlurMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ColorImage`
- `LayerUtility: ImageBlendAdvance`
- `LoadImage`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`
- `取色器_孤海`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ColorPicker` —— 8/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 9 | 100% |
| 重绘幅度 | 0.45 | 0.45 - 0.45 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，9 个样本，一致性 100%
- 重绘幅度 中位数 0.45，观测区间 0.45 - 0.45，9 个样本，取值集中（一致性 100%）
