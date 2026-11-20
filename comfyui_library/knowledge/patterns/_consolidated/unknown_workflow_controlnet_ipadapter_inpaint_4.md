---
name: unknown_workflow_controlnet_ipadapter_inpaint_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.84
common_nodes: [AnyLineArtPreprocessor_aux, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DepthAnythingV2Preprocessor, DifferentialDiffusion, DualCLIPLoader, Fast Bypasser (rgthree), Float, FluxGuidance, GrowMask, INPAINT_ApplyFooocusInpaint, INPAINT_InpaintWithModel, INPAINT_LoadFooocusInpaint, INPAINT_LoadInpaintModel, INPAINT_VAEEncodeInpaintConditioning, IPAdapterAdvanced, IPAdapterNoise, IPAdapterUnifiedLoader, InpaintCrop, InpaintModelConditioning, InpaintStitch, Int, JanusImageUnderstanding, JanusModelLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, Mask Fill Holes, Mask Gaussian Region, PreviewImage, RepeatLatentBatch, SaveImage, ShowText|pysssss, SimpleCondition+, StringConstantMultiline, UNETLoader, VAEDecode, VAELoader, easy promptConcat]
problems: []
missing: []
members: [图片生成/图生图/Flux图像移除 物体消除_1926871772266700802.json, 平台全量/【最强万物移除】FLUX物体消除去水印 完胜PS移除工具_1914907841990225921.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_inpaint_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux图像移除 物体消除_1926871772266700802.json、平台全量/【最强万物移除】FLUX物体消除去水印 完胜PS移除工具_1914907841990225921.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `AnyLineArtPreprocessor_aux`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DepthAnythingV2Preprocessor`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `Fast Bypasser (rgthree)`
- `Float`
- `FluxGuidance`
- `GrowMask`
- `INPAINT_ApplyFooocusInpaint`
- `INPAINT_InpaintWithModel`
- `INPAINT_LoadFooocusInpaint`
- `INPAINT_LoadInpaintModel`
- `INPAINT_VAEEncodeInpaintConditioning`
- `IPAdapterAdvanced`
- `IPAdapterNoise`
- `IPAdapterUnifiedLoader`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `Int`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `Mask Fill Holes`
- `Mask Gaussian Region`
- `PreviewImage`
- `RepeatLatentBatch`
- `SaveImage`
- `ShowText|pysssss`
- `SimpleCondition+`
- `StringConstantMultiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `BaiduTranslateNode` —— 1/2 个有
- `ETN_Translate` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.35 | - | 2 | 100% |
| ControlNet 权重 | 0.6 | - | 2 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.35，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
