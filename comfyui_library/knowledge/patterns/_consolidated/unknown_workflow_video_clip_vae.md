---
name: unknown_workflow_video_clip_vae
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.652091
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSizeAndCount, GetNode, INTConstant, ImageFromBatch, ImageFromBatch+, ImpactFloat, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, MemoryCleaner, PreviewImage, PrimitiveFloat, Qwen3_VQA, SetNode, ShowText|pysssss, StringFunction|pysssss, VAEDecodeTiled, VAELoader, VHS_VideoCombine, easy anythingIndexSwitch, easy imageSize, easy int, easy positive, easy seed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2008198733976047618.json, 视频生成/图生视频/1972733308360675329.json, 视频生成/图生视频/2013149591474020354.json, 视频生成/图生视频/2013824710445899778.json, 视频生成/图生视频/2020662417289650177.json, 视频生成/图生视频/2031681898342260738.json, 视频生成/图生视频/2040367376394362881.json, 视频生成/图生视频/2006343692088516610.json, 视频生成/图生视频/1986620197631098882.json, 视频生成/图生视频/1982742942290984961.json, 视频生成/图生视频/2006371284166385666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_vae

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2008198733976047618.json、视频生成/图生视频/1972733308360675329.json、视频生成/图生视频/2013149591474020354.json、视频生成/图生视频/2013824710445899778.json、视频生成/图生视频/2020662417289650177.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageFromBatch`
- `ImageFromBatch+`
- `ImpactFloat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `MemoryCleaner`
- `PreviewImage`
- `PrimitiveFloat`
- `Qwen3_VQA`
- `SetNode`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `easy imageSize`
- `easy int`
- `easy positive`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 9/11 个有
- `UNETLoader` —— 9/11 个有
- `LoraLoaderModelOnly` —— 8/11 个有
- `ModelBlockSwap` —— 8/11 个有
- `WanImageToVideo` —— 8/11 个有
- `WanMoeKSampler` —— 8/11 个有
- `WanVideoVACEStartToEndFrame` —— 8/11 个有
- `JWFloatToString` —— 4/11 个有
- `RH_LLMAPI_NODE` —— 4/11 个有
- `KSamplerAdvanced` —— 3/11 个有
- `SaveLatent` —— 3/11 个有
- `easy saveText` —— 3/11 个有
- `DiffusionModelLoaderKJ` —— 2/11 个有
- `VAEEncode` —— 2/11 个有
- `WanImageToVideoSVIPro` —— 2/11 个有
- `CLIPVisionEncode` —— 1/11 个有
- `CLIPVisionLoader` —— 1/11 个有
- `ImageBatchExtendWithOverlap` —— 1/11 个有
- `ImageConcanate` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `PainterI2V` —— 1/11 个有
- `VHS_LoadVideo` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 11 | 100% |
| Prompt 约束强度(CFG) | 20 | 8 - 20 | 11 | 68% |
| 采样算法 | 1.5 | 1.5 - 2 | 11 | 86% |
| 调度器 | 1 | 1 - 1 | 8 | 100% |
| 重绘幅度 | sa_solver | - | 11 | 64% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，11 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，观测区间 8 - 20，11 个样本
- 采样算法 中位数 1.5，观测区间 1.5 - 2，11 个样本，取值集中（一致性 86%）
- 调度器 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 sa_solver，11 个样本，一致性 64%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
