---
name: unknown_workflow_video_lora_sampler_331
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.545143
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, GetNode, ImageFromBatch, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, PrimitiveBoolean, SAM3_VideoTrack, SCAIL2ColoredMask, SetNode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanContextWindowsManual, WanSCAILToVideo, easy imageRemBg, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/SCAIL2视频角色替换工作流_2114262578267512834.json, 数字人/数字人/SCAIL2-官方工作流-单参考图_2070690004116008961.json, 数字人/数字人/SCAIL2-官方工作流-多参考图_2070395563316703233.json, 数字人/数字人/scail2纯血官流（多参）_2071488701808599041.json, 数字人/数字人/动作迁移人物替换最新Scail2(多参考图版)V3_2078363419417333761.json, 视频生成/图生视频/SCAIL2视频换人_角色替换-雯雯的后宫_2076246273501515777.json, 视频生成/图生视频/电商带货 剧情模仿 动作迁移最新Scail2多参考图_2076969142116245505.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_331

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/SCAIL2视频角色替换工作流_2114262578267512834.json、数字人/数字人/SCAIL2-官方工作流-单参考图_2070690004116008961.json、数字人/数字人/SCAIL2-官方工作流-多参考图_2070395563316703233.json、数字人/数字人/scail2纯血官流（多参）_2071488701808599041.json、数字人/数字人/动作迁移人物替换最新Scail2(多参考图版)V3_2078363419417333761.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：55%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `PrimitiveBoolean`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SetNode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanContextWindowsManual`
- `WanSCAILToVideo`
- `easy imageRemBg`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImpactConditionalBranch` —— 6/7 个有
- `VAEDecodeTiled` —— 6/7 个有
- `Fast Groups Muter (rgthree)` —— 5/7 个有
- `MuyeTextEditOutput` —— 5/7 个有
- `easy getNode` —— 5/7 个有
- `easy setNode` —— 5/7 个有
- `ComfyMathExpression` —— 4/7 个有
- `ImageBatchMulti` —— 4/7 个有
- `VAEDecode` —— 4/7 个有
- `DownloadAndLoadGIMMVFIModel` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `GIMMVFI_interpolate` —— 3/7 个有
- `ImpactSwitch` —— 3/7 个有
- `Int` —— 3/7 个有
- `MinNode` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `easy float` —— 3/7 个有
- `图像缩放V2_孤海` —— 3/7 个有
- `AFL:ImageSwitch` —— 2/7 个有
- `ImpactIfNone` —— 2/7 个有
- `InversionDemoLazySwitch` —— 2/7 个有
- `SimpleMath+` —— 2/7 个有
- `Text` —— 2/7 个有
- `Vignette` —— 1/7 个有
- `easy anythingIndexSwitch` —— 1/7 个有
- `忽略多组孤海` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 3/7 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
