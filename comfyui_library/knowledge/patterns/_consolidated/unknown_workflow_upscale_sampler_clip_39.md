---
name: unknown_workflow_upscale_sampler_clip_39
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.431667
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageScaleToTotalPixels, JjkText, KSampler, KSamplerAdvanced, LatentColorMatch, LayerUtility: PurgeVRAM V2, LoadImage, LoaderGGUF, ModelSamplingAuraFlow, ModelSamplingZImage, PlaySound|pysssss, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-base底模lora测试工作流_2026565564419809282.json, 图片生成/文生图/zimage 2603lora base极速版_2025979826892447746.json, 图片生成/文生图/zimage base 满血版 z-image 文生图_2016357685683294209.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_39

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image-base底模lora测试工作流_2026565564419809282.json、图片生成/文生图/zimage 2603lora base极速版_2025979826892447746.json、图片生成/文生图/zimage base 满血版 z-image 文生图_2016357685683294209.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：43%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `KSamplerAdvanced`
- `LatentColorMatch`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoaderGGUF`
- `ModelSamplingAuraFlow`
- `ModelSamplingZImage`
- `PlaySound|pysssss`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `ConcatTextOfUtils` —— 1/3 个有
- `PresetTextSelector` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `Textbox` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 30 | 3 | 32% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 3 | 43% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 30，3 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，3 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
