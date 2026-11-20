---
name: unknown_workflow_sampler_checkpoint_vae_7
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.94475
common_nodes: [CLIPVisionEncode, EmptyLatentHunyuan3Dv2, ImageOnlyCheckpointLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveGLB, VAEDecodeHunyuan3D, VoxelToMesh]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [comfyui-workflow-templates-json/3d_hunyuan3d-v2.1.json, comfyui-workflow-templates-json/3d_hunyuan3d_image_to_model.json, comfyui-workflow-templates-json/3d_hunyuan3d_multiview_to_model.json, comfyui-workflow-templates-json/3d_hunyuan3d_multiview_to_model_turbo.json, 图片生成/图生图/006.Hunyuan模型创建001.3D模型生成+录制_2035382715473731585.json, 图片生成/图生图/Hunyuan-图像转3D_2044021314901516290.json, 图片生成/图生图/Qwen_2509镜头精准控制之一混元图片转GLB模型_1990428919314735105.json, 图片生成/图生图/Qwen镜头精准控制-图片转GLB模型_1991895134199672833.json, 图片生成/图生图/混元-2d转3d_1964850814063886338.json, 平台全量/006.Hunyuan模型创建001.3D模型生成+录制_2034651948707745794.json, 平台全量/图片2d转3d模型，可用于建模软件_2004455417264701442.json, 平台全量/混元3d工作流_1964773502886793217.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_7

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（comfyui-workflow-templates-json/3d_hunyuan3d-v2.1.json、comfyui-workflow-templates-json/3d_hunyuan3d_image_to_model.json、comfyui-workflow-templates-json/3d_hunyuan3d_multiview_to_model.json、comfyui-workflow-templates-json/3d_hunyuan3d_multiview_to_model_turbo.json、图片生成/图生图/006.Hunyuan模型创建001.3D模型生成+录制_2035382715473731585.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPVisionEncode`
- `EmptyLatentHunyuan3Dv2`
- `ImageOnlyCheckpointLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveGLB`
- `VAEDecodeHunyuan3D`
- `VoxelToMesh`

**可变部分**（部分 workflow 才有）：
- `Hunyuan3Dv2Conditioning` —— 10/12 个有
- `easy imageRemBg` —— 8/12 个有
- `HfSaveImage` —— 7/12 个有
- `ImageResizeKJv2` —— 7/12 个有
- `Load3D` —— 4/12 个有
- `Hunyuan3Dv2ConditioningMultiView` —— 2/12 个有
- `FluxGuidance` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `SaveImage` —— 1/12 个有
- `VoxelToMeshBasic` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 12 | 87% |
| Prompt 约束强度(CFG) | 8 | 4 - 8 | 12 | 82% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | normal | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 8000 | 3072 - 8000 | 12 | 65% |
| 高度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 12/12 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，12 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 8，12 个样本，取值集中（一致性 82%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 normal，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 8000，观测区间 3072 - 8000，12 个样本
- 高度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：发现KSampler但没有VAEDecode
