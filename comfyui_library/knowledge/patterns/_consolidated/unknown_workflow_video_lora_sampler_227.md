---
name: unknown_workflow_video_lora_sampler_227
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.619333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SAM3_VideoTrack, SCAIL2ColoredMask, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy imageRemBg]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/2071936392262934529.json, 视频生成/图生视频/2065407497409753090.json, 视频生成/图生视频/2072505774076686337.json, 视频生成/图生视频/2068277029560213505.json, 视频生成/图生视频/2067202782653935618.json, 视频生成/图生视频/2067918393696669697.json, 视频生成/图生视频/2082692772032761857.json, 视频生成/图生视频/2073534746168217601.json, 视频生成/图生视频/1995774153481392130.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_227

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2071936392262934529.json、视频生成/图生视频/2065407497409753090.json、视频生成/图生视频/2072505774076686337.json、视频生成/图生视频/2068277029560213505.json、视频生成/图生视频/2067202782653935618.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 9 个 workflow 都包含：
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
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 8/9 个有
- `VHS_VideoInfoLoaded` —— 8/9 个有
- `WanSCAILToVideo` —— 8/9 个有
- `easy int` —— 8/9 个有
- `ImageFromBatch` —— 7/9 个有
- `SetNode` —— 7/9 个有
- `VAEDecodeTiled` —— 7/9 个有
- `WanContextWindowsManual` —— 7/9 个有
- `GetNode` —— 6/9 个有
- `PreviewImage` —— 6/9 个有
- `VAEDecode` —— 6/9 个有
- `easy getNode` —— 6/9 个有
- `easy setNode` —— 6/9 个有
- `easy showAnything` —— 6/9 个有
- `ImpactConditionalBranch` —— 5/9 个有
- `MuyeTextEditOutput` —— 5/9 个有
- `Fast Groups Muter (rgthree)` —— 4/9 个有
- `CR Text` —— 3/9 个有
- `easy float` —— 3/9 个有
- `SimpleMath+` —— 2/9 个有
- `ComfyMathExpression` —— 1/9 个有
- `ComfyNumberConvert` —— 1/9 个有
- `ComfySwitchNode` —— 1/9 个有
- `CompressImages` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `ImageBatchMulti` —— 1/9 个有
- `ImageFromBatch+` —— 1/9 个有
- `Int` —— 1/9 个有
- `RTXVideoSuperResolution` —— 1/9 个有
- `VHS_SelectFilename` —— 1/9 个有
- `WanSCAILContextWindows` —— 1/9 个有
- `WanSCAILToVideoMultiRef` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 9 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 3/9 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，9 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
