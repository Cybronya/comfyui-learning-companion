---
name: unknown_workflow_video_lora_sampler_713
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.404667
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, GetNode, GrowMask, ImageBatch, ImageFromBatch, ImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PixelPerfectResolution, SetNode, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanAnimateToVideo, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Wan2.2 Animate V2 全自动角色替换工作流_1976471239042666497.json, 视频生成/图生视频/Wan2_2_14B_Animate_自动循环-动作迁移_1973652058060533761.json, 视频生成/图生视频/wan2.2 animate 全自动角色替换工作流-改良版_1973951383147819010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_713

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 Animate V2 全自动角色替换工作流_1976471239042666497.json、视频生成/图生视频/Wan2_2_14B_Animate_自动循环-动作迁移_1973652058060533761.json、视频生成/图生视频/wan2.2 animate 全自动角色替换工作流-改良版_1973951383147819010.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：40%

## 共有节点

全部 3 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `GetNode`
- `GrowMask`
- `ImageBatch`
- `ImageFromBatch`
- `ImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PixelPerfectResolution`
- `SetNode`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanAnimateToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AILab_MaskPreview` —— 2/3 个有
- `Int` —— 2/3 个有
- `LayerMask: LoadSegmentAnythingModels` —— 2/3 个有
- `LayerMask: SegmentAnythingUltra V3` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `Bjornulf_ShowFloat` —— 1/3 个有
- `Bjornulf_ShowInt` —— 1/3 个有
- `DownloadAndLoadSAM2Model` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `MaskToImage` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `PointsEditor` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `Sam2Segmentation` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
