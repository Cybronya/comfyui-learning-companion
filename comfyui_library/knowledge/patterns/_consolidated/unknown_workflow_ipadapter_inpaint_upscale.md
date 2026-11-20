---
name: unknown_workflow_ipadapter_inpaint_upscale
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.803333
common_nodes: [BasicGuider, BasicScheduler, CFGZeroStar, CLIPTextEncode, CLIPTextEncodeFlux, DifferentialDiffusion, DualCLIPLoader, FaceAutoFitSingle, FluxGuidance, IPAdapterFaceID, IPAdapterUnifiedLoader, ImageToMask, ImageUpscaleWithModel, InpaintModelConditioning, Int, InvertMask, JoinStringMulti, KSampler, KSamplerSelect, LayerMask: LoadFlorence2Model, LayerMask: MaskGrow, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LayerUtility: ColorImage V2, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: JoyCaptionBeta1, LayerUtility: LaMa, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: PurgeVRAM, LayerUtility: TextBox, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, MaskPreview+, MathExpression|pysssss, PreviewImage, RandomNoise, RepeatLatentBatch, SamplerCustomAdvanced, SaveImage, String, Text _O, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy cleanGpuUsed, easy compare, easy ifElse, easy imageSizeByLongerSide, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/CHAOS FLUX皮克斯风格人物风格转移 多幅画布构图扩图工作流_1934436815535304705.json, 平台全量/CHAOS 像素风风格 多幅画布构图 人物风格转移扩图工作流_1934552443927601154.json, 平台全量/CHAOS 手绘风格 多幅画布构图 人物风格转移扩图工作流_1936053661846114306.json]
source: knowledge_consolidation
---

# unknown_workflow_ipadapter_inpaint_upscale

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/CHAOS FLUX皮克斯风格人物风格转移 多幅画布构图扩图工作流_1934436815535304705.json、平台全量/CHAOS 像素风风格 多幅画布构图 人物风格转移扩图工作流_1934552443927601154.json、平台全量/CHAOS 手绘风格 多幅画布构图 人物风格转移扩图工作流_1936053661846114306.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CFGZeroStar`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FaceAutoFitSingle`
- `FluxGuidance`
- `IPAdapterFaceID`
- `IPAdapterUnifiedLoader`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `Int`
- `InvertMask`
- `JoinStringMulti`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: MaskGrow`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2Ultra`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LaMa`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: TextBox`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `MathExpression|pysssss`
- `PreviewImage`
- `RandomNoise`
- `RepeatLatentBatch`
- `SamplerCustomAdvanced`
- `SaveImage`
- `String`
- `Text _O`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`
- `easy compare`
- `easy ifElse`
- `easy imageSizeByLongerSide`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Replace Text _O` —— 2/3 个有
- `easy clearCacheAll` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
