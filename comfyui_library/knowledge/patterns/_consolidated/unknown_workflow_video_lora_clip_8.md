---
name: unknown_workflow_video_lora_clip_8
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.644917
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DiffusionModelLoaderKJ, Int, LoraLoaderModelOnly, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/SCAIL2-视频人物替换（支持多角色替换）_2064687757309595649.json, 平台全量/SCAIL2-视频动作迁移_2064700829717852162.json, 平台全量/SCAIL2-视频多人替换（长视频for循环）+人物重打光_2078331610633691138.json, 平台全量/SCAIL2-视频背景重绘（须纯色背景视频）_2065605888550985729.json, 平台全量/Scail2-视频指定人物替换_2066888662197039106.json, 平台全量/人物替换_动作迁移-SCAIL2-循环长视频_2064902917202735105.json, 数字人/数字人/SCAIL2人物替换_2064916188177719298.json, 数字人/数字人/scail动作迁移_2004737349160497153.json, 数字人/数字人/女装带货_2089734181499789314.json, 视频生成/图生视频/SCAIL2 全自动循环流+替换人物+动作模仿_2067092376300122114.json, 视频生成/图生视频/SCAIL2视频人物替换无限时长替换人物动作迁移人物替换_2065218467845988354.json, 视频生成/图生视频/视频主角想换就换！SCAIL2人物替换工作流｜全节点注释直接抄_2065014891525795842.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_8

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（平台全量/SCAIL2-视频人物替换（支持多角色替换）_2064687757309595649.json、平台全量/SCAIL2-视频动作迁移_2064700829717852162.json、平台全量/SCAIL2-视频多人替换（长视频for循环）+人物重打光_2078331610633691138.json、平台全量/SCAIL2-视频背景重绘（须纯色背景视频）_2065605888550985729.json、平台全量/Scail2-视频指定人物替换_2066888662197039106.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DiffusionModelLoaderKJ`
- `Int`
- `LoraLoaderModelOnly`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 11/12 个有
- `LoadImage` —— 11/12 个有
- `ModelSamplingSD3` —— 10/12 个有
- `easy imageRemBg` —— 9/12 个有
- `GetImageRangeFromBatch` —— 8/12 个有
- `easy batchAnything` —— 8/12 个有
- `easy forLoopEnd` —— 8/12 个有
- `easy forLoopStart` —— 8/12 个有
- `CheckpointLoaderSimple` —— 7/12 个有
- `SAM3_VideoTrack` —— 7/12 个有
- `SCAIL2ColoredMask` —— 7/12 个有
- `BasicScheduler` —— 6/12 个有
- `GetNode` —— 6/12 个有
- `KSampler` —— 6/12 个有
- `KSamplerSelect` —— 6/12 个有
- `MathExpression|pysssss` —— 6/12 个有
- `PreviewImage` —— 6/12 个有
- `SamplerCustom` —— 6/12 个有
- `SetNode` —— 6/12 个有
- `SimpleMath+` —— 6/12 个有
- `easy showAnything` —— 6/12 个有
- `ComfyNumberConvert` —— 5/12 个有
- `VHS_VideoInfoLoaded` —— 5/12 个有
- `CR Text` —— 4/12 个有
- `ImageConcatMulti` —— 4/12 个有
- `ComfyMathExpression` —— 2/12 个有
- `DF_Int_to_Float` —— 2/12 个有
- `TTResolutionSelector` —— 2/12 个有
- `VHS_VideoInfo` —— 2/12 个有
- `CM_IntToFloat` —— 1/12 个有
- `ImageFromBatch` —— 1/12 个有
- `ImageResize+` —— 1/12 个有
- `Primitive integer [Crystools]` —— 1/12 个有
- `easy boolean` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 6 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（8/12 个样本）：Steps较低可能导致细节不足
