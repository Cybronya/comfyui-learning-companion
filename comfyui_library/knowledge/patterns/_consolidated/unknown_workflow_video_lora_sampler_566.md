---
name: unknown_workflow_video_lora_sampler_566
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.753333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, INTConstant, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动作迁移_1991086021146181634.json, 视频生成/图生视频/Animate_视频自动人物姿势动作迁移_2002231206848655361.json, 视频生成/图生视频/wan animate动作迁移_1972997136394661890.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_566

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/动作迁移_1991086021146181634.json、视频生成/图生视频/Animate_视频自动人物姿势动作迁移_2002231206848655361.json、视频生成/图生视频/wan animate动作迁移_1972997136394661890.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `INTConstant`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `PixelPerfectResolution` —— 2/3 个有
- `DrawViTPose` —— 1/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `OnnxDetectionModelLoader` —— 1/3 个有
- `PoseAndFaceDetection` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

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
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
