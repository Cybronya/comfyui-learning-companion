---
name: unknown_workflow_video_lora_sampler_688
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.46925
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ColorTransfer, ConditioningZeroOut, DiffusionModelLoaderKJ, Display Int (rgthree), GetImageSize+, GetNode, INTConstant, ImageFromBatch, ImageFromBatch+, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PrimitiveString, RIFE VFI, SetNode, VAEDecode, VAELoader, VHS_VideoCombine, WanSCAILToVideo, easy batchAnything, easy clearCacheAll, easy forLoopEnd, easy forLoopStart]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/scail2人物替换（2026年7月17日）_2069355383180849154.json, 平台全量/随意切换SCAIL-2人物替换+动作迁移工作流!_2066058846082256898.json, 视频生成/图生视频/Scail2动作迁移（添加胸肌臀部弹跳效果，更真实）_2069596768408530946.json, 视频生成/图生视频/Scail2动作迁移（简单才是最好的，复杂的东西不适合多数人）_2069574833263960065.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_688

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/scail2人物替换（2026年7月17日）_2069355383180849154.json、平台全量/随意切换SCAIL-2人物替换+动作迁移工作流!_2066058846082256898.json、视频生成/图生视频/Scail2动作迁移（添加胸肌臀部弹跳效果，更真实）_2069596768408530946.json、视频生成/图生视频/Scail2动作迁移（简单才是最好的，复杂的东西不适合多数人）_2069574833263960065.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：47%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ColorTransfer`
- `ConditioningZeroOut`
- `DiffusionModelLoaderKJ`
- `Display Int (rgthree)`
- `GetImageSize+`
- `GetNode`
- `INTConstant`
- `ImageFromBatch`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PrimitiveString`
- `RIFE VFI`
- `SetNode`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanSCAILToVideo`
- `easy batchAnything`
- `easy clearCacheAll`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `LoadVideoUI` —— 3/4 个有
- `CheckpointLoaderSimple` —— 2/4 个有
- `SAM3_TrackPreview` —— 2/4 个有
- `SAM3_VideoTrack` —— 2/4 个有
- `SCAIL2ColoredMask` —— 2/4 个有
- `easy imageRemBg` —— 2/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `孤海注释` —— 1/4 个有
- `忽略多组孤海` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（10/4 个样本）：Steps较低可能导致细节不足
