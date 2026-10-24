---
name: unknown_workflow_sampler_clip_unet_405
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.782
common_nodes: [CLIPLoader, CLIPTextEncode, Canny, DepthAnythingV2Preprocessor, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), ImageResizeKJv2, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoadQwenImageDiffSynthiPipe, ModelSamplingAuraFlow, PreviewImage, PrimitiveStringMultiline, QwenImageDiffSynthSampler, RH_LLMAPI_NODE, SaveImage, SetControlArgs, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Fancy洗图，不加抠图_1959893090406445058.json, 图片生成/图生图/相似logo生成+抠图 V2_1958347191905632258.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_405

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Fancy洗图，不加抠图_1959893090406445058.json、图片生成/图生图/相似logo生成+抠图 V2_1958347191905632258.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Canny`
- `DepthAnythingV2Preprocessor`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadQwenImageDiffSynthiPipe`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `QwenImageDiffSynthSampler`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `SetControlArgs`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `easy imageRemBg` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
