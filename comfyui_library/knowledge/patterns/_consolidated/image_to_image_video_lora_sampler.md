---
name: image_to_image_video_lora_sampler
type: Image To Image
frequency: 11
level: strong
coverage: 0.481636
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageFromBatch, JjkText, KSampler, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingAuraFlow, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, SimpleMath+, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanFirstMiddleLastFrameToVideo, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2037969942770880514.json, 视频生成/图生视频/1986219220310654977.json, 视频生成/图生视频/1985575003364249602.json, 视频生成/图生视频/2033878962325164034.json, 视频生成/图生视频/2075060174733266945.json, 视频生成/图生视频/2076466189928329218.json, 视频生成/图生视频/2077195036592267266.json, 视频生成/图生视频/2079113575385354241.json, 视频生成/图生视频/2079390921430487042.json, 视频生成/图生视频/2080571381951066114.json, 视频生成/图生视频/2038792996770025474.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2037969942770880514.json、视频生成/图生视频/1986219220310654977.json、视频生成/图生视频/1985575003364249602.json、视频生成/图生视频/2033878962325164034.json、视频生成/图生视频/2075060174733266945.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：48%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageFromBatch`
- `JjkText`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingAuraFlow`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SetNode`
- `SimpleMath+`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstMiddleLastFrameToVideo`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `ImageBatch` —— 10/11 个有
- `ImageResizeKJv2` —— 10/11 个有
- `PrimitiveInt` —— 10/11 个有
- `SaveImage` —— 10/11 个有
- `DF_Integer` —— 1/11 个有
- `ImageBatchJoin` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `PreviewImage` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 100% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 11 | 93% |
| 采样算法 | 1 | 1 - 1 | 11 | 100% |
| 调度器 | euler | - | 11 | 100% |
| 重绘幅度 | simple | - | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 44/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，11 个样本，取值集中（一致性 93%）
- 采样算法 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，11 个样本，一致性 100%
- 重绘幅度 最常用 simple，11 个样本，一致性 100%
- 高发问题（44/11 个样本）：Steps较低可能导致细节不足
