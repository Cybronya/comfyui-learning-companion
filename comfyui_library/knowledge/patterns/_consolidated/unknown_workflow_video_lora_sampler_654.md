---
name: unknown_workflow_video_lora_sampler_654
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.529667
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, GetImageRangeFromBatch, GetImageSize, GetNode, Image Comparer (rgthree), ImageResizeKJ, ImageResizeKJv2, ImpactSwitch, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RH_Nano_Banana_Image2Image, SeedVR2, SeedVR2BlockSwap, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanFirstLastFrameToVideo, WanMoeKSampler, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2-大香蕉-首尾帧-seedVR2-循环放大_1955841213301706754.json, 视频生成/图生视频/香_蕉出图模型ai创作加wan2.2组合首尾帧频生成ai动漫视频低成本高清视频创作_2011853910419447809.json, 视频生成/图生视频/香蕉加wan2.2神仙组合首尾帧_1966882574524145666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_654

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/wan2.2-大香蕉-首尾帧-seedVR2-循环放大_1955841213301706754.json、视频生成/图生视频/香_蕉出图模型ai创作加wan2.2组合首尾帧频生成ai动漫视频低成本高清视频创作_2011853910419447809.json、视频生成/图生视频/香蕉加wan2.2神仙组合首尾帧_1966882574524145666.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：53%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RH_Nano_Banana_Image2Image`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanFirstLastFrameToVideo`
- `WanMoeKSampler`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 14 | 14 - 14 | 3 | 100% |
| 采样算法 | 3.5 | 3.5 - 3.5 | 3 | 100% |
| 调度器 | 1 | 1 - 1 | 3 | 100% |
| 重绘幅度 | euler | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 14，观测区间 14 - 14，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 3.5，观测区间 3.5 - 3.5，3 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler，3 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
