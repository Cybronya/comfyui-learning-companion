---
name: unknown_workflow_upscale_latent_upscale_sampler
type: Unknown Workflow
frequency: 27
level: moderate
coverage: 0.840556
common_nodes: [BasicScheduler, CFGGuider, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode]
problems: []
missing: []
members: [视频生成/图生视频/2080844202388312065.json, 视频生成/图生视频/2080143028186079233.json, 视频生成/图生视频/2080934030194855938.json, 视频生成/图生视频/2068975604510318594.json, 视频生成/图生视频/2058931295174086657.json, 视频生成/图生视频/2071771328843173890.json, 视频生成/图生视频/2073210554319200257.json, 视频生成/图生视频/2072568558659391490.json, 视频生成/图生视频/2056571721142071298.json, 视频生成/图生视频/2061086858423136258.json, 视频生成/图生视频/2068969187762069506.json, 视频生成/图生视频/2057459285617102849.json, 视频生成/图生视频/2075939856777302017.json, 视频生成/图生视频/2076263634656907265.json, 视频生成/图生视频/2076279049718161410.json, 视频生成/图生视频/2075959525273849858.json, 视频生成/图生视频/2072850432728326145.json, 视频生成/图生视频/2073964076115513345.json, 视频生成/图生视频/LTX_2.3_Director_2.0_多功能导演台7.11优化版工作流_2088158819493961729.json, 视频生成/图生视频/2073922895696453634.json, 视频生成/图生视频/2072254537259372546.json, 视频生成/图生视频/2072252924708872193.json, 视频生成/图生视频/2072255653216874498.json, 视频生成/图生视频/2074755278909820930.json, 视频生成/图生视频/2072931950360350721.json, 视频生成/图生视频/2073226755028119553.json, 视频生成/图生视频/工作流基础系列29-LTX 2.3+Director导演台_2085570972542922754.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（视频生成/图生视频/2080844202388312065.json、视频生成/图生视频/2080143028186079233.json、视频生成/图生视频/2080934030194855938.json、视频生成/图生视频/2068975604510318594.json、视频生成/图生视频/2058931295174086657.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 27 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 26/27 个有
- `LTXVConditioning` —— 26/27 个有
- `VAELoaderKJ` —— 24/27 个有
- `LTXDirectorCropGuides` —— 19/27 个有
- `VAELoader` —— 18/27 个有
- `CreateVideo` —— 17/27 个有
- `SaveVideo` —— 16/27 个有
- `LoraLoaderModelOnly` —— 14/27 个有
- `ModelPreviewOverrideKJ` —— 14/27 个有
- `VHS_VideoCombine` —— 12/27 个有
- `LTXVCropGuides` —— 8/27 个有
- `GetNode` —— 7/27 个有
- `SetNode` —— 7/27 个有
- `ManualSigmas` —— 6/27 个有
- `LoadImage` —— 5/27 个有
- `CLIPTextEncode` —— 4/27 个有
- `LTX2_NAG` —— 4/27 个有
- `孤海注释` —— 4/27 个有
- `VRAM_Debug` —— 3/27 个有
- `LTX2SamplingPreviewOverride` —— 2/27 个有
- `Label (rgthree)` —— 2/27 个有
- `Fast Groups Bypasser (rgthree)` —— 1/27 个有
- `GetVideoComponents` —— 1/27 个有
- `LiconMSR` —— 1/27 个有
- `PreviewAudio` —— 1/27 个有
- `TTResolutionSelector` —— 1/27 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
