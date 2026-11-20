---
name: unknown_workflow_sampler_clip_unet_173
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.95325
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/image_to_video_wan.json, comfyui-workflow-templates-json/text_to_video_wan.json, comfyui-workflow-templates-json/video_wan2.1_fun_camera_v1.1_1.3B.json, comfyui-workflow-templates-json/video_wan2.1_fun_camera_v1.1_14B.json, 平台全量/图生视频_2041089234244734977.json, 视频生成/图生视频/Wan2.1_Fun_V1.1_Control_Camera_1.3B_I2V_2038456404972933122.json, 视频生成/图生视频/wan2.1-图生视频-发光的身体_1905817606274879490.json, 视频生成/图生视频/图生视频_2046059182419353601.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_173

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（comfyui-workflow-templates-json/image_to_video_wan.json、comfyui-workflow-templates-json/text_to_video_wan.json、comfyui-workflow-templates-json/video_wan2.1_fun_camera_v1.1_1.3B.json、comfyui-workflow-templates-json/video_wan2.1_fun_camera_v1.1_14B.json、平台全量/图生视频_2041089234244734977.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 7/8 个有
- `CLIPVisionLoader` —— 7/8 个有
- `CreateVideo` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `SaveVideo` —— 7/8 个有
- `WanCameraEmbedding` —— 5/8 个有
- `WanCameraImageToVideo` —— 5/8 个有
- `SaveAnimatedWEBP` —— 2/8 个有
- `WanImageToVideo` —— 2/8 个有
- `EmptyHunyuanLatentVideo` —— 1/8 个有
- `SaveImage` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 8 | 84% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 8 | 100% |
| 采样算法 | uni_pc | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，8 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
