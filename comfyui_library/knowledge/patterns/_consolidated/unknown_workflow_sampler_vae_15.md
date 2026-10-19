---
name: unknown_workflow_sampler_vae_15
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.824647
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, VAEDecode]
problems: []
missing: []
members: [视频生成/图生视频/2080844202388312065.json, 视频生成/图生视频/2080143028186079233.json, 视频生成/图生视频/2080934030194855938.json, 视频生成/图生视频/2068975604510318594.json, 视频生成/图生视频/2058028747135217666.json, 视频生成/图生视频/2061320175995150338.json, 视频生成/图生视频/2069688109993910273.json, 视频生成/图生视频/2061986767871500289.json, 视频生成/图生视频/2062332561078181889.json, 视频生成/图生视频/2075939856777302017.json, 视频生成/图生视频/2076263634656907265.json, 视频生成/图生视频/2076279049718161410.json, 视频生成/图生视频/2075959525273849858.json, 视频生成/图生视频/2056198664774791169.json, 视频生成/图生视频/2056712653120294914.json, 视频生成/图生视频/2059095149111767041.json, 视频生成/文生视频/LTX2.3-LTX Director 2.0-导演分镜工作流-文生视频_2075921500900782081.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_15

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/2080844202388312065.json、视频生成/图生视频/2080143028186079233.json、视频生成/图生视频/2080934030194855938.json、视频生成/图生视频/2068975604510318594.json、视频生成/图生视频/2058028747135217666.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LTXVLatentUpsampler` —— 16/17 个有
- `LatentUpscaleModelLoader` —— 16/17 个有
- `UNETLoader` —— 14/17 个有
- `VAELoaderKJ` —— 14/17 个有
- `LoraLoaderModelOnly` —— 13/17 个有
- `VHS_VideoCombine` —— 11/17 个有
- `LTXDirectorCropGuides` —— 9/17 个有
- `VAELoader` —— 9/17 个有
- `LTX2SamplingPreviewOverride` —— 8/17 个有
- `LTXVCropGuides` —— 8/17 个有
- `CreateVideo` —— 7/17 个有
- `GetNode` —— 6/17 个有
- `ModelPreviewOverrideKJ` —— 6/17 个有
- `SaveVideo` —— 6/17 个有
- `SetNode` —— 6/17 个有
- `easy cleanGpuUsed` —— 6/17 个有
- `Anything Everywhere` —— 5/17 个有
- `孤海注释` —— 5/17 个有
- `AudioConcatenate` —— 3/17 个有
- `ImageBatchMulti` —— 3/17 个有
- `PathchSageAttentionKJ` —— 3/17 个有
- `UnetLoaderGGUF` —— 3/17 个有
- `CheckpointLoaderSimple` —— 2/17 个有
- `Fast Groups Bypasser (rgthree)` —— 1/17 个有
- `GetVideoComponents` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
