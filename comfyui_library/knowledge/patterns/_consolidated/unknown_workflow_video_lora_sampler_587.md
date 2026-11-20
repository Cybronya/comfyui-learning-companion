---
name: unknown_workflow_video_lora_sampler_587
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.98975
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, INTConstant, ImageFromBatch+, JWInteger, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, TT_img_enc, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2 Lighnining 1108 VS  1217 VS 10+4原版文生视频_2001622181756977154.json, 视频生成/文生视频/Wan2.2 lightx2v 1217文生视频V1_2001672195485122562.json, 视频生成/文生视频/wan2.2 smooth Vs Lightning V2+混合低噪对比T2V工作流_1987359372651245570.json, 视频生成/文生视频/wan2.2 smooth Vs Lightning V2混合低噪+原版10+4对比T2V工作流_1987403122442219521.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_587

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/wan2.2 Lighnining 1108 VS  1217 VS 10+4原版文生视频_2001622181756977154.json、视频生成/文生视频/Wan2.2 lightx2v 1217文生视频V1_2001672195485122562.json、视频生成/文生视频/wan2.2 smooth Vs Lightning V2+混合低噪对比T2V工作流_1987359372651245570.json、视频生成/文生视频/wan2.2 smooth Vs Lightning V2混合低噪+原版10+4对比T2V工作流_1987403122442219521.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `INTConstant`
- `ImageFromBatch+`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveImage`
- `TT_img_enc`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 3/4 个有
- `GIMMVFI_interpolate` —— 3/4 个有
- `ImageConcanate` —— 3/4 个有
- `ImageSharpen` —— 3/4 个有
- `TorchCompileModel` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `easy seed` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `AddLabel` —— 1/4 个有
- `RH_LLMAPI_Pro_Node` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 12 | 12 - 12 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | uni_pc | - | 4 | 100% |
| 重绘幅度 | beta | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 12，观测区间 12 - 12，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 uni_pc，4 个样本，一致性 100%
- 重绘幅度 最常用 beta，4 个样本，一致性 100%
