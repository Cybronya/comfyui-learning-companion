---
name: unknown_workflow_video_lora_sampler_328
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.886429
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJ, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, RIFE VFI, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine, WanImageToVideo, WanVideoTeaCacheKJ]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/(1) 单图 IP 生成 lora 素材集工作流_1935328650676076545.json, 图片生成/图生图/一张单图生成360度loRa工作流_1911644473741275138.json, 图片生成/文生图/【大炮精选】一图生成多视角最佳解 并配合lora训练_1914199187573960705.json, 视频生成/图生视频/一图生成多视角最佳解 并配合lora训练_1968474583781265410.json, 视频生成/图生视频/单图生成lora工作流_1939649995148857345.json, 视频生成/图生视频/单图生成旋转视频工作流_1942506572570628098.json, 视频生成/图生视频/图生视频并抽帧图工作流_1910994763657740290.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_328

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/(1) 单图 IP 生成 lora 素材集工作流_1935328650676076545.json、图片生成/图生图/一张单图生成360度loRa工作流_1911644473741275138.json、图片生成/文生图/【大炮精选】一图生成多视角最佳解 并配合lora训练_1914199187573960705.json、视频生成/图生视频/一图生成多视角最佳解 并配合lora训练_1968474583781265410.json、视频生成/图生视频/单图生成lora工作流_1939649995148857345.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
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
- `GetImagesFromBatchIndexed` —— 6/7 个有
- `ImageRemoveBackground+` —— 6/7 个有
- `MaskPreview+` —— 6/7 个有
- `MatAnyoneVideoMatting` —— 6/7 个有
- `TransparentBGSession+` —— 6/7 个有
- `GroundingDinoModelLoader (segment anything)` —— 4/7 个有
- `GroundingDinoSAMSegment (segment anything)` —— 4/7 个有
- `MaskToImage` —— 4/7 个有
- `SAMModelLoader (segment anything)` —— 4/7 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/7 个有
- `SaveImage` —— 2/7 个有
- `Label (rgthree)` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 7 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 7 | 100% |
| 采样算法 | uni_pc | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 7/7 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：发现KSampler但没有VAEDecode
