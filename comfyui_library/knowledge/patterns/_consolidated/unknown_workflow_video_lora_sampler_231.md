---
name: unknown_workflow_video_lora_sampler_231
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.579778
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DWPreprocessor, DownloadAndLoadSAM2Model, DrawMaskOnImage, GetNode, GrowMask, INTConstant, ImageBatch, ImageFromBatch, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PixelPerfectResolution, PointsEditor, Sam2Segmentation, SetNode, TrimVideoLatent, UNETLoader, VAEDecode, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/1_1模式视频动作_2000449752623874050.json, 视频生成/图生视频/Wan Animate+kj骨骼绑定人物角色图生视频动作_1999382397340839937.json, 视频生成/图生视频/可爱大头娃娃工作流V2+骨骼绑定与动作迁移_2042618078990704642.json, 视频生成/图生视频/可爱娃娃工作流_2057269921096232961.json, 视频生成/图生视频/可爱娃娃工作流_2059070496771239938.json, 视频生成/图生视频/图生视频---太极动作工作流-Aiwood_2039883987727949826.json, 视频生成/图生视频/大头娃娃工作流-Aiwood_1998717600895000577.json, 视频生成/文生视频/Wan-Animate原生无限流（修正）_1971749907403108354.json, 视频生成/文生视频/角色参考-原生无限流-补帧_1975828769351012354.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_231

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/1_1模式视频动作_2000449752623874050.json、视频生成/图生视频/Wan Animate+kj骨骼绑定人物角色图生视频动作_1999382397340839937.json、视频生成/图生视频/可爱大头娃娃工作流V2+骨骼绑定与动作迁移_2042618078990704642.json、视频生成/图生视频/可爱娃娃工作流_2057269921096232961.json、视频生成/图生视频/可爱娃娃工作流_2059070496771239938.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 9 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `GetNode`
- `GrowMask`
- `INTConstant`
- `ImageBatch`
- `ImageFromBatch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PixelPerfectResolution`
- `PointsEditor`
- `Sam2Segmentation`
- `SetNode`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 8/9 个有
- `GIMMVFI_interpolate` —— 8/9 个有
- `SimpleMath+` —— 8/9 个有
- `AV_VAELoader` —— 7/9 个有
- `Display Int (rgthree)` —— 7/9 个有
- `EmptyImage` —— 7/9 个有
- `ImageResizeKJv2` —— 7/9 个有
- `OnnxDetectionModelLoader` —— 7/9 个有
- `PoseDetectionOneToAllAnimation` —— 7/9 个有
- `Float` —— 2/9 个有
- `GetImageSizeAndCount` —— 2/9 个有
- `MaskPreview` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `VAELoader` —— 2/9 个有
- `easy forLoopEnd` —— 2/9 个有
- `easy forLoopStart` —— 2/9 个有
- `DF_Float` —— 1/9 个有
- `Int` —— 1/9 个有
- `Setter` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（25/9 个样本）：Steps较低可能导致细节不足
