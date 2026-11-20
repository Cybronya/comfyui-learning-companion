---
name: unknown_workflow_inpaint_lora_sampler_35
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9408
common_nodes: [AILab_QwenVL, BasicGuider, BasicScheduler, CFGNorm, CLIPLoader_Any, CLIPTextEncode, DWPreprocessor, DetailDaemonSamplerNode, ImageScaleToTotalPixelsX, InpaintCropImproved, InpaintStitchImproved, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RandomNoise, ReActorFaceSwap, ReferenceLatent, SAM3Segment, SamplerCustom, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SetLatentNoiseMask, SplitSigmas, UNETLoader_Any, VAEDecode, VAEEncode, VAELoader_Any, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/电商服装内衣睡衣模特图生成_2066020868601507842.json, 平台全量/z-image-turbo-firered-image-edit-flux2-klein-电商内衣模特图生成：终极版_2046104413936291842.json, 平台全量/z-image-turbo-firered-image-edit-flux2-klein-电商泳装模特图生成：最终版_2046493082887131138.json, 平台全量/z-image-turbo-flux2-klein-服装电商lookbook展示图：换脸，换装，换姿_2046432076110499841.json, 平台全量/换装换脸姿势迁移 z-image turbo+firered+flux2-klein 电商模特全能编_2047491989666537474.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_35

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/电商服装内衣睡衣模特图生成_2066020868601507842.json、平台全量/z-image-turbo-firered-image-edit-flux2-klein-电商内衣模特图生成：终极版_2046104413936291842.json、平台全量/z-image-turbo-firered-image-edit-flux2-klein-电商泳装模特图生成：最终版_2046493082887131138.json、平台全量/z-image-turbo-flux2-klein-服装电商lookbook展示图：换脸，换装，换姿_2046432076110499841.json、平台全量/换装换脸姿势迁移 z-image turbo+firered+flux2-klein 电商模特全能编_2047491989666537474.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `AILab_QwenVL`
- `BasicGuider`
- `BasicScheduler`
- `CFGNorm`
- `CLIPLoader_Any`
- `CLIPTextEncode`
- `DWPreprocessor`
- `DetailDaemonSamplerNode`
- `ImageScaleToTotalPixelsX`
- `InpaintCropImproved`
- `InpaintStitchImproved`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RandomNoise`
- `ReActorFaceSwap`
- `ReferenceLatent`
- `SAM3Segment`
- `SamplerCustom`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SetLatentNoiseMask`
- `SplitSigmas`
- `UNETLoader_Any`
- `VAEDecode`
- `VAEEncode`
- `VAELoader_Any`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 4/5 个有
- `EmptyFlux2LatentImage` —— 4/5 个有
- `Flux2Scheduler` —— 4/5 个有
- `ImitationHueNode` —— 4/5 个有
- `ModelPatchLoader` —— 4/5 个有
- `TextEncodeQwenImageEditPlus` —— 4/5 个有
- `ZImageFunControlnet` —— 4/5 个有
- `easy imageSize` —— 4/5 个有
- `easy imageSizeBySide` —— 4/5 个有
- `CLIPLoader` —— 3/5 个有
- `UNETLoader` —— 3/5 个有
- `VAELoader` —— 3/5 个有
- `easy ifElse` —— 2/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `ColorBalanceNode` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `easy positive` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
