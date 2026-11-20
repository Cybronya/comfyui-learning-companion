---
name: unknown_workflow_video_lora_sampler_380
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.627125
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SAM3_VideoTrack, SCAIL2ColoredMask, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo, easy imageRemBg]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/SCAIL2-动作迁移+人物替换电商短视频带货工作流+全节点注释_2071936392262934529.json, 视频生成/图生视频/SCAIL2-视频动作迁移+换背景_2065407497409753090.json, 视频生成/图生视频/SCAIL2_动作迁移_官流_2072505774076686337.json, 视频生成/图生视频/SCAIL2_纯血官流_zip_2068277029560213505.json, 视频生成/图生视频/SCAIL2_纯血官流（单图）动作迁移＆人物替换_2067202782653935618.json, 视频生成/图生视频/SCAIL2官方工作流_2067918393696669697.json, 视频生成/图生视频/Scail2动作舞蹈模仿！长视频生成！_2082692772032761857.json, 视频生成/图生视频/短剧转绘——多人对话转绘scail2动作迁移_1995774153481392130.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_380

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/SCAIL2-动作迁移+人物替换电商短视频带货工作流+全节点注释_2071936392262934529.json、视频生成/图生视频/SCAIL2-视频动作迁移+换背景_2065407497409753090.json、视频生成/图生视频/SCAIL2_动作迁移_官流_2072505774076686337.json、视频生成/图生视频/SCAIL2_纯血官流_zip_2068277029560213505.json、视频生成/图生视频/SCAIL2_纯血官流（单图）动作迁移＆人物替换_2067202782653935618.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 7/8 个有
- `VHS_VideoInfoLoaded` —— 7/8 个有
- `WanContextWindowsManual` —— 7/8 个有
- `easy int` —— 7/8 个有
- `ImageFromBatch` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `VAEDecode` —— 6/8 个有
- `VAEDecodeTiled` —— 6/8 个有
- `GetNode` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `easy getNode` —— 5/8 个有
- `easy setNode` —— 5/8 个有
- `easy showAnything` —— 5/8 个有
- `ImpactConditionalBranch` —— 4/8 个有
- `MuyeTextEditOutput` —— 4/8 个有
- `CR Text` —— 3/8 个有
- `Fast Groups Muter (rgthree)` —— 3/8 个有
- `SimpleMath+` —— 2/8 个有
- `easy float` —— 2/8 个有
- `ComfyMathExpression` —— 1/8 个有
- `ComfyNumberConvert` —— 1/8 个有
- `ComfySwitchNode` —— 1/8 个有
- `CompressImages` —— 1/8 个有
- `Int` —— 1/8 个有
- `RTXVideoSuperResolution` —— 1/8 个有
- `VHS_SelectFilename` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 8 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/8 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，8 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
