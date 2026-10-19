---
name: unknown_workflow_clip_unet_vae
type: Unknown Workflow
frequency: 14
level: weak
coverage: 0.896643
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, LoadImage, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/video_wan2_2_14B_flf2v.json, comfyui-workflow-templates-json/video_wan2_2_14B_fun_camera.json, comfyui-workflow-templates-json/video_wan2_2_14B_fun_inpaint.json, comfyui-workflow-templates-json/video_wan2_2_5B_fun_inpaint.json, 图片生成/文生图/1952243604368642050.json, 视频生成/图生视频/1952243604368642050.json, 视频生成/图生视频/2028386555664015362.json, 视频生成/图生视频/2053748789495771138.json, 视频生成/图生视频/2034133687608025089.json, 视频生成/图生视频/2028500989350776833.json, 视频生成/图生视频/1957255296970317825.json, 视频生成/图生视频/1956752541822410754.json, 视频生成/图生视频/1989241417262313474.json, 视频生成/图生视频/1956204129557336066.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（comfyui-workflow-templates-json/video_wan2_2_14B_flf2v.json、comfyui-workflow-templates-json/video_wan2_2_14B_fun_camera.json、comfyui-workflow-templates-json/video_wan2_2_14B_fun_inpaint.json、comfyui-workflow-templates-json/video_wan2_2_5B_fun_inpaint.json、图片生成/文生图/1952243604368642050.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 13/14 个有
- `LoraLoaderModelOnly` —— 13/14 个有
- `WanFirstLastFrameToVideo` —— 8/14 个有
- `WanFunInpaintToVideo` —— 5/14 个有
- `Label (rgthree)` —— 2/14 个有
- `PrimitiveInt` —— 2/14 个有
- `Text Multiline` —— 2/14 个有
- `WanCameraEmbedding` —— 2/14 个有
- `WanCameraImageToVideo` —— 2/14 个有
- `KSampler` —— 1/14 个有
- `PreViewVideo` —— 1/14 个有
- `VHS_LoadVideo` —— 1/14 个有
- `Wan22FunControlToVideo` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 14 | 50% |
| Prompt 约束强度(CFG) | 5 | 4 - 20 | 14 | 29% |
| 采样算法 | 1 | 1 - 4 | 13 | 39% |
| 调度器 | euler | - | 14 | 93% |
| 重绘幅度 | simple | - | 14 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，14 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 5，观测区间 4 - 20，14 个样本，取值分散，一致性仅 29%
- 采样算法 中位数 1，观测区间 1 - 4，13 个样本，取值分散，一致性仅 39%
- 调度器 最常用 euler，14 个样本，一致性 93%
- 重绘幅度 最常用 simple，14 个样本，一致性 93%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
