---
name: text_to_image_video_lora_sampler_84
type: Text To Image
frequency: 9
level: strong
coverage: 0.649444
common_nodes: [AFL:ImageSwitch, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ComfyMathExpression, DiffusionModelLoaderKJ, DownloadAndLoadGIMMVFIModel, EmptyLatentImage, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), GIMMVFI_interpolate, GetNode, ImageBatchMulti, ImageFromBatch, ImageResizeKJv2, ImpactConditionalBranch, ImpactIfNone, ImpactSwitch, Int, InversionDemoLazySwitch, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MinNode, ModelSamplingSD3, PreviewImage, PrimitiveBoolean, SAM3_VideoTrack, SCAIL2ColoredMask, SetNode, Text, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanContextWindowsManual, WanSCAILToVideo, easy cleanGpuUsed, easy imageRemBg, easy int, easy showAnything, solarL_SaveImagesToZip, 图像缩放V2_孤海, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Scail2纯血官流动作迁移｜多参数灵活适配角色场景_2092721335620431874.json, 图片生成/图生图/Scail2纯血官流动作迁移｜多参数适配角色场景图生图_2093124409627340802.json, 图片生成/图生图/Scail2纯血官流版动作迁移｜多参数灵活适配角色场景_2090547739670179841.json, 图片生成/图生图/动作迁移Scail2纯血官流版 多参数支持灵活适配各类角色场景_2092547310298419202.json, 图片生成/图生图/纯血官流版动作迁移｜Scail2多参数灵活适配场景_2092923769936506881.json, 数字人/数字人/Scail2多参考图版V3动作迁移人物替换视频处理工具_2102475358082781185.json, 数字人/数字人/Scail2最新版｜多参考图动作迁移人物替换｜美少女数字人一键换主角_2102207160028581890.json, 数字人/数字人/动作迁移人物替换Scail2多参考图版V2工具_2100265714266497026.json, 视频生成/图生视频/Scail2最新版｜多参考图动作迁移人物替换｜美少女数字人一键换主角_2104059415866462210.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_84

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Scail2纯血官流动作迁移｜多参数灵活适配角色场景_2092721335620431874.json、图片生成/图生图/Scail2纯血官流动作迁移｜多参数适配角色场景图生图_2093124409627340802.json、图片生成/图生图/Scail2纯血官流版动作迁移｜多参数灵活适配角色场景_2090547739670179841.json、图片生成/图生图/动作迁移Scail2纯血官流版 多参数支持灵活适配各类角色场景_2092547310298419202.json、图片生成/图生图/纯血官流版动作迁移｜Scail2多参数灵活适配场景_2092923769936506881.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 9 个 workflow 都包含：
- `AFL:ImageSwitch`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `DiffusionModelLoaderKJ`
- `DownloadAndLoadGIMMVFIModel`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `GIMMVFI_interpolate`
- `GetNode`
- `ImageBatchMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImpactConditionalBranch`
- `ImpactIfNone`
- `ImpactSwitch`
- `Int`
- `InversionDemoLazySwitch`
- `JjkText`
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
- `Text`
- `UNETLoader`
- `VAEDecode`
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
- `solarL_SaveImagesToZip`
- `图像缩放V2_孤海`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CompressImages` —— 5/9 个有
- `VAEDecodeTiled` —— 5/9 个有
- `VHS_SelectFilename` —— 5/9 个有
- `SimpleMath+` —— 4/9 个有
- `SaveImage` —— 2/9 个有
- `忽略多组孤海` —— 2/9 个有
- `EmptyImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（21/9 个样本）：Steps较低可能导致细节不足
