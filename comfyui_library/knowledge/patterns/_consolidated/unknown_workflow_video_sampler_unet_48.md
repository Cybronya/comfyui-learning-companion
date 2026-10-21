---
name: unknown_workflow_video_sampler_unet_48
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.675286
common_nodes: [BasicScheduler, CFGGuider, DualCLIPLoader, GetNode, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, SetNode, TTResolutionSelector, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2078873049419571202.json, 视频生成/图生视频/2061378483611328514.json, 视频生成/图生视频/2062509553996091394.json, 视频生成/图生视频/2062715570117758978.json, 视频生成/图生视频/2071479057736355841.json, 视频生成/文生视频/万象+rh九宫格横屏1280导演台自动化工作流（固定18秒）_2067903674852134913.json, 视频生成/文生视频/万象+rh九宫格横屏1280导演台自动化工作流（固定20秒）_2069405147431792641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_48

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2078873049419571202.json、视频生成/图生视频/2061378483611328514.json、视频生成/图生视频/2062509553996091394.json、视频生成/图生视频/2062715570117758978.json、视频生成/图生视频/2071479057736355841.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `DualCLIPLoader`
- `GetNode`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `LTXDirectorGuide` —— 6/7 个有
- `LTXVCropGuides` —— 6/7 个有
- `LoadImage` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `PreviewAny` —— 5/7 个有
- `RH_LLMAPI_Pro_Node` —— 5/7 个有
- `CS-LTXGridDirector` —— 3/7 个有
- `CS-LTXSixGridDirector` —— 2/7 个有
- `LTXDirector` —— 2/7 个有
- `LoadVideo` —— 2/7 个有
- `Text Multiline` —— 2/7 个有
- `CLIPTextEncode` —— 1/7 个有
- `CS-LTXDirectorGuide` —— 1/7 个有
- `DiffusionModelLoaderKJ` —— 1/7 个有
- `LTXDirectorCropGuides` —— 1/7 个有
- `LTXVLatentUpsampler` —— 1/7 个有
- `LatentUpscaleModelLoader` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
