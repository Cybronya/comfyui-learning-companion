---
name: unknown_workflow_video_lora_sampler_337
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.842833
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJ, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, RIFE VFI, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine, WanImageToVideo, WanVideoTeaCacheKJ]
problems: [发现KSampler但没有VAEDecode]
missing: [ImageRemoveBackground+, LayerMask: SegmentAnythingUltra V2, Note Plus (mtb), RIFE VFI, TransparentBGSession+, MaskPreview+]
members: [图片生成/文生图/1914199187573960705.json, 视频生成/图生视频/1903708781744656386.json, 视频生成/图生视频/1968474583781265410.json, 视频生成/图生视频/1939649995148857345.json, 视频生成/图生视频/1942506572570628098.json, 视频生成/图生视频/1910994763657740290.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_337

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1914199187573960705.json、视频生成/图生视频/1903708781744656386.json、视频生成/图生视频/1968474583781265410.json、视频生成/图生视频/1939649995148857345.json、视频生成/图生视频/1942506572570628098.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJ`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RIFE VFI`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanVideoTeaCacheKJ`

**可变部分**（部分 workflow 才有）：
- `GetImagesFromBatchIndexed` —— 5/6 个有
- `ImageRemoveBackground+` —— 5/6 个有
- `MaskPreview+` —— 5/6 个有
- `MatAnyoneVideoMatting` —— 5/6 个有
- `TransparentBGSession+` —— 5/6 个有
- `GroundingDinoModelLoader (segment anything)` —— 3/6 个有
- `GroundingDinoSAMSegment (segment anything)` —— 3/6 个有
- `MaskToImage` —— 3/6 个有
- `SAMModelLoader (segment anything)` —— 3/6 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/6 个有
- `Label (rgthree)` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `SaveImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 6 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 6 | 100% |
| 采样算法 | uni_pc | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 6/6 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：发现KSampler但没有VAEDecode
- 这些节点还没有知识卡，系统对它们的理解有限：ImageRemoveBackground+、LayerMask: SegmentAnythingUltra V2、Note Plus (mtb)、RIFE VFI、TransparentBGSession+
