---
name: unknown_workflow_video_lora_sampler_79
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.5259
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, GetNode, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveBoolean, SAM3_VideoTrack, SCAIL2ColoredMask, SetNode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy imageRemBg, easy int]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/SCAIL2视频角色替换工作流_2114262578267512834.json, 图片生成/图生图/SCAIL2视频角色替换工作流_2115291790650728450.json, 平台全量/JIAN WEI SCAIL2_ 单_2073039045520871426.json, 平台全量/SCAIL-2 动作转移_2068696142724034562.json, 平台全量/SCAIL2_纯血官流（单图）_2067080216358514690.json, 平台全量/SCAIL2_纯血官流（单图）动作迁移＆人物替换_2067509446787551233.json, 平台全量/SCAIL2官流单多参考图-动作迁移替换多合一工作流_2071681846588563458.json, 平台全量/SCAIL2官流单多参考图-动作迁移替换多合一工作流_2072225373894561794.json, 平台全量/SCAIL2视频角色替换工作流_2083928461894316033.json, 平台全量/Scail2 动作迁移 l 人物替换 l 上下文高人物一致性 I 可处理分钟级视频_2080627293239726082.json, 平台全量/Scail2 动作迁移_人物替换，人物身份稳定_2080648699440623618.json, 平台全量/scail2社区官流（多参）_2067080196347482114.json, 平台全量/scail2纯血官流（多参）_2068576199093346306.json, 平台全量/多人对话转绘scail2动作迁移，有声版_2070101985281527810.json, 平台全量/长视频-角色替换或动作迁移-SCAIL2【目前开源最强】_2064775587482390530.json, 平台全量/长视频-角色替换或动作迁移-SCAIL2【纯血官流（上下文）】【syqiangk】_2067825567327674370.json, 数字人/数字人/SCAIL2-官方工作流-单参考图_2070690004116008961.json, 数字人/数字人/SCAIL2-官方工作流-多参考图_2070395563316703233.json, 数字人/数字人/scail2纯血官流（多参）_2071488701808599041.json, 视频生成/图生视频/scail2社区官流（多参）动作替换 动作迁移_2073534746168217601.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_79

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/SCAIL2视频角色替换工作流_2114262578267512834.json、图片生成/图生图/SCAIL2视频角色替换工作流_2115291790650728450.json、平台全量/JIAN WEI SCAIL2_ 单_2073039045520871426.json、平台全量/SCAIL-2 动作转移_2068696142724034562.json、平台全量/SCAIL2_纯血官流（单图）_2067080216358514690.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：53%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PrimitiveBoolean`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SetNode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy imageRemBg`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 19/20 个有
- `ImageFromBatch` —— 18/20 个有
- `VAEDecodeTiled` —— 18/20 个有
- `WanContextWindowsManual` —— 18/20 个有
- `WanSCAILToVideo` —— 18/20 个有
- `easy getNode` —— 18/20 个有
- `easy setNode` —— 18/20 个有
- `easy showAnything` —— 18/20 个有
- `Fast Groups Muter (rgthree)` —— 16/20 个有
- `MuyeTextEditOutput` —— 16/20 个有
- `ImpactConditionalBranch` —— 14/20 个有
- `easy float` —— 12/20 个有
- `ImageBatchMulti` —— 10/20 个有
- `Fast Groups Bypasser (rgthree)` —— 9/20 个有
- `VAEDecode` —— 9/20 个有
- `ComfyMathExpression` —— 4/20 个有
- `CM_FloatToInt` —— 2/20 个有
- `ComfySwitchNode` —— 2/20 个有
- `CompressImages` —— 2/20 个有
- `ImageFromBatch+` —— 2/20 个有
- `Label (rgthree)` —— 2/20 个有
- `Text` —— 2/20 个有
- `WanSCAILContextWindows` —— 2/20 个有
- `WanSCAILToVideoMultiRef` —— 2/20 个有
- `solarL_SaveImagesToZip` —— 2/20 个有
- `PlaySound|pysssss` —— 1/20 个有
- `RIFE VFI` —— 1/20 个有
- `Vignette` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 20 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 11/20 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（20/20 个样本）：Steps较低可能导致细节不足
- 高发问题（11/20 个样本）：发现KSampler但没有VAEDecode
