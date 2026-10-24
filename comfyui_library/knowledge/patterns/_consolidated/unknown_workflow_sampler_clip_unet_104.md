---
name: unknown_workflow_sampler_clip_unet_104
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9477
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/klein 9B-文生图-测试lora工作流_2046045126165798913.json, 图片生成/图生图/klein 9B-文生图-测试lora工作流_2046055960355016705.json, 图片生成/图生图/klein 9B-测试lora工作流_2042946925502144514.json, 图片生成/图生图/klein 添加真实细节_2027767576952049665.json, 图片生成/图生图/klein(多图编辑)_2016069562856378370.json, 图片生成/图生图/klein+添加真实细节_2042527177735938050.json, 图片生成/图生图/kleinBFS换头，亚洲人也能换_2060971030277087233.json, 图片生成/图生图/klein单图编辑_图像修复_2018568599132184578.json, 图片生成/图生图/klein高一致性高清修复_2030545132830859266.json, 图片生成/图生图/一键去水印FLUX2-klein-增强版_2028855059450171393.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_104

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/klein 9B-文生图-测试lora工作流_2046045126165798913.json、图片生成/图生图/klein 9B-文生图-测试lora工作流_2046055960355016705.json、图片生成/图生图/klein 9B-测试lora工作流_2042946925502144514.json、图片生成/图生图/klein 添加真实细节_2027767576952049665.json、图片生成/图生图/klein(多图编辑)_2016069562856378370.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/10 个有
- `GetImageSize` —— 8/10 个有
- `LoraLoaderModelOnly` —— 8/10 个有
- `VAEEncode` —— 8/10 个有
- `Image Comparer (rgthree)` —— 7/10 个有
- `ImageScaleToTotalPixels` —— 7/10 个有
- `CR Text` —— 5/10 个有
- `CustomAddLabel` —— 4/10 个有
- `PDImageConcante` —— 3/10 个有
- `ColorMatch` —— 2/10 个有
- `ImageSharpen` —— 2/10 个有
- `Int` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `ImageConcanate` —— 1/10 个有
- `ImageResize+` —— 1/10 个有
- `PDIMAGE_LongerSize` —— 1/10 个有
- `PD_ModelLoraLoader` —— 1/10 个有
- `ResizeImagesByLongerEdge` —— 1/10 个有
- `SeedVR2` —— 1/10 个有
- `SeedVR2BlockSwap` —— 1/10 个有
- `SeedVR2ExtraArgs` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
