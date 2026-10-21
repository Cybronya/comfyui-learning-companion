---
name: unknown_workflow_sampler_vae_20
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.812231
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/2061320175995150338.json, 视频生成/图生视频/2069688109993910273.json, 视频生成/图生视频/2055482875381862402.json, 视频生成/图生视频/2061986767871500289.json, 视频生成/图生视频/2062332561078181889.json, 视频生成/图生视频/2056198664774791169.json, 视频生成/图生视频/2073044076907294721.json, 视频生成/图生视频/2059896575970861058.json, 视频生成/图生视频/2055094635088891905.json, 视频生成/图生视频/2061748200293355521.json, 视频生成/图生视频/2069360572709298178.json, 视频生成/图生视频/2056712653120294914.json, 视频生成/图生视频/2059095149111767041.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_20

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/2061320175995150338.json、视频生成/图生视频/2069688109993910273.json、视频生成/图生视频/2055482875381862402.json、视频生成/图生视频/2061986767871500289.json、视频生成/图生视频/2062332561078181889.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 13 个 workflow 都包含：
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
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LTX2SamplingPreviewOverride` —— 12/13 个有
- `LatentUpscaleModelLoader` —— 12/13 个有
- `LoraLoaderModelOnly` —— 11/13 个有
- `VAEDecode` —— 11/13 个有
- `VHS_VideoCombine` —— 11/13 个有
- `LTXVLatentUpsampler` —— 10/13 个有
- `UNETLoader` —— 10/13 个有
- `GetNode` —— 7/13 个有
- `PathchSageAttentionKJ` —— 7/13 个有
- `SetNode` —— 7/13 个有
- `easy cleanGpuUsed` —— 7/13 个有
- `Anything Everywhere` —— 5/13 个有
- `CheckpointLoaderSimple` —— 5/13 个有
- `CreateVideo` —— 5/13 个有
- `UnetLoaderGGUF` —— 5/13 个有
- `SaveVideo` —— 4/13 个有
- `AudioConcatenate` —— 3/13 个有
- `ImageBatchMulti` —— 3/13 个有
- `CR Prompt Text` —— 2/13 个有
- `Fast Groups Bypasser (rgthree)` —— 2/13 个有
- `Lora Loader Stack (rgthree)` —— 2/13 个有
- `RH_LLMAPI_Pro_Node` —— 2/13 个有
- `VAEDecodeTiled` —— 2/13 个有
- `solarL_SaveImagesToZip` —— 2/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
