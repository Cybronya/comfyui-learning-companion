---
name: unknown_workflow_sampler_clip_unet_81
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.952
common_nodes: [CFGZeroStar, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, ModelSamplingSD3, SkipLayerGuidanceDiT, UNETLoader, UNetTemporalAttentionMultiply, VAEDecode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/wan2.1_fun_control.json, comfyui-workflow-templates-json/wan2.1_fun_inp.json, 视频生成/图生视频/1951294089633452033.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_81

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（comfyui-workflow-templates-json/wan2.1_fun_control.json、comfyui-workflow-templates-json/wan2.1_fun_inp.json、视频生成/图生视频/1951294089633452033.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `SkipLayerGuidanceDiT`
- `UNETLoader`
- `UNetTemporalAttentionMultiply`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 2/3 个有
- `SaveVideo` —— 2/3 个有
- `WanFunInpaintToVideo` —— 2/3 个有
- `Canny` —— 1/3 个有
- `GetVideoComponents` —— 1/3 个有
- `LoadVideo` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有
- `WanFunControlToVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
