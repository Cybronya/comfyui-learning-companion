---
name: unknown_workflow_upscale_latent_upscale_sampler_2
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.926211
common_nodes: [BasicScheduler, CFGGuider, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, RandomNoise, SamplerCustomAdvanced, UNETLoader]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3-LTX Director 2.0-导演分镜工作流-图生视频_2076256951222231041.json, 数字人/数字人/LTX2.3唱歌对口型数字人_2071844848252055554.json, 数字人/数字人/LTX_Director_2_Workflow_retake_mode重拍_2072257436500713473.json, 数字人/数字人/LTX导演台2.0白模驱动视频_2074797734040784897.json, 数字人/数字人/数字人唱歌视频工作流_2082356548390707201.json, 视频生成/图生视频/AI多镜头图片参考生成视频 Ltx2.3 Director_2080844202388312065.json, 视频生成/图生视频/AI数字人 图片加音频生成视频 Ltx2.3 Director_2080143028186079233.json, 视频生成/图生视频/AI数字人 图片加音频生成视频 Ltx2.3 Director_2080934030194855938.json, 视频生成/图生视频/LTX Director  漫剧工作台_2068975604510318594.json, 视频生成/图生视频/LTX2.3 创新导演剪辑流，创意无限！二创神器！_2055482875381862402.json, 视频生成/图生视频/LTX2.3+LTX Director V2.0 导演台升级版慢剧视频_2068969187762069506.json, 视频生成/图生视频/LTX2.3-LTX Director 2.0-导演分镜工作流-图生视频_2075939856777302017.json, 视频生成/图生视频/LTX2.3-LTX Director 2.0-导演分镜工作流-视频扩展_2076263634656907265.json, 视频生成/图生视频/LTX2.3-LTX Director 2.0-导演分镜工作流-视频编辑_2076279049718161410.json, 视频生成/图生视频/LTX2.3-LTX Director 2.0-导演分镜工作流-首尾帧视频_2075959525273849858.json, 视频生成/图生视频/LTX2.3导演台2.0Director_2072850432728326145.json, 视频生成/图生视频/LTX2.3导演台_音频驱动_修复版_2073964076115513345.json, 视频生成/文生视频/LTX2.3-LTX Director 2.0-导演分镜工作流-文生视频_2075921500900782081.json, 视频生成/文生视频/LTX2.3导演台2.0工作流_2081613434218700801.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/LTX2.3-LTX Director 2.0-导演分镜工作流-图生视频_2076256951222231041.json、数字人/数字人/LTX2.3唱歌对口型数字人_2071844848252055554.json、数字人/数字人/LTX_Director_2_Workflow_retake_mode重拍_2072257436500713473.json、数字人/数字人/LTX导演台2.0白模驱动视频_2074797734040784897.json、数字人/数字人/数字人唱歌视频工作流_2082356548390707201.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 18/19 个有
- `ConditioningZeroOut` —— 17/19 个有
- `LTXDirectorCropGuides` —— 16/19 个有
- `VAELoader` —— 16/19 个有
- `VAELoaderKJ` —— 16/19 个有
- `ModelPreviewOverrideKJ` —— 12/19 个有
- `CreateVideo` —— 11/19 个有
- `LoraLoaderModelOnly` —— 11/19 个有
- `VHS_VideoCombine` —— 10/19 个有
- `SaveVideo` —— 9/19 个有
- `孤海注释` —— 6/19 个有
- `CLIPTextEncode` —— 5/19 个有
- `LTX2_NAG` —— 5/19 个有
- `LTX2SamplingPreviewOverride` —— 4/19 个有
- `LTXVCropGuides` —— 3/19 个有
- `BatchCount+` —— 2/19 个有
- `ImageFromBatch` —— 2/19 个有
- `SimpleMath+` —— 2/19 个有
- `Fast Groups Bypasser (rgthree)` —— 1/19 个有
- `GetVideoComponents` —— 1/19 个有
- `Label (rgthree)` —— 1/19 个有
- `LoadImage` —— 1/19 个有
- `VAEDecodeTiled` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
