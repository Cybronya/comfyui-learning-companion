---
name: unknown_workflow_inpaint_sampler_clip_19
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.817444
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Color Panel, ConditioningZeroOut, DifferentialDiffusion, DownloadAndLoadFlorence2Model, Florence2Run, FluxGuidance, ImageCrop, ImageToMask, InpaintModelConditioning, Int, KSampler, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextJoin, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, VAEDecode, VAELoader, easy imageConcat, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Flux-Redux 漫画人物一键快速换装_1951929706251759617.json, 图片生成/图生图/Nunchaku极速换装Fill+ACE+Redux_1943999439797125121.json, 平台全量/FLUX最强换装Redux+ACE lora_1944795710053076994.json, 平台全量/Flux Nunchaku ACE万物迁移极速换背景-StarAI_1912341497436434433.json, 平台全量/Flux-Redux 一键快速换装_1951893253467615233.json, 平台全量/Nunchaku极速万物迁移工作流-FLUX模型Fill+ACE+Redux_1912179012544753665.json, 平台全量/Nunchaku极速电商换装Fill+ACE+Redux_1914692808106803201.json, 平台全量/最强万物迁移工作流-FLUX模型Fill+ACE+Redux_1904017257716944897.json, 平台全量/最强迁移人物-无中生有_1935142487063207937.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux-Redux 漫画人物一键快速换装_1951929706251759617.json、图片生成/图生图/Nunchaku极速换装Fill+ACE+Redux_1943999439797125121.json、平台全量/FLUX最强换装Redux+ACE lora_1944795710053076994.json、平台全量/Flux Nunchaku ACE万物迁移极速换背景-StarAI_1912341497436434433.json、平台全量/Flux-Redux 一键快速换装_1951893253467615233.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Color Panel`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `FluxGuidance`
- `ImageCrop`
- `ImageToMask`
- `InpaintModelConditioning`
- `Int`
- `KSampler`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: TextJoin`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageConcat`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 8/9 个有
- `AutoDownloadBiRefNetModel` —— 6/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `RembgByBiRefNet` —— 6/9 个有
- `DualCLIPLoader` —— 5/9 个有
- `UNETLoader` —— 5/9 个有
- `easy anythingIndexSwitch` —— 5/9 个有
- `Image Comparer (rgthree)` —— 4/9 个有
- `ModelSamplingFlux` —— 4/9 个有
- `NunchakuFluxDiTLoader` —— 4/9 个有
- `NunchakuTextEncoderLoader` —— 4/9 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/9 个有
- `NunchakuFluxLoraLoader` —— 3/9 个有
- `Mask Fill Holes` —— 2/9 个有
- `CR Text` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `GrowMaskWithBlur` —— 1/9 个有
- `LayerUtility: CropByMask V2` —— 1/9 个有
- `MaskPreview+` —— 1/9 个有
- `Note Plus (mtb)` —— 1/9 个有
- `RMBG` —— 1/9 个有
- `SUPIR_Upscale` —— 1/9 个有
- `String` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有
- `easy ifElse` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 10 - 28 | 9 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | normal | - | 9 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 10 - 28，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 normal，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
