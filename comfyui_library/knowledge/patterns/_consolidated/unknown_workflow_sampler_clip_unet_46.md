---
name: unknown_workflow_sampler_clip_unet_46
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9688
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/image_to_video_wan.json, comfyui-workflow-templates-json/text_to_video_wan.json, comfyui-workflow-templates-json/video_wan2.1_fun_camera_v1.1_1.3B.json, comfyui-workflow-templates-json/video_wan2.1_fun_camera_v1.1_14B.json, 视频生成/图生视频/2038456404972933122.json, 视频生成/图生视频/1905817606274879490.json, 视频生成/图生视频/1928340598107815937.json, 视频生成/图生视频/1904560347657777154.json, 视频生成/图生视频/2046059182419353601.json, 视频生成/文生视频/图生视频WAN2.1开源_2093540211702718466.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_46

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（comfyui-workflow-templates-json/image_to_video_wan.json、comfyui-workflow-templates-json/text_to_video_wan.json、comfyui-workflow-templates-json/video_wan2.1_fun_camera_v1.1_1.3B.json、comfyui-workflow-templates-json/video_wan2.1_fun_camera_v1.1_14B.json、视频生成/图生视频/2038456404972933122.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 9/10 个有
- `CLIPVisionLoader` —— 9/10 个有
- `LoadImage` —— 9/10 个有
- `ModelSamplingSD3` —— 8/10 个有
- `CreateVideo` —— 6/10 个有
- `SaveVideo` —— 6/10 个有
- `SaveAnimatedWEBP` —— 5/10 个有
- `WanImageToVideo` —— 5/10 个有
- `SaveImage` —— 4/10 个有
- `WanCameraEmbedding` —— 4/10 个有
- `WanCameraImageToVideo` —— 4/10 个有
- `SaveWEBM` —— 2/10 个有
- `EmptyHunyuanLatentVideo` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 10 | 86% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 10 | 100% |
| 采样算法 | uni_pc | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，10 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
