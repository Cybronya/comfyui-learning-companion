---
name: unknown_workflow_video_sampler_clip_74
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.681143
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSizeAndCount, INTConstant, ImageLoader, ImageResizeKJ, ImpactFloat, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, PathchSageAttentionKJ, PrimitiveFloat, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, WanMoeKSampler, WanVideoNAG, easy int, easy positive, easy seed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2003823135168339969.json, 视频生成/图生视频/2008209726496051201.json, 视频生成/图生视频/视频-首尾帧视频扩写(动漫-真人)_2091124043847127042.json, 视频生成/图生视频/1986618366645465090.json, 视频生成/图生视频/1983005590224011265.json, 视频生成/图生视频/1973043040770199553.json, 视频生成/图生视频/2011383850940764161.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_74

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2003823135168339969.json、视频生成/图生视频/2008209726496051201.json、视频生成/图生视频/视频-首尾帧视频扩写(动漫-真人)_2091124043847127042.json、视频生成/图生视频/1986618366645465090.json、视频生成/图生视频/1983005590224011265.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageLoader`
- `ImageResizeKJ`
- `ImpactFloat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `WanMoeKSampler`
- `WanVideoNAG`
- `easy int`
- `easy positive`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `ImageFromBatch` —— 6/7 个有
- `MemoryCleaner` —— 6/7 个有
- `ModelBlockSwap` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `StringFunction|pysssss` —— 6/7 个有
- `easy anythingIndexSwitch` —— 6/7 个有
- `easy imageSize` —— 6/7 个有
- `MultiplePathsInput` —— 5/7 个有
- `Qwen3_VQA` —— 5/7 个有
- `RH_LLMAPI_NODE` —— 4/7 个有
- `ImageConcanate` —— 3/7 个有
- `CLIPVisionEncode` —— 1/7 个有
- `CLIPVisionLoader` —— 1/7 个有
- `CM_IntUnaryOperation` —— 1/7 个有
- `Florence2ModelLoader` —— 1/7 个有
- `Florence2Run` —— 1/7 个有
- `GetImageRangeFromBatch` —— 1/7 个有
- `ImageFromBatch+` —— 1/7 个有
- `ImageListToBatch+` —— 1/7 个有
- `ImageToDevice+` —— 1/7 个有
- `JoinStrings` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `RHUploadZip_V2` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `easy batchAnything` —— 1/7 个有
- `easy forLoopEnd` —— 1/7 个有
- `easy forLoopStart` —— 1/7 个有
- `easy string` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 100% |
| Prompt 约束强度(CFG) | 20 | 20 - 20 | 7 | 100% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | 1 | 1 - 1 | 7 | 100% |
| 重绘幅度 | sa_solver | - | 7 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，观测区间 20 - 20，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 sa_solver，7 个样本，一致性 86%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
