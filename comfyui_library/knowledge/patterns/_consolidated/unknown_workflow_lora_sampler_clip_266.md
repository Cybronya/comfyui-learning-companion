---
name: unknown_workflow_lora_sampler_clip_266
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.844667
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, CreateVideo, GetImageRangeFromBatch, GetVideoComponents, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, PathchSageAttentionKJ, PreviewImage, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RMBG, SAM3_VideoTrack, SCAIL2ColoredMask, SaveVideo, SimpleMathDual+, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoInfoLoaded, WanMoeKSampler, WanSCAILToVideo, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy ifElse, easy int, easy lengthAnything, easy mathInt, easy mergeVideosFromPaths, easy saveVideo, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/SCAIL 2 动作迁移&角色替换 长视频循环版2606_2065756470448312322.json, 平台全量/SCAIL 2 动作迁移&角色替换 长视频循环版2608_2090084503493627906.json, 视频生成/图生视频/WanScailV2 动作迁移&角色替换 循环_2064567633801990146.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_266

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/SCAIL 2 动作迁移&角色替换 长视频循环版2606_2065756470448312322.json、平台全量/SCAIL 2 动作迁移&角色替换 长视频循环版2608_2090084503493627906.json、视频生成/图生视频/WanScailV2 动作迁移&角色替换 循环_2064567633801990146.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `GetImageRangeFromBatch`
- `GetVideoComponents`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RMBG`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SaveVideo`
- `SimpleMathDual+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `WanMoeKSampler`
- `WanSCAILToVideo`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy int`
- `easy lengthAnything`
- `easy mathInt`
- `easy mergeVideosFromPaths`
- `easy saveVideo`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `FlashVSRInitPipe` —— 2/3 个有
- `FlashVSRNodeAdv` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `ImageResizeKJv2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 3 | 46% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | euler_ancestral | - | 3 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，3 个样本，取值分散，一致性仅 46%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，3 个样本，一致性 67%
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
