---
name: image_to_image_video_lora_sampler
type: Image To Image
frequency: 12
level: strong
coverage: 0.481833
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageFromBatch, JjkText, KSampler, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingAuraFlow, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, SimpleMath+, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanFirstMiddleLastFrameToVideo, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/技术赋能创作：WAN2.2 与 QWEN 联合，实现图片到运镜长视频一键生成_1986723518039666690.json, 视频生成/图生视频/Qwen-Image-Edit图片多角度镜头+首中尾图生视频工作流_2037969942770880514.json, 视频生成/图生视频/WAN2.2+QWEN强强联合 图片多角度一键生成并运镜长视频优化版_1986219220310654977.json, 视频生成/图生视频/一键多角度Ai运镜+长视频生成=B站艾橘溪_1985575003364249602.json, 视频生成/图生视频/一键多角度Ai运镜+长视频生成_2033878962325164034.json, 视频生成/图生视频/一键多角度Ai运镜+长视频生成_2075060174733266945.json, 视频生成/图生视频/一键多角度Ai运镜+长视频生成_2076466189928329218.json, 视频生成/图生视频/一键多角度Ai运镜+长视频生成_2077195036592267266.json, 视频生成/图生视频/一键多角度Ai运镜+长视频生成_2079113575385354241.json, 视频生成/图生视频/一键多角度Ai运镜+长视频生成_2079390921430487042.json, 视频生成/图生视频/一键多角度Ai运镜+长视频生成_2080571381951066114.json, 视频生成/图生视频/图生视频一键多角度Ai运镜+长视频生成_2038792996770025474.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/技术赋能创作：WAN2.2 与 QWEN 联合，实现图片到运镜长视频一键生成_1986723518039666690.json、视频生成/图生视频/Qwen-Image-Edit图片多角度镜头+首中尾图生视频工作流_2037969942770880514.json、视频生成/图生视频/WAN2.2+QWEN强强联合 图片多角度一键生成并运镜长视频优化版_1986219220310654977.json、视频生成/图生视频/一键多角度Ai运镜+长视频生成=B站艾橘溪_1985575003364249602.json、视频生成/图生视频/一键多角度Ai运镜+长视频生成_2033878962325164034.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：48%

## 共有节点

全部 12 个 workflow 都包含：
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
- `ImageBatch` —— 11/12 个有
- `ImageResizeKJv2` —— 11/12 个有
- `PrimitiveInt` —— 11/12 个有
- `SaveImage` —— 11/12 个有
- `DF_Integer` —— 1/12 个有
- `ImageBatchJoin` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `PreviewImage` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 12 | 100% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 12 | 90% |
| 采样算法 | 1 | 1 - 1 | 12 | 100% |
| 调度器 | euler | - | 12 | 100% |
| 重绘幅度 | simple | - | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 48/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，12 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，12 个样本，取值集中（一致性 90%）
- 采样算法 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，12 个样本，一致性 100%
- 重绘幅度 最常用 simple，12 个样本，一致性 100%
- 高发问题（48/12 个样本）：Steps较低可能导致细节不足
