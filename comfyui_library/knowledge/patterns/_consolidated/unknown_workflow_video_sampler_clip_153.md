---
name: unknown_workflow_video_sampler_clip_153
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.65725
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSizeAndCount, GetNode, INTConstant, ImageFromBatch, ImageFromBatch+, ImpactFloat, JWFloatToString, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, MemoryCleaner, PreviewImage, PrimitiveFloat, Qwen3_VQA, RH_LLMAPI_NODE, SaveLatent, SetNode, ShowText|pysssss, StringFunction|pysssss, VAEDecodeTiled, VAELoader, VHS_VideoCombine, easy anythingIndexSwitch, easy imageSize, easy int, easy positive, easy saveText, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/视频-图生视频扩写02延长-wan2.2-SVI 2.0 Pro-smooth-官方_2006352644528410625.json, 视频生成/图生视频/视频-图生视频扩写(动漫)-wan2.2-DasiwaV10-官方_2008198733976047618.json, 视频生成/图生视频/视频-图生视频扩写01-wan2.2-SVI 2.0 Pro-smooth-官方_2006343692088516610.json, 视频生成/图生视频/视频-视频延长扩写-wan2.2-SVI 2.0 Pro-smooth-官方_2006371284166385666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_153

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/视频-图生视频扩写02延长-wan2.2-SVI 2.0 Pro-smooth-官方_2006352644528410625.json、视频生成/图生视频/视频-图生视频扩写(动漫)-wan2.2-DasiwaV10-官方_2008198733976047618.json、视频生成/图生视频/视频-图生视频扩写01-wan2.2-SVI 2.0 Pro-smooth-官方_2006343692088516610.json、视频生成/图生视频/视频-视频延长扩写-wan2.2-SVI 2.0 Pro-smooth-官方_2006371284166385666.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageFromBatch`
- `ImageFromBatch+`
- `ImpactFloat`
- `JWFloatToString`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `MemoryCleaner`
- `PreviewImage`
- `PrimitiveFloat`
- `Qwen3_VQA`
- `RH_LLMAPI_NODE`
- `SaveLatent`
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
- `easy saveText`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DiffusionModelLoaderKJ` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `WanImageToVideoSVIPro` —— 3/4 个有
- `DJZ-LoadLatent` —— 1/4 个有
- `ImageBatchExtendWithOverlap` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `LatentLoaderAdvanced` —— 1/4 个有
- `LoadLatent` —— 1/4 个有
- `PainterI2V` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `UNETLoader` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 75% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | 2 | 1 - 2 | 4 | 75% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2，观测区间 1 - 2，4 个样本
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
