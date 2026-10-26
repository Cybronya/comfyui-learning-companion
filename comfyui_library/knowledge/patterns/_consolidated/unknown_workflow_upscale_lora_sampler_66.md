---
name: unknown_workflow_upscale_lora_sampler_66
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.844
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler (Efficient), LayerFilter: HDREffects, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, StringFunction|pysssss, UNETLoader, VAELoader, easy stylesSelector]
problems: []
missing: []
members: [图片生成/图生图/一键运行：Z-IMAGE CN 控制Controlnet-Union 图像控制。、修改_1997556295177801729.json, 图片生成/文生图/一键运行：z-imgae 最简文生图 洗图  高清放大_1997558973375135745.json, 图片生成/文生图/一键运行：z_image 文生图最简放大_1997189042540331009.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_66

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/一键运行：Z-IMAGE CN 控制Controlnet-Union 图像控制。、修改_1997556295177801729.json、图片生成/文生图/一键运行：z-imgae 最简文生图 洗图  高清放大_1997558973375135745.json、图片生成/文生图/一键运行：z_image 文生图最简放大_1997189042540331009.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler (Efficient)`
- `LayerFilter: HDREffects`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAELoader`
- `easy stylesSelector`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `ModelPatchLoader` —— 1/3 个有
- `QwenImageDiffsynthControlnet` —— 1/3 个有
- `easy imageChooser` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 728 - 768 | 3 | 98% |
| 高度 | 1024 | 1024 - 1200 | 3 | 92% |
| 采样步数 | 6 | 6 - 6 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 728 - 768，3 个样本，取值集中（一致性 98%）
- 高度 中位数 1024，观测区间 1024 - 1200，3 个样本，取值集中（一致性 92%）
- 采样步数 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
