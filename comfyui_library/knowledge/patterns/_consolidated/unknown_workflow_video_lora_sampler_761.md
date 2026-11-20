---
name: unknown_workflow_video_lora_sampler_761
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.835
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DrawViTPose, GetImageSize, ImageFromBatch+, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, OnnxDetectionModelLoader, PathchSageAttentionKJ, PoseAndFaceDetection, SimpleMath+, TorchCompileModelWanVideoV2, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanAnimateToVideo, easy int, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/爆款舞蹈视频复刻，高清超高一致性，涨粉利器_2027070947370471426.json, 视频生成/图生视频/爆款舞蹈视频复刻，高清超高一致性，涨粉利器_2038584125384302594.json, 视频生成/图生视频/跳舞动作模仿_2070380445308645377.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_761

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/爆款舞蹈视频复刻，高清超高一致性，涨粉利器_2027070947370471426.json、视频生成/图生视频/爆款舞蹈视频复刻，高清超高一致性，涨粉利器_2038584125384302594.json、视频生成/图生视频/跳舞动作模仿_2070380445308645377.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetImageSize`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `OnnxDetectionModelLoader`
- `PathchSageAttentionKJ`
- `PoseAndFaceDetection`
- `SimpleMath+`
- `TorchCompileModelWanVideoV2`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanAnimateToVideo`
- `easy int`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 3 | 3 - 4 | 3 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | sa_solver | - | 3 | 100% |
| 调度器 | linear_quadratic | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 3，观测区间 3 - 4，3 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，3 个样本，一致性 100%
- 调度器 最常用 linear_quadratic，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
