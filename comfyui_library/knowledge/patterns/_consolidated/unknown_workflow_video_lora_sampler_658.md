---
name: unknown_workflow_video_lora_sampler_658
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.535667
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, DisableNoise, Fast Groups Bypasser (rgthree), ForLoopClose, ForLoopOpen, GetNode, ImageBatchExtendWithOverlap, ImpactInt, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RIFEInterpolation, RTXVideoSuperResolution, RandomNoise, SamplerCustomAdvanced, ScheduledCFGGuidance, SetNode, SomethingToString, SplitSigmas, String Replace (mtb), UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_GetImageCount, VHS_VideoCombine, WanImageToVideoSVIPro, easy promptLine, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [视频生成/图生视频/2048784808272207873.json, 视频生成/图生视频/2041333413067628545.json, 视频生成/文生视频/wan2.2无限文视频工作流_2042218145586356225.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_658

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2048784808272207873.json、视频生成/图生视频/2041333413067628545.json、视频生成/文生视频/wan2.2无限文视频工作流_2042218145586356225.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `DisableNoise`
- `Fast Groups Bypasser (rgthree)`
- `ForLoopClose`
- `ForLoopOpen`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `ImpactInt`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RIFEInterpolation`
- `RTXVideoSuperResolution`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `ScheduledCFGGuidance`
- `SetNode`
- `SomethingToString`
- `SplitSigmas`
- `String Replace (mtb)`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`
- `easy promptLine`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `PainterVRAM` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `UnloadModel` —— 2/3 个有
- `DuckHideNode` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
