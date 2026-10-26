---
name: unknown_workflow_sampler_unet_vae_218
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9768
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, CreateVideo, DualCLIPLoader, KSamplerSelect, LTX2SamplingPreviewOverride, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3 分镜导演台V2，漫剧+数字人+MV_2056302595207159810.json, 视频生成/图生视频/【阿良绘】LTX Director _ 导演工作流 V2_2064886980097429505.json, 视频生成/图生视频/【阿良绘】LTX Director _ 导演工作流 V2_2073289175195205632.json, 视频生成/图生视频/【阿良绘】LTX Director导演工作流_2059132036383858689.json, 视频生成/图生视频/图生视频漫画制作短剧制作LTX2.3-Director 导演台-多图漫剧长视频_2068702491201593346.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_218

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3 分镜导演台V2，漫剧+数字人+MV_2056302595207159810.json、视频生成/图生视频/【阿良绘】LTX Director _ 导演工作流 V2_2064886980097429505.json、视频生成/图生视频/【阿良绘】LTX Director _ 导演工作流 V2_2073289175195205632.json、视频生成/图生视频/【阿良绘】LTX Director导演工作流_2059132036383858689.json、视频生成/图生视频/图生视频漫画制作短剧制作LTX2.3-Director 导演台-多图漫剧长视频_2068702491201593346.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
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
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LTXVLatentUpsampler` —— 3/5 个有
- `LatentUpscaleModelLoader` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `SaveImage` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `DapaoImageSplitNode` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `GuHaiAutoImageSplit` —— 1/5 个有
- `Int` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `LoadVideo` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `RH_LLMAPI_Pro_Node` —— 1/5 个有
- `TT_img_enc` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
