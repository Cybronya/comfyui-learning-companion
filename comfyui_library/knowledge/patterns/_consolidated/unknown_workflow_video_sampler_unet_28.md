---
name: unknown_workflow_video_sampler_unet_28
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.6439
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DualCLIPLoader, GetNode, KSamplerSelect, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2056245217631756289.json, 视频生成/图生视频/2064037629812895745.json, 视频生成/图生视频/2064373452538208258.json, 视频生成/图生视频/2075025517912346625.json, 视频生成/图生视频/2070124907555545090.json, 视频生成/图生视频/2070402488083238913.json, 视频生成/图生视频/2062509553996091394.json, 视频生成/图生视频/2062715570117758978.json, 视频生成/图生视频/2071479057736355841.json, 视频生成/图生视频/2057271107857768450.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_28

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2056245217631756289.json、视频生成/图生视频/2064037629812895745.json、视频生成/图生视频/2064373452538208258.json、视频生成/图生视频/2075025517912346625.json、视频生成/图生视频/2070124907555545090.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `GetNode`
- `KSamplerSelect`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/10 个有
- `LoadImage` —— 7/10 个有
- `TTResolutionSelector` —— 7/10 个有
- `PreviewAny` —— 6/10 个有
- `RH_LLMAPI_Pro_Node` —— 6/10 个有
- `CS-LTXGridDirector` —— 5/10 个有
- `Fast Groups Bypasser (rgthree)` —— 3/10 个有
- `LTXDirector` —— 3/10 个有
- `CS-LTXSixGridDirector` —— 2/10 个有
- `DiffusionModelLoaderKJ` —— 2/10 个有
- `Int` —— 2/10 个有
- `JjkText` —— 2/10 个有
- `RHSettingsNode` —— 2/10 个有
- `RH_RhartImageG2TextToImage` —— 2/10 个有
- `RH_Utils` —— 2/10 个有
- `SaveImage` —— 2/10 个有
- `Text` —— 2/10 个有
- `ttN concat` —— 2/10 个有
- `孤海注释` —— 2/10 个有
- `AppParams` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
