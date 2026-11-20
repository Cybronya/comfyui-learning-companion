---
name: unknown_workflow_clip_unet_vae_3
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.8995
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, LoadImage, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/video_wan2_2_14B_flf2v.json, comfyui-workflow-templates-json/video_wan2_2_14B_fun_camera.json, comfyui-workflow-templates-json/video_wan2_2_14B_fun_inpaint.json, comfyui-workflow-templates-json/video_wan2_2_5B_fun_inpaint.json, 图片生成/文生图/Wan2.2 14B FLF2V工作流程示例_1952243604368642050.json, 视频生成/图生视频/AI视频开始懂物理了？VBVR推理模型实测：路径规划+光学反射，不再穿模！_2028386555664015362.json, 视频生成/图生视频/Wan2.2 14B极速首尾帧视频生成_2053748789495771138.json, 视频生成/图生视频/Wan2.2 分镜版本 VBVR lora逻辑推理增强PLUS版_2034133687608025089.json, 视频生成/图生视频/Wan2.2 首尾帧 VBVR lora逻辑推理增强_2028500989350776833.json, 视频生成/图生视频/Wan2.2-InP首尾帧-ComfyUI官方 (v1)_1957255296970317825.json, 视频生成/图生视频/Wan2.2-InP首尾帧-ComfyUI官方_1956752541822410754.json, 视频生成/图生视频/video_wan2_2_14B_fun_camera 趣味相机控制：视频生成工作流示例_1989241417262313474.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_3

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（comfyui-workflow-templates-json/video_wan2_2_14B_flf2v.json、comfyui-workflow-templates-json/video_wan2_2_14B_fun_camera.json、comfyui-workflow-templates-json/video_wan2_2_14B_fun_inpaint.json、comfyui-workflow-templates-json/video_wan2_2_5B_fun_inpaint.json、图片生成/文生图/Wan2.2 14B FLF2V工作流程示例_1952243604368642050.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
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
- `KSamplerAdvanced` —— 11/12 个有
- `LoraLoaderModelOnly` —— 11/12 个有
- `WanFirstLastFrameToVideo` —— 6/12 个有
- `WanFunInpaintToVideo` —— 4/12 个有
- `PrimitiveInt` —— 2/12 个有
- `Text Multiline` —— 2/12 个有
- `WanCameraEmbedding` —— 2/12 个有
- `WanCameraImageToVideo` —— 2/12 个有
- `KSampler` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `PreViewVideo` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 12 | 50% |
| Prompt 约束强度(CFG) | 5 | 4 - 20 | 12 | 28% |
| 采样算法 | 1 | 1 - 4 | 11 | 39% |
| 调度器 | euler | - | 12 | 92% |
| 重绘幅度 | simple | - | 12 | 92% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，12 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 5，观测区间 4 - 20，12 个样本，取值分散，一致性仅 28%
- 采样算法 中位数 1，观测区间 1 - 4，11 个样本，取值分散，一致性仅 39%
- 调度器 最常用 euler，12 个样本，一致性 92%
- 重绘幅度 最常用 simple，12 个样本，一致性 92%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
