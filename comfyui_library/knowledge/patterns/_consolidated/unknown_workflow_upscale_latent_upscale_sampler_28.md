---
name: unknown_workflow_upscale_latent_upscale_sampler_28
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.979
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, CreateVideo, DualCLIPLoader, KSamplerSelect, LTX2SamplingPreviewOverride, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, SaveVideo, UNETLoader, VAEDecode, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3 分镜导演台V2，漫剧+数字人+MV_2056302595207159810.json, 视频生成/图生视频/图生视频漫画制作短剧制作LTX2.3-Director 导演台-多图漫剧长视频_2068702491201593346.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_28

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3 分镜导演台V2，漫剧+数字人+MV_2056302595207159810.json、视频生成/图生视频/图生视频漫画制作短剧制作LTX2.3-Director 导演台-多图漫剧长视频_2068702491201593346.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `ConditioningZeroOut`
- `CreateVideo`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `DapaoImageSplitNode` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GuHaiAutoImageSplit` —— 1/2 个有
- `Int` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `LoadVideo` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `TT_img_enc` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
