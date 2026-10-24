---
name: unknown_workflow_video_upscale_sampler_24
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6805
common_nodes: [CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetNode, ImageResizeKJ, ImageSmartSharpen+, KSampler, LoadImage, ModelSamplingSD3, RH_Captioner, SeargePromptText, SetNode, ShowText|pysssss, SimpleCondition+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, Video_Upscale_With_Model, WanVideoEnhanceAVideoKJ]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/🈚️i2v图生视频_官方Native-Wan_FusionX_1935035535151046657.json, 视频生成/图生视频/🈚️首尾帧vace-官方native-wan fusionX_1935039588719370241.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_24

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/🈚️i2v图生视频_官方Native-Wan_FusionX_1935035535151046657.json、视频生成/图生视频/🈚️首尾帧vace-官方native-wan fusionX_1935039588719370241.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `GetNode`
- `ImageResizeKJ`
- `ImageSmartSharpen+`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `RH_Captioner`
- `SeargePromptText`
- `SetNode`
- `ShowText|pysssss`
- `SimpleCondition+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `Video_Upscale_With_Model`
- `WanVideoEnhanceAVideoKJ`

**可变部分**（部分 workflow 才有）：
- `ApplySageAttention` —— 1/2 个有
- `CLIPVisionEncode` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `SkipLayerGuidanceWanVideo` —— 1/2 个有
- `TrimVideoLatent` —— 1/2 个有
- `WanImageToVideo` —— 1/2 个有
- `WanVaceToVideo` —— 1/2 个有
- `WanVideoTeaCacheKJ` —— 1/2 个有
- `WanVideoVACEStartToEndFrame` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有
- `wanBlockSwap` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
