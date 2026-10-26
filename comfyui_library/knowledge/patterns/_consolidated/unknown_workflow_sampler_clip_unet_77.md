---
name: unknown_workflow_sampler_clip_unet_77
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.92675
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/klein换头【可选  Bnanana pro】_2016044457656852482.json, 图片生成/图生图/pro_2026893876430118913.json, 图片生成/图生图/tang成熟手绘-Klein-马克笔转换_2032270065495707649.json, 图片生成/图生图/人物真实换脸 光影一致_2081923793060188162.json, 图片生成/图生图/换头换脸_真实自然-Flux2-Klein工作流_2017928641371443202.json, 图片生成/图生图/换头换脸_真实自然-Flux2-Klein工作流_2067849412315013121.json, 图片生成/图生图/换脸_real-Flux2+Klein+工作流_2090347115141746689.json, 图片生成/图生图/换脸_real-Flux2+Klein+工作流_2091704075195871233.json, 图片生成/图生图/换脸_real-Flux2+Klein+工作流_2091835881744330753.json, 图片生成/图生图/换脸_real-Flux2+Klein+工作流_2092522636768272386.json, 图片生成/图生图/换脸_real-Flux2+Klein+工作流_2100488808281235458.json, 图片生成/图生图/换脸换装 真实高度一致 多图编辑 加强版_2089609145862414337.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_77

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/klein换头【可选  Bnanana pro】_2016044457656852482.json、图片生成/图生图/pro_2026893876430118913.json、图片生成/图生图/tang成熟手绘-Klein-马克笔转换_2032270065495707649.json、图片生成/图生图/人物真实换脸 光影一致_2081923793060188162.json、图片生成/图生图/换头换脸_真实自然-Flux2-Klein工作流_2017928641371443202.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 11/12 个有
- `EmptyFlux2LatentImage` —— 11/12 个有
- `GetImageSize` —— 11/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/12 个有
- `Image Comparer (rgthree)` —— 9/12 个有
- `SegmentV2` —— 9/12 个有
- `easy imageColorMatch` —— 9/12 个有
- `LayerUtility: ImageReel` —— 8/12 个有
- `LayerUtility: ImageReelComposit` —— 8/12 个有
- `LoraLoaderModelOnly` —— 4/12 个有
- `Fast Groups Bypasser (rgthree)` —— 2/12 个有
- `RH_Nano_Banana2_Image2Image` —— 2/12 个有
- `Text Multiline` —— 2/12 个有
- `1hew_AnySwitchInt` —— 1/12 个有
- `Any Switch (rgthree)` —— 1/12 个有
- `Anything Everywhere3` —— 1/12 个有
- `CR Text` —— 1/12 个有
- `ConstrainImage|pysssss` —— 1/12 个有
- `Fast Groups Muter (rgthree)` —— 1/12 个有
- `ImageConcatMulti` —— 1/12 个有
- `JjkText` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `RH_AlibabaQwenImage30ProImageEdit` —— 1/12 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
