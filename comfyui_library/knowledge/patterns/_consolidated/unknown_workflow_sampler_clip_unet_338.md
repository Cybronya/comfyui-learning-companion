---
name: unknown_workflow_sampler_clip_unet_338
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.815333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, ImageResizeKJv2, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, ModelSamplingAuraFlow, PrimitiveStringMultiline, RH_LLMAPI_NODE, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/一键改变标贴文字布局v1_1965263751576473601.json, 图片生成/图生图/Fancy洗图，不加抠图_1959893090406445058.json, 图片生成/图生图/相似logo生成+抠图 V2_1958347191905632258.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_338

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/一键改变标贴文字布局v1_1965263751576473601.json、图片生成/图生图/Fancy洗图，不加抠图_1959893090406445058.json、图片生成/图生图/相似logo生成+抠图 V2_1958347191905632258.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `ImageResizeKJv2`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Canny` —— 2/3 个有
- `DepthAnythingV2Preprocessor` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `LoadQwenImageDiffSynthiPipe` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `QwenImageDiffSynthSampler` —— 2/3 个有
- `SetControlArgs` —— 2/3 个有
- `easy imageRemBg` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
