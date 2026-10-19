---
name: unknown_workflow_sampler_clip_unet_41
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.908833
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/video_wan2_2_5B_ti2v.json, comfyui-workflow-templates-json/video_wan_ati.json, comfyui-workflow-templates-json/wan2.1_flf2v_720_f16.json, 视频生成/图生视频/1989234682468372481.json, 视频生成/图生视频/1949854984923996162.json, 视频生成/图生视频/1948615618990866434.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_41

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（comfyui-workflow-templates-json/video_wan2_2_5B_ti2v.json、comfyui-workflow-templates-json/video_wan_ati.json、comfyui-workflow-templates-json/wan2.1_flf2v_720_f16.json、视频生成/图生视频/1989234682468372481.json、视频生成/图生视频/1949854984923996162.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 4/6 个有
- `CLIPVisionLoader` —— 4/6 个有
- `CreateVideo` —— 4/6 个有
- `SaveVideo` —— 4/6 个有
- `WanFirstLastFrameToVideo` —— 3/6 个有
- `VHS_VideoCombine` —— 2/6 个有
- `Wan22ImageToVideoLatent` —— 2/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `LoadImageFromUrl` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `WanTrackToVideo` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 5 | 6 | 74% |
| 采样算法 | uni_pc | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 5，6 个样本
- 采样算法 最常用 uni_pc，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
