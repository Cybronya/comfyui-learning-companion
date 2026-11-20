---
name: unknown_workflow_video_lora_sampler_232
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.574455
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ComfyMathExpression, DiffusionModelLoaderKJ, DownloadAndLoadGIMMVFIModel, Fast Groups Muter (rgthree), GIMMVFI_interpolate, GetNode, ImageFromBatch, ImageResizeKJv2, ImpactConditionalBranch, ImpactSwitch, Int, KSampler, LoadImage, LoraLoaderModelOnly, MinNode, ModelSamplingSD3, PreviewImage, PrimitiveBoolean, SAM3_VideoTrack, SCAIL2ColoredMask, SetNode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanContextWindowsManual, WanSCAILToVideo, easy cleanGpuUsed, easy imageRemBg, easy int, easy showAnything, 图像缩放V2_孤海]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [平台全量/Scail2动作迁移(支持多参_优化版本）_2085663603537043458.json, 平台全量/Scail2动作迁移(支持多参_纯血官流）_2068726908203921410.json, 平台全量/Scail2动作迁移(支持多参_纯血官流）_2085658640178040834.json, 平台全量/动作迁移人物替换最新Scail2(多参考图版)V2_2101859248408977410.json, 平台全量/动作迁移人物替换最新Scail2(多参考图版)V2_2102675821008867329.json, 平台全量/动作迁移最新Scail2(支持多参考图)_2068531506972282881.json, 平台全量/动作迁移最新Scail2(支持多参考图)_2070003903676112897.json, 平台全量/视频换人_角色替换_全自动_SCAIL2_2068361359150112770.json, 数字人/数字人/动作迁移人物替换最新Scail2(多参考图版)V3_2078363419417333761.json, 视频生成/图生视频/SCAIL2视频换人_角色替换-雯雯的后宫_2076246273501515777.json, 视频生成/图生视频/电商带货 剧情模仿 动作迁移最新Scail2多参考图_2076969142116245505.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_232

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/Scail2动作迁移(支持多参_优化版本）_2085663603537043458.json、平台全量/Scail2动作迁移(支持多参_纯血官流）_2068726908203921410.json、平台全量/Scail2动作迁移(支持多参_纯血官流）_2085658640178040834.json、平台全量/动作迁移人物替换最新Scail2(多参考图版)V2_2101859248408977410.json、平台全量/动作迁移人物替换最新Scail2(多参考图版)V2_2102675821008867329.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：57%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `DiffusionModelLoaderKJ`
- `DownloadAndLoadGIMMVFIModel`
- `Fast Groups Muter (rgthree)`
- `GIMMVFI_interpolate`
- `GetNode`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImpactConditionalBranch`
- `ImpactSwitch`
- `Int`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MinNode`
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
- `easy cleanGpuUsed`
- `easy imageRemBg`
- `easy int`
- `easy showAnything`
- `图像缩放V2_孤海`

**可变部分**（部分 workflow 才有）：
- `AFL:ImageSwitch` —— 9/11 个有
- `Fast Groups Bypasser (rgthree)` —— 9/11 个有
- `ImageBatchMulti` —— 9/11 个有
- `ImpactIfNone` —— 9/11 个有
- `InversionDemoLazySwitch` —— 9/11 个有
- `Text` —— 9/11 个有
- `VAEDecodeTiled` —— 8/11 个有
- `CompressImages` —— 5/11 个有
- `SimpleMath+` —— 5/11 个有
- `VAEDecode` —— 5/11 个有
- `VHS_SelectFilename` —— 5/11 个有
- `忽略多组孤海` —— 3/11 个有
- `MuyeTextEditOutput` —— 2/11 个有
- `easy anythingIndexSwitch` —— 2/11 个有
- `easy getNode` —— 2/11 个有
- `easy setNode` —— 2/11 个有
- `孤海注释` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 6/11 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
- 高发问题（6/11 个样本）：发现KSampler但没有VAEDecode
