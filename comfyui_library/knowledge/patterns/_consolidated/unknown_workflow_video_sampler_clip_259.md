---
name: unknown_workflow_video_sampler_clip_259
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8195
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, DepthAnythingV2Preprocessor, ImageBlend, ImageFromBatch, ImpactSwitch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, PrimitiveInt, TrimVideoLatent, UNETLoader, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/wan2.1 fusionx 动作迁移（gguf）极速版_1936818908869349377.json, 视频生成/图生视频/动作迁移wan2.1 fusionx GGUF版本_1946143075989417985.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_259

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/wan2.1 fusionx 动作迁移（gguf）极速版_1936818908869349377.json、视频生成/图生视频/动作迁移wan2.1 fusionx GGUF版本_1946143075989417985.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `DepthAnythingV2Preprocessor`
- `ImageBlend`
- `ImageFromBatch`
- `ImpactSwitch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveInt`
- `TrimVideoLatent`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `OpenposePreprocessor` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
