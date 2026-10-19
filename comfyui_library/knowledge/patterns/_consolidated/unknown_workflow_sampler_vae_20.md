---
name: unknown_workflow_sampler_vae_20
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.952308
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced]
problems: []
missing: []
members: [视频生成/图生视频/2059276164383985666.json, 视频生成/图生视频/2057350661624393729.json, 视频生成/图生视频/2061748200293355521.json, 视频生成/图生视频/2069360572709298178.json, 视频生成/图生视频/2064886980097429505.json, 视频生成/图生视频/2073289175195205632.json, 视频生成/图生视频/2059132036383858689.json, 视频生成/图生视频/2058003640417349634.json, 视频生成/图生视频/2068702491201593346.json, 视频生成/图生视频/2056691705071620098.json, 视频生成/图生视频/2056028640659427329.json, 视频生成/文生视频/LTX 2.3 Director 导演工作台 ComfyUI 在线工作流_2060986578205503489.json, 视频生成/文生视频/LTX Director 导演工作台 (2采)_2064170624049827841.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_20

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/2059276164383985666.json、视频生成/图生视频/2057350661624393729.json、视频生成/图生视频/2061748200293355521.json、视频生成/图生视频/2069360572709298178.json、视频生成/图生视频/2064886980097429505.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `ConditioningZeroOut`
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

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 12/13 个有
- `DualCLIPLoader` —— 12/13 个有
- `LTX2SamplingPreviewOverride` —— 12/13 个有
- `LatentUpscaleModelLoader` —— 11/13 个有
- `SaveVideo` —— 11/13 个有
- `VAELoaderKJ` —— 11/13 个有
- `VAEDecode` —— 10/13 个有
- `CheckpointLoaderSimple` —— 9/13 个有
- `LTXVLatentUpsampler` —— 9/13 个有
- `LoraLoaderModelOnly` —— 9/13 个有
- `UNETLoader` —— 6/13 个有
- `VHS_VideoCombine` —— 4/13 个有
- `PathchSageAttentionKJ` —— 3/13 个有
- `VAEDecodeTiled` —— 3/13 个有
- `CR Prompt Text` —— 2/13 个有
- `LTXAVTextEncoderLoader` —— 2/13 个有
- `LTXVAudioVAELoader` —— 2/13 个有
- `Lora Loader Stack (rgthree)` —— 2/13 个有
- `RH_LLMAPI_Pro_Node` —— 2/13 个有
- `UnetLoaderGGUF` —— 2/13 个有
- `solarL_SaveImagesToZip` —— 2/13 个有
- `GetNode` —— 1/13 个有
- `SaveImage` —— 1/13 个有
- `SetNode` —— 1/13 个有
- `TT_img_enc` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
