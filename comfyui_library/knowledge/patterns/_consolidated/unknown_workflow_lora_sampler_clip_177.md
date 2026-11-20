---
name: unknown_workflow_lora_sampler_clip_177
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.875
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy setNode]
problems: []
missing: []
members: [图片生成/图生图/Klein-9B  极速 全自动换脸  任意姿势  图片编辑_2046208662577876994.json, 图片生成/图生图/Klein极速全自动_2065004946201866242.json, 图片生成/图生图/ZimageTurbo+Klein9b动漫转真人合集 By 像素幻想Lab_2028801108172345345.json, 平台全量/Klein-9B极速全自动换脸+任意姿势编辑_2040748304593592321.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_177

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Klein-9B  极速 全自动换脸  任意姿势  图片编辑_2046208662577876994.json、图片生成/图生图/Klein极速全自动_2065004946201866242.json、图片生成/图生图/ZimageTurbo+Klein9b动漫转真人合集 By 像素幻想Lab_2028801108172345345.json、平台全量/Klein-9B极速全自动换脸+任意姿势编辑_2040748304593592321.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 3/4 个有
- `Anything Everywhere3` —— 3/4 个有
- `AutoCropFaces` —— 3/4 个有
- `DrawMaskOnImage` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `LayerMask: MaskGrow` —— 3/4 个有
- `LayerMask: PersonMaskUltra V2` —— 3/4 个有
- `LayerUtility: ImageReel` —— 3/4 个有
- `LayerUtility: ImageReelComposit` —— 3/4 个有
- `SeedVR2LoadDiTModel` —— 3/4 个有
- `SeedVR2LoadVAEModel` —— 3/4 个有
- `SeedVR2VideoUpscaler` —— 3/4 个有
- `easy getNode` —— 3/4 个有
- `GetImageSize+` —— 2/4 个有
- `NuiKr.OpenPoseEditor` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `KSamplerAdvanced` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `Qwen3_VQA` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 1 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 1 | 100% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | euler | - | 1 | 100% |
| 重绘幅度 | FlowMatchEulerDiscreteScheduler | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
