---
name: unknown_workflow_video_lora_sampler_680
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9795
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DrawViTPose, ImageResizeKJv2, ImageStitch, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, OnnxDetectionModelLoader, PathchSageAttentionKJ, PoseAndFaceDetection, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimateToVideo, easy getNode, easy int, easy setNode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Wan-animate动作迁移_视频转绘_2007482946818678785.json, 平台全量/Wan-animate角色替换_2007774730069217281.json, "视频生成/图生视频/【推荐,动态增强】Wan-animate动作迁移_视频转绘_2009846390779809793.json", "视频生成/图生视频/【推荐,动态增强】Wan-animate角色替换_2009846422258065410.json"]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_680

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Wan-animate动作迁移_视频转绘_2007482946818678785.json、平台全量/Wan-animate角色替换_2007774730069217281.json、视频生成/图生视频/【推荐,动态增强】Wan-animate动作迁移_视频转绘_2009846390779809793.json、视频生成/图生视频/【推荐,动态增强】Wan-animate角色替换_2009846422258065410.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DrawViTPose`
- `ImageResizeKJv2`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `OnnxDetectionModelLoader`
- `PathchSageAttentionKJ`
- `PoseAndFaceDetection`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimateToVideo`
- `easy getNode`
- `easy int`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 2/4 个有
- `DrawMaskOnImage` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `GrowMask` —— 2/4 个有
- `MaskToImage` —— 2/4 个有
- `RIFE VFI` —— 2/4 个有
- `easy framesEditor` —— 2/4 个有
- `easy sam3ModelLoader` —— 2/4 个有
- `easy sam3VideoSegmentation` —— 2/4 个有
- `Int` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
