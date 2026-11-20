---
name: unknown_workflow_upscale_lora_clip_5
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.797
common_nodes: [CLIPTextEncode, DualCLIPLoader, Get Image Size, Image Comparer (rgthree), ImageResize+, ImageScaleToTotalPixels, LayerColor: ColorAdapter, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2, SeedVR2BlockSwap, TeaCache, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAELoader, easy compare, easy ifElse]
problems: []
missing: []
members: [图片生成/图生图/AA很好 单张_批量处理室内 最牛高清放大万物保留细节最新版_1953453729653641217.json, 图片生成/图生图/图片无损4k高清放大增加细节_1965292057768153090.json, 图片生成/图生图/批量去水印加高清工作流_1976897391767044097.json, 图片生成/图生图/批量高清工作流_1977317943342190593.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_clip_5

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/AA很好 单张_批量处理室内 最牛高清放大万物保留细节最新版_1953453729653641217.json、图片生成/图生图/图片无损4k高清放大增加细节_1965292057768153090.json、图片生成/图生图/批量去水印加高清工作流_1976897391767044097.json、图片生成/图生图/批量高清工作流_1977317943342190593.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleToTotalPixels`
- `LayerColor: ColorAdapter`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `TeaCache`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAELoader`
- `easy compare`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowInt` —— 3/4 个有
- `RHBatchImages:` —— 3/4 个有
- `RHExtractImage` —— 3/4 个有
- `RHUploadZip` —— 3/4 个有
- `easy forLoopEnd` —— 3/4 个有
- `easy forLoopStart` —— 3/4 个有
- `easy imageCount` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `ImageScaleDownToSize` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `FluxGuidance` —— 1/4 个有
- `KSampler` —— 1/4 个有
- `NunchakuFluxDiTLoader` —— 1/4 个有
- `ReferenceLatent` —— 1/4 个有
- `VAEDecode` —— 1/4 个有
- `VAEEncode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
