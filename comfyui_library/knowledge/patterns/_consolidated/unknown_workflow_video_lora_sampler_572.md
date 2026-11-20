---
name: unknown_workflow_video_lora_sampler_572
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8688
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/GOZAO-Animate-动作迁移-优化版_2077400238037495810.json, 平台全量/Wan Animate姿势迁移官方版_1990427310165811202.json, 平台全量/动作参考_1983769804194684929.json, 视频生成/图生视频/Animate_视频自动人物姿势动作迁移_2002231206848655361.json, 视频生成/图生视频/wan animate动作迁移_1972997136394661890.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_572

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/GOZAO-Animate-动作迁移-优化版_2077400238037495810.json、平台全量/Wan Animate姿势迁移官方版_1990427310165811202.json、平台全量/动作参考_1983769804194684929.json、视频生成/图生视频/Animate_视频自动人物姿势动作迁移_2002231206848655361.json、视频生成/图生视频/wan animate动作迁移_1972997136394661890.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
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
- `DWPreprocessor` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `PixelPerfectResolution` —— 4/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `DrawViTPose` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `OnnxDetectionModelLoader` —— 1/5 个有
- `PoseAndFaceDetection` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `VHS_VideoInfo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
