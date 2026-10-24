---
name: unknown_workflow_upscale_sampler_clip_41
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.621667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Fast Groups Bypasser (rgthree), GetNode, KSamplerAdvanced, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [图片生成/文生图/星绘ZB+ZT双模型双采样 摄影写真_2035293525453049857.json, 图片生成/文生图/百度 ERNIE 文生图 图生图 反推提示 洗图_2044983158545846273.json, 图片生成/文生图/百度 ERNIE 文生图 图生图 反推提示 洗图_2044993015319633921.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_41

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/星绘ZB+ZT双模型双采样 摄影写真_2035293525453049857.json、图片生成/文生图/百度 ERNIE 文生图 图生图 反推提示 洗图_2044983158545846273.json、图片生成/文生图/百度 ERNIE 文生图 图生图 反推提示 洗图_2044993015319633921.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSamplerAdvanced`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 2/3 个有
- `EmptyLatentImage` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `VRAM_Debug` —— 2/3 个有
- `llama_cpp_parameters` —— 2/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LatentUpscaleBy` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 12 | 3 | 80% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 67% |
| 宽度 | 720 | - | 2 | 100% |
| 高度 | 1280 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 12，3 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 67%
- 宽度 中位数 720，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
