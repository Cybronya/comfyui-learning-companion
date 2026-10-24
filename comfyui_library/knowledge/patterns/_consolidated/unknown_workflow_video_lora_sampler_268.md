---
name: unknown_workflow_video_lora_sampler_268
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.965375
common_nodes: [CLIPLoader, CLIPTextEncode, DownloadAndLoadGIMMVFIModel, EmptyHunyuanLatentVideo, GIMMVFI_interpolate, INTConstant, ImageFromBatch+, ImageSharpen, JWInteger, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, TorchCompileModel, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2 Lighnining 1108 VS  1217 VS 10+4原版文生视频_2001622181756977154.json, 视频生成/文生视频/(官方版10+4)Wan2.2 HoloCine电影多镜头分镜实验版V1（目前效果一般）_1982413564600295425.json, 视频生成/文生视频/(官方版10+6)Wan2.2+Palingenesis差异加速高动态720P文生视频（慢速版）v2_1972348168056860674.json, 视频生成/文生视频/(官方版10+6)Wan2.2差异加速高动态720P文生视频v2（慢速版）_1972269268110864386.json, 视频生成/文生视频/(官方版2+2)Wan2.2新版Lighting0928-720P文生视频（极速版）V3_1972287084159496194.json, 视频生成/文生视频/Wan 2.2 lighning V2高低噪文生视频V1_1987455645072953345.json, 视频生成/文生视频/wan2.2 smooth Vs Lightning V2+混合低噪对比T2V工作流_1987359372651245570.json, 视频生成/文生视频/wan2.2 smooth Vs Lightning V2混合低噪+原版10+4对比T2V工作流_1987403122442219521.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_268

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/wan2.2 Lighnining 1108 VS  1217 VS 10+4原版文生视频_2001622181756977154.json、视频生成/文生视频/(官方版10+4)Wan2.2 HoloCine电影多镜头分镜实验版V1（目前效果一般）_1982413564600295425.json、视频生成/文生视频/(官方版10+6)Wan2.2+Palingenesis差异加速高动态720P文生视频（慢速版）v2_1972348168056860674.json、视频生成/文生视频/(官方版10+6)Wan2.2差异加速高动态720P文生视频v2（慢速版）_1972269268110864386.json、视频生成/文生视频/(官方版2+2)Wan2.2新版Lighting0928-720P文生视频（极速版）V3_1972287084159496194.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DownloadAndLoadGIMMVFIModel`
- `EmptyHunyuanLatentVideo`
- `GIMMVFI_interpolate`
- `INTConstant`
- `ImageFromBatch+`
- `ImageSharpen`
- `JWInteger`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 7/8 个有
- `easy cleanGpuUsed` —— 7/8 个有
- `LayerUtility: PurgeVRAM` —— 4/8 个有
- `ImageConcanate` —— 3/8 个有
- `SaveImage` —— 3/8 个有
- `TT_img_enc` —— 3/8 个有
- `AddLabel` —— 1/8 个有
- `CR Prompt Text` —— 1/8 个有
- `RH_LLMAPI_Pro_Node` —— 1/8 个有
- `WanContextWindowsManual` —— 1/8 个有
- `easy seed` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 100% |
| Prompt 约束强度(CFG) | 10 | 10 - 12 | 8 | 91% |
| 采样算法 | 1 | 1 - 3.5 | 8 | 33% |
| 调度器 | uni_pc | - | 8 | 62% |
| 重绘幅度 | beta | - | 8 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 12，8 个样本，取值集中（一致性 91%）
- 采样算法 中位数 1，观测区间 1 - 3.5，8 个样本，取值分散，一致性仅 33%
- 调度器 最常用 uni_pc，8 个样本，一致性 62%
- 重绘幅度 最常用 beta，8 个样本，一致性 50%
