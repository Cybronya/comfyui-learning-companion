---
name: unknown_workflow_video_clip_vae_3
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6534
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSizeAndCount, GetNode, INTConstant, ImageFromBatch, ImageFromBatch+, ImpactFloat, JWFloatToString, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, MemoryCleaner, PreviewImage, PrimitiveFloat, Qwen3_VQA, RH_LLMAPI_NODE, SetNode, ShowText|pysssss, StringFunction|pysssss, VAEDecodeTiled, VAELoader, VHS_VideoCombine, easy anythingIndexSwitch, easy imageSize, easy int, easy positive, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/视频-图生视频扩写02延长-wan2.2-SVI 2.0 Pro-smooth-官方_2006352644528410625.json, 视频生成/图生视频/视频-图生视频扩写(动漫)-wan2.2-DasiwaV10-官方_2008198733976047618.json, 视频生成/图生视频/视频-图生视频扩写01-wan2.2-SVI 2.0 Pro-smooth-官方_2006343692088516610.json, 视频生成/图生视频/视频-图生视频自动扩写-wan2.2-smoothMix-官方_1982742942290984961.json, 视频生成/图生视频/视频-视频延长扩写-wan2.2-SVI 2.0 Pro-smooth-官方_2006371284166385666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_vae_3

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/视频-图生视频扩写02延长-wan2.2-SVI 2.0 Pro-smooth-官方_2006352644528410625.json、视频生成/图生视频/视频-图生视频扩写(动漫)-wan2.2-DasiwaV10-官方_2008198733976047618.json、视频生成/图生视频/视频-图生视频扩写01-wan2.2-SVI 2.0 Pro-smooth-官方_2006343692088516610.json、视频生成/图生视频/视频-图生视频自动扩写-wan2.2-smoothMix-官方_1982742942290984961.json、视频生成/图生视频/视频-视频延长扩写-wan2.2-SVI 2.0 Pro-smooth-官方_2006371284166385666.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageFromBatch`
- `ImageFromBatch+`
- `ImpactFloat`
- `JWFloatToString`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `MemoryCleaner`
- `PreviewImage`
- `PrimitiveFloat`
- `Qwen3_VQA`
- `RH_LLMAPI_NODE`
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
- `KSamplerAdvanced` —— 4/5 个有
- `SaveLatent` —— 4/5 个有
- `easy saveText` —— 4/5 个有
- `DiffusionModelLoaderKJ` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `VAEEncode` —— 3/5 个有
- `WanImageToVideoSVIPro` —— 3/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `UNETLoader` —— 2/5 个有
- `DJZ-LoadLatent` —— 1/5 个有
- `ImageBatchExtendWithOverlap` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `LatentLoaderAdvanced` —— 1/5 个有
- `LoadLatent` —— 1/5 个有
- `ModelBlockSwap` —— 1/5 个有
- `PainterI2V` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `WanImageToVideo` —— 1/5 个有
- `WanMoeKSampler` —— 1/5 个有
- `WanVideoVACEStartToEndFrame` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 80% |
| Prompt 约束强度(CFG) | 8 | 8 - 20 | 5 | 54% |
| 采样算法 | 2 | 1 - 2 | 5 | 76% |
| 调度器 | euler | - | 5 | 80% |
| 重绘幅度 | simple | - | 5 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 20，5 个样本
- 采样算法 中位数 2，观测区间 1 - 2，5 个样本
- 调度器 最常用 euler，5 个样本，一致性 80%
- 重绘幅度 最常用 simple，5 个样本，一致性 80%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
